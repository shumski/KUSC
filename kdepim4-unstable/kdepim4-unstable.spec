#
# spec file for package kdepim4
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


Name:           kdepim4-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0+ ; LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        kdepim-git.tar.xz
Patch0:         4_8_BRANCH.diff
Patch1:         akregator-useragent.diff
Patch2:         desktop-files.diff
Patch3:         knode-kontact-default.diff
BuildRequires:  fdupes
BuildRequires:  gpgme-devel
BuildRequires:  grantlee-devel
BuildRequires:  libassuan-devel
BuildRequires:  libkdepimlibs-unstable-devel akonadi-runtime-unstable
BuildRequires:  libqca2-devel
BuildRequires:  xz
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  libkgapi1-unstable-devel libkgapi2-unstable-devel 
BuildRequires:  libnepomukwidgets-unstable-devel
BuildRequires:  libkactivities-unstable-devel
BuildRequires:  oxygen-icon-theme-unstable
Requires:       libkdepim4-unstable = %{version}
Suggests:       akregator-unstable
Suggests:       blogilo-unstable
Suggests:       kaddressbook-unstable
Suggests:       kalarm-unstable
Suggests:       kjots-unstable
Suggests:       kleopatra-unstable
Suggests:       kmail-unstable
Suggests:       knode-unstable
Suggests:       knotes-unstable
Suggests:       kontact-unstable
Suggests:       korganizer-unstable
Suggests:       ktimetracker-unstable
Suggests:       libkdepim4-unstable
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_akonadi_requires
%kde_unstable_pimlibs_requires
%kde_unstable_runtime_requires

%description
This package contains the core files of the kdepim module.

%prep
%setup -q -n kdepim-git
%patch0 -p1
%patch1
%patch2
%patch3

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kde_unstable -d build -- -DKDEPIM_BUILD_MOBILE=OFF
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall

  %create_subdir_filelist -d akonadi_next -v akonadi.devel
  %create_subdir_filelist -d akregator -v devel
  %create_subdir_filelist -d blogilo -v devel
  %create_subdir_filelist -d kaddressbook -v devel
  %create_subdir_filelist -d kalarm -v devel
  %create_subdir_filelist -d kjots -v devel
  %create_subdir_filelist -d kleopatra/libkleopatraclient -f libkdepim -v libkdepim.devel
  %create_subdir_filelist -d kmail -v devel
  %create_subdir_filelist -d kmailcvt -f kmail
  %create_subdir_filelist -d knode -v devel
  %create_subdir_filelist -d ktnef -v devel
  %create_subdir_filelist -d knotes -v devel
  %create_subdir_filelist -d kontact -v devel
  %create_subdir_filelist -d korganizer -v devel
  %create_subdir_filelist -d ktimetracker
  %create_subdir_filelist -d libkdepim -v libkdepim.devel
  cd ..
%if 0
  cat filelists/akonadi.devel | while read line; do echo "%exclude $line";done >>filelists/devel
