#
# spec file for package plasma-addons
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


Name:           plasma-addons-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        Additional Plasma Widgets
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source0:        kdeplasma-addons-git.tar.xz
Patch0:         4_7_BRANCH.diff
Patch1:         krunner-akonadi-dont-cause-start.diff
Patch2:         lancelot-suse.diff
BuildRequires:  fdupes
BuildRequires:  ibus-devel
BuildRequires:  kdebase-workspace-unstable-devel libkdepimlibs-unstable-devel akonadi-runtime-unstable
#BuildRequires:  kopete-devel
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libeigen2-devel
#BuildRequires:  libkexiv2-devel
BuildRequires:  libqalculate-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqimageblitz-devel
#BuildRequires:  marble-devel
BuildRequires:  python-qt4-devel
BuildRequires:  xz
BuildRequires:  libqjson-devel
BuildRequires:  mediastreamer2-devel
BuildRequires:  libortp-devel
Recommends:     plasma-addons-unstable-akonadi
Recommends:     plasma-addons-unstable-lancelot
Recommends:     plasma-addons-unstable-marble
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):     shared-mime-info
Requires(postun):   shared-mime-info
%kde_unstable_runtime_requires

%description
Additional plasmoids from upstream for use on the KDE workspace

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       %{name}-akonadi = %{version}
Requires:       %{name}-lancelot = %{version}

%description devel
Development files and headers needed to build software
using %{name}

%package akonadi

Summary:        Additional Plasmoids Depending on Akonadi
Group:          System/GUI/KDE
Requires:       kdepim4-runtime-unstable
%kde_unstable_pimlibs_requires
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires

%description akonadi
Additional plasmoids from upstream that require Akonadi

%package lancelot
Summary:        Additional Lancelot Launcher Plasmoid
Group:          System/GUI/KDE
Requires:       kdepim4-runtime-unstable
%kde_unstable_pimlibs_requires
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires

%description lancelot
Additional launcher plasmoid from upstream that requires Akonadi

#%package marble
#Summary:        Additional Plasmoids Depending on Marble
#Group:          System/GUI/KDE
#Requires:       marble-unstable = %{version}
#%kde_unstable_runtime_requires

#%description marble
#Additional plasmoids from upstream that require Marble

%prep
%setup -q -n kdeplasma-addons-git
%patch0 -p1
%patch1
%patch2

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  cd ..
  %fdupes -s %{buildroot}
  %kde_unstable_post_install

%post
/sbin/ldconfig
%{_bindir}/update-mime-database %{_kde_unstable_datadir}/mime &> /dev/null || :

%postun
/sbin/ldconfig
%{_bindir}/update-mime-database %{_kde_unstable_datadir}/mime &> /dev/null || :

%post   akonadi -p /sbin/ldconfig
%postun akonadi -p /sbin/ldconfig

%post   lancelot -p /sbin/ldconfig
%postun lancelot -p /sbin/ldconfig

#%post   marble -p /sbin/ldconfig
#%postun marble -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%dir %{_kde_unstable_includedir}/lancelot-datamodels
%{_kde_unstable_includedir}/lancelot
%{_kde_unstable_includedir}/KDE/Lancelot
%{_kde_unstable_includedir}/lancelot-datamodels/
%{_kde_unstable_libdir}/liblancelot.so
%{_kde_unstable_libdir}/liblancelot-datamodels.so
%{_kde_unstable_libdir}/libplasma*.so
%{_kde_unstable_libdir}/librtm.so
%{_kde_unstable_appsdir}/cmake/modules/FindLancelot*

%files akonadi
%defattr(-,root,root)
%doc COPYING

