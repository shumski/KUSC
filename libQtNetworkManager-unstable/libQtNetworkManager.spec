#
# spec file for package libModemManager-qt (Version 0.9.svn1043876)
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

Name:           libQtNetworkManager-unstable
BuildRequires:  NetworkManager-devel > 0.8.997
BuildRequires:  libQtModemManager-devel
Version:        0.9.3_git20111023
Release:        1
License:        GPL v2 or later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          System/GUI/KDE
Summary:        NetworkManager client for KDE 4
Source0:        libnm-qt-%{version}.tar.bz2

%description
KNetworkManager is a KDE 4 applet for controlling
network connections on systems that use the NetworkManager service.

%package devel
Group:          Development/Libraries/KDE
Summary:        Qt Wrapper for NetworkManager libraries
Requires:       libQtNetworkManager%{soversion}-unstable = %version
Requires:       libQtModemManager-unstable-devel

%description devel
A qt wrapper around the NetworkManager libraries

%package -n libQtNetworkManager%{soversion}-unstable
Group:          Development/Libraries/KDE
Summary:        Qt Wrapper for NetworkManager libraries

%description -n libQtNetworkManager%{soversion}-unstable
A qt wrapper around the NetworkManager libraries


%prep
%setup -q -n libnm-qt-%{version}

%build
  %cmake_kde_unstable -d build 
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %kde_unstable_post_install

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -n libQtNetworkManager%{soversion}-unstable -p /sbin/ldconfig
%postun -n libQtNetworkManager%{soversion}-unstable -p /sbin/ldconfig

%files -n libQtNetworkManager%{soversion}-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libQtNetworkManager.so.*

%files devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/QtNetworkManager/
%{_kde_unstable_libdir}/libQtNetworkManager.so
%{_kde_unstable_libdir}/pkgconfig/QtNetworkManager.pc

%changelog
