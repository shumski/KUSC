#
# spec file for package kdebase4-workspace
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

%if %suse_version > 1220
%define with_systemd 1
%else
%define with_systemd 0
%endif

Name:           kdebase-workspace-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        The KDE Workspace Components
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
%if !%{with_systemd}
BuildRequires:  ConsoleKit-devel
%endif
%if 0%{?suse_version} > 1140
BuildRequires:  NetworkManager-devel > 0.8.997
%else
BuildRequires:  NetworkManager-devel < 0.8.5
%endif
BuildRequires:  audit-devel
BuildRequires:  bluez-devel
BuildRequires:  fdupes
BuildRequires:  gpsd-devel
BuildRequires:  libQtWebKit-devel
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libkactivities-unstable-devel
BuildRequires:  libkde-unstable-devel >= %{version}
BuildRequires:  libkdepimlibs-unstable-devel akonadi-runtime-unstable
BuildRequires:  liblazy-devel
BuildRequires:  libpolkit-qt-1-unstable-devel
BuildRequires:  libprison-devel
BuildRequires:  libqalculate-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libusb-devel
BuildRequires:  pam-devel
BuildRequires:  pciutils-devel
BuildRequires:  libqjson-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  python-devel
%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
%endif
Source0:        kde-workspace-git.tar.xz
Source1:        rcksysguardd
Source2:        titlebar_decor.png
Source3:        kwin-cubecap.png
Source91:       %{name}-rpmlintrc
Patch0:         4_7_BRANCH.diff
Patch8:         kwin-suse.diff
Patch18:        startkde.diff
Patch70:        same-pam-generic-classic.diff
Patch71:        kdm-kdmconf.diff
Patch77:        systemsettings-desktop.diff
Patch82:        rotate-wacom-pointers.diff
Patch88:        kde4-migrate.diff
Patch94:        systemsettings-root-kcm.diff
Patch104:       plasma-branding-defaults-applets.diff
Patch106:       plasma-dashboard-leave.diff
Patch107:       plasma-kickoff-newly-collapsing.diff
Patch108:       plasma-panel-resize-hint.diff
Patch125:       pam-translate.diff
Patch201:       plasma-notifications-kill-timer.diff
Patch202:       plasma-disable-networkmanager.diff
#Patch211:       disable-python-support.diff
# PATCH-FIX-OPENSUSE kdm_systemd_shutdown.patch Avoid the situation where systemd would kill KDM 
# which prevents reboot/shutdown (Fedora Patch)
Patch213:       kdm_systemd_shutdown.patch
# PATCH-FIX-OPENSUSE opensuse-homepage.diff
Patch401:       opensuse-homepage.diff
Patch999:       desktop_files.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %suse_version > 1200
Requires:       %{name}-branding = %{version}
%else
Requires:       %{name}-branding
%endif
Requires:       %{name}-ksysguardd = %{version}
Requires:       %{name}-liboxygenstyle = %{version}
# Requires /etc/xdg/menus/applications.menu (bnc#754104)
Requires:       desktop-data-openSUSE
Requires:       kactivities-unstable >= %{version}
Requires:       kde4-kgreeter-plugins-unstable = %{version}
#Requires:       polkit-kde-kcmmodules-1
Requires:       kde-base-artwork-unstable
# patch kdm-sysconfig-values.diff requires /var/lib/xdm/authdir/authfiles (bnc#784212)
Requires:       xdm
Requires:       /usr/share/polkit-1/actions/org.kde.fontinst.policy
Recommends:     kwin-unstable
Recommends:     plasma-addons-unstable
Recommends:     python-kdebase-unstable
Suggests:       kdebase-wallpapers-unstable
Requires(pre):  permissions
%define debug_package_requires %{name} = %{version}-%{release} kdelibs-unstable-debuginfo
%kde_unstable_runtime_requires
%define _dminitdir %{_kde_unstable_prefix}/lib/X11/displaymanagers

%description
This package contains the basic packages for a K Desktop Environment
workspace.

%package branding-upstream
Summary:        The KDE Workspace Components
Group:          System/GUI/KDE
Provides:       %{name}-branding = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)

%description branding-upstream
This package contains the basic packages for a K Desktop Environment
workspace.

