#
# spec file for package kde4-filesystem
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


Name:           kde-unstable-filesystem
Url:            http://www.kde.org
Version:        4.10.40
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        KDE4 Directory Layout
License:        LGPL-2.1+
Group:          System/Fhs
Source0:        macros.kde-unstable
Source1:        COPYING
Source2:        kde-unstable.sh
#
# keep in sync with macros.kde4
# TODO: can we include macros.kde4 directly to define it?
%define _kde_unstable_config_dir /opt/kde-unstable/share/kde4/config

%description
This package installs the KDE directory structure.

%prep

%build

%install
  install -D -m644 %{SOURCE0} %{buildroot}/etc/rpm/macros.kde-unstable
  mkdir -p %{buildroot}/opt/kde-unstable/
  mkdir -p %{buildroot}/opt/kde-unstable/etc/
  mkdir -p %{buildroot}/opt/kde-unstable/etc/profile.d/
  install -D -m644 %{SOURCE2} %{buildroot}/opt/kde-unstable/etc/profile.d/kde-unstable.sh
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde-unstable-filesystem/
  mkdir -p %{buildroot}/opt/kde-unstable/share/doc/
  install -D -m644 %{SOURCE1} %{buildroot}/opt/kde-unstable/share/doc/kde-unstable-filesystem/COPYING
  mkdir -p %{buildroot}/%{_kde_unstable_config_dir}
  mkdir -p %{buildroot}/opt/kde-unstable/share/applications/kde4
  for size in scalable 128x128 64x64 48x48 32x32 22x22 16x16; do
    for type in actions apps devices filesystems mimetypes status; do
      for theme in crystalsvg oxygen hicolor locolor; do
        mkdir -p %{buildroot}/opt/share/icons/$theme/$size/$type
      done
    done
  done
  mkdir -p %{buildroot}/opt/kde-unstable/bin
  mkdir -p %{buildroot}/opt/kde-unstable/etc/dbus-1
  mkdir -p %{buildroot}/opt/kde-unstable/etc/dbus-1/system.d
  mkdir -p %{buildroot}/opt/kde-unstable/etc/xdg
  mkdir -p %{buildroot}/opt/kde-unstable/include/KDE
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/cmake
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/pkgconfig
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/qt4
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/qt4/plugins
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/qt4/plugins/designer
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/kde4
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/kde4/libexec
  mkdir -p %{buildroot}/opt/kde-unstable/%{_lib}/kde4/plugins
  mkdir -p %{buildroot}/opt/kde-unstable/sbin
  mkdir -p %{buildroot}/opt/kde-unstable/share/
  mkdir -p %{buildroot}/opt/kde-unstable/share/dbus-1
  mkdir -p %{buildroot}/opt/kde-unstable/share/dbus-1/interfaces
  mkdir -p %{buildroot}/opt/kde-unstable/share/doc/kde
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/services/
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/services/phononbackends
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/services/ServiceMenus
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/apps
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/apps/color-schemes
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/apps/khtml/kpartplugins
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/apps/konqsidebartng/virtual_folders/services
  mkdir -p %{buildroot}/opt/kde-unstable/share/kde4/config.kcfg
  mkdir -p %{buildroot}/opt/kde-unstable/share/locale
  mkdir -p %{buildroot}/opt/kde-unstable/share/locale/en_US
  mkdir -p %{buildroot}/opt/kde-unstable/share/man
  mkdir -p %{buildroot}/opt/kde-unstable/share/man/man1
  mkdir -p %{buildroot}/opt/kde-unstable/share/man/man7
  mkdir -p %{buildroot}/opt/kde-unstable/share/man/man8
  mkdir -p %{buildroot}/opt/kde-unstable/share/mime
  mkdir -p %{buildroot}/opt/kde-unstable/share/mime/packages
  mkdir -p %{buildroot}/opt/kde-unstable/share/qt4
  mkdir -p %{buildroot}/opt/kde-unstable/share/qt4/mkspecs
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/16x16
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/16x16/actions
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/32x32
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/32x32/actions
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/48x48
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/hicolor/48x48/actions
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/oxygen/scalable/apps/small/16x16
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/oxygen/scalable/apps/small/32x32
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/oxygen/scalable/status/small/16x16
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/oxygen/scalable/status/small/22x22
  mkdir -p %{buildroot}/opt/kde-unstable/share/icons/oxygen/scalable/status/small/48x48
  for lang in `find /opt/kde-unstable/share/locale/* -maxdepth 0 -type d -printf "%f\n"`; do mkdir -p %{buildroot}%/opt/kde-unstable/share/doc/kde/HTML/$lang; done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config %{_sysconfdir}/rpm/macros.kde-unstable
