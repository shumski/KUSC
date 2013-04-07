#
# spec file for package NetworkManager-kde4 (Version 0.9.svn1043876)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Url:            http://www.kde.org
Name:           NetworkManager-kde4-unstable
BuildRequires:  NetworkManager-devel > 0.8.997
BuildRequires:  kdebase-workspace-unstable-devel
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  libQtNetworkManager-unstable-devel
BuildRequires:  libQtModemManager-unstable-devel
Version:        0.9.3_git20111023
Release:        1
License:        GPL v2 or later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          System/GUI/KDE
Summary:        NetworkManager client for KDE 4
Source0:        networkmanagement-%{version}.tar.bz2
Source1:        knetworkmanager.default.sh
Source99:       NetworkManager-kde4-unstable-rpmlintrc
Requires:       NetworkManager-kde4-unstable-libs = %{version}-%{release}
Requires:       mobile-broadband-provider-info
ExcludeArch:    s390 s390x
%kde_unstable_runtime_requires

%description
KNetworkManager is a KDE 4 applet for controlling
network connections on systems that use the NetworkManager service.



Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package libs
License:        LGPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Requires:       NetworkManager
%kde_unstable_runtime_requires

%description libs
Support libraries for KNetworkManager and Network Management plasmoid
KNetworkManager is a KDE 4 applet and connection editor for controlling
network connections on systems that use the NetworkManager service



Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package -n plasmoid-networkmanagement-unstable
License:        GPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-client
Requires:       %{name}-libs = %{version}-%{release}
Requires:       mobile-broadband-provider-info
%kde_unstable_runtime_requires

%description -n plasmoid-networkmanagement-unstable
Network Management Plasma applet for controlling network connections
on systems that use the NetworkManager service.

%package -n NetworkManager-openvpn-kde4-unstable
License:        GPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-openvpn-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       NetworkManager-openvpn
%kde_unstable_runtime_requires

%description -n NetworkManager-openvpn-kde4-unstable
OpenVPN VPN plugin for KDE Network Management components.



Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package -n NetworkManager-openconnect-kde4-unstable
License:        GPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-openconnect-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       NetworkManager-openconnect
%kde_unstable_runtime_requires

%description -n NetworkManager-openconnect-kde4-unstable
OpenConnect VPN plugin for KDE Network Management components.



Authors:
--------
    Will Stephenson <wstephenson@novell.com>


%package -n NetworkManager-pptp-kde4-unstable
License:        GPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-pptp-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       NetworkManager-pptp
%kde_unstable_runtime_requires

%description -n NetworkManager-pptp-kde4-unstable
PPTP VPN plugin for KDE Network Management components.


Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package -n NetworkManager-vpnc-kde4-unstable
License:        GPL v2 or later
Summary:        NetworkManager client for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-vpnc-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       NetworkManager-vpnc
%kde_unstable_runtime_requires

%description -n NetworkManager-vpnc-kde4-unstable
Cisco VPN plugin for KDE Network Management components.


Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package -n NetworkManager-novellvpn-kde4-unstable
License:        GPL v2 or later
Summary:        NovellVPN NetworkManager plugin for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-novellvpn-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       NetworkManager-novellvpn
%kde_unstable_runtime_requires

%description -n NetworkManager-novellvpn-kde4-unstable
NovellVPN VPN plugin for KDE Network Management components.



Authors:
--------
    Will Stephenson <wstephenson@novell.com>

%package -n NetworkManager-strongswan-kde4-unstable
License:        GPL v2 or later
Summary:        Strongswan NetworkManager plugin for KDE 4
Group:          System/GUI/KDE
Provides:       NetworkManager-strongswan-frontend
Requires:       %{name}-libs = %{version}-%{release}
Requires:       strongswan
%kde_unstable_runtime_requires

%description -n NetworkManager-strongswan-kde4-unstable
Strongswan VPN plugin for KDE Network Management components.



Authors:
--------
    Will Stephenson <wstephenson@novell.com>


%package libs-devel
Group:          Development/Libraries/KDE
Summary:        Development files for NetworkManager-kde4
Requires:       %{name}-libs = %{version}

%description libs-devel
Support libraries for KNetworkManager and Network Management plasmoid
KNetworkManager is a KDE 4 applet and connection editor for controlling
network connections on systems that use the NetworkManager service



Authors:
--------
    Will Stephenson <wstephenson@novell.com>


%prep
%setup -q -n networkmanagement-%{version}

