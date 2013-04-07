#
# spec file for package kde-gtk-config
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


Name:           kde-gtk-config-unstable
Version:        2.1.1
Release:        0
Summary:        KCM Module to Configure GTK2 and GTK3 Applications Appearance Under KDE
License:        LGPL-3.0+ and GPL-3.0+
Group:          System/GUI/KDE
Url:            https://projects.kde.org/projects/playground/base/kde-gtk-config/
Source0:        ftp://ftp.kde.org/pub/kde/stable/kde-gtk-config/%{version}/src/kde-gtk-config-%{version}.tar.bz2
Source1:        kde_gtk_config.suse.sh
Source2:        gtkrc-2.0-kde4.template
Source3:        gtk3-settings.ini-kde4.template
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libkde-unstable-devel
BuildRequires:  pango-devel
%kde_unstable_runtime_requires
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
kde-gtk-config is a KCM module to configure GTK2 and GTK3 applications
appearance under KDE.

Among its many features, it lets you:
 - Choose which theme is used for GTK2 and GTK3 applications.
 - Tweak some GTK applications behaviour.
 - Select what icon theme to use in GTK applications.
 - Select GTK applications default fonts.
 - Easily browse and install new GTK2 and GTK3 themes.

%lang_package

%prep
%setup -q -n kde-gtk-config-%{version}

%build
%cmake_kde_unstable -d build
%make_jobs

%install
%kde_unstable_makeinstall -C build

install -Dpm 0755 %{SOURCE1} %{buildroot}%{_kde_unstable_sharedir}/env/kde_gtk_config.suse.sh
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_kde_unstable_appsdir}/%{name}/gtkrc-2.0-kde4.template
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_kde_unstable_appsdir}/%{name}/gtk3-settings.ini-kde4.template

%kde_unstable_post_install

%find_lang kde-gtk-config

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_kde_unstable_appsdir}/kcm-gtk-module/
%{_kde_unstable_appsdir}/kde-gtk-config/
%{_kde_unstable_bindir}/gtk_preview
%{_kde_unstable_bindir}/gtk3_preview
%{_kde_unstable_bindir}/reload_gtk_apps
%{_kde_unstable_configdir}/*.knsrc
%{_kde_unstable_iconsdir}/hicolor/*x*/apps/gtkconfig.png
%dir %{_kde_unstable_sharedir}/env
%{_kde_unstable_sharedir}/env/kde_gtk_config.suse.sh
%{_kde_unstable_modulesdir}/kcm_cgc.so
%{_kde_unstable_servicesdir}/kde-gtk-config.desktop

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
