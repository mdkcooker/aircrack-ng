Name:		aircrack-ng
Version:	1.1
Release:	%mkrel 2
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.aircrack-ng.org/doku.php
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
Patch0:		aircrack-ng-1.1-makefile-fixes.patch
Patch1:		aircrack-ng-1.1-airodump-oui-destdir.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build
export CFLAGS="%{optflags} -O3" LDFLAGS="%{ldflags}" SQLITE=true UNSTABLE=true
%make datadir=%{_datadir} || make datadir=%{_datadir}

%install
%{__rm} -rf %{buildroot}
%makeinstall SQLITE=true UNSTABLE=true
DESTDIR=%{buildroot} sh ./scripts/airodump-ng-oui-update

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README AUTHORS VERSION 
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*.1*
%dir %{_datadir}/aircrack-ng
%{_datadir}/aircrack-ng/airodump-ng-oui.txt


