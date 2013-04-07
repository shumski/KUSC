#
# spec file for package akonadi-runtime
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

Name:           akonadi-runtime-unstable
Version:        1.9.52
Release:        0
%define rversion %{version}
Summary:        PIM Storage Service
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://akonadi-project.org
Source:         akonadi-git.tar.xz
Patch0:         gcc41.diff
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.8.8
BuildRequires:  fdupes
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libsoprano-unstable-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  shared-mime-info
#There is a warning, but it's not needed at all, but for completness
%if !0%{?sles_version}
BuildRequires:  mysql-community-server
%else
BuildRequires:  mysql
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# rename from 10.3, which had 4.x version
Provides:       akonadi = %{version}
Obsoletes:      akonadi < 4.1
Requires(post):    shared-mime-info
Requires(postun):  shared-mime-info

Requires:       libakonadiprotocolinternals1-unstable = %{version}
Requires:       libqt4-sql-mysql
Requires:       mysql
Requires:       libqt4 >= %(rpm -q --queryformat '%{VERSION}' libqt4)
%if !0%{?sles_version}
Suggests:       mysql-community-server
%endif

%description
This package contains the data files of Akonadi, the KDE PIM storage
service.

%package -n libakonadiprotocolinternals-unstable-devel
Summary:        PIM Storage Service: Build Environment
Group:          Development/Libraries/X11
Requires:       libakonadiprotocolinternals1-unstable = %{version}
Requires:       libsoprano-unstable-devel
Requires:       libqt4-devel >= %( echo `rpm -q --queryformat '%{VERSION}' libqt4-devel`)
# rename from 10.3, which had 4.x version
Provides:       akonadi-devel = %{version}
Obsoletes:      akonadi-devel < 4.1

%description -n libakonadiprotocolinternals-unstable-devel
This package contains development files of Akonadi, the KDE PIM storage
service.

%package -n libakonadiprotocolinternals1-unstable
Summary:        PIM Storage Service
Group:          System/GUI/KDE
%requires_ge    libqt4

%description -n libakonadiprotocolinternals1-unstable
This package contains the data files of Akonadi, the KDE PIM storage
service.

%prep
%setup -q -n akonadi-git
%patch0

%build
  %cmake_kde_unstable -d build -- -DCONFIG_INSTALL_DIR=/opt/kde-unstable/etc -DAKONADI_BUILD_QSQLITE=FALSE
  %make_jobs

%install
  cd build
  make DESTDIR=%{buildroot} install
  %fdupes -s %{buildroot}%{_prefix}/include

%post
/sbin/ldconfig
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :

%post -n libakonadiprotocolinternals1-unstable -p /sbin/ldconfig

%postun -n libakonadiprotocolinternals1-unstable -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_kde_unstable_bindir}/akonadi_agent_launcher
%{_kde_unstable_bindir}/akonadi_agent_server
%{_kde_unstable_bindir}/akonadi_control
%{_kde_unstable_bindir}/akonadi_rds
%{_kde_unstable_bindir}/akonadictl
%{_kde_unstable_bindir}/akonadiserver
%dir %{_kde_unstable_sysconfdir}
%dir %{_kde_unstable_datadir}/dbus-1/services
%dir %{_kde_unstable_datadir}/mime
%dir %{_kde_unstable_datadir}/mime/packages
%dir %{_kde_unstable_sysconfdir}/akonadi
%config %{_kde_unstable_sysconfdir}/akonadi/mysql-global.conf
%config %{_kde_unstable_sysconfdir}/akonadi/mysql-global-mobile.conf
%{_kde_unstable_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_kde_unstable_datadir}/mime/packages/akonadi-mime.xml
# A database access plugin, not a development file
#%dir %{_kde_unstable_libdir}/plugins/
#%{_kde_unstable_libdir}/plugins/libqsqlite3.so

%files -n libakonadiprotocolinternals-unstable-devel
%defattr(-,root,root)
%dir %{_kde_unstable_includedir}/akonadi
%{_kde_unstable_includedir}/akonadi/private
%dir %{_kde_unstable_libdir}/cmake
%{_kde_unstable_libdir}/cmake/Akonadi
%{_kde_unstable_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_kde_unstable_libdir}/libakonadiprotocolinternals.so
%{_kde_unstable_libdir}/pkgconfig/akonadi.pc

%files -n libakonadiprotocolinternals1-unstable
%defattr(-,root,root)
%{_kde_unstable_libdir}/libakonadiprotocolinternals.so.1*

%changelog
