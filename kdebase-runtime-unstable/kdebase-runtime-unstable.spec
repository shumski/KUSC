#
# spec file for package kdebase4-runtime
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

Name:           kdebase-runtime-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        The KDE Runtime Components
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source0:        kde-runtime-git.tar.xz
Source1:        kde4-essential.menu
Source2:        kde-settings.menu
Source3:        kde-settings.directory
Source4:        KDE-Sys-Log-Out.ogg
Source98:       kdebase-runtime-unstable-rpmlintrc
Source99:       nepomuk.png
Patch0:         4_7_BRANCH.diff
Patch2:         phonon-wakeups.diff
Patch3:         hotplug-kde3.diff
Patch4:         kde4-wrapper.diff
Patch5:         kdesu-remember-keep-password.diff
Patch7:         simple-ccsm-kde.diff
Patch10:        khelpcenter-gnome-support.patch
Patch11:        khelpcenter-use-susehelp.patch
Patch15:        kdesu-symbol-lookup-workaround.diff
Patch16:        phonon-always-forget.diff
Patch17:        desktop-files.diff
BuildRequires:  NetworkManager-devel
BuildRequires:  QtZeitgeist-devel
BuildRequires:  bluez-devel
BuildRequires:  fdupes
BuildRequires:  libcanberra-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libkde-unstable-devel >= %{version} kdelibs-unstable kdelibs-unstable-doc
BuildRequires:  libksuseinstall-unstable-devel
BuildRequires:  libpulse-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  libusb-devel
BuildRequires:  lzma-devel
BuildRequires:  openslp-devel
BuildRequires:  xz
BuildRequires:  libkactivities-unstable-devel
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  libkdepimlibs-unstable-devel
BuildRequires:  nepomuk-core-unstable-devel
PreReq:         permissions
Requires:       dbus-1-x11
Requires:       kdelibs-unstable >= %{version}
Requires:       oxygen-icon-theme-unstable >= 4.6.40
Requires:       phonon-unstable
Requires:       nepomuk-core-unstable
Recommends:     enscript
#htdig is needed by khelpcenter for indexing help files
Recommends:     htdig
Recommends:     ispell
Recommends:     kdialog
Suggests:       cagibi
Provides:       suse_help_viewer
%define debug_package_requires %{name} = %{version}-%{release} kdelibs-unstable-debuginfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):     shared-mime-info
Requires(postun):   shared-mime-info
%if 0%{?suse_version} == 1130
Requires:       %{name}-branding = 11.3
%endif
%if 0%{?suse_version} == 1140
Requires:       %{name}-branding = 11.4
%endif
%if 0%{?suse_version} == 1210
Requires:       %{name}-branding = 12.1
%endif
%if 0%{?suse_version} == 1220
Requires:       %{name}-branding = 12.2
%endif
%if 0%{?suse_version} > 1220
Requires:       %{name}-branding = 12.3
%endif
%kde_unstable_runtime_requires

%description
This package contains all run-time dependencies of KDE applications.

%package branding-upstream
Summary:        The KDE Runtime Components
Group:          System/GUI/KDE
#BRAND: FIXME
%if 0%{?suse_version} == 1130
Provides:       kdebase-runtime-unstable-branding = 11.3
%endif
%if 0%{?suse_version} == 1140
Provides:       kdebase-runtime-unstable-branding = 11.4
%endif
%if 0%{?suse_version} == 1210
Provides:       kdebase-runtime-unstable-branding = 12.1
%endif
%if 0%{?suse_version} == 1220
Provides:       kdebase-runtime-unstable-branding = 12.2
%endif
%if 0%{?suse_version} > 1220
Provides:       kdebase-runtime-unstable-branding = 12.3
%endif
Supplements:    packageand(kdebase-runtime-unstable:branding-upstream)
Conflicts:      otherproviders(kdebase-runtime-unstable-branding)

%description branding-upstream
This package contains all run-time dependencies of KDE applications.

%package -n plasma-theme-oxygen-unstable
Summary:        The Oxygen Plasma Theme
Group:          System/GUI/KDE
Provides:       kdebase-runtime-unstable:/opt/kde-unstable/share/kde4/apps/desktoptheme/oxygen/metadata.desktop

