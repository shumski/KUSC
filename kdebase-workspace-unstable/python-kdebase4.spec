#
# spec file for package python-kdebase4
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


Name:           python-kdebase4
Version:        4.10.40_20130111
Release:        0
Summary:        Python bindings for KDE 4 desktop shell
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source0:        kde-workspace-%{version}.tar.xz
BuildRequires:  ConsoleKit-devel
BuildRequires:  NetworkManager-devel
BuildRequires:  bluez-devel
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libkactivities-devel
BuildRequires:  libkde4-devel >= %{version}
BuildRequires:  libkdepimlibs4-devel
BuildRequires:  libknotificationitem-devel
BuildRequires:  libpolkit-qt-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libusb-devel
BuildRequires:  python-kde4-devel
BuildRequires:  pkgconfig(libxklavier)
Requires:       python-kde4 = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires

%description
Python bindings for Plasma, the KDE 4 desktop shell.  These bindings
allow Plasmoids written in Python

%prep
%setup -q -n kde-workspace-%{version}

%build
  %cmake_kde4 -d build
  cd plasma/generic/scriptengines/python
  %make_jobs

%install
  cd build/plasma/generic/scriptengines/python
  %make_install
  %kde_post_install

%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{py_sitedir}/PyKDE4
%{_kde4_appsdir}/plasma_scriptengine_python
%{_kde4_servicesdir}/plasma-*.desktop

%changelog
