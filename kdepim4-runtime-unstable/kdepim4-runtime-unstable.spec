#
# spec file for package kdepim4-runtime
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


Name:           kdepim4-runtime-unstable
Version:        4.10.40_20130331
Release:        0
Summary:        Base package of kdepim
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        kdepim-runtime-git.tar.xz
Source1:        akonadi.png
Patch0:         4_8_BRANCH.diff
Patch1:         disable-knut.diff
BuildRequires:  fdupes
BuildRequires:  libkdepimlibs-unstable-devel akonadi-runtime-unstable
BuildRequires:  xz
BuildRequires:  libkgapi2-unstable-devel libkgapi1-unstable-devel
#BuildRequires:  libkolab-devel
BuildRequires:  nepomuk-core-unstable-devel
Suggests:       kontact
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_akonadi_requires
%kde_unstable_pimlibs_requires
%kde_unstable_runtime_requires

%description
This package contains the Akonadi files of the kdepim module.

%prep
%setup -q -n kdepim-runtime-git
%patch0 -p1
%patch1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  cd ..
  #remove menu entries of development tools
  mkdir -p %{buildroot}%{_kde_unstable_datadir}/pixmaps
  install $RPM_SOURCE_DIR/akonadi.png %{buildroot}%{_kde_unstable_datadir}/pixmaps/
  export PATH=/opt/kde-unstable/:$PATH
  %suse_update_desktop_file -u akonaditray      Network  Email
  %fdupes -s %{buildroot}
  # remove stuff we don't want to package
  rm %{buildroot}%_kde_unstable_libdir/libakonadi*.so
  rm %{buildroot}%_kde_unstable_libdir/libkmindexreader.so
  rm %{buildroot}%_kde_unstable_libdir/libmaildir.so
  export PATH=/opt/kde-unstable/:$PATH
  %kde_unstable_post_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}
  rm -rf filelists

%files
%defattr(-,root,root)
%{_kde_unstable_datadir}/akonadi
%{_kde_unstable_datadir}/autostart/kaddressbookmigrator.desktop
%{_kde_unstable_datadir}/dbus-1/interfaces/*
%{_kde_unstable_datadir}/mime/packages/*.xml
%{_kde_unstable_datadir}/pixmaps/akonadi.png
%{_kde_unstable_datadir}/ontology/kde/
%{_kde_unstable_applicationsdir}/accountwizard.desktop
%{_kde_unstable_applicationsdir}/akonaditray.desktop
%{_kde_unstable_appsdir}/akonadi
%{_kde_unstable_appsdir}/akonadi_maildispatcher_agent/
%{_kde_unstable_bindir}/*
%{_kde_unstable_configdir}/*
%{_kde_unstable_iconsdir}/hicolor/*/apps/*.png
%{_kde_unstable_libdir}/libakonadi-filestore.so.4*
%{_kde_unstable_libdir}/libakonadi-xml.so.4*
%{_kde_unstable_libdir}/libkdepim-copy.so.4*
%{_kde_unstable_libdir}/libkmindexreader.so.4*
%{_kde_unstable_libdir}/libmaildir.so.4*
%{_kde_unstable_modulesdir}/*
%{_kde_unstable_servicetypesdir}/davgroupwareprovider.desktop
%{_kde_unstable_servicetypesdir}/akonadinepomukfeeder.desktop
%{_kde_unstable_sharedir}/services
%{_kde_unstable_libdir}/libnepomukfeederpluginlib.a
%{_kde_unstable_libdir}/libkdepim-copy.so
%{_kde_unstable_appsdir}/akonadi_nepomuk_feeder/
%{_kde_unstable_appsdir}/nepomukpimindexerutility/
%dir %{_kde_unstable_iconsdir}/hicolor/128x128
%dir %{_kde_unstable_iconsdir}/hicolor/128x128/apps
%dir %{_kde_unstable_iconsdir}/hicolor/16x16/apps
%dir %{_kde_unstable_iconsdir}/hicolor/32x32/apps
%dir %{_kde_unstable_iconsdir}/hicolor/48x48/apps
%dir %{_kde_unstable_iconsdir}/hicolor/64x64
%dir %{_kde_unstable_iconsdir}/hicolor/64x64/apps

%changelog