%config %{_kde_unstable_config_dir}
/opt/kde-unstable/share/kde4
/opt/kde-unstable/share/applications/kde4
/opt/kde-unstable/share/doc/kde
/opt/kde-unstable/share/icons/*
/opt/kde-unstable/share/kde4/services/phononbackends
%dir /opt/kde-unstable
%dir /opt/kde-unstable/etc/
%dir /opt/kde-unstable/etc/profile.d/
/opt/kde-unstable/etc/profile.d/kde-unstable.sh
%dir /opt/kde-unstable/share/doc/kde-unstable-filesystem
%dir /opt/kde-unstable/etc/dbus-1
%dir /opt/kde-unstable/etc/dbus-1/system.d
%dir /opt/kde-unstable/etc/xdg
%dir /opt/kde-unstable/include/KDE
%dir /opt/kde-unstable/%{_lib}
%dir /opt/kde-unstable/%{_lib}/cmake
%dir /opt/kde-unstable/%{_lib}/pkgconfig
%dir /opt/kde-unstable/%{_lib}/qt4
%dir /opt/kde-unstable/%{_lib}/qt4/plugins
%dir /opt/kde-unstable/%{_lib}/qt4/plugins/designer
%dir /opt/kde-unstable/%{_lib}/kde4
%dir /opt/kde-unstable/%{_lib}/kde4/libexec
%dir /opt/kde-unstable/%{_lib}/kde4/plugins
%dir /opt/kde-unstable/sbin
%dir /opt/kde-unstable/share/
%dir /opt/kde-unstable/share/dbus-1
%dir /opt/kde-unstable/share/dbus-1/interfaces
%dir /opt/kde-unstable/share/doc/kde
%dir /opt/kde-unstable/share/kde4/services/
%dir /opt/kde-unstable/share/kde4/services/phononbackends
%dir /opt/kde-unstable/share/kde4/services/ServiceMenus
%dir /opt/kde-unstable/share/kde4/apps
%dir /opt/kde-unstable/share/kde4/apps/color-schemes
%dir /opt/kde-unstable/share/kde4/apps/khtml/kpartplugins
%dir /opt/kde-unstable/share/kde4/apps/konqsidebartng/virtual_folders/services
%dir /opt/kde-unstable/share/kde4/config.kcfg
%dir /opt/kde-unstable/share/locale
%dir /opt/kde-unstable/share/locale/en_US
%dir /opt/kde-unstable/share/man
%dir /opt/kde-unstable/share/man/man1
%dir /opt/kde-unstable/share/man/man7
%dir /opt/kde-unstable/share/man/man8
%dir /opt/kde-unstable/share/mime
%dir /opt/kde-unstable/share/mime/packages
%dir /opt/kde-unstable/share/qt4
%dir /opt/kde-unstable/share/qt4/mkspecs
%dir /opt/kde-unstable/share/icons/hicolor
%dir /opt/kde-unstable/share/icons/hicolor/16x16
%dir /opt/kde-unstable/share/icons/hicolor/16x16/actions
%dir /opt/kde-unstable/share/icons/hicolor/32x32
%dir /opt/kde-unstable/share/icons/hicolor/32x32/actions
%dir /opt/kde-unstable/share/icons/hicolor/48x48
%dir /opt/kde-unstable/share/icons/hicolor/48x48/actions
%dir /opt/kde-unstable/share/icons/oxygen/scalable/apps/small/16x16
%dir /opt/kde-unstable/share/icons/oxygen/scalable/apps/small/32x32
%dir /opt/kde-unstable/share/icons/oxygen/scalable/status/small/16x16
%dir /opt/kde-unstable/share/icons/oxygen/scalable/status/small/22x22
%dir /opt/kde-unstable/share/icons/oxygen/scalable/status/small/48x48
###Obsolete?
%dir /opt/kde-unstable/include
%dir /opt/kde-unstable/share
%dir /opt/kde-unstable/share/applications
%dir /opt/kde-unstable/share/doc
%dir /opt/kde-unstable/share/icons
%dir /opt/kde-unstable/bin
%dir /opt/kde-unstable/share/man
%dir /opt/kde-unstable/sbin
%dir /opt/kde-unstable/%{_lib}
%dir /opt/kde-unstable/%{_lib}/cmake
%dir /opt/kde-unstable/%{_lib}/pkgconfig
%dir /opt/kde-unstable/share/dbus-1
%dir /opt/kde-unstable/share/dbus-1/interfaces
%dir /opt/kde-unstable/%{_lib}/qt4
%dir /opt/kde-unstable/%{_lib}/qt4/plugins
%dir /opt/kde-unstable/%{_lib}/qt4/plugins/designer
%dir /opt/kde-unstable/share/qt4
%dir /opt/kde-unstable/share/qt4/mkspecs
/opt/kde-unstable/share/doc/kde-unstable-filesystem/COPYING
/opt/kde-unstable/include/KDE
/opt/kde-unstable/%{_lib}/kde4

%changelog