%files lancelot
%defattr(-,root,root)
%doc COPYING
%{_kde_unstable_appsdir}/lancelot
%{_kde_unstable_bindir}/lancelot
%{_kde_unstable_modulesdir}/plasma_applet_lancelot*.so
%{_kde_unstable_libdir}/liblancelot.so.*
%{_kde_unstable_libdir}/liblancelot-datamodels.so.*
%{_kde_unstable_iconsdir}/*/*/apps/lancelot*.png
%{_kde_unstable_appsdir}/desktoptheme/*/lancelot
%{_kde_unstable_servicesdir}/lancelot.desktop
%{_kde_unstable_servicesdir}/plasma-applet-lancelot*.desktop
%{_kde_unstable_datadir}/mime/packages/lancelotpart-mime.xml

#%files marble
#%defattr(-,root,root)
#%doc COPYING
#%{_kde_unstable_modulesdir}/plasma_wallpaper_marble.so
#%{_kde_unstable_servicesdir}/plasma-wallpaper-marble.desktop

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_kde_unstable_appsdir}/plasma-applet-opendesktop-activities
%{_kde_unstable_appsdir}/bball
%{_kde_unstable_appsdir}/desktoptheme/
%exclude %{_kde_unstable_appsdir}/desktoptheme/*/lancelot
%dir %{_kde_unstable_appsdir}/kdeplasma-addons
%{_kde_unstable_appsdir}/kdeplasma-addons/mediabuttonsrc
%{_kde_unstable_appsdir}/plasma/services/
%{_kde_unstable_appsdir}/plasma-applet-*
%{_kde_unstable_appsdir}/plasmaboard/
%{_kde_unstable_appsdir}/plasma_pastebin
%{_kde_unstable_appsdir}/plasma/packages/
%{_kde_unstable_appsdir}/plasma/wallpapers/
%{_kde_unstable_appsdir}/plasma_wallpaper_pattern
%{_kde_unstable_appsdir}/rssnow
%config %{_kde_unstable_configdir}/*.knsrc
%{_kde_unstable_iconsdir}/*/*/apps/*
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/actions
%dir %{_kde_unstable_iconsdir}/hicolor/256x256
%dir %{_kde_unstable_iconsdir}/hicolor/256x256/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/actions
%dir %{_kde_unstable_iconsdir}/hicolor/scalable/actions
%exclude %{_kde_unstable_iconsdir}/*/*/apps/lancelot*.png
%{_kde_unstable_libdir}/libplasma*.so.*
%{_kde_unstable_libdir}/librtm.so.*
%{_kde_unstable_modulesdir}/plasma_*
%exclude %{_kde_unstable_modulesdir}/plasma_applet_lancelot*.so
%{_kde_unstable_modulesdir}/plasma-applet_systemloadviewer.so
#%exclude %{_kde_unstable_modulesdir}/plasma_wallpaper_marble.so
%{_kde_unstable_servicesdir}/*
%{_kde_unstable_servicetypesdir}/plasma_*.desktop
%{_kde_unstable_sharedir}/config.kcfg/kimpanelconfig.kcfg
%exclude %{_kde_unstable_servicesdir}/lancelot.desktop
%exclude %{_kde_unstable_servicesdir}/plasma-applet-lancelot*.desktop
#%exclude %{_kde_unstable_servicesdir}/plasma-wallpaper-marble.desktop
%{_kde_unstable_appsdir}/plasma/plasmoids/konqprofiles/
%{_kde_unstable_appsdir}/plasma/plasmoids/konsoleprofiles/
%{_kde_unstable_modulesdir}/krunner_*.so
%{_kde_unstable_modulesdir}/kcm_krunner_*.so
%{_kde_unstable_modulesdir}/kcm_plasma_runner_events*.so
%{_kde_unstable_iconsdir}/hicolor/*/actions/youtube.*
%{_kde_unstable_appsdir}/plasma/plasmoids/nowplaying/
%{_kde_unstable_appsdir}/plasma/plasmoids/calculator/
%if %{suse_version} > 1220
%{_kde_unstable_modulesdir}/libexec/kimpanel-ibus-panel
%endif

%changelog
