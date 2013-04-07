#
# spec file for package polkit-qt-1
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define debug_package_requires libpolkit-qt-1-0 = %{version}-%{release}

Name:           polkit-qt-1-unstable
Version:        0.99.1
Release:        14
License:        LGPL-2.1+
Summary:        PolicyKit Library Qt Bindings
Url:            http://api.kde.org/kdesupport-api/kdesupport-apidocs/polkit-qt/html/
Group:          Development/Libraries/KDE
# ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/
Source0:        polkit-qt-1-%{version}.tar.bz2
Source99:       baselibs.conf
Patch0:         ck-avoid-crash.diff
Patch1:         d3c337da.patch
BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libqt4-devel
BuildRequires:  polkit-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Polkit-qt-1 aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt-1-1-unstable
License:        LGPL-2.1+
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE

%description -n libpolkit-qt-1-1-unstable
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt-1-unstable-devel
License:        LGPL-2.1+
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE
Requires:       libpolkit-qt-1-1-unstable = %{version}
Requires:       polkit-devel

%description -n libpolkit-qt-1-unstable-devel
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%prep
%setup -q -n polkit-qt-1-0.99.1
%patch0
%patch1 -p1

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %make_install

%post -n libpolkit-qt-1-1-unstable -p /sbin/ldconfig

%postun -n libpolkit-qt-1-1-unstable -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n libpolkit-qt-1-unstable-devel
%defattr(-,root,root)
%doc AUTHORS README
%{_kde_unstable_includedir}/polkit-qt-1/
%{_kde_unstable_libdir}/pkgconfig/polkit-qt*
%{_kde_unstable_libdir}/libpolkit-qt-gui-1.so
%{_kde_unstable_libdir}/libpolkit-qt-core-1.so
%{_kde_unstable_libdir}/libpolkit-qt-agent-1.so
%{_kde_unstable_libdir}/cmake/PolkitQt-1/

%files -n libpolkit-qt-1-1-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libpolkit-qt-gui-1.so.*
%{_kde_unstable_libdir}/libpolkit-qt-core-1.so.*
%{_kde_unstable_libdir}/libpolkit-qt-agent-1.so.*

%changelog
