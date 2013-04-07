#
# spec file for package amarok
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Name:           amarok-unstable
Version:        x
Release:        0
Summary:        Media Player for KDE
License:        GPL-2.0+
Url:            http://amarok.kde.org/
Group:          Productivity/Multimedia/Sound/Players
Source0:        amarok-%{version}.tar.bz2
Source1:        amarok-lang.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Required for the fdupes macro
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpod-devel >= 0.7.0
BuildRequires:  libkde-unstable-devel
BuildRequires:  libksuseinstall-unstable-devel
BuildRequires:  liblastfm-devel >= 1.0.2
BuildRequires:  libmtp-devel
BuildRequires:  libmygpo-qt-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libmysqld-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libqca2-devel
BuildRequires:  libqjson-devel
BuildRequires:  libtag-devel >= 1.8
BuildRequires:  loudmouth-devel
BuildRequires:  mysql
BuildRequires:  nepomuk-core-unstable-devel >= 4.9.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  qt4-qtscript
BuildRequires:  taglib-extras-devel
BuildRequires:  tcpd-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       libtag-extras1 >= 1.0
Requires:       taglib >= 1.8
Recommends:     amarok-lang = %{version}
Recommends:     cagibi
Recommends:     clamz
Recommends:     moodbar
Recommends:     qt4-qtscript
%kde_unstable_runtime_requires

%description
Amarok is a media player for all kinds of media. This includes MP3, Ogg
Vorbis, audio CDs, podcasts and streams. Play lists can be stored in
.m3u or .pls files.

%lang_package
%prep
%setup -q -n amarok-%{version} -a 1
cat >> CMakeLists.txt << EOF
add_subdirectory( po )
EOF

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/main.cpp

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kde_unstable -d build
%make_jobs

%install
cd build
%kde_unstable_makeinstall
cd ..

%if 0%{?suse_version}
%suse_update_desktop_file amarok Qt KDE AudioVideo Audio Player
%endif

%fdupes -s %{buildroot}

%find_lang amarok
%find_lang amarok_scriptengine_qscript amarok.lang
%find_lang amarokcollectionscanner_qt amarok.lang
%find_lang amarokpkg amarok.lang

%kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files lang -f amarok.lang
%defattr(-,root,root,-)
%dir %{_kde_unstable_datadir}/locale/
%dir %{_kde_unstable_datadir}/locale/*/
%dir %{_kde_unstable_datadir}/locale/*/LC_MESSAGES/

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog README TODO
%dir %{_kde_unstable_appsdir}/desktoptheme
%dir %{_kde_unstable_appsdir}/desktoptheme/default
%dir %{_kde_unstable_appsdir}/desktoptheme/default/widgets
%dir %{_kde_unstable_appsdir}/solid
%dir %{_kde_unstable_appsdir}/solid/actions

%{_kde_unstable_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.player.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.root.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.tracklist.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.amarok.App.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.amarok.Collection.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.amarok.Mpris1Extensions.Player.xml
%{_kde_unstable_datadir}/dbus-1/interfaces/org.kde.amarok.Mpris2Extensions.Player.xml

%{_kde_unstable_applicationsdir}/amarok*.desktop

%{_kde_unstable_appsdir}/amarok/
%{_kde_unstable_appsdir}/desktoptheme/default/widgets/amarok-*
%{_kde_unstable_appsdir}/kconf_update/amarok*
%{_kde_unstable_appsdir}/solid/actions/amarok*.desktop

%{_kde_unstable_bindir}/amarok
%{_kde_unstable_bindir}/amarok_afttagger
%{_kde_unstable_bindir}/amarokcollectionscanner
%{_kde_unstable_bindir}/amarokmp3tunesharmonydaemon
%{_kde_unstable_bindir}/amarokpkg
%{_kde_unstable_bindir}/amzdownloader

%{_kde_unstable_configdir}/amarok*

%{_kde_unstable_configkcfgdir}/amarokconfig.kcfg

%dir %{_kde_unstable_iconsdir}/hicolor/*/
%dir %{_kde_unstable_iconsdir}/hicolor/*/apps/
%{_kde_unstable_iconsdir}/hicolor/*/apps/amarok.*

%{_kde_unstable_libdir}/libamarok*.so.*
%{_kde_unstable_libdir}/libamarok_service_lastfm_shared.so
%{_kde_unstable_libdir}/libampache_account_login.so

%{_kde_unstable_modulesdir}/amarok_*
%{_kde_unstable_modulesdir}/kcm_amarok_service_*

%{_kde_unstable_servicesdir}/ServiceMenus/amarok_append.desktop
%{_kde_unstable_servicesdir}/amarok*

%{_kde_unstable_servicetypesdir}/amarok*

%exclude %{_kde_unstable_libdir}/libamarok-sqlcollection.so
%exclude %{_kde_unstable_libdir}/libamarok-transcoding.so
%exclude %{_kde_unstable_libdir}/libamarokcore.so
%exclude %{_kde_unstable_libdir}/libamaroklib.so
%exclude %{_kde_unstable_libdir}/libamarokocsclient.so
%exclude %{_kde_unstable_libdir}/libamarokpud.so

%changelog
