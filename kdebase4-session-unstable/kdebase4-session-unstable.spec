#
# spec file for package kdebase4-session
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



Name:           kdebase4-session-unstable
Version:        %_kde_unstable_platform_version
Release:        11
License:        GPLv2+
Summary:        The KDE Session
Url:            http://www.kde.org/
Group:          System/GUI/KDE
Source1:        kde-unstable.desktop
Source2:        COPYING
Source3:        kde-unstable.sh
Source4:        kde-unstable64.sh
Source5:        startkde-unstable
Source6:        kdeglobals
BuildRequires:  kde-unstable-filesystem
Requires:       kdebase-workspace-unstable >= %_kde_unstable_platform_version
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1140
Requires:       update-desktop-files
%endif
Provides:       kdebase3-session = %{version}
Obsoletes:      kdebase3-session <= 3.5.1

%description
This package contains the startup scripts necessary to start a KDE
session from kdm.

%prep

%build

%install
mkdir -p %{buildroot}%{_kde_unstable_configdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_kde_unstable_configdir}/kdeglobals
install -m 0755 -d %{buildroot}%{_datadir}/xsessions/
mkdir -p %{buildroot}%{_kde_unstable_bindir}
install -m 0755 %{SOURCE5} %{buildroot}%{_kde_unstable_bindir}/startkde-unstable
mkdir -p %{buildroot}%{_kde_unstable_sharedir}/env/
%ifarch i386 i486 i586 i686
install -m 0755 %{SOURCE3} %{buildroot}%{_kde_unstable_sharedir}/env/kde-unstable.sh
cat >> %{buildroot}%{_kde_unstable_bindir}/startkde-unstable << EOF
#!/bin/sh

. /opt/kde-unstable/share/kde4/env/kde-unstable.sh
exec startkde
EOF
%else 
install -m 0755 %{SOURCE4} %{buildroot}%{_kde_unstable_sharedir}/env/kde-unstable64.sh
cat >> %{buildroot}%{_kde_unstable_bindir}/startkde-unstable << EOF
#!/bin/sh

. /opt/kde-unstable/share/kde4/env/kde-unstable64.sh
exec startkde
EOF
%endif


cp %{SOURCE1} %{buildroot}%{_datadir}/xsessions/
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/doc/packages/kdebase4-session-unstable/COPYING

%clean
  rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_kde_unstable_configdir}
%{_kde_unstable_configdir}/kdeglobals
%{_kde_unstable_bindir}/startkde-unstable
%dir %{_kde_unstable_sharedir}/env/
%ifarch i386 i486 i586 i686
%{_kde_unstable_sharedir}/env/kde-unstable.sh
%endif
%ifarch x86_64
%{_kde_unstable_sharedir}/env/kde-unstable64.sh
%endif
%{_datadir}/xsessions/kde-unstable.desktop
%dir %{_datadir}/doc/packages/kdebase4-session-unstable
%{_datadir}/doc/packages/kdebase4-session-unstable/COPYING

%changelog
