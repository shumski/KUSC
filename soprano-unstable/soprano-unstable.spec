#
# spec file for package soprano
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           soprano-unstable
Summary:        C++/Qt based interface library for RDF
License:        LGPL-2.1+ and GPL-2.0+
Group:          System/Libraries
# COMMON1-BEGIN
Version:        2.9.0_20130331
Release:        0
Url:            http://soprano.sourceforge.net/
Source0:        http://downloads.sourceforge.net/soprano/soprano-git.tar.xz
Source100:      baselibs.conf
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libqt4-devel
BuildRequires:  libraptor-devel
BuildRequires:  librasqal-devel
BuildRequires:  libredland-devel
BuildRequires:  libiodbc-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
# COMMON1-END
BuildRequires:  fdupes
Requires:       libsoprano4-unstable = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Soprano is an open and pluggable RDF resource framework which is build
on top of Qt. It provides RDF storage, RDF parsing, serialization,
inference, and full text indexing in a nice C++ API. The main target of
Soprano are desktop applications as it is being developed as a
subproject of Nepomuk, the semantic desktop initiative.

%prep
# COMMON2-BEGIN
%setup -q -n soprano-git
# COMMON2-END

%package backend-redland
Summary:        Redland backend for Soprano
License:        LGPL-2.1+
Group:          System/Libraries
Requires:       libsoprano4-unstable = %{version}
Provides:       soprano_backend = %{version}

%description backend-redland
This package provides a Redland based backend for Soprano.

%package -n libsoprano4-unstable
Summary:        C++/Qt based interface library for RDF
License:        LGPL-2.1+
Group:          System/Libraries
%requires_ge    libqt4

%description -n libsoprano4-unstable
Soprano is an open and pluggable RDF resource framework which is build
on top of QT4. It provides RDF storage, RDF parsing, serialization,
inference, and full text indexing in a nice C++ API. The main target of
Soprano are desktop applications as it is being developed as a
subroject of Nepomuk, the semantic desktop initiative.

%package -n libsoprano-unstable-devel
Summary:        Developer files for Soprano
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libraptor-devel
Requires:       libredland-devel
Requires:       libsoprano4-unstable = %{version}
Requires:       soprano-unstable-backend-redland = %{version}
%requires_ge    libqt4-devel

%description -n libsoprano-unstable-devel
This package contains developer files for Soprano.

%build
%cmake_kde_unstable -d build -- -DCMAKE_SKIP_RPATH=ON -DBUILD_VIRTUOSO_BACKEND=ON
%make_jobs

%install
cd build
make DESTDIR=%{buildroot} install
cd ..

%if 0%{?suse_version}
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/nquadparser.desktop
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/nquadserializer.desktop
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/raptorparser.desktop
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/raptorserializer.desktop
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/redlandbackend.desktop
%suse_update_desktop_file %{buildroot}%{_kde_unstable_datadir}/soprano/plugins/virtuosobackend.desktop
%endif

%fdupes -s %{buildroot}%{_kde_unstable_includedir}

%post -n libsoprano4-unstable -p /sbin/ldconfig

%postun -n libsoprano4-unstable -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB ChangeLog README TODO
%{_kde_unstable_bindir}/onto2vocabularyclass
%{_kde_unstable_bindir}/sopranocmd
%{_kde_unstable_bindir}/sopranod
%dir %{_kde_unstable_datadir}/dbus-1/
%dir %{_kde_unstable_datadir}/dbus-1/interfaces/
%{_kde_unstable_datadir}/dbus-1/interfaces/org.soprano.*.xml
%dir %{_kde_unstable_datadir}/soprano
%dir %{_kde_unstable_datadir}/soprano/rules
%dir %{_kde_unstable_datadir}/soprano/plugins
%{_kde_unstable_datadir}/soprano/rules/*
%{_kde_unstable_datadir}/soprano/plugins/nquadparser.desktop
%{_kde_unstable_datadir}/soprano/plugins/nquadserializer.desktop
%{_kde_unstable_datadir}/soprano/plugins/raptorparser.desktop
%{_kde_unstable_datadir}/soprano/plugins/raptorserializer.desktop
%{_kde_unstable_datadir}/soprano/plugins/virtuosobackend.desktop
%dir %{_kde_unstable_libdir}/soprano
%{_kde_unstable_libdir}/soprano/libsoprano_nquadparser.so
%{_kde_unstable_libdir}/soprano/libsoprano_nquadserializer.so
%{_kde_unstable_libdir}/soprano/libsoprano_raptorparser.so
%{_kde_unstable_libdir}/soprano/libsoprano_raptorserializer.so
%{_kde_unstable_libdir}/soprano/libsoprano_virtuosobackend.so

%files backend-redland
%defattr(-,root,root,-)
%{_kde_unstable_libdir}/soprano/libsoprano_redlandbackend.so
%{_kde_unstable_datadir}/soprano/plugins/redlandbackend.desktop

%files -n libsoprano4-unstable
%defattr(-,root,root,-)
%{_kde_unstable_libdir}/libsopranoclient.so.1*
%{_kde_unstable_libdir}/libsopranoserver.so.1*
%{_kde_unstable_libdir}/libsoprano.so.4*

%files -n libsoprano-unstable-devel
%defattr(-,root,root,-)
%{_kde_unstable_includedir}/soprano/
%{_kde_unstable_includedir}/Soprano/
%{_kde_unstable_libdir}/libsoprano.so
%{_kde_unstable_libdir}/libsopranoclient.so
%{_kde_unstable_libdir}/libsopranoserver.so
%{_kde_unstable_libdir}/pkgconfig/soprano.pc
%{_kde_unstable_libdir}/pkgconfig/sopranoclient.pc
%{_kde_unstable_libdir}/pkgconfig/sopranoserver.pc
%{_kde_unstable_datadir}/soprano/cmake/

%changelog
