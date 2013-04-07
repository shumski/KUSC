#
# spec file for package kwebkitpart
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



Name:           kwebkitpart-unstable
Version:        1.3.1_20130331
Release:        1
License:        LGPL-2.0+ ; LGPL-2.1+
Summary:        KDE Webkit web browser component
Url:            https://projects.kde.org/projects/extragear/base/kwebkitpart
Group:          System/GUI/KDE
Source:         kwebkitpart-git.tar.xz
Source1:        README.html.bz2
BuildRequires:  glew-devel
BuildRequires:  libkde-unstable-devel
BuildRequires:  sqlite-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
A webkit web browser component for KDE (KPart).

%prep
%setup -q -n kwebkitpart-git
%{uncompress:%{S:1}} >README.html 

%build
%cmake_kde_unstable -d build
%make_jobs

%install
pushd build
  %kde_unstable_makeinstall
popd
%kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_kde_unstable_libdir}/kde4
%{_kde_unstable_libdir}/kde4/kwebkitpart.so
%{_kde_unstable_servicesdir}/kwebkitpart.desktop
%{_kde_unstable_appsdir}/kwebkitpart
%{_kde_unstable_iconsdir}/hicolor/*/apps/webkit.*
%dir %{_kde_unstable_iconsdir}/hicolor/*
%dir %{_kde_unstable_iconsdir}/hicolor/*/apps
%doc COPYING.LIB README README.html


%changelog
