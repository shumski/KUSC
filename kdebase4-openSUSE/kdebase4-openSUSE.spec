#
# spec file for package kdebase4-openSUSE
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


Name:           kdebase4-openSUSE
Version:        12.3
Release:        0
Summary:        openSUSE KDE Extension
License:        GPL-2.0+
Group:          System/GUI/KDE
# git clone git://github.com/openSUSE/kdebase-opensuse.git
Url:            http://www.opensuse.org/
Source0:        kdebase4-openSUSE-%{version}.tar.bz2
Source2:        plasma-change-defaults.diff
Source3:        plasma-cache.upd
Source4:        plasma-cache.sh
Patch0:         remove_path.diff
BuildRequires:  fdupes
BuildRequires:  hwinfo-devel
BuildRequires:  kdebase4-workspace-branding-upstream
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  libkde4-devel
BuildRequires:  oxygen-icon-theme
BuildRequires:  rpm-devel
BuildRequires:  wallpaper-branding-openSUSE

PreReq:         %fillup_prereq
Requires:       kdebase4-workspace
Requires:       plasmoid-folderview
Recommends:     %{name}-lang
Provides:       kdebase4-SuSE = %{version}
Obsoletes:      kdebase4-SuSE < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_ge    libqt4-x11
%kde4_runtime_requires

%description
This package contains the standard openSUSE desktop and extensions.

%package -n kdebase4-workspace-branding-openSUSE
Summary:        openSUSE KDE Extension
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Requires:       kdebase4-workspace
Requires:       ksplashx-branding-openSUSE = %{version}
Requires:       susegreeter-branding-openSUSE = %{version}
Requires:       wallpaper-branding-openSUSE = %{version}
Supplements:    packageand(kdebase4-workspace:branding-openSUSE)
Provides:       kdebase4-workspace-branding = %( echo `rpm -q --provides kdebase4-workspace-branding-upstream | grep 'kdebase4-workspace-branding =' | cut -d= -f2` )
Conflicts:      otherproviders(kdebase4-workspace-branding)
%kde4_runtime_requires

%description -n kdebase4-workspace-branding-openSUSE
This package contains the standard openSUSE desktop and extensions.

%package -n kdebase4-runtime-branding-openSUSE
Summary:        The KDE Runtime Components
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Supplements:    packageand(kdebase4-runtime:branding-openSUSE)
Provides:       kdebase4-runtime-branding = %{version}
Conflicts:      otherproviders(kdebase4-runtime-branding)
%kde4_runtime_requires

%description -n kdebase4-runtime-branding-openSUSE
This package contains all run-time dependencies of KDE applications.

%lang_package
%prep
%setup -q -n %{name}
%patch0 -p1

#Make the Link to the software search from the greeter default to to the correct version of openSUSE (bnc#681131)
  sed -i s/12.1/%{version}/ greeter/greetings.cpp

%build
  %cmake_kde4 -d build
  %make_jobs

