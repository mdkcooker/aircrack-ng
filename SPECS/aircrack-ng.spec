%define prerel	beta2
%define rel	1

Name:		aircrack-ng
Version:	1.2
Release:	%mkrel -c %{prerel} %{rel}
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.aircrack-ng.org/doku.php
Source0:	http://download.aircrack-ng.org/%{name}-%{version}%{?prerel:-%prerel}.tar.gz

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
%setup -qn %{name}-%{version}%{?prerel:-%prerel}

%build
export CFLAGS="%{optflags} -O3"
export LDFLAGS="%{ldflags}"
# unstable=true needed for wesside-ng, easside-ng, buddy-ng and tkiptun-ng
# (also needed in make install)
%make -j4 datadir=%{_datadir} unstable=true sqlite=true

%install
%makeinstall unstable=true sqlite=true

mkdir -p %{buildroot}%{_datadir}/%{name}
# License unclear, originates from:
# http://standards.ieee.org/regauth/oui/oui.txt
touch %{buildroot}%{_datadir}/%{name}/airodump-ng-oui.txt

# move manual pages to a correct location
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/*.1 %{buildroot}%{_mandir}/man1/

%post
%{_sbindir}/airodump-ng-oui-update

%files
%doc ChangeLog README AUTHORS VERSION
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%dir %{_datadir}/aircrack-ng
%ghost %{_datadir}/aircrack-ng/airodump-ng-oui.txt