%build
  %cmake_kde_unstable -d build \-DDBUS_SYSTEM_POLICY_DIR=/opt/kde-unstable/etc/dbus-1/system.d 
  make VERBOSE=1

%install
  cd build
  %kde_unstable_makeinstall
  %kde_post_install
%ifarch s390 s390x
rm -f $RPM_BUILD_ROOT/%_kde_unstable_modules/networkmanagement_openvpnui.so
rm -f $RPM_BUILD_ROOT/%_kde_unstable_servicesdir/networkmanagement_openvpnui.desktop
%endif
  cd ..

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf "$RPM_BUILD_ROOT"


%files libs
%defattr(-,root,root)
%_kde_unstable_servicesdir/kcm_networkmanagement.desktop
%dir %_kde_unstable_appsdir/networkmanagement
%_kde_unstable_appsdir/networkmanagement/*
%_kde_unstable_modulesdir/kcm_networkmanagement.so
%_kde_unstable_modulesdir/kcm_networkmanagement_tray.so
#_kde_unstable_modulesdir/solid_networkmanager09.so
%{_kde_unstable_libdir}/libknmui.so.*
%{_kde_unstable_libdir}/libknminternals.so.*
%{_kde_unstable_libdir}/libknmservice.so.*
%{_kde_unstable_libdir}/libknmclient.so.*
%{_kde_unstable_libdir}/libknm_nm.so*
#{_kde_unstable_libdir}/libsolidcontrolfuture.so
#{_kde_unstable_libdir}/libsolidcontrolnm09.so.*
#{_kde_unstable_libdir}/libsolidcontrolnm09ifaces.so.*
%_kde_unstable_servicetypesdir/networkmanagement_vpnuiplugin.desktop
#_kde_unstable_servicetypesdir/solidnetworkmanagernm09.desktop
%_kde_unstable_servicesdir/kcm_networkmanagement_tray.desktop
#_kde_unstable_servicesdir/solidbackends/solid_networkmanager09.desktop
%_kde_unstable_iconsdir/oxygen/16x16/devices/
%_kde_unstable_iconsdir/oxygen/22x22/devices/
%_kde_unstable_iconsdir/oxygen/32x32/devices/
%_kde_unstable_iconsdir/oxygen/48x48/devices/
%_kde_unstable_iconsdir/oxygen/64x64/devices/
%_kde_unstable_iconsdir/oxygen/128x128/devices/
%_kde_unstable_modulesdir/libexec/networkmanagement_configshell
%_kde_unstable_appsdir/desktoptheme/default/icons/network2.svgz

%files -n plasmoid-networkmanagement-unstable
%defattr(-,root,root)
%_kde_unstable_servicesdir/plasma-applet-networkmanagement.desktop
%_kde_unstable_modulesdir/plasma_applet_networkmanagement.so
%_kde_unstable_modulesdir/kded_networkmanagement.so
%_kde_unstable_servicesdir/kded
%_kde_unstable_modulesdir/plasma_engine_networkmanagement.so
%_kde_unstable_servicesdir/plasma-engine-networkmanagement.desktop

%files -n NetworkManager-openvpn-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_openvpnui.so
%_kde_unstable_servicesdir/networkmanagement_openvpnui.desktop

%files -n NetworkManager-vpnc-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_vpncui.so
%_kde_unstable_servicesdir/networkmanagement_vpncui.desktop

%files -n NetworkManager-pptp-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_pptpui.so
%_kde_unstable_servicesdir/networkmanagement_pptpui.desktop

%files -n NetworkManager-novellvpn-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_novellvpnui.so
%_kde_unstable_servicesdir/networkmanagement_novellvpnui.desktop

%if 0
%files -n NetworkManager-openconnect-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_openconnectui.so
%_kde_unstable_servicesdir/networkmanagement_openconnectui.desktop
%endif

%files -n NetworkManager-strongswan-kde4-unstable
%defattr(-,root,root)
%_kde_unstable_modulesdir/networkmanagement_strongswanui.so
%_kde_unstable_servicesdir/networkmanagement_strongswanui.desktop

%files libs-devel
%defattr(-,root,root)
%{_kde_unstable_libdir}/libknmui.so
%{_kde_unstable_libdir}/libknminternals.so
%{_kde_unstable_libdir}/libknmservice.so
%{_kde_unstable_libdir}/libknmclient.so
#{_kde_unstable_libdir}/libsolidcontrolnm09.so
#{_kde_unstable_libdir}/libsolidcontrolnm09ifaces.so
#/usr/include/solid/controlnm09/

%changelog
