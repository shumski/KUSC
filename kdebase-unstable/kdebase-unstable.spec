#
# spec file for package kdebase4
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

Name:           kdebase-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        The Base KDE Apps
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source0:        kde-baseapps-git.tar.xz
Source1:        baselibs.conf
Source2:        rpmlintrc
Source3:        dolphinsu.desktop
Patch0:         4_7_BRANCH.diff
Patch1:         dolphin-go_up.diff
BuildRequires:  NetworkManager-devel
BuildRequires:  bluez-devel
BuildRequires:  fdupes
BuildRequires:  libkde-unstable-devel >= %{version} libkactivities-unstable-devel nepomuk-core-unstable-devel libnepomukwidgets-unstable-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libsoprano-unstable-devel
BuildRequires:  libtidy-devel
BuildRequires:  libusb-devel
BuildRequires:  pciutils-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libxklavier)
Provides:       browser(npapi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
This package contains the basic applications for a KDE workspace.

%prep
%setup -q -n kde-baseapps-git
%patch0 -p1
%patch1 -p1

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  pushd build
  %kde_unstable_makeinstall
  %create_subdir_filelist -d dolphin
  %create_subdir_filelist -d kdepasswd
  %create_subdir_filelist -d kdialog
  %create_subdir_filelist -d keditbookmarks
  %create_subdir_filelist -d kfind
  %create_subdir_filelist -d konqueror
  %create_subdir_filelist -d konq-plugins
  %create_subdir_filelist -d lib -v lib.devel
  %create_subdir_filelist -d nsplugins
  popd
  %create_exclude_filelist
  gzip %{buildroot}%{_kde_unstable_mandir}/man1/*
  install -D -m 0644 %{SOURCE3} %{buildroot}%{_kde_unstable_applicationsdir}
  %fdupes -s %{buildroot}
  %kde_unstable_post_install

%verifyscript
%verify_permissions -e %{_kde_unstable_bindir}/kcheckpass
%verify_permissions -e %{_kde_unstable_bindir}/kdesud

%clean
  rm -rf %{buildroot}
  rm -rf filelists

%package -n dolphin-unstable
Summary:        KDE File Manager
Group:          Productivity/File utilities
Requires:       %{name}-libkonq-unstable = %{version}
%kde_unstable_runtime_requires

%description -n dolphin-unstable
This package contains the default file manager of KDE 4.

%package -n kdepasswd-unstable
Summary:        KDE Password Changer
Group:          System/GUI/KDE
Provides:       kde4-kdepasswd = 4.3.0
Obsoletes:      kde4-kdepasswd < 4.3.0
%kde_unstable_runtime_requires

%description -n kdepasswd-unstable
This application allows you to change your UNIX password.

%package -n kdialog-unstable
Summary:        KDE version of xdialog
Group:          System/GUI/KDE
Provides:       kde4-kdialog = 4.3.0
Obsoletes:      kde4-kdialog < 4.3.0
%kde_unstable_runtime_requires

%description -n kdialog-unstable
KDialog can be used to show nice dialog boxes from shell scripts.

%package -n keditbookmarks-unstable
Summary:        KDE Bookmark Editor
Group:          System/GUI/KDE
Provides:       kde4-keditbookmarks = 4.3.0
Obsoletes:      kde4-keditbookmarks < 4.3.0
%kde_unstable_runtime_requires

%description -n keditbookmarks-unstable
This is an editor to edit your KDE-wide bookmark set.

%package -n kfind-unstable
Summary:        KDE Find File Utility
Group:          Productivity/File utilities
Provides:       kde4-kfind = 4.3.0
Obsoletes:      kde4-kfind < 4.3.0
%kde_unstable_runtime_requires

%description -n kfind-unstable
KFind allows you to search for directories and files.

%package -n konqueror-unstable
Summary:        KDE File Manager and Browser
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name}-libkonq-unstable = %{version}
Requires:       konqueror-plugins-unstable = %{version}
# needed for embedded filemanagement part
Recommends:     dolphin-unstable
Provides:       kde4-konqueror = 4.3.0
Obsoletes:      kde4-konqueror < 4.3.0
%kde_unstable_runtime_requires

%description -n konqueror-unstable
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package -n konqueror-plugins-unstable
Summary:        KDE File Manager and Browser
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name}-libkonq-unstable = %{version}
Provides:       konqueror-plugins-lang = %{version}
Obsoletes:      konqueror-plugins-lang < %{version}
%kde_unstable_runtime_requires

%description -n konqueror-plugins-unstable
These plugins extend the functionality of Konqueror.

%package libkonq-unstable
Summary:        KDE Konqueror Libraries
Group:          System/GUI/KDE
Requires:       libkonq5-unstable = %{version}
%kde_unstable_runtime_requires

%description libkonq-unstable
This package contains the files used by file managers as Konqueror.

%package -n libkonq-unstable-devel
Summary:        KDE Konqueror Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       libkde-unstable-devel
Requires:       libkonq5-unstable = %{version}

%description -n libkonq-unstable-devel
This package contains all necessary include files and libraries needed
to develop KDE file manager applications.

%package -n libkonq5-unstable
Summary:        KDE Konqueror Libraries
Group:          System/GUI/KDE
# naming error, make seamless upgrade possible
Provides:       libkonq4 = 4.0.85
Obsoletes:      libkonq4 < 4.0.85
%requires_ge    libqt4-x11

%description -n libkonq5-unstable
This package contains the libraries used by file managers as Konqueror.

%package nsplugin-unstable
Provides:       %{name}-nsplugin64 = 4.0.72
Obsoletes:      %{name}-nsplugin64 < 4.0.72
%ifarch x86_64 ppc64 s390x ia64
Recommends:     nspluginwrapper
%endif
Summary:        Netscape plugin support for KDE
Group:          System/GUI/KDE
%kde_unstable_runtime_requires

%description nsplugin-unstable
This package contains support for Netscape plug-ins in konqueror. You
have to enable JavaScript for this.

%package -n plasmoid-folderview-unstable
Summary:        Plasmoid to display a folder
Group:          System/GUI/KDE
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
%kde_unstable_runtime_requires

%description -n plasmoid-folderview-unstable
This applet displays the contents of a folder or kio slave on your
desktop or in your panel

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   -n dolphin-unstable -p /sbin/ldconfig

%postun -n dolphin-unstable -p /sbin/ldconfig

%post   -n kdepasswd-unstable -p /sbin/ldconfig

%postun -n kdepasswd-unstable -p /sbin/ldconfig

%post   -n kdialog-unstable -p /sbin/ldconfig

%postun -n kdialog-unstable -p /sbin/ldconfig

%post   -n keditbookmarks-unstable -p /sbin/ldconfig

%postun -n keditbookmarks-unstable -p /sbin/ldconfig

%post   -n kfind-unstable -p /sbin/ldconfig

%postun -n kfind-unstable -p /sbin/ldconfig

%post   -n konqueror-unstable -p /sbin/ldconfig

%postun -n konqueror-unstable -p /sbin/ldconfig

%post   -n konqueror-plugins-unstable -p /sbin/ldconfig

%postun -n konqueror-plugins-unstable -p /sbin/ldconfig

%post   libkonq-unstable -p /sbin/ldconfig

%postun libkonq-unstable -p /sbin/ldconfig

%post   -n libkonq5-unstable -p /sbin/ldconfig

%postun -n libkonq5-unstable -p /sbin/ldconfig

%files -n dolphin-unstable -f filelists/dolphin
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_appsdir}/dolphinpart
%{_kde_unstable_applicationsdir}/dolphinsu.desktop

%files -n kdepasswd-unstable -f filelists/kdepasswd
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_appsdir}/kdm
%dir %{_kde_unstable_appsdir}/kdm/pics
%dir %{_kde_unstable_appsdir}/kdm/pics/users

%files -n kdialog-unstable -f filelists/kdialog
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%doc kdialog/README kdialog/progressdemo kdialog/progresscanceldemo kdialog/test

%files -n keditbookmarks-unstable -f filelists/keditbookmarks
%defattr(-,root,root)
%doc COPYING COPYING.DOC README

%files -n kfind-unstable -f filelists/kfind
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/22x22
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps


%files -n konqueror-unstable -f filelists/konqueror
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_datadir}/autostart
%dir %{_kde_unstable_appsdir}/dolphinpart/kpartplugins
%dir %{_kde_unstable_appsdir}/kcmcss
%dir %{_kde_unstable_appsdir}/kcontrol
%dir %{_kde_unstable_appsdir}/kcontrol/pics
%dir %{_kde_unstable_appsdir}/konqsidebartng/dirtree
%dir %{_kde_unstable_appsdir}/konqsidebartng/entries
%dir %{_kde_unstable_appsdir}/konqsidebartng/plugins
%dir %{_kde_unstable_appsdir}/konqsidebartng/virtual_folders/remote
%dir %{_kde_unstable_appsdir}/konqsidebartng/virtual_folders/remote/ftp
%dir %{_kde_unstable_appsdir}/konqsidebartng/virtual_folders/remote/web
%dir %{_kde_unstable_appsdir}/konqueror/opensearch
%dir %{_kde_unstable_appsdir}/konqueror/kpartplugins
%dir %{_kde_unstable_appsdir}/kwebkitpart/kpartplugins
%dir %{_kde_unstable_servicesdir}/useragentstrings
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
# installed from apps/lib/konq/ and hence in kdebase4-libkonq
%exclude %{_kde_unstable_appsdir}/konqueror/pics/arrow_bottomleft.png
%exclude %{_kde_unstable_appsdir}/konqueror/pics/arrow_bottomright.png
%exclude %{_kde_unstable_appsdir}/konqueror/pics/arrow_topleft.png
%exclude %{_kde_unstable_appsdir}/konqueror/pics/arrow_topright.png
%exclude %{_kde_unstable_includedir}/konqsidebarplugin.h
%exclude %{_kde_unstable_libdir}/libkonqsidebarplugin.so

%files -n konqueror-plugins-unstable -f filelists/konq-plugins
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_appsdir}/akregator
%dir %{_kde_unstable_appsdir}/akregator/pics
%dir %{_kde_unstable_appsdir}/domtreeviewer
%dir %{_kde_unstable_appsdir}/fsview
%dir %{_kde_unstable_appsdir}/konqueror/icons
%dir %{_kde_unstable_appsdir}/konqueror/icons/oxygen
%dir %{_kde_unstable_appsdir}/konqueror/icons/oxygen/*
%dir %{_kde_unstable_appsdir}/konqueror/icons/oxygen/*/actions
%dir %{_kde_unstable_appsdir}/konqueror/kpartplugins
%dir %{_kde_unstable_appsdir}/konqueror/opensearch
%dir %{_kde_unstable_iconsdir}/hicolor/
%dir %{_kde_unstable_iconsdir}/hicolor/22x22
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/oxygen/16x16
%dir %{_kde_unstable_iconsdir}/oxygen/16x16/actions
%dir %{_kde_unstable_iconsdir}/oxygen/22x22
%dir %{_kde_unstable_iconsdir}/oxygen/22x22/actions
%dir %{_kde_unstable_iconsdir}/oxygen/32x32
%dir %{_kde_unstable_iconsdir}/oxygen/32x32/actions
%dir %{_kde_unstable_iconsdir}/oxygen/48x48
%dir %{_kde_unstable_iconsdir}/oxygen/48x48/actions
%dir %{_kde_unstable_iconsdir}/oxygen/64x64
%dir %{_kde_unstable_iconsdir}/oxygen/64x64/actions
%dir %{_kde_unstable_iconsdir}/oxygen/scalable/actions
%dir %{_kde_unstable_appsdir}/kwebkitpart

%files libkonq-unstable -f filelists/lib
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_appsdir}/kbookmark
%dir %{_kde_unstable_sharedir}/templates
%dir %{_kde_unstable_sharedir}/templates/.source
%exclude %{_kde_unstable_includedir}/knewmenu.h
%exclude %{_kde_unstable_includedir}/konq_*.h
%exclude %{_kde_unstable_includedir}/konqmimedata.h
%exclude %{_kde_unstable_includedir}/kversioncontrolplugin.h
%exclude %{_kde_unstable_includedir}/libkonq_export.h
%exclude %{_kde_unstable_libdir}/libkonq.so
%exclude %{_kde_unstable_libdir}/libkonq.so.*

%files -n libkonq-unstable-devel -f filelists/lib.devel
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_includedir}/knewmenu.h
%{_kde_unstable_includedir}/konq_*.h
%{_kde_unstable_includedir}/konqmimedata.h
%{_kde_unstable_includedir}/konqsidebarplugin.h
%{_kde_unstable_includedir}/kversioncontrolplugin.h
%{_kde_unstable_includedir}/libkonq_export.h
%{_kde_unstable_libdir}/libkonq.so
%{_kde_unstable_libdir}/libkonqsidebarplugin.so

%files -n libkonq5-unstable
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_libdir}/libkonq.so.*

%files nsplugin-unstable -f filelists/nsplugins
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%dir %{_kde_unstable_appsdir}/nsplugin

%files -n plasmoid-folderview-unstable
%defattr(-,root,root)
%doc COPYING COPYING.DOC README
%{_kde_unstable_modulesdir}/plasma_applet_folderview.so
%{_kde_unstable_servicesdir}/plasma-applet-folderview.desktop

%changelog
