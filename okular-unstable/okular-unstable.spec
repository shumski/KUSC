#
# spec file for package okular
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


Name:           okular-unstable
Version:        4.10.40_20130207
Release:        0
Summary:        Document Viewer
License:        GPL-2.0+
Group:          Productivity/Office/Other
Url:            http://www.kde.org
Source0:        okular-%{version}.tar.xz
Patch0:         4_8_BRANCH.diff
Patch1:         fix-priority-okular.diff
BuildRequires:  OpenEXR-devel
BuildRequires:  chmlib-devel
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  libdjvulibre-devel
BuildRequires:  libepub-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libkde-unstable-devel
BuildRequires:  libpoppler-qt4-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libspectre-devel
BuildRequires:  net-snmp-devel
BuildRequires:  oxygen-icon-theme-unstable-large
BuildRequires:  soprano-unstable-backend-redland
BuildRequires:  xz
BuildRequires:  libkactivities-unstable-devel
%if 0%{?suse_version} > 1130
BuildRequires:  sane-backends-devel
%else
BuildRequires:  sane-backends
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_ge    libpoppler-qt4-3
%kde_unstable_runtime_requires

%description
Document viewing program; supports document in PDF, PS and
many other formats.

%package devel
Summary:        Document Viewer - Development Files
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       libkde-unstable-devel
%kde_unstable_runtime_requires

%description devel
Document viewing program; supports document in various formats

%prep
%setup -q -n okular-%{version}
%patch0
%patch1 -p0

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  mkdir -p %{buildroot}%{_kde_unstable_iconsdir}/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps
  cp %{_kde_unstable_iconsdir}/oxygen/128x128/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/128x128/apps/
  cp %{_kde_unstable_iconsdir}/oxygen/16x16/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/16x16/apps/
  cp %{_kde_unstable_iconsdir}/oxygen/22x22/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/22x22/apps/
  cp %{_kde_unstable_iconsdir}/oxygen/32x32/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/32x32/apps/
  cp %{_kde_unstable_iconsdir}/oxygen/48x48/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/48x48/apps/
  cp %{_kde_unstable_iconsdir}/oxygen/64x64/apps/graphics-viewer-document.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/64x64/apps/
  cd ..
  %suse_update_desktop_file -r okular   Office Viewer
  %fdupes -s %{buildroot}%{_kde_unstable_datadir}
  %kde_unstable_post_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde_unstable_applicationsdir}/okular*.desktop
%{_kde_unstable_applicationsdir}/active-documentviewer*.desktop
%{_kde_unstable_appsdir}/okular/
%{_kde_unstable_bindir}/okular
%config %{_kde_unstable_configkcfgdir}/*.kcfg
%{_kde_unstable_htmldir}/en/okular/
%{_kde_unstable_iconsdir}/hicolor/*/apps/graphics-viewer-document.*
%{_kde_unstable_iconsdir}/hicolor/*/apps/okular.*
%{_kde_unstable_libdir}/libokularcore.so.*
%{_kde_unstable_modulesdir}/*.so
%{_kde_unstable_servicesdir}/*.desktop
%{_kde_unstable_servicesdir}/*.protocol
%{_kde_unstable_servicetypesdir}/*.desktop
%{_kde_unstable_modulesdir}/imports/
%{_kde_unstable_appsdir}/kconf_update/okular.upd
%{_kde_unstable_mandir}/man1/okular.1.gz

%files devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/okular/
%{_kde_unstable_libdir}/cmake/Okular/
%{_kde_unstable_libdir}/libokularcore.so

%changelog
