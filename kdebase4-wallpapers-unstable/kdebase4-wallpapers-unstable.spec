#
# spec file for package kdebase4-wallpapers
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


Name:           kdebase4-wallpapers-unstable
Version:        4.10.40_20130207
Release:        0
Summary:        KDE 4 Wallpapers
License:        LGPL-3.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source0:        kde-wallpapers-%{version}.tar.xz
BuildRequires:  libkde-unstable-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the wallpapers of KDE 4.

%prep
%setup -q -n kde-wallpapers-%{version}

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  make DESTDIR=%{buildroot} install
  %kde_unstable_post_install

%files
%defattr(-,root,root)
%doc LICENSE
%{_kde_unstable_datadir}/wallpapers

%changelog