%package ksysguardd
Summary:        KDE base package: ksysguard daemon
Group:          System/GUI/KDE
Requires(pre):  %insserv_prereq
%kde_unstable_runtime_requires

%description ksysguardd
This package contains the ksysguard daemon. It is needed for ksysguard.

This package can be installed on servers without any other KDE packages
to enable monitoring them remotely with ksysguard.

%package -n kwin-unstable
Summary:        KDE Window Manager
Group:          System/GUI/KDE
Provides:       windowmanager
%kde_unstable_runtime_requires
%if %suse_version > 1200
Requires:       %{name}-branding = %{version}
%else
Requires:       %{name}-branding
%endif

%description -n kwin-unstable
KWin is the window manager of the K desktop environment.

%package -n kde4-kgreeter-plugins-unstable
Summary:        The KDE Greeter Plugin Components
Group:          System/GUI/KDE
Provides:       windowmanager
%kde_unstable_runtime_requires

%description -n kde4-kgreeter-plugins-unstable
This package contains the Greeter Plugins that are needed by KDM and
Screensaver unlocking

%package devel
Summary:        The KDE Workspace Components
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       kwin-unstable = %{version}
Requires:       libQtWebKit-devel
Requires:       libkde-unstable-devel
%kde_unstable_runtime_requires

%description devel
This package contains the basic packages for a K Desktop Environment
workspace.

%package liboxygenstyle
Summary:        The Libraries of the oxygen-style
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
%kde_unstable_runtime_requires

%description liboxygenstyle
This package contains the libraries of the oxygen style.

%package plasma-calendar
Summary:        The calendar Plasma engine and applet
Group:          System/GUI/KDE
Supplements:    packageand(akonadi-runtime-unstable:kdebase4-workspace-unstable)
Provides:       kdebase4-workspace-unstable:%_libdir/kde4/plasma_engine_calendar.so
Requires:       %{name} = %{version}
%kde_unstable_akonadi_requires

%description plasma-calendar
This packages contains the calendar Plasma engine and applet, which are based on Akonadi.

%prep
%setup -q -n kde-workspace-git
%patch0 -p1
###KDE47: rewrite!
#%%patch8
%patch18
%patch70 -p0
%patch71
%patch77
%patch82
%patch88
### Remove when KDM KCM configuration bugs are fixed
###KDE47: rediff!
#%%patch94
%patch104
%patch106
%patch107
%patch108
###KDE47: rediff
#%%patch125
%patch201 -p1
%patch202 -p1
#patch211
%patch213 -p1
%patch401 -p1
%patch999 -p1
cp %{SOURCE3} kwin/effects/cube/data/cubecap.png

%build
### TODO: -DKDE4_ENABLE_FINAL=1
  EXTRA_FLAGS="-DKDE4_COMMON_PAM_SERVICE=xdm \
      -DKDE4_KCHECKPASS_PAM_SERVICE=xdm \
      -DSYSCONF_INSTALL_DIR=/opt/kde-unstable/etc \
      -DKDE4_ENABLE_FPIE=1"
  %cmake_kde_unstable -d build -- $EXTRA_FLAGS
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  install -m 644 %{SOURCE2} %{buildroot}%{_kde_unstable_appsdir}/kwin/
  %create_subdir_filelist -d kwin      -v devel
  %create_subdir_filelist -d ksysguard -v devel
  cd ..
  ls -1 %{buildroot}%{_kde_unstable_wallpapersdir}/ | while read wallpaper; \
    do test "$wallpaper" = "Elarun" -o ! -d "%{buildroot}%{_kde_unstable_wallpapersdir}/$wallpaper" \
	|| rm -r "%{buildroot}%{_kde_unstable_wallpapersdir}/$wallpaper"; done
  mkdir -p %{buildroot}/etc
  rm -rf %{buildroot}%{_kde_unstable_htmldir}/en/kicker
  pushd $RPM_BUILD_DIR/%buildsubdir/
  cat filelists/devel filelists/kwin | while read line; do echo "%exclude $line";done >filelists/exclude
  popd
  %suse_update_desktop_file    systemsettings X-SuSE-core
  %suse_update_desktop_file    ksysguard      System Monitor
  %suse_update_desktop_file    kmenuedit      Core-Configuration
  %suse_update_desktop_file -r klipper        System TrayIcon
  %suse_update_desktop_file -r krandrtray     System TrayIcon
  %fdupes -s %{buildroot}
  %kde_unstable_post_install

