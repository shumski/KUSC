#
# spec file for package rekonq
#
# Copyright 2009 Buschmann <buschmann23@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

# norootforbuild

Name:           rekonq-unstable
Version:        X
Release:        1
Summary:        WebKit Based Web Browser for KDE4
License:        GPL-3.0
Url:            http://rekonq.kde.org/
Group:          Productivity/Networking/Web/Browsers
Source0:        rekonq-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  libkde-unstable-devel >= 4.7.0
BuildRequires:  nepomuk-core-unstable-devel
BuildRequires:  libqt4-devel >= 4.8.0
BuildRequires:  libqca2-devel
BuildRequires:  qoauth-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
%kde_unstable_runtime_requires

%description
Rekonq is a web browser for KDE based on WebKit. It first focuses on being a
light, fast & clean way to access to net. Its development is doubly based on
using the new amazing features offered by the WebKit rendering engine and on
the rock solid network KDE technologies.

%prep
%setup -q -n rekonq-%{version}

%build
%cmake_kde_unstable -d build
%make_jobs

%install
%kde_unstable_makeinstall -C build

%if 0%{?suse_version}
%suse_update_desktop_file rekonq Qt KDE Network WebBrowser
%endif

%fdupes -s %{buildroot}

%kde_unstable_post_install

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING*
%{_kde_unstable_applicationsdir}/rekonq.desktop
%{_kde_unstable_appsdir}/rekonq/
%{_kde_unstable_bindir}/rekonq
%{_kde_unstable_iconsdir}/hicolor/*/apps/rekonq.png
%{_kde_unstable_libdir}/libkdeinit4_rekonq.so
%{_kde_unstable_configkcfgdir}/rekonq.kcfg
%dir %{_kde_unstable_htmldir}/en/rekonq
%{_kde_unstable_htmldir}/en/rekonq/*

%dir %{_kde_unstable_iconsdir}/hicolor/*
%dir %{_kde_unstable_iconsdir}/hicolor/*/apps/

%changelog
