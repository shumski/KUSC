#
# spec file for package kdelibs4
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


# a hack for building apidoc, currently unused and unneeded (rev.312)
%bcond_with gendoxygen

# This is KDE revision number, setting it to a higher value will enable more features
# e.g. 420117248 enables kconfig_compiler.1
%define kderev 0 

Name:           kdelibs-unstable
Version:        4.10.40_20130331
Release:        1
BuildRequires:  OpenEXR-devel
BuildRequires:  alsa-devel
BuildRequires:  automoc4
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  enchant-devel
BuildRequires:  fam-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  giflib-devel
BuildRequires:  grantlee-devel
BuildRequires:  help2man
%if 0%{?kdelibs_is_fully_gplv3_compatible}
BuildRequires:  herqq-devel
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  kde-unstable-filesystem
BuildRequires:  krb5-devel
BuildRequires:  libQtWebKit-devel
BuildRequires:  libacl-devel
BuildRequires:  libattica-unstable-devel
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libgssglue-devel
BuildRequires:  libjasper-devel
BuildRequires:  libpolkit-qt-1-unstable-devel
BuildRequires:  libqca2-devel
BuildRequires:  libsoprano-unstable-devel
BuildRequires:  libudev-devel
BuildRequires:  libxslt-devel
BuildRequires:  pcre-devel
BuildRequires:  phonon-unstable-devel
BuildRequires:  shared-desktop-ontologies-unstable-devel
BuildRequires:  shared-mime-info
BuildRequires:  strigi-unstable
BuildRequires:  strigi-unstable-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1130
BuildRequires:  utempter-devel
%else
BuildRequires:  utempter
%endif
BuildRequires:  xz
BuildRequires:  xz-devel
%if %suse_version > 1210
%define brandingversion 4.8
%endif
%if %suse_version == 1130
%define brandingversion 11.3
%endif
%if %suse_version == 1140
%define brandingversion 11.4
%endif
%if %suse_version == 1210
%define brandingversion 12.1
%endif
Summary:        KDE Base Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        kdelibs-git.tar.xz
Source1:        baselibs.conf
Source2:        hidden.desktop
Source3:        ycp.xml
Source4:        kde4rc
Source99:       %{name}-rpmlintrc
Patch0:         4_7_BRANCH.diff
Patch1:         kde3-applications.diff
Patch2:         default-useragent.diff
Patch3:         add-suse-translations.diff
Patch5:         clever-menu.diff
Patch6:         hotplug-kde3.diff
Patch8:         windeco-color.diff
Patch9:         kdesu-settings.diff
Patch10:        kdebug-areas-update.diff
Patch12:        desktop-translations.diff
Patch13:        kjs-mark-register-stack.diff
Patch17:        flash-player-non-oss.diff
Patch18:        plasma-libs.diff
Patch20:        ignore-inline-menu.diff
Patch24:        ksuseinstall.diff
PreReq:         permissions
Requires:       soprano-unstable >= %( echo `rpm -q --queryformat '%{VERSION}' libsoprano-unstable-devel`)
Recommends:     strigi-unstable >= %( echo `rpm -q --queryformat '%{VERSION}' strigi-unstable-devel`)
Requires:       kdelibs-core-unstable = %{version}
Requires:       libkde-unstable = %{version}
%if %{suse_version} > 1220
Requires:       udisks2
%else
Requires:       udisks
%endif
Requires:       upower
Requires(post):     shared-mime-info
Requires(postun):   shared-mime-info

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%requires_ge        libstrigi0-unstable
%requires_ge        shared-mime-info
%requires_ge        shared-desktop-ontologies-unstable
%requires_ge        libqt4-x11

%if 0%{?opensuse_bs}
%define debug_package_requires %{name} = %{version}-%{release} libqt4-debuginfo
%endif

Requires:       %{name}-branding = %{brandingversion}

%description
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%package branding-upstream
Summary:        KDE Base Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
Provides:       %{name}-branding = %{brandingversion}

Supplements:    packageand(kdelibs-unstable:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)

%description branding-upstream
This package contains the basic packages for a K Desktop Environment
branding.

# KDE	292715 	292723 292725 292764 292765 
# kconfig_compiler pending upstream <URL: http://lists.kde.org/?l=kde-doc-english&m=132791095310563&w=2 >
%define kde_auto_man nepomuk-rcgen kde4-config kunittestmodrunner kfilemetadatareader meinproc4 

%prep
%setup -q -n kdelibs-git
%patch0 -p1
%patch1
%patch2
%patch3
%patch5
%patch6
%patch8
%patch9
%patch10
%patch12
%patch13
%patch17
%patch18
%patch20
%patch24

