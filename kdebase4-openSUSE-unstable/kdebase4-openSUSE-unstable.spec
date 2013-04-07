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


Name:           kdebase4-openSUSE-unstable
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
BuildRequires:  fdupes
BuildRequires:  hwinfo-devel
BuildRequires:  kdebase-workspace-unstable-branding-upstream
BuildRequires:  kdebase-workspace-unstable-devel
BuildRequires:  libkde-unstable-devel
BuildRequires:  oxygen-icon-theme-unstable
BuildRequires:  rpm-devel
BuildRequires:  wallpaper-branding-openSUSE
PreReq:         %fillup_prereq
Requires:       kdebase4-workspace-unstable
Requires:       plasmoid-folderview-unstable
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_ge    libqt4-x11
%kde_unstable_runtime_requires

%description
This package contains the standard openSUSE desktop and extensions.

%package -n kdebase-workspace-unstable-branding-openSUSE
Summary:        openSUSE KDE Extension
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Requires:       kdebase-workspace-unstable
Requires:       ksplashx-branding-openSUSE = %{version}
Requires:       susegreeter-branding-openSUSE = %{version}
Requires:       wallpaper-branding-openSUSE = %{version}
Supplements:    packageand(kdebase-workspace-unstable:branding-openSUSE)
Provides:       kdebase-workspace-unstable-branding = %( echo `rpm -q --provides kdebase-workspace-unstable-branding-upstream | grep 'kdebase-workspace-unstable-branding =' | cut -d= -f2` )
Conflicts:      otherproviders(kdebase-workspace-unstable-branding)
%kde_unstable_runtime_requires

%description -n kdebase-workspace-unstable-branding-openSUSE
This package contains the standard openSUSE desktop and extensions.

%package -n kdebase-runtime-unstable-branding-openSUSE
Summary:        The KDE Runtime Components
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Supplements:    packageand(kdebase-runtime-unstable:branding-openSUSE)
Provides:       kdebase-runtime-unstable-branding = %{version}
Conflicts:      otherproviders(kdebase-runtime-unstable-branding)
%kde_unstable_runtime_requires

%description -n kdebase-runtime-unstable-branding-openSUSE
This package contains all run-time dependencies of KDE applications.

%lang_package
%prep
%setup -q -n kdebase4-openSUSE

#Make the Link to the software search from the greeter default to to the correct version of openSUSE (bnc#681131)
  sed -i s/12.1/%{version}/ greeter/greetings.cpp

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  cd ..
  for l in SUSEgreeter krpmview kde4-openSUSE; do
    %find_lang $l suse.lang
  done
  mv config-files/COPYING .
  for dir in %_kde_unstable_appsdir/plasma-desktop/init %_kde_unstable_appsdir/plasma-netbook/init %_kde_unstable_appsdir/plasma/layout-templates; do
     mkdir -p %{buildroot}$dir
     cp -a $dir/* %{buildroot}$dir/
  done
  cp -a config-files/* %{buildroot}/opt/kde-unstable/
  gzip %{buildroot}%{_kde_unstable_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svg
  mv %{buildroot}%{_kde_unstable_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svg.gz %{buildroot}%{_kde_unstable_appsdir}/desktoptheme/openSUSEdefault/widgets/branding.svgz
  chmod og-w -R %{buildroot}
  install -m644 -p %{SOURCE3} %{buildroot}%{_kde_unstable_appsdir}/kconf_update/
  install -m755 -p %{SOURCE4} %{buildroot}%{_kde_unstable_appsdir}/kconf_update/
  chmod a+x %{buildroot}%{_kde_unstable_appsdir}/kconf_update/sysinfo_to_kinfocenter.sh 
  %suse_update_desktop_file -u SUSEgreeter System Documentation
  %fdupes -s %{buildroot}%{_kde_unstable_configdir}/SuSE/default/
  %kde_unstable_post_install
  cd %{buildroot}
  patch -p0 < %{SOURCE2}

#Make the "rpm:"-search default to to the correct version of openSUSE (see bnc#695417)
  sed -i s/12.1/%{version}/ %{buildroot}%{_kde_unstable_servicesdir}/searchproviders/rpm.desktop

#remove sysinfo from the standard desktop
rm %{buildroot}%{_kde_unstable_configdir}/SuSE/default/myComputer.desktop

%files lang -f suse.lang
%defattr(-,root,root)

%files
%defattr(-,root,root)
%{_kde_unstable_applicationsdir}/konqfilemgr_rpm.desktop
%{_kde_unstable_appsdir}/krpmview
%{_kde_unstable_bindir}/kde_add_yast_source.sh
%{_kde_unstable_bindir}/kde4-migrate
%{_kde_unstable_bindir}/preloadkde
%dir %{_kde_unstable_configdir}
%dir %{_kde_unstable_configdir}/SuSE
%dir %{_kde_unstable_configdir}/SuSE/default
%{_kde_unstable_configdir}/SuSE/default/beagled-autostart.desktop.live
%{_kde_unstable_configdir}/SuSE/default/kupdateapplet-autostart.desktop.live
%{_kde_unstable_configdir}/SuSE/default/lowspacesuse.live
%{_kde_unstable_iconsdir}/hicolor/*/apps/Support.*
%{_kde_unstable_modulesdir}/libkrpmview.so
%{_kde_unstable_servicesdir}/krpmview.desktop
%{_kde_unstable_servicesdir}/searchproviders