%endif
  gzip %{buildroot}%{_kde_unstable_mandir}/man1/*
  #remove kontact plugins' desktop files that are in subpackages from the kontact list
  akregatorplugins="%{_kde_unstable_modulesdir}/kontact_akregatorplugin.so %{_kde_unstable_servicesdir}/kontact/akregatorplugin.desktop"
  kaddressbookplugin="%{_kde_unstable_modulesdir}/kontact_kaddressbookplugin.so"
  kjotsplugin="%{_kde_unstable_modulesdir}/kontact_kjotsplugin.so %{_kde_unstable_servicesdir}/kontact/kjots_plugin.desktop"
  kmailplugin="%{_kde_unstable_modulesdir}/kontact_kmailplugin.so %{_kde_unstable_servicesdir}/kontact/kmailplugin.desktop"
  knodeplugin="%{_kde_unstable_modulesdir}/kontact_knodeplugin.so %{_kde_unstable_servicesdir}/kontact/knodeplugin.desktop"
  knotesplugin="%{_kde_unstable_modulesdir}/kontact_knotesplugin.so %{_kde_unstable_servicesdir}/kontact/knotesplugin.desktop"
  korganizerplugins="%{_kde_unstable_modulesdir}/kontact_journalplugin.so %{_kde_unstable_modulesdir}/kontact_korganizerplugin.so %{_kde_unstable_modulesdir}/kontact_todoplugin.so %{_kde_unstable_servicesdir}/kontact/korganizerplugin.desktop %{_kde_unstable_servicesdir}/kontact/journalplugin.desktop %{_kde_unstable_servicesdir}/kontact/todoplugin.desktop"
  for i in $akregatorplugins $kaddressbookplugin $kjotsplugin $kmailplugin $knodeplugin $knotesplugin $korganizerplugins
  do
    sed -ri s,$i,, filelists/kontact
  done
  for i in $akregatorplugins
  do
    echo $i >> filelists/akregator
  done
  for i in $kaddressbookplugin
  do
    echo $i >> filelists/kaddressbook
  done
  for i in $kjotsplugin
  do
    echo $i >> filelists/kjots
  done
  for i in $kmailplugin
  do
    echo $i >> filelists/kmail
  done
  for i in $knodeplugin
  do
    echo $i >> filelists/knode
  done
  for i in $knotesplugin
  do
    echo $i >> filelists/knotes
  done
  for i in $korganizerplugins
  do
    echo $i >> filelists/korganizer
  done
  for i in $ktimetrackerplugin
  do
    echo $i >> filelists/ktimetracker
  done

  sed -ri s,.*/opt/kde-unstable/%{_lib}/libkabcommon.so.*,, filelists/kaddressbook

  grep "/opt/kde-unstable/lib" filelists/libkdepim | grep "/kde4/" >filelists/libkdepim.devel
  cat filelists/libkdepim.devel | while read line; do echo "%exclude $line";done >>filelists/devel

  %create_exclude_filelist
  %suse_update_desktop_file -r blogilo         Utility WebUtility
  %suse_update_desktop_file -u akonadiconsole Network  Email
  %suse_update_desktop_file KNode           Network  News
  %suse_update_desktop_file Kjots           Utility TimeUtility
  %suse_update_desktop_file Kontact         Office   Core-Office
  %suse_update_desktop_file akregator       Network  RSS-News
  %suse_update_desktop_file kaddressbook    Office   ContactManagement
  %suse_update_desktop_file kalarm          Utility  TimeUtility
  %suse_update_desktop_file kleopatra       Utility Security
  %suse_update_desktop_file knotes          Utility  DesktopUtility
  %suse_update_desktop_file korganizer      Office   Calendar
  %suse_update_desktop_file ktimetracker            Utility  TimeUtility
  %suse_update_desktop_file importwizard    Network Email

  %kde_unstable_post_install
  #Restrict fdupes call to not cause unwanted dependencies between packages
  %fdupes -s %{buildroot}%{_kde_unstable_htmldir}
  %fdupes -s %{buildroot}%{_kde_unstable_appsdir}/libkleopatra/
  %fdupes -s %{buildroot}%{_kde_unstable_appsdir}/knode/
  %fdupes -s %{buildroot}%{_kde_unstable_appsdir}/kmail2/
  %fdupes -s %{buildroot}%{_kde_unstable_iconsdir}
  %kde_unstable_post_install

  rm %{buildroot}%{_kde_unstable_libdir}/*.so
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/akonadi.devel > filelists/akonadi.devel.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/akonadi_next > filelists/akonadi_next.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/akregator > filelists/akregator.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/exclude > filelists/exclude.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/kalarm > filelists/kalarm.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/knode > filelists/knode.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/korganizer > filelists/korganizer.upd
  grep -v "%{_kde_unstable_libdir}/lib.*so$" filelists/libkdepim > filelists/libkdepim.upd
  rm filelists/devel
  mkdir -p %{buildroot}%{_kde_unstable_iconsdir}/hicolor/64x64/apps
  cp %{_kde_unstable_iconsdir}/oxygen/64x64/apps/kontact-import-wizard.png %{buildroot}%{_kde_unstable_iconsdir}/hicolor/64x64/apps/

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}
  rm -rf filelists

%package -n akonadi-unstable
Summary:        KDE Resources for PIM Storage Service
License:        GPL-2.0+ ; LGPL-2.1+
Group:          System/GUI/KDE
Requires:       kdepim4-runtime-unstable = %{version}
Requires:       soprano-unstable
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires
%kde_unstable_akonadi_requires

%description -n akonadi-unstable
This package contains the KDE resources for Akonadi, the KDE PIM
storage service.

%post   -n akonadi-unstable -p /sbin/ldconfig

%postun -n akonadi-unstable -p /sbin/ldconfig

%files -n akonadi-unstable -f filelists/akonadi_next.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%dir %{_kde_unstable_datadir}/akonadi
%dir %{_kde_unstable_datadir}/akonadi/agents
%dir %{_kde_unstable_libdir}/akonadi
%dir %{_kde_unstable_libdir}/akonadi/contact
%dir %{_kde_unstable_libdir}/akonadi/contact/editorpageplugins
%{_kde_unstable_datadir}/akonadi/agents/mailfilteragent.desktop
%{_kde_unstable_datadir}/akonadi/agents/archivemailagent.desktop
%{_kde_unstable_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so

%package -n akregator-unstable
Summary:        RSS Feed Reader
License:        LGPL-2.1+
Group:          Productivity/Networking/News/Utilities
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n akregator-unstable
A KDE Feed Aggregator

%post   -n akregator-unstable -p /sbin/ldconfig

%postun -n akregator-unstable -p /sbin/ldconfig

%files -n akregator-unstable -f filelists/akregator.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README

%package -n blogilo-unstable
Summary:        KDE Blog Editor
License:        LGPL-2.1+
Group:          Productivity/Editors/Other
Requires:       libkdepim4-unstable = %{version}
Requires:       libktexteditor-unstable
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n blogilo-unstable
A blog editor for KDE

%post   -n blogilo-unstable -p /sbin/ldconfig

%postun -n blogilo-unstable -p /sbin/ldconfig

%files -n blogilo-unstable -f filelists/blogilo
%defattr(-,root,root)

%package -n kaddressbook-unstable
Summary:        Address Manager
License:        LGPL-2.1+
Group:          Productivity/Networking/Email/Utilities
Requires:       kdepim4-runtime-unstable = %{version}
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n kaddressbook-unstable
The KDE Address Book

%post   -n kaddressbook-unstable -p /sbin/ldconfig

%postun -n kaddressbook-unstable -p /sbin/ldconfig

%files -n kaddressbook-unstable -f filelists/kaddressbook
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README

%package -n kmail-unstable
Summary:        Mail Client
License:        GPL-2.0
Group:          Productivity/Networking/Email/Clients
Requires:       akonadi-runtime-unstable
Requires:       kdepim4-runtime-unstable = %{version}
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n kmail-unstable
KMail is the KDE mail client.

%post   -n kmail-unstable -p /sbin/ldconfig

%postun -n kmail-unstable -p /sbin/ldconfig

%files -n kmail-unstable -f filelists/kmail
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%config %{_kde_unstable_configdir}/kmail.antispamrc
%config %{_kde_unstable_configdir}/kmail.antivirusrc

%package -n ktnef-unstable
License:        LGPLv2.1+
Summary:        Viewer for email attachments in TNEF format
Group:          Productivity/Networking/Email/Clients
Requires:       akonadi-runtime-unstable
Requires:       kdepim4-runtime = %version
Requires:       libkdepim4 = %version
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n ktnef-unstable
KTNEF is a viewer for email attachments in the TNEF format.

%post -n ktnef-unstable -p /sbin/ldconfig

%postun -n ktnef-unstable -p /sbin/ldconfig

%files -n ktnef-unstable -f filelists/ktnef
%defattr(-,root,root)
%{_kde_unstable_iconsdir}/locolor/*/*/ktnef*.png
%dir %{_kde_unstable_iconsdir}/locolor/
%dir %{_kde_unstable_iconsdir}/locolor/*
%dir %{_kde_unstable_iconsdir}/locolor/*/*

