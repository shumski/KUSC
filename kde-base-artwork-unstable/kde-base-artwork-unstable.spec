#
# spec file for package kdegames4 (Version 4.7.80_20111122)
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


Name:           kde-base-artwork-unstable
BuildRequires:  libkde-unstable-devel 
BuildRequires:  oxygen-icon-theme-unstable-large
BuildRequires:  xz
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        KSplash themes and other artwork
Url:            http://www.kde.org
Version:        4.10.40_20130207
Release:        1
Source0:        kde-base-artwork-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
This package contains KSplash themes and other artwork


%prep
%setup -q -n kde-base-artwork-%{version}

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %kde_unstable_post_install

%clean
  rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_kde_unstable_appsdir/ksplash/

%changelog
