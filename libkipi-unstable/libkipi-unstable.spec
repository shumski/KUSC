#
# spec file for package libkipi
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libkipi-unstable
BuildRequires:  libkde-unstable-devel
BuildRequires:  oxygen-icon-theme-unstable-large
BuildRequires:  xz
Summary:        KDE Image Plugin Interface
License:        BSD-3-Clause ; GPL-2.0+ ; LGPL-2.1+ ; MIT
Group:          Development/Libraries/KDE
Url:            http://www.kde.org
Version:        4.10.40_20130207
Release:        0
Source0:        libkipi-%{version}.tar.xz
Patch0:         4_6_BRANCH.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%prep
%setup -q -n libkipi-%version
%patch0

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %kde_unstable_post_install

%clean
  rm -rf $RPM_BUILD_ROOT

%package -n libkipi10-unstable
Summary:        KDE Image Plug-In Interface
Group:          Development/Libraries/KDE
%requires_ge  libqt4-x11

%description -n libkipi10-unstable
This package provides a generic KDE image plug-in interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%files -n libkipi10-unstable
%defattr(-,root,root)
%_kde_unstable_appsdir/kipi/
%_kde_unstable_libdir/libkipi.so.*
%_kde_unstable_iconsdir/hicolor/*/apps/kipi.png
%_kde_unstable_servicetypesdir/kipiplugin.desktop
%dir %_kde_unstable_iconsdir/hicolor/128x128
%dir %_kde_unstable_iconsdir/hicolor/128x128/apps
%dir %_kde_unstable_iconsdir/hicolor/16x16/apps
%dir %_kde_unstable_iconsdir/hicolor/22x22
%dir %_kde_unstable_iconsdir/hicolor/22x22/apps
%dir %_kde_unstable_iconsdir/hicolor/32x32/apps
%dir %_kde_unstable_iconsdir/hicolor/48x48/apps



%post -n libkipi10-unstable -p /sbin/ldconfig

%postun -n libkipi10-unstable -p /sbin/ldconfig

%package devel
Summary:        KDE Image Plugin Interface
Group:          Development/Libraries/KDE
Requires:       libkde-unstable-devel
Requires:       libkipi10-unstable = %version

%description devel
This package provides a generic KDE Image Plug-in Interface used by
some KDE image applications. Plug-ins for this interface are in the
kipi-plugins package.

%files devel
%defattr(-,root,root)
%doc COPYING README
%_kde_unstable_libdir/libkipi.so
%_kde_unstable_includedir/libkipi/
%_kde_unstable_libdir/pkgconfig/libkipi.pc

%files 
%defattr(-,root,root)
%doc COPYING README

%changelog