%description -n plasma-theme-oxygen-unstable
This package contains the Plasma theme Oxygen.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
This package contains development files and headers needed to
build software using %{name}

%prep
%setup -q -n kde-runtime-git
cp %{SOURCE4} $RPM_BUILD_DIR/kde-runtime-git/knotify/sounds/
%patch0 -p1
# causes crashes, disabled for now
#%patch2
%patch3
%patch4
%patch5
%patch7
%patch10
%patch11
%patch15
%patch16
%patch17

%build
  %cmake_kde_unstable -d build -- -DKDE4_ENABLE_FPIE=1
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  rm -rf %{buildroot}%{_kde_unstable_datadir}/wallpapers
  rm -rf %{buildroot}%{_kde_unstable_iconsdir}/hicolor/index.theme
  rm -rf %{buildroot}%{_kde_unstable_iconsdir}/oxygen
  mkdir -p %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus
  mv %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/kde-information.menu %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/kde4-information.menu
  mkdir -p %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/applications-merged
  install -m 644 %{SOURCE1} %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/applications-merged/kde4-essential.menu
  install -m 644 %{SOURCE2} %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/kde4-settings.menu
  install -m 644 %{SOURCE3} %{buildroot}%{_kde_unstable_datadir}/desktop-directories/
  mkdir -p %{buildroot}%{_kde_unstable_prefix}/bin
  ln -s %{_kde_unstable_libexecdir}/kdesu %{buildroot}%{_kde_unstable_bindir}/kdesu
  rm -rf %{buildroot}%{_kde_unstable_includedir}/KDE
  %fdupes -s %{buildroot}
  %kde_unstable_post_install

%post
/sbin/ldconfig
%{_kde_unstable_bindir}/update-mime-database %{_kde_unstable_datadir}/mime &> /dev/null || :
%if 0%{?suse_version} > 1130
%set_permissions %{_kde_unstable_libexecdir}/kdesud
%endif

%postun
/sbin/ldconfig
%{_kde_unstable_bindir}/update-mime-database %{_kde_unstable_datadir}/mime &> /dev/null || :

%verifyscript
%verify_permissions -e %{_kde_unstable_bindir}/kcheckpass
%verify_permissions -e %{_kde_unstable_bindir}/kdesud
%verify_permissions -e %{_kde_unstable_libexecdir}/kdesud

%clean
rm -rf %{buildroot}

%files branding-upstream
%defattr(-,root,root)
%doc COPYING

%files -n plasma-theme-oxygen-unstable
%defattr(-,root,root)
%doc COPYING
%{_kde_unstable_appsdir}/desktoptheme/oxygen

%files devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/knotify_export*
%{_kde_unstable_includedir}/knotifyconfig.h
%{_kde_unstable_includedir}/knotifyplugin.h

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB

# --- knewstuff sources ---
%config %{_kde_unstable_configdir}/emoticons.knsrc
%config %{_kde_unstable_configdir}/icons.knsrc
%config %{_kde_unstable_configdir}/khotnewstuff.knsrc
%config %{_kde_unstable_configdir}/khotnewstuff_upload.knsrc

# --- menus ---
%config %{_kde_unstable_sysconfdir}/xdg/menus/applications-merged
%config %{_kde_unstable_sysconfdir}/xdg/menus/kde4-information.menu
%config %{_kde_unstable_sysconfdir}/xdg/menus/kde4-settings.menu

