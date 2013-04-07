#
# spec file for package kate
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


Name:           kate-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        Advanced Text Editor
License:        GPL-2.0+
Group:          Productivity/Editors/Other
Url:            http://www.kde.org/
Source0:        kate-git.tar.xz
BuildRequires:  fdupes
BuildRequires:  libkde-unstable-devel
BuildRequires:  libkactivities-unstable-devel
BuildRequires:  xz
BuildRequires:  python-kde4-unstable-devel
BuildRequires:  libqjson-devel
Requires:       libktexteditor-unstable = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_runtime_requires

%description
Kate is an advanced text editor for KDE.
  
%prep
%setup -q -n kate-git

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %suse_update_desktop_file kate                 TextEditor
  %suse_update_desktop_file kwrite               TextEditor
  %fdupes -s %{buildroot}
  %kde_unstable_post_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}
  rm -rf filelists

%package devel
Summary:        Advanced Text Editor Development Headers
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       libkde-unstable-devel

%description devel
Files needed for development of Kate plugins.
 
%files devel
%defattr(-,root,root)
%{_kde_unstable_includedir}/kate/
%{_kde_unstable_includedir}/kate_export.h
%{_kde_unstable_libdir}/libkateinterfaces.so
%{_kde_unstable_libdir}/libkatepartinterfaces.so

%package -n libktexteditor-unstable
Summary:        Advanced Text Editor library
Group:          Productivity/Editors/Other

%description -n libktexteditor-unstable
The libraries shared by kwrite and kate editors.
 
%post -n libktexteditor-unstable -p /sbin/ldconfig

%postun -n libktexteditor-unstable -p /sbin/ldconfig

%files -n libktexteditor-unstable
%defattr(-,root,root)
%{_kde_unstable_appsdir}/katepart/
%{_kde_unstable_appsdir}/ktexteditor_exporter/
%{_kde_unstable_appsdir}/ktexteditor_iconinserter/
%{_kde_unstable_appsdir}/ktexteditor_insertfile/
%{_kde_unstable_iconsdir}/hicolor/*/apps/ktexteditorautobrace.svgz
%{_kde_unstable_iconsdir}/oxygen/*/actions/*.png
%dir %{_kde_unstable_iconsdir}/hicolor/scalable
%dir %{_kde_unstable_iconsdir}/hicolor/scalable/apps
%dir %{_kde_unstable_iconsdir}/oxygen/16x16
%dir %{_kde_unstable_iconsdir}/oxygen/16x16/actions
%{_kde_unstable_libdir}/libkatepartinterfaces.so.*
%{_kde_unstable_modulesdir}/katepart.so
%{_kde_unstable_modulesdir}/ktexteditor_*.so
%{_kde_unstable_modulesdir}/pateplugin.so
%{_kde_unstable_servicesdir}/ktexteditor_*.desktop
%{_kde_unstable_servicesdir}/pate.desktop

%files
%defattr(-,root,root)
%config %{_kde_unstable_configdir}/katemoderc
%config %{_kde_unstable_configdir}/katerc
%{_kde_unstable_py_sitedir}/PyKate4

%exclude %{_kde_unstable_modulesdir}/katepart.so
%{_kde_unstable_applicationsdir}/kate.desktop
%{_kde_unstable_appsdir}/kate/
%{_kde_unstable_appsdir}/katexmltools/
%{_kde_unstable_appsdir}/kconf_update/kate-2.4.upd
%{_kde_unstable_bindir}/kate
%{_kde_unstable_htmldir}/en/kate/
%{_kde_unstable_iconsdir}/hicolor/*/apps/kate.*
%dir %{_kde_unstable_iconsdir}/hicolor/128x128
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/apps
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/22x22
%dir %{_kde_unstable_iconsdir}/hicolor/22x22/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps
%{_kde_unstable_libdir}/libkateinterfaces.so.*
%{_kde_unstable_libdir}/libkdeinit4_kate.so
%{_kde_unstable_mandir}/man?/*
%{_kde_unstable_modulesdir}/kate*.so
%{_kde_unstable_modulesdir}/plasma_applet_katesession.so
%{_kde_unstable_servicesdir}/kate*.desktop
%{_kde_unstable_servicesdir}/plasma-applet-katesession.desktop
%{_kde_unstable_servicetypesdir}/kateplugin.desktop
%{_kde_unstable_configdir}/kateschemarc
%{_kde_unstable_configdir}/katesyntaxhighlightingrc

%package -n kwrite-unstable
Summary:        KDE Text Editor
Group:          Productivity/Editors/Other
Requires:       libktexteditor-unstable = %{version}
%kde_unstable_runtime_requires

%description -n kwrite-unstable
KWrite is the default text editor of the K desktop environment.
 
%package -n kwrite-doc-unstable
Summary:        KDE Text Editor: Documentation
Group:          Productivity/Editors/Other
Requires:       kwrite-unstable = %{version}

%description -n kwrite-doc-unstable
KWrite is the default text editor of the K desktop environment.

This package contains the documentation for KWrite
 
%post -n kwrite-unstable -p /sbin/ldconfig

%postun -n kwrite-unstable -p /sbin/ldconfig

%files -n kwrite-unstable
%defattr(-,root,root)
%{_kde_unstable_bindir}/kwrite
%{_kde_unstable_libdir}/libkdeinit4_kwrite.so
%{_kde_unstable_applicationsdir}/kwrite.desktop
%{_kde_unstable_appsdir}/kwrite/

%files -n kwrite-doc-unstable
%defattr(-,root,root,-)
%doc %lang(en) %{_kde_unstable_htmldir}/en/kwrite/

%changelog
