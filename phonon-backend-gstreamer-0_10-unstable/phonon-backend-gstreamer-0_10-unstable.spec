#
# spec file for package phonon-backend-gstreamer-0_10
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


Name:           phonon-backend-gstreamer-0_10-unstable
Version:        4.6.50_20130331
Release:        0
Summary:        Phonon Multimedia Platform Abstraction
License:        LGPL-2.0+
Group:          System/GUI/KDE
Url:            http://phonon.kde.org/
%define filename phonon-gstreamer
%define _phonon_version 4.6.0
Source0:        %{filename}-git.tar.xz
Patch0:         build_fix.diff
BuildRequires:  alsa-devel
BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gstreamer-0_10-plugins-base-devel
BuildRequires:  kde-unstable-filesystem
BuildRequires:  phonon-unstable-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
Requires:       libphonon4-unstable => %{_phonon_version}
Supplements:    packageand(gstreamer-0_10-plugins-base:phonon)
Provides:       phonon-backend = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%prep
%setup -q -n %{filename}-git
%patch0 -p1
%build
  # compile everything for now, actually we should compile
  # against installed phonon, but this is always the same
  # in OBS setup
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %suse_update_desktop_file %{buildroot}%{_kde_unstable_servicesdir}/phononbackends/gstreamer.desktop
  %fdupes %{buildroot}%{_includedir}

%files
%defattr(-,root,root)
%{_kde_unstable_modulesdir}/plugins/phonon_backend/phonon_gstreamer.so
%{_kde_unstable_servicesdir}/phononbackends/gstreamer.desktop
%{_kde_unstable_iconsdir}/*/*/apps/phonon-gstreamer.*
%dir %{_kde_unstable_iconsdir}/hicolor/*/*

%changelog