# --- dbus configuraton ---
%config %{_kde_unstable_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmremotewidgets.conf

# --- default configurations ---
%config %{_kde_unstable_configkcfgdir}/khelpcenter.kcfg
%config %{_kde_unstable_configkcfgdir}/jpegcreatorsettings.kcfg

# --- misc configuration ---
%config %{_kde_unstable_configdir}/kshorturifilterrc

# --- man file manuals ---
%doc %{_kde_unstable_mandir}/man1/kdesu.1*
%doc %{_kde_unstable_mandir}/man8/nepomukserver.8
%doc %{_kde_unstable_mandir}/man8/nepomukservicestub.8
%doc %{_kde_unstable_mandir}/man1/plasmapkg.1

# --- html manuals  ---
%doc %lang(en) %{_kde_unstable_htmldir}/en/kcontrol
%doc %lang(en) %{_kde_unstable_htmldir}/en/kdebugdialog
%doc %lang(en) %{_kde_unstable_htmldir}/en/kdesu
%doc %lang(en) %{_kde_unstable_htmldir}/en/khelpcenter
%doc %lang(en) %{_kde_unstable_htmldir}/en/kioslave
%doc %lang(en) %{_kde_unstable_htmldir}/en/knetattach
%doc %lang(en) %{_kde_unstable_htmldir}/en/network
%doc %lang(en) %{_kde_unstable_htmldir}/en/onlinehelp
%doc %lang(en) %{_kde_unstable_htmldir}/en/fundamentals

# --- thumbnail generators ---
%{_kde_unstable_modulesdir}/comicbookthumbnail.so
%{_kde_unstable_modulesdir}/cursorthumbnail.so
%{_kde_unstable_modulesdir}/djvuthumbnail.so
%{_kde_unstable_modulesdir}/exrthumbnail.so
%{_kde_unstable_modulesdir}/fixhosturifilter.so
%{_kde_unstable_modulesdir}/htmlthumbnail.so
%{_kde_unstable_modulesdir}/imagethumbnail.so
%{_kde_unstable_modulesdir}/jpegthumbnail.so
%{_kde_unstable_modulesdir}/svgthumbnail.so
%{_kde_unstable_modulesdir}/textthumbnail.so
%{_kde_unstable_modulesdir}/windowsexethumbnail.so
%{_kde_unstable_modulesdir}/windowsimagethumbnail.so

# --- kcm modules ---
%{_kde_unstable_modulesdir}/kcm_attica.so
%{_kde_unstable_modulesdir}/kcm_cgi.so
%{_kde_unstable_modulesdir}/kcm_componentchooser.so
%{_kde_unstable_modulesdir}/kcm_device_automounter.so
%{_kde_unstable_modulesdir}/kcm_emoticons.so
%{_kde_unstable_modulesdir}/kcm_filetypes.so
%{_kde_unstable_modulesdir}/kcm_icons.so
%{_kde_unstable_modulesdir}/kcm_kded.so
%{_kde_unstable_modulesdir}/kcm_kdnssd.so
%{_kde_unstable_modulesdir}/kcm_knotify.so
%{_kde_unstable_modulesdir}/kcm_locale.so
%{_kde_unstable_modulesdir}/kcm_nepomuk.so
%{_kde_unstable_modulesdir}/kcm_phonon.so
%{_kde_unstable_modulesdir}/kcmspellchecking.so
%{_kde_unstable_modulesdir}/kcm_trash.so

# --- kded modules ---
%{_kde_unstable_modulesdir}/kded_desktopnotifier.so
%{_kde_unstable_modulesdir}/kded_device_automounter.so
%{_kde_unstable_modulesdir}/kded_kpasswdserver.so
%{_kde_unstable_modulesdir}/kded_ktimezoned.so
%{_kde_unstable_modulesdir}/kded_nepomuksearchmodule.so
%{_kde_unstable_modulesdir}/kded_networkstatus.so
%{_kde_unstable_modulesdir}/kded_networkwatcher.so
%{_kde_unstable_modulesdir}/kded_phononserver.so
%{_kde_unstable_modulesdir}/kded_remotedirnotify.so
%{_kde_unstable_modulesdir}/kded_solidautoeject.so
%{_kde_unstable_modulesdir}/kded_soliduiserver.so

# --- kdeinit modules ---
%{_kde_unstable_libdir}/libkdeinit4_kcmshell4.so
%{_kde_unstable_libdir}/libkdeinit4_kglobalaccel.so
%{_kde_unstable_libdir}/libkdeinit4_khelpcenter.so
%{_kde_unstable_libdir}/libkdeinit4_kuiserver.so
%{_kde_unstable_libdir}/libkdeinit4_kwalletd.so

# --- kio slaves ---
%{_kde_unstable_modulesdir}/kio_about.so
%{_kde_unstable_modulesdir}/kio_applications.so
%{_kde_unstable_modulesdir}/kio_archive.so
%{_kde_unstable_modulesdir}/kio_bookmarks.so
%{_kde_unstable_modulesdir}/kio_cgi.so
%{_kde_unstable_modulesdir}/kio_desktop.so
%{_kde_unstable_modulesdir}/kio_filter.so
%{_kde_unstable_modulesdir}/kio_finger.so
%{_kde_unstable_modulesdir}/kio_fish.so
%{_kde_unstable_modulesdir}/kio_floppy.so
%{_kde_unstable_modulesdir}/kio_info.so
%{_kde_unstable_modulesdir}/kio_man.so
%{_kde_unstable_modulesdir}/kio_nepomuk.so
%{_kde_unstable_modulesdir}/kio_nepomuksearch.so
%{_kde_unstable_modulesdir}/kio_network.so
%{_kde_unstable_modulesdir}/kio_nfs.so
%{_kde_unstable_modulesdir}/kio_remote.so
%{_kde_unstable_modulesdir}/kio_settings.so
%{_kde_unstable_modulesdir}/kio_sftp.so
%{_kde_unstable_modulesdir}/kio_smb.so
%{_kde_unstable_modulesdir}/kio_thumbnail.so
%{_kde_unstable_modulesdir}/kio_timeline.so
%{_kde_unstable_modulesdir}/kio_trash.so
%{_kde_unstable_modulesdir}/kio_tags.so

# --- uri filters ---
%{_kde_unstable_modulesdir}/kshorturifilter.so
%{_kde_unstable_modulesdir}/kuriikwsfilter.so
%{_kde_unstable_modulesdir}/kurisearchfilter.so
%{_kde_unstable_modulesdir}/localdomainurifilter.so

# --- rename plugins ---
%{_kde_unstable_modulesdir}/librenaudioplugin.so
%{_kde_unstable_modulesdir}/librenimageplugin.so

# --- kparts ---
%{_kde_unstable_modulesdir}/libkmanpart.so

# --- plasma ---
%{_kde_unstable_modulesdir}/plasma_appletscript_declarative.so
%{_kde_unstable_modulesdir}/plasma_appletscript_simple_javascript.so
%{_kde_unstable_modulesdir}/plasma_containment_newspaper.so
%{_kde_unstable_modulesdir}/plasma_dataenginescript_javascript.so
%{_kde_unstable_modulesdir}/plasma-kpart.so
%{_kde_unstable_modulesdir}/plasma_packagestructure_javascriptaddon.so
%{_kde_unstable_modulesdir}/plasma_runnerscript_javascript.so

# --- other ---
%{_kde_unstable_libdir}/attica_kde.so
%{_kde_unstable_libdir}/libknotifyplugin.so
%{_kde_unstable_libdir}/libkwalletbackend.so
%{_kde_unstable_libdir}/libmolletnetwork.so
%{_kde_unstable_modulesdir}/imports/
%{_kde_unstable_modulesdir}/plugins/phonon_platform
%{_kde_unstable_modulesdir}/kio_recentdocuments.so
%{_kde_unstable_modulesdir}/kded_recentdocumentsnotifier.so

# --- libexec ---
%verify(not mode) %attr(2755,root,nogroup) %{_kde_unstable_libexecdir}/kdesud
%{_kde_unstable_libexecdir}/drkonqi
%{_kde_unstable_libexecdir}/kcmremotewidgetshelper
%{_kde_unstable_libexecdir}/kdeeject
%{_kde_unstable_libexecdir}/kdesu
%{_kde_unstable_libexecdir}/kdontchangethehostname
%{_kde_unstable_libexecdir}/khc_docbookdig.pl
%{_kde_unstable_libexecdir}/khc_htdig.pl
%{_kde_unstable_libexecdir}/khc_htsearch.pl
%{_kde_unstable_libexecdir}/khc_indexbuilder
%{_kde_unstable_libexecdir}/khc_mansearch.pl
%{_kde_unstable_libexecdir}/kioexec
%{_kde_unstable_libexecdir}/knetattach

# --- apps directories ---
%dir %{_kde_unstable_appsdir}/hardwarenotifications
%dir %{_kde_unstable_appsdir}/kde
%dir %{_kde_unstable_appsdir}/konqueror
%dir %{_kde_unstable_appsdir}/konqueror/dirtree
%dir %{_kde_unstable_appsdir}/konqueror/dirtree/remote

# --- apps ---
%exclude %{_kde_unstable_appsdir}/desktoptheme/oxygen
%{_kde_unstable_appsdir}/cmake
%{_kde_unstable_appsdir}/desktoptheme
%{_kde_unstable_appsdir}/drkonqi
%{_kde_unstable_appsdir}/hardwarenotifications/hardwarenotifications.notifyrc
%{_kde_unstable_appsdir}/kcm_componentchooser
%{_kde_unstable_appsdir}/kcmlocale
%{_kde_unstable_appsdir}/kcm_phonon
%{_kde_unstable_appsdir}/kconf_update/devicepreference.upd
%{_kde_unstable_appsdir}/kconf_update/kuriikwsfilter.upd
%{_kde_unstable_appsdir}/kconf_update/drkonqi-rename-config-section.upd
%{_kde_unstable_appsdir}/kde/kde.notifyrc
%{_kde_unstable_appsdir}/kglobalaccel
%{_kde_unstable_appsdir}/khelpcenter
%{_kde_unstable_appsdir}/kio_bookmarks
%{_kde_unstable_appsdir}/kio_desktop
%{_kde_unstable_appsdir}/kio_docfilter
%{_kde_unstable_appsdir}/kio_finger
%{_kde_unstable_appsdir}/kio_info
%{_kde_unstable_appsdir}/konqsidebartng
%{_kde_unstable_appsdir}/konqueror/dirtree/remote/smb-network.desktop
%{_kde_unstable_appsdir}/ksmserver
%{_kde_unstable_appsdir}/kwalletd
%{_kde_unstable_appsdir}/libphonon
%{_kde_unstable_appsdir}/phonon
%{_kde_unstable_appsdir}/remoteview

# --- protocols ---
%{_kde_unstable_servicesdir}/about.protocol
%{_kde_unstable_servicesdir}/applications.protocol
%{_kde_unstable_servicesdir}/ar.protocol
%{_kde_unstable_servicesdir}/bookmarks.protocol
%{_kde_unstable_servicesdir}/bzip.protocol
%{_kde_unstable_servicesdir}/bzip2.protocol
%{_kde_unstable_servicesdir}/cgi.protocol
%{_kde_unstable_servicesdir}/desktop.protocol
%{_kde_unstable_servicesdir}/finger.protocol
%{_kde_unstable_servicesdir}/fish.protocol
%{_kde_unstable_servicesdir}/floppy.protocol
%{_kde_unstable_servicesdir}/gzip.protocol
%{_kde_unstable_servicesdir}/info.protocol
%{_kde_unstable_servicesdir}/lzma.protocol
%{_kde_unstable_servicesdir}/man.protocol
%{_kde_unstable_servicesdir}/nepomuk.protocol
%{_kde_unstable_servicesdir}/nepomuksearch.protocol
%{_kde_unstable_servicesdir}/network.protocol
%{_kde_unstable_servicesdir}/nfs.protocol
%{_kde_unstable_servicesdir}/programs.protocol
%{_kde_unstable_servicesdir}/remote.protocol
%{_kde_unstable_servicesdir}/settings.protocol
%{_kde_unstable_servicesdir}/smb.protocol
%{_kde_unstable_servicesdir}/sftp.protocol
%{_kde_unstable_servicesdir}/tar.protocol
%{_kde_unstable_servicesdir}/thumbnail.protocol
%{_kde_unstable_servicesdir}/timeline.protocol
%{_kde_unstable_servicesdir}/trash.protocol
%{_kde_unstable_servicesdir}/xz.protocol
%{_kde_unstable_servicesdir}/zip.protocol
%{_kde_unstable_servicesdir}/recentdocuments.protocol
%{_kde_unstable_servicesdir}/tags.protocol

# --- services ---
%{_kde_unstable_servicesdir}/comicbookthumbnail.desktop
%{_kde_unstable_servicesdir}/componentchooser.desktop
%{_kde_unstable_servicesdir}/cursorthumbnail.desktop
%{_kde_unstable_servicesdir}/desktopthumbnail.desktop
%{_kde_unstable_servicesdir}/device_automounter_kcm.desktop
%{_kde_unstable_servicesdir}/directorythumbnail.desktop
%{_kde_unstable_servicesdir}/djvuthumbnail.desktop
%{_kde_unstable_servicesdir}/emoticons.desktop
%{_kde_unstable_servicesdir}/exrthumbnail.desktop
%{_kde_unstable_servicesdir}/filetypes.desktop
%{_kde_unstable_servicesdir}/fixhosturifilter.desktop
%{_kde_unstable_servicesdir}/htmlthumbnail.desktop
%{_kde_unstable_servicesdir}/icons.desktop
%{_kde_unstable_servicesdir}/imagethumbnail.desktop
%{_kde_unstable_servicesdir}/jpegthumbnail.desktop
%{_kde_unstable_servicesdir}/kcm_attica.desktop
%{_kde_unstable_servicesdir}/kcmcgi.desktop
%{_kde_unstable_servicesdir}/kcmkded.desktop
%{_kde_unstable_servicesdir}/kcm_kdnssd.desktop
%{_kde_unstable_servicesdir}/kcm_nepomuk.desktop
%{_kde_unstable_servicesdir}/kcmnotify.desktop
%{_kde_unstable_servicesdir}/kcm_phonon.desktop
%{_kde_unstable_servicesdir}/kcmtrash.desktop
%{_kde_unstable_servicesdir}/kglobalaccel.desktop
%{_kde_unstable_servicesdir}/khelpcenter.desktop
%{_kde_unstable_servicesdir}/kmanpart.desktop
%{_kde_unstable_servicesdir}/knotify4.desktop
%{_kde_unstable_servicesdir}/kshorturifilter.desktop
%{_kde_unstable_servicesdir}/kuiserver.desktop
%{_kde_unstable_servicesdir}/kuriikwsfilter.desktop
%{_kde_unstable_servicesdir}/kurisearchfilter.desktop
%{_kde_unstable_servicesdir}/kwalletd.desktop
%{_kde_unstable_servicesdir}/language.desktop
%{_kde_unstable_servicesdir}/localdomainurifilter.desktop
%{_kde_unstable_servicesdir}/plasma-containment-newspaper.desktop
%{_kde_unstable_servicesdir}/plasma-kpart.desktop
%{_kde_unstable_servicesdir}/plasma-packagestructure-javascript-addon.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-applet-declarative.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-applet-simple-javascript.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-dataengine-javascript.desktop
%{_kde_unstable_servicesdir}/plasma-scriptengine-runner-javascript.desktop
%{_kde_unstable_servicesdir}/renaudiodlg.desktop
%{_kde_unstable_servicesdir}/renimagedlg.desktop
%{_kde_unstable_servicesdir}/searchproviders
%{_kde_unstable_servicesdir}/spellchecking.desktop
%{_kde_unstable_servicesdir}/svgthumbnail.desktop
%{_kde_unstable_servicesdir}/textthumbnail.desktop
%{_kde_unstable_servicesdir}/windowsimagethumbnail.desktop
%{_kde_unstable_servicesdir}/windowsexethumbnail.desktop
%{_kde_unstable_servicesdir}/desktop-search.desktop

# --- kded services ---
%{_kde_unstable_servicesdir}/kded/desktopnotifier.desktop
%{_kde_unstable_servicesdir}/kded/device_automounter.desktop
%{_kde_unstable_servicesdir}/kded/kpasswdserver.desktop
%{_kde_unstable_servicesdir}/kded/ktimezoned.desktop
%{_kde_unstable_servicesdir}/kded/nepomuksearchmodule.desktop
%{_kde_unstable_servicesdir}/kded/networkstatus.desktop
%{_kde_unstable_servicesdir}/kded/networkwatcher.desktop
%{_kde_unstable_servicesdir}/kded/phononserver.desktop
%{_kde_unstable_servicesdir}/kded/remotedirnotify.desktop
%{_kde_unstable_servicesdir}/kded/solidautoeject.desktop
%{_kde_unstable_servicesdir}/kded/soliduiserver.desktop
%{_kde_unstable_servicesdir}/kded/recentdocumentsnotifier.desktop

# --- service types ---
%{_kde_unstable_servicetypesdir}/knotifynotifymethod.desktop
%{_kde_unstable_servicetypesdir}/phononbackend.desktop
%{_kde_unstable_servicetypesdir}/plasma-javascriptaddon.desktop
%{_kde_unstable_servicetypesdir}/searchprovider.desktop
%{_kde_unstable_servicetypesdir}/thumbcreator.desktop

# --- applications ---
%{_kde_unstable_applicationsdir}/Help.desktop
%{_kde_unstable_applicationsdir}/knetattach.desktop
%{_kde_unstable_applicationsdir}/nepomukcontroller.desktop

# --- autostart ---
%{_kde_unstable_datadir}/autostart/nepomukcontroller.desktop

# --- libraries---
%{_kde_unstable_libdir}/libkwalletbackend.so.*
%{_kde_unstable_libdir}/libmolletnetwork.so.*

# --- kconf update---
%{_kde_unstable_libdir}/kconf_update_bin/phonon_devicepreference_update
%{_kde_unstable_libdir}/kconf_update_bin/phonon_deviceuids_update

# --- executables ---
%{_kde_unstable_bindir}/kcmshell4
%{_kde_unstable_bindir}/kde4
%{_kde_unstable_bindir}/kde4-menu
%{_kde_unstable_bindir}/kdebugdialog
%{_kde_unstable_bindir}/kde-cp
%{_kde_unstable_bindir}/kde-mv
%{_kde_unstable_bindir}/kde-open
%{_kde_unstable_bindir}/kdesu
%{_kde_unstable_bindir}/keditfiletype
%{_kde_unstable_bindir}/kfile4
%{_kde_unstable_bindir}/kglobalaccel
%{_kde_unstable_bindir}/khelpcenter
%{_kde_unstable_bindir}/khotnewstuff4
%{_kde_unstable_bindir}/khotnewstuff-upload
%{_kde_unstable_bindir}/kiconfinder
%{_kde_unstable_bindir}/kioclient
%{_kde_unstable_bindir}/kmimetypefinder
%{_kde_unstable_bindir}/knotify4
%{_kde_unstable_bindir}/kquitapp
%{_kde_unstable_bindir}/kreadconfig
%{_kde_unstable_bindir}/kstart
%{_kde_unstable_bindir}/ksvgtopng
%{_kde_unstable_bindir}/ktraderclient
%{_kde_unstable_bindir}/ktrash
%{_kde_unstable_bindir}/kuiserver
%{_kde_unstable_bindir}/kwalletd
%{_kde_unstable_bindir}/kwriteconfig
%{_kde_unstable_bindir}/nepomukcontroller
%{_kde_unstable_bindir}/plasmapkg
%{_kde_unstable_bindir}/plasma-remote-helper
%{_kde_unstable_bindir}/solid-hardware

# --- dbus interfaces---
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.khelpcenter.kcmhelpcenter.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.KTimeZoned.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.network.kioslavenotifier.xml

# --- dbus services ---
%dir %{_kde_unstable_datadir}/dbus-1/services/
%{_kde_unstable_datadir}/dbus-1/services/org.kde.knotify.service
%{_kde_unstable_datadir}/dbus-1/services/org.kde.kuiserver.service
%dir %{_kde_unstable_datadir}/dbus-1/system-services/
%{_kde_unstable_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmremotewidgets.service

# --- theme-related files ---
%{_kde_unstable_datadir}/emoticons/
%{_kde_unstable_iconsdir}/default.kde4
%dir %{_kde_unstable_datadir}/sounds/
%{_kde_unstable_datadir}/sounds/*.ogg
%dir %{_kde_unstable_iconsdir}/hicolor/128x128
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/apps
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/22x22
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps
%dir %{_kde_unstable_iconsdir}/hicolor/scalable
%dir %{_kde_unstable_iconsdir}/hicolor/scalable/apps
%{_kde_unstable_iconsdir}/hicolor/*/apps/knetattach.*

# --- imports from platforms ---
%dir %{_kde_unstable_modulesdir}/platformimports/
%{_kde_unstable_modulesdir}/platformimports/touch/

# --- other ---
%{_kde_unstable_datadir}/desktop-directories
%{_kde_unstable_datadir}/locale/*
%{_kde_unstable_datadir}/mime/packages/network.xml
%dir %{_kde_unstable_datadir}/polkit-1/
%dir %{_kde_unstable_datadir}/polkit-1/actions/
%{_kde_unstable_datadir}/polkit-1/actions/org.kde.kcontrol.kcmremotewidgets.policy

%changelog
