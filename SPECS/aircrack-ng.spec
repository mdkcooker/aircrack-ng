Name:		aircrack-ng
Version:	1.1
Release:	%mkrel 7
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.aircrack-ng.org/doku.php
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
Patch0:		aircrack-ng-1.1-makefile-fixes.patch
Patch1:		aircrack-ng-1.1-airodump-oui-destdir.patch
Patch2:		aircrack-ng-1.1-ignore-channel-1-error.patch
Patch3:		aircrack-ng-1.1-CVE-2010-1159.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite3-devel

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an 
enhanced/reborn version of aircrack. It consists of airodump (an 802.11 
packet capture program), aireplay (an 802.11 packet injection program), 
aircrack (static WEP and WPA-PSK cracking), airdecap (decrypts WEP/WPA 
capture files), and some tools to handle capture files (merge, convert, 
etc.).

%prep
%setup -q
%patch0 -p1 -b .make_makeup~
%patch1 -p1 -b .oui_destdir~
%patch2 -p1
%patch3 -p0 -b .CVE-2010-1159

%build
export CFLAGS="%{optflags} -O3"
export LDFLAGS="%{ldflags}"
# unstable=true needed for wesside-ng, easside-ng, buddy-ng and tkiptun-ng
# (also needed in make install)
%make -j4 datadir=%{_datadir} unstable=true sqlite=true

%install
%{__rm} -rf %{buildroot}
%makeinstall unstable=true sqlite=true

mkdir -p %{buildroot}%{_datadir}/%{name}
# License unclear, originates from:
# http://standards.ieee.org/regauth/oui/oui.txt
touch %{buildroot}%{_datadir}/%{name}/airodump-ng-oui.txt

%post 
%{_sbindir}/airodump-ng-oui-update

%files
%doc ChangeLog README AUTHORS VERSION 
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*.1*
%dir %{_datadir}/aircrack-ng
%ghost %{_datadir}/aircrack-ng/airodump-ng-oui.txt
