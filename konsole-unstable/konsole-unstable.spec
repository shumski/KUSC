#
# spec file for package konsole
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


Name:           konsole-unstable
Version:        4.10.40_20130207
Release:        0
Summary:        KDE Terminal
License:        GPL-2.0+
Group:          System/X11/Terminals
Url:            http://www.kde.org/
Source0:        konsole-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libkde-unstable-devel
BuildRequires:  libkonq-unstable-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libxklavier)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
Konsole is a terminal emulator for the K Desktop Environment.

%prep
%setup -q -n konsole-%{version}

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  pushd build
%kde_unstable_makeinstall
  popd
  %suse_update_desktop_file konsole TerminalEmulator
  %fdupes -s %{buildroot} 
  %kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_kde_unstable_bindir}/konsole
%{_kde_unstable_bindir}/konsoleprofile
%{_kde_unstable_applicationsdir}/konsole.desktop
%{_kde_unstable_appsdir}/konsole/
%{_kde_unstable_servicesdir}/*.desktop
%{_kde_unstable_servicesdir}/ServiceMenus/*.desktop
%{_kde_unstable_servicetypesdir}/*.desktop
%{_kde_unstable_libdir}/*.so
%{_kde_unstable_modulesdir}/*.so
%{_kde_unstable_htmldir}/en/konsole/
%{_kde_unstable_appsdir}/kconf_update/

%changelog