%files -n kdebase-runtime-unstable-branding-openSUSE
%defattr(-,root,root)
%doc COPYING
%dir %{_kde_unstable_appsdir}/desktoptheme
%{_kde_unstable_appsdir}/desktoptheme/openSUSEdefault
%{_kde_unstable_appsdir}/desktoptheme/openSUSE

%files -n kdebase-workspace-unstable-branding-openSUSE
%defattr(-,root,root)
%doc COPYING
%{_kde_unstable_datadir}/autostart/
%{_kde_unstable_datadir}/opensuse-kiwi
%{_kde_unstable_applicationsdir}/SUSEgreeter.desktop
%{_kde_unstable_appsdir}/kconf_update/
%{_kde_unstable_appsdir}/konsole/
%{_kde_unstable_appsdir}/kwin/
%{_kde_unstable_appsdir}/plasma-desktop
%{_kde_unstable_appsdir}/color-schemes
%{_kde_unstable_appsdir}/SUSEgreeter
%{_kde_unstable_bindir}/SUSEgreeter
%dir %{_kde_unstable_configdir}
%dir %{_kde_unstable_configdir}/SuSE
%dir %{_kde_unstable_configdir}/SuSE/default
%{_kde_unstable_configdir}/SuSE/default/MozillaFirefox.desktop
%{_kde_unstable_configdir}/SuSE/default/Office.desktop
%{_kde_unstable_configdir}/SuSE/default/Support.desktop
%{_kde_unstable_configdir}/SuSE/default/SuSE.desktop
%{_kde_unstable_configdir}/SuSE/default/live-installer.desktop
%{_kde_unstable_configdir}/SuSE/default/documents.directory
%{_kde_unstable_configdir}/SuSE/default/clock-no-events.js.live
%{_kde_unstable_configdir}/SuSE/default/kcmnspluginrc.live
%{_kde_unstable_configdir}/SuSE/default/kdedrc.live
%{_kde_unstable_configdir}/SuSE/default/krunnerrc.live
%{_kde_unstable_configdir}/SuSE/default/kwallet.kwl.live
%{_kde_unstable_configdir}/SuSE/default/kwalletrc.live
%{_kde_unstable_configdir}/SuSE/default/mysql-local.conf.live
%{_kde_unstable_configdir}/SuSE/default/nepomukserverrc.live
%{_kde_unstable_configdir}/SuSE/default/feeds.opml
%{_kde_unstable_configdir}/SuSE/default/bookmarks.xml
%{_kde_unstable_iconsdir}/hicolor/*/apps/SUSEgreeter.*
%{_kde_unstable_iconsdir}/hicolor/*/apps/mycomp.*
%{_kde_unstable_iconsdir}/oxygen/
%{_kde_unstable_sharedir}/env/
%config %{_kde_unstable_sysconfdir}/kde4
%_kde_unstable_appsdir/plasma-desktop
%_kde_unstable_appsdir/plasma-netbook
%_kde_unstable_appsdir/plasma

%changelog
