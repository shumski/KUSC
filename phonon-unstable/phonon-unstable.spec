#
# spec file for package phonon
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


Name:           phonon-unstable
Version:        4.6.0_20130331
Release:        0
Summary:        Multimedia Platform Abstraction
License:        LGPL-2.0+
Group:          System/GUI/KDE
Url:            http://phonon.kde.org/
Source0:        phonon-git.tar.xz
Source1:        baselibs.conf
BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libpulse-devel
BuildRequires:  libqt4-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Phonon is a cross-platform portable multimedia support abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package devel
Summary:        Phonon Multimedia Platform Abstraction
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       libphonon4-unstable = %{version}
Requires:       libqt4-devel

%description devel
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package -n libphonon4-unstable
Summary:        Phonon Multimedia Platform Abstraction
Group:          System/Libraries
Recommends:     phonon-backend
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= %{version}
%requires_ge    libqt4-x11

%description -n libphonon4-unstable
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%prep
%setup -q -n phonon-git

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  install -d -m 0755 %{buildroot}%{_kde_unstable_modulesdir}/plugins
  install -d -m 0755 %{buildroot}%{_kde_unstable_modulesdir}/plugins/phonon_backend
  %fdupes %{buildroot}%{_kde_unstable_includedir}

%post   -n libphonon4-unstable -p /sbin/ldconfig

%postun -n libphonon4-unstable -p /sbin/ldconfig

%files -n libphonon4-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libphonon.so.*
%{_kde_unstable_libdir}/libphononexperimental.so.*
%dir %{_kde_unstable_modulesdir}/plugins
%dir %{_kde_unstable_modulesdir}/plugins/phonon_backend
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%dir %{_kde_unstable_libdir}/qt4/imports/Phonon/
%{_kde_unstable_libdir}/qt4/imports/Phonon/

%files devel
%defattr(-,root,root)
%{_kde_unstable_datadir}/phonon/
%{_kde_unstable_datadir}/qt4/mkspecs/modules/
%{_kde_unstable_includedir}/phonon
%{_kde_unstable_includedir}/KDE
%{_kde_unstable_libdir}/libphonon.so
%{_kde_unstable_libdir}/libphononexperimental.so
%{_kde_unstable_libdir}/cmake/phonon/
%{_kde_unstable_libdir}/pkgconfig/phonon.pc

%changelog
