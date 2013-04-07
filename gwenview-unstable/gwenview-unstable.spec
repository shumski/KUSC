#
# spec file for package gwenview
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


Name:           gwenview-unstable
Version:        4.10.40_20130207
Release:        0
Summary:        Simple Image Viewer for KDE
License:        GPL-2.0+
Group:          Productivity/Graphics/Viewers
Url:            http://www.kde.org
Source0:        gwenview-%{version}.tar.xz
Patch0:         desktop_file.diff
BuildRequires:  libexiv2-devel
BuildRequires:  libkipi-unstable-devel
BuildRequires:  libkonq-unstable-devel
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  xz
BuildRequires:  libkactivities-unstable-devel
BuildRequires:  liblcms2-devel
Recommends:     kipi-plugins
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
Gwenview is a simple image viewer for KDE. It features a folder tree
window and a file list window, providing easy navigation of your file
hierarchy.

%prep
%setup -q -n gwenview-%{version}
#%patch0 -p1

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %suse_update_desktop_file -r gwenview       Graphics RasterGraphics Viewer
  %kde_unstable_post_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_kde_unstable_appsdir}/gwenview/
%{_kde_unstable_appsdir}/gvpart/
%{_kde_unstable_appsdir}/solid
%{_kde_unstable_applicationsdir}/gwenview.desktop
%{_kde_unstable_bindir}/gwenview
%{_kde_unstable_bindir}/gwenview_importer
%{_kde_unstable_htmldir}/en/gwenview/
%{_kde_unstable_libdir}/libgwenviewlib.*
%{_kde_unstable_modulesdir}/gvpart.so
%{_kde_unstable_servicesdir}/gvpart.desktop
%{_kde_unstable_servicesdir}/ServiceMenus/slideshow.desktop
%{_kde_unstable_iconsdir}/hicolor/*/*/*
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/actions
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/actions
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/actions
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps
%dir %{_kde_unstable_iconsdir}/hicolor/scalable
%dir %{_kde_unstable_iconsdir}/hicolor/scalable/actions
%dir %{_kde_unstable_iconsdir}/hicolor/scalable/apps


%changelog