%package -n knode-unstable
Summary:        News Reader
License:        LGPL-2.1+
Group:          Productivity/Networking/News/Clients
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n knode-unstable
KNode is a usenet news reader for KDE.

%post   -n knode-unstable -p /sbin/ldconfig

%postun -n knode-unstable -p /sbin/ldconfig

%files -n knode-unstable -f filelists/knode.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%{_kde_unstable_appsdir}/knode/pics/*

%package -n knotes-unstable
Summary:        Popup Notes
License:        LGPL-2.1+
Group:          Productivity/Other
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n knotes-unstable
KNotes is a note taking application for KDE.

%post   -n knotes-unstable -p /sbin/ldconfig

%postun -n knotes-unstable -p /sbin/ldconfig

%files -n knotes-unstable -f filelists/knotes
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%exclude %{_kde_unstable_appsdir}/knotes/knotes_part.rc

%package -n kontact-unstable
Summary:        Personal Information Manager
License:        LGPL-2.1+
Group:          Productivity/Other
Requires:       libkdepim4-unstable = %{version}
Recommends:     kmail-unstable
Suggests:       kaddressbook-unstable
Suggests:       kjots-unstable
Suggests:       knode-unstable
Suggests:       knotes-unstable
Suggests:       korganizer-unstable
Suggests:       ktimetracker-unstable
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n kontact-unstable
Kontact combines the individual applications KMail, KAddressBook and
KOrganizer as views in one window.

%post   -n kontact-unstable -p /sbin/ldconfig

%postun -n kontact-unstable -p /sbin/ldconfig

%files -n kontact-unstable -f filelists/kontact
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README

%package -n korganizer-unstable
Summary:        Personal Organizer
License:        GPL-2.0
Group:          Productivity/Office/Organizers
Requires:       kdepim4-runtime-unstable = %{version}
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n korganizer-unstable
KOrganizer is a calendar application for KDE.

%post   -n korganizer-unstable -p /sbin/ldconfig

%postun -n korganizer-unstable -p /sbin/ldconfig

%files -n korganizer-unstable -f filelists/korganizer.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%config %{_kde_unstable_configdir}/korganizer.knsrc
%{_kde_unstable_servicetypesdir}/calendardecoration.desktop
%{_kde_unstable_servicetypesdir}/calendarplugin.desktop

%package -n ktimetracker-unstable
Summary:        Personal Time Tracker
License:        LGPL-2.1+
Group:          Productivity/Other
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n ktimetracker-unstable
KTimeTracker tracks time spent on various tasks.

%post   -n ktimetracker-unstable -p /sbin/ldconfig

%postun -n ktimetracker-unstable -p /sbin/ldconfig

%files -n ktimetracker-unstable -f filelists/ktimetracker
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README

%package -n kjots-unstable
Summary:        Note Taker
License:        GPL-2.0+
Group:          Productivity/Other
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n kjots-unstable
KDE Note Taking Utility

%post   -n kjots-unstable -p /sbin/ldconfig

%postun -n kjots-unstable -p /sbin/ldconfig

%files -n kjots-unstable -f filelists/kjots
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README

%package -n kalarm-unstable
Summary:        Personal Alarm Scheduler
License:        LGPL-2.1+
Group:          Productivity/Other
Requires:       libkdepim4-unstable = %{version}
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description -n kalarm-unstable
Personal alarm message, command and email scheduler for KDE

%post -n kalarm-unstable -p /sbin/ldconfig

%postun -n kalarm-unstable -p /sbin/ldconfig

%files -n kalarm-unstable -f filelists/kalarm.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%config %{_kde_unstable_sysconfdir}/dbus-1/system.d/org.kde.kalarmrtcwake.conf

%package -n libkdepim4-unstable
Summary:        KDE PIM Libraries
License:        LGPL-2.1+
Group:          System/GUI/KDE
%requires_ge libqt4-x11

%description -n libkdepim4-unstable
This package contains the basic packages for KDE PIM applications.

%post   -n libkdepim4-unstable -p /sbin/ldconfig

%postun -n libkdepim4-unstable -p /sbin/ldconfig

%files -n libkdepim4-unstable -f filelists/libkdepim.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%{_kde_unstable_modulesdir}/kcm_ldap.so
%{_kde_unstable_modulesdir}/plugins/designer/kdepimwidgets.so

%files -f filelists/exclude.upd
%defattr(-,root,root)
%doc COPYING COPYING.LIB COPYING.DOC README
%config %{_kde_unstable_configdir}/libkleopatrarc
%doc %lang(en) %{_kde_unstable_htmldir}/en/kontact-admin
%doc %lang(en) %{_kde_unstable_htmldir}/en/kabcclient
%doc %lang(en) %{_kde_unstable_htmldir}/en/konsolekalendar
%doc %lang(en) %{_kde_unstable_htmldir}/en/kioslave/news
%doc %lang(en) %{_kde_unstable_htmldir}/en/kioslave
%doc %lang(en) %{_kde_unstable_htmldir}/en/kwatchgnupg
%doc %lang(en) %{_kde_unstable_htmldir}/en/kleopatra
%{_kde_unstable_datadir}/dbus-1/interfaces/*
%dir %{_kde_unstable_datadir}/ontology/kde
%{_kde_unstable_datadir}/ontology/kde/messagetag.ontology
%{_kde_unstable_datadir}/ontology/kde/messagetag.trig
%{_kde_unstable_applicationsdir}/*
%{_kde_unstable_appsdir}
%{_kde_unstable_bindir}/*
%{_kde_unstable_configkcfgdir}
%{_kde_unstable_iconsdir}/hicolor
%{_kde_unstable_iconsdir}/oxygen
%{_kde_unstable_libdir}/*.so.*
%{_kde_unstable_mandir}/man1/kabcclient.1.gz
%{_kde_unstable_modulesdir}/*
%{_kde_unstable_servicesdir}
%exclude %{_kde_unstable_appsdir}/knode/pics/*

%changelog