%install
  cd build
  %kde4_makeinstall
  cd ..
  for l in SUSEgreeter krpmview kde4-openSUSE; do
    %find_lang $l suse.lang
  done
  mv config-files/COPYING .
  for dir in %_kde4_appsdir/plasma-desktop/init %_kde4_appsdir/plasma-netbook/init %_kde4_appsdir/plasma/layout-templates; do
     mkdir -p %{buildroot}$dir
     cp -a $dir/* %{buildroot}$dir/
  done
  cp -a config-files/* %{buildroot}
  gzip %{buildroot}%{_kde4_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svg
  mv %{buildroot}%{_kde4_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svg.gz %{buildroot}%{_kde4_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svgz
  chmod og-w -R %{buildroot}
  install -m644 -p %{SOURCE3} %{buildroot}%{_kde4_appsdir}/kconf_update/
  install -m755 -p %{SOURCE4} %{buildroot}%{_kde4_appsdir}/kconf_update/
  chmod a+x %{buildroot}/usr/share/kde4/apps/kconf_update/sysinfo_to_kinfocenter.sh 
  %suse_update_desktop_file -u SUSEgreeter System Documentation
  %fdupes -s %{buildroot}%{_kde4_configdir}/SuSE/default/
  %kde_post_install
  cd %{buildroot}
  patch -p0 < %{SOURCE2}

#Make the "rpm:"-search default to to the correct version of openSUSE (see bnc#695417)
  sed -i s/12.1/%{version}/ %{buildroot}%{_kde4_servicesdir}/searchproviders/rpm.desktop

#remove sysinfo from the standard desktop
rm %{buildroot}%{_kde4_configdir}/SuSE/default/myComputer.desktop

%post -n kdebase4-workspace-branding-openSUSE
%{fillup_only -n windowmanager -s kde4}

%files lang -f suse.lang
%defattr(-,root,root)

%files
%defattr(-,root,root)
%{_kde4_applicationsdir}/konqfilemgr_rpm.desktop
%{_kde4_appsdir}/krpmview
%{_kde4_bindir}/kde_add_yast_source.sh
%{_kde4_bindir}/kde4-migrate
%{_kde4_bindir}/preloadkde
%dir %{_kde4_configdir}
%dir %{_kde4_configdir}/SuSE
%dir %{_kde4_configdir}/SuSE/default
%{_kde4_configdir}/SuSE/default/beagled-autostart.desktop.live
%{_kde4_configdir}/SuSE/default/kupdateapplet-autostart.desktop.live
%{_kde4_configdir}/SuSE/default/lowspacesuse.live
%{_kde4_iconsdir}/hicolor/*/apps/Support.*
%{_kde4_modulesdir}/libkrpmview.so
%{_kde4_servicesdir}/krpmview.desktop
%{_kde4_servicesdir}/searchproviders

%files -n kdebase4-runtime-branding-openSUSE
%defattr(-,root,root)
%doc COPYING
%dir %{_kde4_appsdir}/desktoptheme
%{_kde4_appsdir}/desktoptheme/openSUSEdefault
%{_kde4_appsdir}/desktoptheme/openSUSE

%files -n kdebase4-workspace-branding-openSUSE
%defattr(-,root,root)
%doc COPYING
%{_datadir}/autostart/
%{_datadir}/opensuse-kiwi
%{_kde4_applicationsdir}/SUSEgreeter.desktop
%{_kde4_appsdir}/kconf_update/
%{_kde4_appsdir}/konsole/
%{_kde4_appsdir}/kwin/
%{_kde4_appsdir}/plasma-desktop
%{_kde4_appsdir}/color-schemes
%{_kde4_appsdir}/SUSEgreeter
%{_kde4_bindir}/SUSEgreeter
%dir %{_kde4_configdir}
%dir %{_kde4_configdir}/SuSE
%dir %{_kde4_configdir}/SuSE/default
%{_kde4_configdir}/SuSE/default/MozillaFirefox.desktop
%{_kde4_configdir}/SuSE/default/Office.desktop
%{_kde4_configdir}/SuSE/default/Support.desktop
%{_kde4_configdir}/SuSE/default/SuSE.desktop
%{_kde4_configdir}/SuSE/default/live-installer.desktop
%{_kde4_configdir}/SuSE/default/documents.directory
%{_kde4_configdir}/SuSE/default/clock-no-events.js.live
%{_kde4_configdir}/SuSE/default/kcmnspluginrc.live
%{_kde4_configdir}/SuSE/default/kdedrc.live
%{_kde4_configdir}/SuSE/default/krunnerrc.live
%{_kde4_configdir}/SuSE/default/kwallet.kwl.live
%{_kde4_configdir}/SuSE/default/kwalletrc.live
%{_kde4_configdir}/SuSE/default/mysql-local.conf.live
%{_kde4_configdir}/SuSE/default/nepomukserverrc.live
%{_kde4_configdir}/SuSE/default/feeds.opml
%{_kde4_configdir}/SuSE/default/bookmarks.xml
%{_kde4_iconsdir}/hicolor/*/apps/SUSEgreeter.*
%{_kde4_iconsdir}/hicolor/*/apps/mycomp.*
%{_kde4_iconsdir}/oxygen/
%{_kde4_sharedir}/env/
%{_localstatedir}/adm/fillup-templates/sysconfig.windowmanager-kde4
%config %{_sysconfdir}/kde4
%_kde4_appsdir/plasma-desktop
%_kde4_appsdir/plasma-netbook
%_kde4_appsdir/plasma

%changelog
