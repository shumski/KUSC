#
# spec file for package kactivities4
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright 2010 Open-SLX GmbH <sebas@open-slx.com>
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

Name:           kactivities-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        KDE Plasma Activities support
License:        GPL-2.0+ ; LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        kactivities-git.tar.xz
BuildRequires:  libkde-unstable-devel
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
Kactivities provides an API for using and interacting with the Plasma Active
Activities Manager.

%package -n libkactivities-unstable
Provides:       libkactivities-unstable = %version
Obsoletes:      libkactivities-unstable <= 4.8.0
Summary:        Development files and headers for kactivities
Group:          System/Libraries

%description -n libkactivities-unstable
Kactivities provides an API for using and interacting with the Plasma Active
Activities Manager.

%package -n libkactivities-unstable-devel
Summary:        Development files and headers for kactivities
Group:          Development/Libraries/KDE
Requires:       libkactivities-unstable = %{version}

%description -n libkactivities-unstable-devel
Development headers for the kactivities4 library

%prep
%setup -qn kactivities-git

%build
%cmake_kde_unstable -d builddir
%make_jobs

%install
pushd builddir
%kde_unstable_makeinstall
popd
%kde_unstable_post_install

%post -n libkactivities-unstable -p /sbin/ldconfig

%postun -n libkactivities-unstable -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_kde_unstable_bindir}/kactivitymanagerd
%{_kde_unstable_modulesdir}/*
%{_kde_unstable_servicesdir}/*
%{_kde_unstable_servicetypesdir}/*
%{_kde_unstable_datadir}/ontology/
%{_kde_unstable_appsdir}/activitymanager/

%files -n libkactivities-unstable
%defattr(-,root,root,-)
%{_kde_unstable_libdir}/libkactivities.so.*
%{_kde_unstable_libdir}/libkactivities-models.so.*

%files -n libkactivities-unstable-devel
%defattr(-,root,root,-)
%{_kde_unstable_libdir}/libkactivities.so
%{_kde_unstable_libdir}/libkactivities-models.so
%{_kde_unstable_includedir}/kactivities/
%{_kde_unstable_includedir}/kactivities-models/
%{_kde_unstable_includedir}/KDE/KActivities/
%_kde_unstable_libdir/cmake/KActivities/
%_kde_unstable_libdir/cmake/KActivities-Models/
%_kde_unstable_libdir/pkgconfig/*

%changelog
