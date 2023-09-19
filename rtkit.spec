#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : rtkit
Version  : 0.11
Release  : 4
URL      : http://0pointer.de/public/rtkit-0.11.tar.xz
Source0  : http://0pointer.de/public/rtkit-0.11.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: rtkit-bin = %{version}-%{release}
Requires: rtkit-data = %{version}-%{release}
Requires: rtkit-libexec = %{version}-%{release}
Requires: rtkit-license = %{version}-%{release}
Requires: rtkit-man = %{version}-%{release}
Requires: rtkit-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : libcap-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0005-rtkit-daemon-Don-t-log-debug-messages-by-default.patch

%description
REALTIMEKIT Realtime Policy and Watchdog Daemon
GIT:
git://git.0pointer.de/rtkit.git

%package bin
Summary: bin components for the rtkit package.
Group: Binaries
Requires: rtkit-data = %{version}-%{release}
Requires: rtkit-libexec = %{version}-%{release}
Requires: rtkit-license = %{version}-%{release}
Requires: rtkit-services = %{version}-%{release}

%description bin
bin components for the rtkit package.


%package data
Summary: data components for the rtkit package.
Group: Data

%description data
data components for the rtkit package.


%package libexec
Summary: libexec components for the rtkit package.
Group: Default
Requires: rtkit-license = %{version}-%{release}

%description libexec
libexec components for the rtkit package.


%package license
Summary: license components for the rtkit package.
Group: Default

%description license
license components for the rtkit package.


%package man
Summary: man components for the rtkit package.
Group: Default

%description man
man components for the rtkit package.


%package services
Summary: services components for the rtkit package.
Group: Systemd services
Requires: systemd

%description services
services components for the rtkit package.


%prep
%setup -q -n rtkit-0.11
cd %{_builddir}/rtkit-0.11
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695140685
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1695140685
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rtkit
cp %{_builddir}/rtkit-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/rtkit/3117576320c22664b6f771dbd140b6eb73a024b9 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rtkitctl

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
/usr/share/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
/usr/share/polkit-1/actions/org.freedesktop.RealtimeKit1.policy

%files libexec
%defattr(-,root,root,-)
/usr/libexec/rtkit-daemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rtkit/3117576320c22664b6f771dbd140b6eb73a024b9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/rtkitctl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rtkit-daemon.service
