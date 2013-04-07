#
# spec file for package libmm-qt (Version 0.9.svn1043876)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Url:            http://www.kde.org
%define soversion 0

Name:           libQtModemManager-unstable
BuildRequires:  NetworkManager-devel > 0.8.997
BuildRequires:  ModemManager-devel
Version:        0.9.3_git20111023
Release:        1
License:        GPL v2 or later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          System/GUI/KDE
Summary:        NetworkManager client for KDE 4
Source0:        libmm-qt-%{version}.tar.bz2


%description
KNetworkManager is a KDE 4 applet for controlling
network connections on systems that use the NetworkManager service.


%package devel
Group:          Development/Libraries/KDE
Summary:        Development package for the libmm-qt library
Requires:       libQtModemManager%{soversion}-unstable = %version

%description devel

%package -n libQtModemManager%{soversion}-unstable
Group:          Development/Libraries/KDE
Summary:        Qt wrapper around the ModemManager libraries

%description -n libQtModemManager%{soversion}-unstable

%prep
%setup -q -n libmm-qt-%{version}


%build
  %cmake_kde_unstable -d build 
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall


%clean
rm -rf "$RPM_BUILD_ROOT"

%post -n libQtModemManager%{soversion}-unstable -p /sbin/ldconfig
%postun -n libQtModemManager%{soversion}-unstable -p /sbin/ldconfig

%files -n libQtModemManager%{soversion}-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libQtModemManager.so.*

%files devel
%defattr(-,root,root)
%{_kde_unstable_libdir}/libQtModemManager.so
%{_kde_unstable_includedir}/QtModemManager/
%{_kde_unstable_libdir}/pkgconfig/QtModemManager.pc

%changelog
