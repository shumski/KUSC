#
# spec file for package nepomuk-widgets (Version 4.7.80_20111122)
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

Name:           libnepomukwidgets-unstable
BuildRequires:  libkde-unstable-devel
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  fdupes 
BuildRequires:  shared-desktop-ontologies-unstable-devel
BuildRequires:  libexiv2-devel 
BuildRequires:  libsoprano-unstable-devel
BuildRequires:  strigi-unstable-devel
BuildRequires:  xz
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        The Library containing the Nepomuk Widgets
Url:            http://nepomuk.kde.org/
Version:        4.10.40_20130308
Release:        1
Source0:        nepomuk-widgets-git.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libqt4-x11 >= %( echo `rpm -q --queryformat '%{VERSION}' libqt4-x11`)
Requires:       kdelibs-unstable
Requires:       soprano-unstable-backend-redland
%kde_unstable_runtime_requires
%define debug_package_requires %name = %version-%release kdelibs-unstable-debuginfo

%description
This package contains all the Nepomuk Widgets 

%package devel
Summary:        NepomukWidgets
License:        GPLv2+
Group:          System/GUI/KDE
Requires:       libnepomukwidgets-unstable = %{version}

%description devel
The devel package of the Nepomuk Widgets

%prep
%setup -q -n nepomuk-widgets-git

%build
  %cmake_kde_unstable -d build -- -DKDE4_ENABLE_FPIE=1
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %if %suse_version > 1020
  %fdupes -s $RPM_BUILD_ROOT
  %endif
  %kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root)
%{_kde_unstable_libdir}/libnepomukwidgets.so
%{_kde_unstable_includedir}/nepomuk2/
%{_kde_unstable_libdir}/cmake/NepomukWidgets/

%files
%defattr(-,root,root)
%{_kde_unstable_libdir}/libnepomukwidgets.so.*

%changelog