#
# define KDE version exactly
#
if [ '%{_project}' != KDE:Distro:Factory -a \
     '%{_project}' != KDE:KDE4:Unstable:SC -a \
     '%{_project}' != openSUSE:Factory ] ; then
  sed -ri "s,#cmakedefine KDE_VERSION_STRING \"@KDE_VERSION_STRING@\",#cmakedefine KDE_VERSION_STRING \"@KDE_VERSION_STRING@ \\\\\"release $(echo %{release} | cut -d. -f-1)\\\\\"\"," kdecore/util/kdeversion.h.cmake
fi

export PATH=/opt/kde-unstable/:$PATH
%build
  EXTRA_FLAGS="-DLIB_INSTALL_DIR=%{_kde_unstable_libdir} \
        -DCONFIG_INSTALL_DIR=%{_kde_unstable_configdir} \
        -DDATA_INSTALL_DIR=%{_kde_unstable_appsdir} \
        -DKCFG_INSTALL_DIR=%{_kde_unstable_configkcfgdir} \
        -DMIME_INSTALL_DIR=/nogo \
%if 0
        -DKDE4_ENABLE_FINAL=1 \
%endif
        -DKDE4_ENABLE_FPIE=1
        -DTEMPLATES_INSTALL_DIR=%{_kde_unstable_sharedir}/templates \
        -DHTML_INSTALL_DIR=%{_kde_unstable_htmldir} \
%if %{suse_version} > 1220
        -DWITH_SOLID_UDISKS2=TRUE \
%endif
        -DKDE_DEFAULT_HOME=.kde-unstable -DSYSCONF_INSTALL_DIR=%{_kde_unstable_sysconfdir}"
  %cmake_kde_unstable -d build -- -DKDE_DISTRIBUTION_TEXT="%distribution" $EXTRA_FLAGS
  %make_jobs
  mkdir man1
  for f in %kde_auto_man 
  do o="man1/$f.1"
# no pipe: abort on fail
  help2man>"$o" "bin/$f.shell" 
  gzip "$o"
  done

