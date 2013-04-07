#
# spec file for package polkit-kde-agent-1
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



Name:           polkit-kde-agent-1-unstable
Version:        0.99.0
Release:        6
License:        GPLv2 ; LGPLv2.1+
Summary:        PolicyKit authentication agent for KDE
Url:            https://projects.kde.org/projects/extragear/base/polkit-kde-agent-1
Group:          Development/Libraries/KDE
# ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  libkde-unstable-devel
BuildRequires:  libpolkit-qt-1-unstable-devel
#Requires:       polkit-kde-kcmmodules-unstable
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.

%prep
%setup -q -n polkit-kde-agent-1-%{version}

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %kde_unstable_post_install
  cd ..

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde_unstable_datadir}/autostart/polkit-kde-authentication-agent-1.desktop
%{_kde_unstable_libexecdir}/polkit-kde-authentication-agent-1
%{_kde_unstable_appsdir}/policykit1-kde/

%changelog