%clean
  rm -rf %{buildroot}
  rm -rf filelists

%if 0%{?suse_version} >= 1140
%verifyscript
%verify_permissions -e %{_kde_unstable_libexecdir}/kcheckpass
%verify_permissions -e %{_kde_unstable_libexecdir}/kdesud
%endif

%post
/sbin/ldconfig
%if 0%{?suse_version} >= 1140
%set_permissions %{_kde_unstable_libexecdir}/kcheckpass
%set_permissions %{_kde_unstable_libexecdir}/kdesud
%endif

%postun -p /sbin/ldconfig

%preun ksysguardd

%post ksysguardd
/sbin/ldconfig

%postun ksysguardd
/sbin/ldconfig
exit 0

%post   -n kwin-unstable -p /sbin/ldconfig

%postun -n kwin-unstable -p /sbin/ldconfig

%post   liboxygenstyle -p /sbin/ldconfig

%postun liboxygenstyle -p /sbin/ldconfig

%package -n python-kdebase4-unstable
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        Python bindings for KDE 4 desktop shell
Requires:       python-kde4-unstable = %{version}

%description -n python-kdebase4-unstable
Python bindings for Plasma, the KDE 4 desktop shell.  These bindings
allow Plasmoids written in Python


%files branding-upstream
%defattr(-,root,root)
%doc COPYING
%{_kde_unstable_appsdir}/kwin/cubecap.png
%{_kde_unstable_appsdir}/kwin/titlebar_decor.png
%dir %{_kde_unstable_wallpapersdir}
%if 0%{?suse_version} > 1140
%{_kde_unstable_appsdir}/plasma-desktop/init
%{_kde_unstable_appsdir}/plasma-netbook/init
%{_kde_unstable_appsdir}/plasma/layout-templates
%endif

%files -n kde4-kgreeter-plugins-unstable
%defattr(-,root,root)
%{_kde_unstable_modulesdir}/kgreet_*.so

%files ksysguardd -f filelists/ksysguard
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_appsdir}/ksysguard/
%config(noreplace) %{_kde_unstable_sysconfdir}/ksysguarddrc
%config %{_kde_unstable_configdir}/ksysguard.knsrc
%dir %{_kde_unstable_iconsdir}/oxygen/16x16

%files -n kwin-unstable -f filelists/kwin
%defattr(-,root,root)
%doc COPYING COPYING.DOC README kwin/clients/aurorae/theme-description
%dir %{_kde_unstable_servicesdir}/kwin
%exclude %{_kde_unstable_appsdir}/kwin/cubecap.png
%exclude %{_kde_unstable_appsdir}/kwin/titlebar_decor.png
%{_kde_unstable_appsdir}/kwin/default_rules/plasma_desktop_containment.kwinrules
%dir %{_kde_unstable_iconsdir}/oxygen/128x128
%dir %{_kde_unstable_iconsdir}/oxygen/16x16
%dir %{_kde_unstable_iconsdir}/oxygen/22x22
%dir %{_kde_unstable_iconsdir}/oxygen/32x32
%dir %{_kde_unstable_iconsdir}/oxygen/48x48
%dir %{_kde_unstable_iconsdir}/oxygen/64x64
%dir %{_kde_unstable_datadir}/sounds

%files liboxygenstyle
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_libdir}/liboxygenstyle.*
%dir %{_kde_unstable_modulesdir}/plugins/styles
%{_kde_unstable_modulesdir}/plugins/styles/oxygen.so

%files plasma-calendar
%defattr(-,root,root)
%{_kde_unstable_modulesdir}/plasma_*_calendar.so
%{_kde_unstable_servicesdir}/plasma-*-calendar.desktop