%install
  cd build
  %kde_unstable_makeinstall
  chmod +x %{buildroot}%{_kde_unstable_appsdir}/kconf_update/ksslcertificatemanager.upd.sh
  %create_subdir_filelist -d kdecore -v kdecore.devel
  %create_subdir_filelist -d kpty -f kdecore -v kdecore.devel
  install -ma=r '-t%{buildroot}%{_kde_unstable_mandir}/man1/' man1/*.1.gz
  cd ..
  %create_exclude_filelist
  %if %{with gendoxygen}
  install -p -D doc/api/doxygen.sh %{buildroot}%{_kde_unstable_bindir}/kde4-doxygen.sh
  %endif
  mkdir -p %{buildroot}/opt/etc/xdg/menus/applications-merged
  mv %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/applications.menu \
     %{buildroot}%{_kde_unstable_sysconfdir}/xdg/menus/applications.menu.kde4
  : rm %{buildroot}%{_kde_unstable_mandir}/man1/checkXML.1
  mv %{buildroot}%{_kde_unstable_mandir}/man7/kdeoptions.7 \
     %{buildroot}%{_kde_unstable_mandir}/man7/kde4options.7
  mv %{buildroot}%{_kde_unstable_mandir}/man7/qtoptions.7 \
     %{buildroot}%{_kde_unstable_mandir}/man7/qt4options.7
  mkdir -p %{buildroot}%{_kde_unstable_datadir}/autostart/
  install -m 0644 %{SOURCE2} %{buildroot}%{_kde_unstable_datadir}/autostart/panel.desktop
  install -m 0644 %{SOURCE2} %{buildroot}%{_kde_unstable_datadir}/autostart/ktip.desktop
  install -m 0644 %{SOURCE2} %{buildroot}%{_kde_unstable_datadir}/autostart/kdesktop.desktop
  install -m 0644 %{SOURCE4} %{buildroot}%{_kde_unstable_sysconfdir}/
  mkdir -p %{buildroot}/%{_kde_unstable_libdir}/kconf_update_bin
  %kde_unstable_post_install
  %fdupes -s %{buildroot}

%post
/sbin/ldconfig
%{_kde_unstable_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :

%if 0%{?suse_version} > 1130
%set_permissions %{_kde_unstable_libexecdir}/start_kdeinit
%endif

%postun
/sbin/ldconfig
%{_kde_unstable_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :

%verifyscript
%verify_permissions -e %{_kde_unstable_libexecdir}/start_kdeinit

%package doc
Summary:        Documentation for KDE Base Libraries
License:        LGPL-2.1+ and SUSE-GFDL-1.2+
Group:          System/GUI/KDE
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat}
PreReq:         /usr/bin/edit-xml-catalog
PreReq:         /usr/bin/xmlcatalog
PreReq:         awk
PreReq:         grep
PreReq:         sed
Requires:       sgml-skel

%description doc
This package contains the core environment and templates for the KDE
help system.

%files doc
%defattr(-,root,root)
%doc %lang(en) %{_kde_unstable_htmldir}/en/kioslave
%{_kde_unstable_appsdir}/ksgmltools2
%{_kde_unstable_bindir}/meinproc4
%{_kde_unstable_bindir}/meinproc4_simple
%doc COPYING.LIB COPYING.DOC
%doc %{_kde_unstable_mandir}/man1/meinproc4.1.gz

%if %{with gendoxygen}
%{_kde_unstable_bindir}/kde4-doxygen.sh
%doc %{_kde_unstable_mandir}/man1/kde4-doxygen.sh.1.gz
%endif

%package -n libkdecore-unstable
Summary:        KDE Core Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
%requires_ge        libqt4

%description -n libkdecore-unstable
This package contains the core libraries of the K Desktop Environment.

This package is absolutely necessary for using KDE applications.

%post -n libkdecore-unstable -p /sbin/ldconfig

%postun -n libkdecore-unstable -p /sbin/ldconfig

%files -n libkdecore-unstable
%defattr(-,root,root)
%doc COPYING COPYING.DOC COPYING.LIB README
%{_kde_unstable_libdir}/libkdecore.so.*
%{_kde_unstable_libdir}/libkdefakes.so.*
%{_kde_unstable_libdir}/libkpty.so.*

%package -n kdelibs-core-unstable
Summary:        KDE Base Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
Requires:       kde-unstable-filesystem >= %{_kde_unstable_platform_version}
Requires:       libkdecore-unstable = %{version}
%requires_ge        libpolkit-qt-1-1

%description -n kdelibs-core-unstable
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%files -n kdelibs-core-unstable -f filelists/kdecore
%defattr(-,root,root)
%doc COPYING.LIB 
%{_kde_unstable_configdir}/kdebug.areas
%{_kde_unstable_configdir}/kdebugrc
%config %{_kde_unstable_sysconfdir}/dbus-1/system.d/org.kde.auth.conf
%config %{_kde_unstable_sysconfdir}/kde4rc

%dir %{_kde_unstable_libdir}/kde4
%dir %{_kde_unstable_sharedir}/servicetypes

%exclude %{_kde_unstable_datadir}/locale/all_languages
%exclude %{_kde_unstable_bindir}/kconfig_compiler
%exclude %{_kde_unstable_libdir}/libkdecore.so.*
%exclude %{_kde_unstable_libdir}/libkdefakes.so.*
%exclude %{_kde_unstable_libdir}/libkpty.so.*

%doc %{_kde_unstable_mandir}/man1/kde4-config.1.gz

%package -n libkdecore-unstable-devel
Summary:        KDE Core Libraries: Build Environment
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Requires:       automoc4
Requires:       cmake
Requires:       kdelibs-core-unstable = %{version}
Requires:       libkdecore-unstable = %{version}
Requires:       libqt4-devel

%description -n libkdecore-unstable-devel
This package contains all necessary include files and libraries needed
to develop non-graphical KDE applications.

%files -n libkdecore-unstable-devel -f filelists/kdecore.devel
%defattr(-,root,root)
%doc COPYING.LIB README
%{_kde_unstable_bindir}/kconfig_compiler
%{_kde_unstable_includedir}/kdemacros.h

#pending upstream
%if %{kderev} >= 420117248
%doc %{_kde_unstable_mandir}/man1/kconfig_compiler.1.gz
%endif

%package -n libkde-unstable
Summary:        KDE Base Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
%requires_ge        libqt4-x11

%description -n libkde-unstable
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%post -n libkde-unstable -p /sbin/ldconfig

%postun -n libkde-unstable -p /sbin/ldconfig

%files branding-upstream
%defattr(-,root,root)
%doc COPYING.LIB
%if %suse_version > 1200
%{_kde_unstable_appsdir}/kdeui/about
%else
%{_kde_unstable_appsdir}/kdeui/about/body-background.jpg
%endif

%files -n libkde-unstable
%defattr(-,root,root)
%doc COPYING.LIB
%{_kde_unstable_datadir}/locale/all_languages
%{_kde_unstable_libdir}/libkcmutils.so.*
%{_kde_unstable_libdir}/libkde3support.so.*
%{_kde_unstable_libdir}/libkdeclarative.so.*
%{_kde_unstable_libdir}/libkdesu.so.*
%{_kde_unstable_libdir}/libkdeui.so.*
%{_kde_unstable_libdir}/libkdewebkit.so.*
%{_kde_unstable_libdir}/libkdnssd.so.*
%{_kde_unstable_libdir}/libkemoticons.so.*
%{_kde_unstable_libdir}/libkfile.so.*
%{_kde_unstable_libdir}/libkhtml.so.*
%{_kde_unstable_libdir}/libkidletime.so.*
%{_kde_unstable_libdir}/libkimproxy.so.*
%{_kde_unstable_libdir}/libkio.so.*
%{_kde_unstable_libdir}/libkjs.so.*
%{_kde_unstable_libdir}/libkjsapi.so.*
%{_kde_unstable_libdir}/libkjsembed.so.*
%{_kde_unstable_libdir}/libkmediaplayer.so.*
%{_kde_unstable_libdir}/libknewstuff2.so.*
%{_kde_unstable_libdir}/libknewstuff3.so.*
%{_kde_unstable_libdir}/libknotifyconfig.so.*
%{_kde_unstable_libdir}/libkntlm.so.*
%{_kde_unstable_libdir}/libkparts.so.*
%{_kde_unstable_libdir}/libkprintutils.so.*
%{_kde_unstable_libdir}/libkrosscore.so.*
%{_kde_unstable_libdir}/libkrossui.so.*
%{_kde_unstable_libdir}/libktexteditor.so.*
%{_kde_unstable_libdir}/libkunitconversion.so.*
%{_kde_unstable_libdir}/libkunittest.so.*
%{_kde_unstable_libdir}/libkutils.so.*
%{_kde_unstable_libdir}/libnepomuk.so.*
%{_kde_unstable_libdir}/libnepomukquery.so.*
%{_kde_unstable_libdir}/libnepomukutils.so.*
%{_kde_unstable_libdir}/libplasma.so.*
%{_kde_unstable_libdir}/libsolid.so.*
%{_kde_unstable_libdir}/libthreadweaver.so.*

%package -n libkde-unstable-devel
Summary:        KDE Base Libraries: Build Environment
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Requires:       OpenEXR-devel
Requires:       alsa-devel
Requires:       avahi-compat-mDNSResponder-devel
Requires:       cups-devel
Requires:       docbook-xsl-stylesheets
Requires:       enchant-devel
Requires:       fam-devel
Requires:       giflib-devel
Requires:       kdelibs-unstable = %{version}
Requires:       kdelibs-unstable-doc = %{version}
Requires:       libQtWebKit-devel
Requires:       libacl-devel
Requires:       libattica-unstable-devel
Requires:       libbz2-devel
Requires:       libidn-devel
Requires:       libkde-unstable = %{version}
Requires:       libkdecore-unstable-devel = %{version}
Requires:       libpolkit-qt-1-unstable-devel
Requires:       libsoprano-unstable-devel
Requires:       libxslt-devel
Requires:       pcre-devel
Requires:       phonon-unstable-devel
Requires:       shared-desktop-ontologies-unstable-devel
Requires:       strigi-unstable-devel
Requires:       update-desktop-files
Requires:       pkgconfig(libxml-2.0)
Provides:       libknotificationitem-devel = 4.3.66svn1016707
Obsoletes:      libknotificationitem-devel < 4.3.66svn1016707
Provides:       kde4-webkitpart-devel = 4.3.73svn1042829
Obsoletes:      kde4-webkitpart-devel < 4.3.73svn1042829

%description -n libkde-unstable-devel
This package contains all necessary include files and libraries needed
to develop KDE applications.

%files -n libkde-unstable-devel -f filelists/exclude
%defattr(-,root,root)
%exclude %{_kde_unstable_includedir}/ksuseinstall*
%exclude %{_kde_unstable_includedir}/kdemacros.h
%exclude %{_kde_unstable_libdir}/libkdeinit4_*.so
%exclude %{_kde_unstable_libdir}/libksuseinstall.so

%{_kde_unstable_appsdir}/cmake
%{_kde_unstable_includedir}/*
%{_kde_unstable_libdir}/*.so
%{_kde_unstable_libdir}/kde4/plugins/script/libkrossqtsplugin.so
%{_kde_unstable_libdir}/cmake/KDeclarative/

%doc COPYING.LIB README

%files -f filelists/exclude
%defattr(-,root,root)
%verify(not mode caps) %attr(4755,root,root) %{_kde_unstable_libexecdir}/start_kdeinit

%{_kde_unstable_configdir}/*
%config %{_kde_unstable_sysconfdir}/xdg/menus/applications.menu.kde4

%dir %{_kde_unstable_datadir}/autostart
%dir %{_kde_unstable_datadir}/doc/kde
%doc %dir %{_kde_unstable_docdir}/HTML
%doc %dir %{_kde_unstable_htmldir}/en
%doc %dir %{_kde_unstable_htmldir}/en/common
%dir %{_kde_unstable_libdir}/kconf_update_bin
%dir %{_kde_unstable_libdir}/kde4
%dir %{_kde_unstable_sharedir}/servicetypes
%dir %{_kde_unstable_sysconfdir}/xdg/menus

%doc %lang(en) %{_kde_unstable_htmldir}/en/sonnet

%exclude %{_kde_unstable_appsdir}/cmake
%if %suse_version > 1200
%exclude %{_kde_unstable_appsdir}/kdeui/about
%else
%exclude %{_kde_unstable_appsdir}/kdeui/about/body-background.jpg
%endif
%exclude %{_kde_unstable_appsdir}/ksgmltools2
%exclude %{_kde_unstable_bindir}/meinproc4
%exclude %{_kde_unstable_bindir}/meinproc4_simple
%exclude %{_kde_unstable_libdir}/kde4/plugins/script/libkrossqtsplugin.so

%{_kde_unstable_datadir}/autostart/kdesktop.desktop
%{_kde_unstable_datadir}/autostart/ktip.desktop
%{_kde_unstable_datadir}/autostart/panel.desktop
%{_kde_unstable_datadir}/dbus-1/interfaces/*
%{_kde_unstable_datadir}/mime/packages/kde.xml

%{_kde_unstable_applicationsdir}/kmailservice.desktop
%{_kde_unstable_applicationsdir}/ktelnetservice.desktop
%{_kde_unstable_appsdir}/*
%{_kde_unstable_bindir}/*
%doc %{_kde_unstable_htmldir}/en/common/*
%{_kde_unstable_iconsdir}/hicolor/*/actions/presence_away.*
%{_kde_unstable_iconsdir}/hicolor/*/actions/presence_offline.*
%{_kde_unstable_iconsdir}/hicolor/*/actions/presence_online.*
%{_kde_unstable_iconsdir}/hicolor/*/actions/presence_unknown.*
%{_kde_unstable_libdir}/libkdeinit4_*.so

%doc %{_kde_unstable_mandir}/man*/*
%exclude %{_kde_unstable_mandir}/man1/kde4-config.1.gz
%exclude %{_kde_unstable_mandir}/man1/meinproc4.1.gz

