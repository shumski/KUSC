#
# spec file for package oxygen-gtk2
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


Name:           oxygen-gtk2-unstable
Version:        1.3.2.1
Release:        0
Summary:        A Port of the default KDE Widget Theme (Oxygen), to GTK 2.x
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            https://projects.kde.org/projects/playground/artwork/oxygen-gtk/
Source0:        ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk2/%{version}/src/oxygen-gtk2-%{version}.tar.bz2
Source100:      baselibs.conf
BuildRequires:  kde-unstable-filesystem
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Oxygen-Gtk2 is a port of the default KDE widget theme (Oxygen), to gtk 2.x.

It's primary goal is to ensure visual consistency between gtk-based and qt-based
applications running under KDE. A secondary objective is to also have a
stand-alone nice looking gtk theme that would behave well on other Desktop
Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this attempt does
not depend on Qt (via some Qt to Gtk conversion engine), nor does render the
widget appearance via hard coded pixmaps, which otherwise breaks everytime some
setting is changed in KDE.

%package -n gtk2-engine-oxygen-unstable
Summary:        Oxygen GTK 2.x Theme Engine
Group:          System/GUI/Other

%description -n gtk2-engine-oxygen-unstable
Oxygen-Gtk2 is a port of the default KDE widget theme (Oxygen), to gtk 2.x.

It's primary goal is to ensure visual consistency between gtk-based and qt-based
applications running under KDE. A secondary objective is to also have a
stand-alone nice looking gtk theme that would behave well on other Desktop
Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this attempt does
not depend on Qt (via some Qt to Gtk conversion engine), nor does render the
widget appearance via hard coded pixmaps, which otherwise breaks everytime some
setting is changed in KDE.

This package contains the Oxygen gtk 2.x theme engine.

%package -n gtk2-theme-oxygen-unstable
Summary:        Oxygen GTK 2.x Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-oxygen-unstable = %{version}


%description -n gtk2-theme-oxygen-unstable
Oxygen-Gtk2 is a port of the default KDE widget theme (Oxygen), to gtk 2.x.

It's primary goal is to ensure visual consistency between gtk-based and qt-based
applications running under KDE. A secondary objective is to also have a
stand-alone nice looking gtk theme that would behave well on other Desktop
Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this attempt does
not depend on Qt (via some Qt to Gtk conversion engine), nor does render the
widget appearance via hard coded pixmaps, which otherwise breaks everytime some
setting is changed in KDE.

This package contains the Oxygen gtk 2.x theme.

%prep
%setup -q -n oxygen-gtk2-%{version}

%build
mkdir -p build
pushd build
  %cmake_kde_unstable
  %make_jobs
popd

%install
pushd build
%kde_unstable_makeinstall
popd

%files -n gtk2-engine-oxygen-unstable
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{_kde_unstable_libdir}/gtk-2.0/2.10.0/engines/liboxygen-gtk.so

%files -n gtk2-theme-oxygen-unstable
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{_kde_unstable_bindir}/oxygen-gtk-demo
%dir %{_kde_unstable_datadir}/themes/oxygen-gtk
%{kde_unstable__datadir}/themes/oxygen-gtk/gtk-2.0/

%changelog