%files devel -f filelists/devel
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_includedir}/*
%{_kde_unstable_appsdir}/cmake
%{_kde_unstable_libdir}/liblsofui.so
%{_kde_unstable_modulesdir}/plugins/designer/ksysguardlsofwidgets.so
%{_kde_unstable_libdir}/libsolidcontrolifaces.so
%{_kde_unstable_libdir}/libsolidcontrol.so
%{_kde_unstable_libdir}/libkworkspace.so
%{_kde_unstable_libdir}/libkscreensaver.so
%{_kde_unstable_libdir}/libprocesscore.so
%{_kde_unstable_libdir}/libprocessui.so
%{_kde_unstable_libdir}/libksgrd.so
%{_kde_unstable_libdir}/libtaskmanager.so
%{_kde_unstable_libdir}/libksignalplotter.so
%{_kde_unstable_libdir}/libweather_ion.so
%{_kde_unstable_libdir}/libkfontinst.so
%{_kde_unstable_libdir}/libkfontinstui.so
%{_kde_unstable_libdir}/libplasmaclock.so
%{_kde_unstable_libdir}/libkephal.so
%{_kde_unstable_libdir}/libplasma_applet-system-monitor.so
%{_kde_unstable_libdir}/libplasma-geolocation-interface.so
%{_kde_unstable_libdir}/libplasmagenericshell.so
%{_kde_unstable_libdir}/libsystemsettingsview.so
%{_kde_unstable_libdir}/cmake/KDE4Workspace/

%files -f filelists/exclude
%defattr(-,root,root)
#positives
%doc COPYING COPYING.DOC README
%doc %lang(en) %{_kde_unstable_htmldir}/en/
%{_kde_unstable_applicationsdir}/
%{_kde_unstable_appsdir}/
%{_kde_unstable_bindir}/*
%config %{_kde_unstable_configdir}/
%config %{_kde_unstable_configkcfgdir}/
%{_kde_unstable_datadir}/autostart/
%{_kde_unstable_datadir}/dbus-1/
%{_kde_unstable_datadir}/polkit-1/
%{_kde_unstable_iconsdir}/Oxygen*
%{_kde_unstable_iconsdir}/hicolor/*/*/*
%{_kde_unstable_iconsdir}/oxygen/*/*
%{_kde_unstable_libdir}/kconf_update_bin/
%dir %{_kde_unstable_libdir}/strigi
%{_kde_unstable_libdir}/strigi/strigita_font.so
%{_kde_unstable_libdir}/*.so
%{_kde_unstable_libdir}/*.so.*
%attr(-, root, shadow) %{_kde_unstable_libexecdir}/kcheckpass
%{_kde_unstable_modulesdir}/
%{_kde_unstable_sharedir}/services/
%{_kde_unstable_sharedir}/servicetypes/
%{_kde_unstable_wallpapersdir}/stripes.png
%{_kde_unstable_wallpapersdir}/stripes.png.desktop
%config %{_kde_unstable_sysconfdir}/dbus-1/system.d/org.kde.*
%dir %{_kde_unstable_iconsdir}/hicolor/128x128
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/apps
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/22x22
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps
%dir %{_kde_unstable_iconsdir}/oxygen/128x128
%dir %{_kde_unstable_iconsdir}/oxygen/16x16
%dir %{_kde_unstable_iconsdir}/oxygen/22x22
%dir %{_kde_unstable_iconsdir}/oxygen/32x32
%dir %{_kde_unstable_iconsdir}/oxygen/48x48
%dir %{_kde_unstable_iconsdir}/oxygen/64x64

#blacklist
%exclude %{_kde_unstable_sharedir}/apps/plasma_scriptengine_python
%exclude %{_kde_unstable_applicationsdir}/ksysguard.desktop
%exclude %{_kde_unstable_appsdir}/kwin/default_rules/plasma_desktop_containment.kwinrules
%exclude %{_kde_unstable_appsdir}/cmake
%exclude %{_kde_unstable_appsdir}/doc
%exclude %{_kde_unstable_appsdir}/doc/kdm
%exclude %{_kde_unstable_appsdir}/kdm
%exclude %{_kde_unstable_appsdir}/ksysguard
%exclude %{_kde_unstable_appsdir}/kwin/cubecap.png
%exclude %{_kde_unstable_appsdir}/kwin/titlebar_decor.png
%exclude %{_kde_unstable_bindir}/ksysguard
%exclude %{_kde_unstable_bindir}/ksysguardd
%exclude %{_kde_unstable_configdir}/kdm
%exclude %{_kde_unstable_configdir}/kdm/backgroundrc
%exclude %{_kde_unstable_configdir}/ksysguard.knsrc
%exclude %{_kde_unstable_htmldir}/en/kdm
%exclude %{_kde_unstable_htmldir}/en/ksysguard
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/daemon.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/ksysguardd.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/waiting.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/kernel.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/computer.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/running.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/unknownapp.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/kdeapp.png
%exclude %{_kde_unstable_iconsdir}/oxygen/16x16/apps/shell.png
%exclude %{_kde_unstable_libdir}/libkdeinit4_ksysguard.so
%exclude %{_kde_unstable_libdir}/libkephal.so
%exclude %{_kde_unstable_libdir}/libkfontinst.so
%exclude %{_kde_unstable_libdir}/libkfontinstui.so
%exclude %{_kde_unstable_libdir}/libkscreensaver.so
%exclude %{_kde_unstable_libdir}/libksignalplotter.so
%exclude %{_kde_unstable_libdir}/libksgrd.so
%exclude %{_kde_unstable_libdir}/libkworkspace.so
%exclude %{_kde_unstable_libdir}/liblsofui.so
%exclude %{_kde_unstable_libdir}/liboxygenstyle.*
%exclude %{_kde_unstable_libdir}/libplasmaclock.so
%exclude %{_kde_unstable_libdir}/libplasmagenericshell.so
%exclude %{_kde_unstable_libdir}/libplasma_applet-system-monitor.so
%exclude %{_kde_unstable_libdir}/libplasma-geolocation-interface.so
%exclude %{_kde_unstable_libdir}/libprocesscore.so
%exclude %{_kde_unstable_libdir}/libprocessui.so
%exclude %{_kde_unstable_libdir}/libsolidcontrol.so
%exclude %{_kde_unstable_libdir}/libsolidcontrolifaces.so
%exclude %{_kde_unstable_libdir}/libsystemsettingsview.so
%exclude %{_kde_unstable_libdir}/libtaskmanager.so
%exclude %{_kde_unstable_libdir}/libweather_ion.so
%exclude %{_kde_unstable_modulesdir}/kcm_kdm.so
%exclude %{_kde_unstable_modulesdir}/kgreet_*.so
%exclude %{_kde_unstable_modulesdir}/plasma_*_calendar.so
%exclude %{_kde_unstable_modulesdir}/plugins/designer/ksysguardlsofwidgets.so
%exclude %{_kde_unstable_modulesdir}/plugins/styles
%exclude %{_kde_unstable_modulesdir}/plugins/styles/oxygen.so
%exclude %{_kde_unstable_servicesdir}/kwin
%exclude %{_kde_unstable_servicesdir}/plasma-*-calendar.desktop
%exclude %{_kde_unstable_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%if 0%{?suse_version} > 1140
%exclude %{_kde_unstable_appsdir}/plasma-desktop/init
%exclude %{_kde_unstable_appsdir}/plasma-netbook/init
%exclude %{_kde_unstable_appsdir}/plasma/layout-templates
%endif
%exclude %{_kde_unstable_servicesdir}/plasma-scriptengine-applet-python.desktop
%exclude %{_kde_unstable_servicesdir}/plasma-scriptengine-dataengine-python.desktop
%exclude %{_kde_unstable_servicesdir}/plasma-scriptengine-runner-python.desktop
%exclude %{_kde_unstable_servicesdir}/plasma-scriptengine-wallpaper-python.desktop


%files -n python-kdebase4-unstable
%defattr(-,root,root)
%doc COPYING README
%dir %{_kde_unstable_py_sitedir}/PyKDE4
%dir %{_kde_unstable_libdir}/python2.7
%dir %{_kde_unstable_libdir}/python2.7/site-packages
%{_kde_unstable_py_sitedir}/PyKDE4/plasmascript.*
%{_kde_unstable_sharedir}/apps/plasma_scriptengine_python
%{_kde_unstable_servicesdir}/plasma-scriptengine-applet-python.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-dataengine-python.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-runner-python.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-wallpaper-python.desktop

%changelog