%if %{kderev} >= 420117248
%exclude %{_kde_unstable_mandir}/man1/kconfig_compiler.1.gz
%endif

%{_kde_unstable_modulesdir}/*
%{_kde_unstable_servicesdir}/*
%{_kde_unstable_servicetypesdir}/*
%{_kde_unstable_sysconfdir}/xdg/menus/applications.menu.kde4

%if %{with gendoxygen}
%exclude %{_kde_unstable_mandir}/man1/kde4-doxygen.sh.1.gz
%exclude %{_kde_unstable_bindir}/kde4-doxygen.sh
%endif

# IMPORTANT: When this is obsolete, do not just remove this, but create
# a separate package (for backwards compatibility).

%package -n libksuseinstall1-unstable
Summary:        On-demand installation of packages
License:        MIT
Group:          Development/Libraries/KDE
Requires:       yast2-packager >= 2.19.7
Requires:       zypper
Recommends:     ptools
%requires_ge        libqt4-x11

%description -n libksuseinstall1-unstable
This library implements private API to install additional packages for KDE.

%package -n libksuseinstall-unstable-devel
Summary:        On-demand installation of packages
License:        MIT
Group:          Development/Libraries/KDE
Requires:       libkde-unstable-devel
Requires:       libksuseinstall1-unstable = %{version}

%description -n libksuseinstall-unstable-devel
This library implements private API to install additional packages for KDE.

%post -n libksuseinstall1-unstable -p /sbin/ldconfig

%postun -n libksuseinstall1-unstable -p /sbin/ldconfig

%files -n libksuseinstall1-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libksuseinstall.so.*

%files -n libksuseinstall-unstable-devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/ksuseinstall.h
%{_kde_unstable_includedir}/ksuseinstall_export.h
%{_kde_unstable_libdir}/libksuseinstall.so

%changelog
