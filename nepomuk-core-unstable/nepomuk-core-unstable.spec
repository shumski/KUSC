#
# spec file for package nepomuk-core (Version 4.7.80_20111122)
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

Name:           nepomuk-core-unstable
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libkde-unstable-devel
BuildRequires:  libsoprano-unstable-devel
BuildRequires:  fdupes 
BuildRequires:  shared-desktop-ontologies-unstable-devel
BuildRequires:  libexiv2-devel 
BuildRequires:  soprano-unstable-backend-redland soprano-unstable
BuildRequires:  strigi-unstable-devel
BuildRequires:  xz-devel
BuildRequires:  lzma-devel
BuildRequires:  xz
BuildRequires:  libpoppler-qt4-devel
BuildRequires:  libtag-devel
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        The KDE Nepomuk Core Library
Url:            http://nepomuk.kde.org/
Version:        4.10.40_20130331
Release:        1
Source0:        nepomuk-core-git.tar.xz
Source99:       nepomuk.png
Patch0:         desktop_files.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libqt4-x11 >= %( echo `rpm -q --queryformat '%{VERSION}' libqt4-x11`)
Requires:       kdelibs-unstable >= %version
Requires:       soprano-unstable-backend-redland
%define debug_package_requires %name = %version-%release kdelibs-unstable-debuginfo

%description
This package contains all the core libraries for nepomuk 

%package devel
Summary:        The Nepomuk Core Library
License:        GPLv2+
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description devel
The devel package of the core library for nepomuk

%prep
%setup -q -n nepomuk-core-git
%patch0 -p1

%build
  %cmake_kde_unstable -d build -- -DKDE4_ENABLE_FPIE=1
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %{__mkdir_p} %{buildroot}%{_kde_unstable_datadir}/pixmaps
  install $RPM_SOURCE_DIR/nepomuk.png %{buildroot}%{_kde_unstable_datadir}/pixmaps/
  %if %suse_version > 1020
  %fdupes -s $RPM_BUILD_ROOT
  %endif
#   %suse_update_desktop_file -r %{buildroot}%{_kde_unstable_applicationsdir}/nepomukcleaner.desktop             Utility Archiving
  %kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/Nepomuk2/
%{_kde_unstable_includedir}/nepomuk2/
%{_kde_unstable_libdir}/cmake/NepomukCore/
%{_kde_unstable_libdir}/libnepomukcore.so
%{_kde_unstable_libdir}/libnepomukcleaner.so

%files 
%defattr(-,root,root)
%dir %{_kde_unstable_datadir}/pixmaps
%_kde_unstable_bindir/nepomuk*
%_kde_unstable_modulesdir/nepomuk*.so
%{_kde_unstable_libdir}/libnepomukcommon.so
%{_kde_unstable_libdir}/libnepomukcore.so.*
%{_kde_unstable_libdir}/libnepomukcleaner.so.*
%{_kde_unstable_libdir}/libkdeinit4_nepomukserver.so
%{_kde_unstable_applicationsdir}/nepomuk*.desktop
%{_kde_unstable_datadir}/autostart/nepomukserver.desktop
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.nepomuk.*.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.NepomukServer.xml
%{_kde_unstable_appsdir}/fileindexerservice/
%{_kde_unstable_appsdir}/nepomukfilewatch/
%{_kde_unstable_appsdir}/nepomukstorage/
%{_kde_unstable_servicesdir}/nepomuk*.desktop
%{_kde_unstable_servicetypesdir}/nepomuk*.desktop
%{_kde_unstable_datadir}/ontology/
%{_kde_unstable_datadir}/pixmaps/nepomuk.png
%{_kde_unstable_servicetypesdir}/nepomukextractor.desktop

%changelog
