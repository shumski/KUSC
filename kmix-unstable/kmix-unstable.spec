#
# spec file for package kmix (Version 4.7.80_204.10.40_201302074.10.40_201302074.10.40_201302074.10.40_2013020722)
#
# Copyright (c) 204.10.40_201302074.10.40_20130207 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 4.10.40_20130207.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           kmix-unstable
BuildRequires:  glib2-devel
BuildRequires:  alsa-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libkde-unstable-devel
BuildRequires:  libpulse-devel
BuildRequires:  xz
License:        GPLv2+
Group:          Productivity/Multimedia/Sound/Mixers
Summary:        Sound Mixer
Url:            http://www.kde.org
Version:        4.10.40_20130207
Release:        1
Source0:        kmix-%{version}.tar.xz
Patch0:         4_6_BRANCH.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
KDE's full featured mini mixer

%prep
%setup -q -n kmix-%{version}
%patch0 -p0

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %suse_update_desktop_file kmix           AudioVideo Mixer
  %kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{_kde_unstable_bindir}/kmix
%{_kde_unstable_bindir}/kmixctrl
%{_kde_unstable_modulesdir}/kded_kmixd.so
%{_kde_unstable_modulesdir}/plasma_engine_mixer.so
%{_kde_unstable_libdir}/libkdeinit4_kmix.so
%{_kde_unstable_libdir}/libkdeinit4_kmixctrl.so
%{_kde_unstable_applicationsdir}/kmix.desktop
%{_kde_unstable_datadir}/autostart/kmix_autostart.desktop
%{_kde_unstable_datadir}/autostart/restore_kmix_volumes.desktop
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.kmix.*
%{_kde_unstable_iconsdir}/hicolor/*/apps/kmix.*
%{_kde_unstable_appsdir}/kmix/
%{_kde_unstable_appsdir}/plasma/
%{_kde_unstable_servicesdir}/kded/kmixd.desktop
%{_kde_unstable_servicesdir}/kmixctrl_restore.desktop
%{_kde_unstable_servicesdir}/plasma-engine-mixer.desktop
%{_kde_unstable_htmldir}/en/kmix/
%dir %{_kde_unstable_iconsdir}/hicolor/128x128
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/apps
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps


%changelog
