#
# spec file for package patterns-openSUSE
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


Name:           patterns-openSUSE-kde4-unstable
Version:        12.3
Release:        0
Summary:        Meta package for pattern kde4 unstable
License:        MIT
Group:          Metapackages
Url:            http://en.opensuse.org/Patterns
BuildRequires:  patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       patterns-openSUSE-kde4 = 11.1
#Requires:     ark
#Requires:     kcalc
#Requires:     kde4-print-manager
#Requires:     kgpg
#Requires:     kio_mtp
#Requires:     ksnapshot
#Requires:     kwalletmanager
#Requires:     mozilla-kde4-integration
#Requires:     patterns-openSUSE-games
#Requires:     patterns-openSUSE-imaging
#Requires:     patterns-openSUSE-kde4_internet
#Requires:     patterns-openSUSE-kde4_utilities
#Requires:     patterns-openSUSE-multimedia
#Requires:     patterns-openSUSE-non_oss
#Requires:     patterns-openSUSE-office
#Requires:       patterns-openSUSE-kde4-unstable-basis

%description
This package is installed if a pattern is selected to have a working update path

%package basis
Summary:        Meta package for pattern kde4_basis
Group:          Metapackages
Requires:     akregator-unstable
Requires:     nepomuk-core-unstable
Requires:     polkit-kde-agent-1-unstable
Requires:     kdepasswd-unstable
Requires:     keditbookmarks-unstable
Requires:     kde-base-artwork-unstable
Requires:     kmail-unstable
Requires:     knotes-unstable
Requires:     konqueror-unstable
Requires:     konsole-unstable
Requires:     kontact-unstable
Requires:     korganizer-unstable
Requires:     phonon-backend-gstreamer-0_10-unstable
Requires:     kwebkitpart-unstable
Requires:     oxygen-icon-theme-unstable
Requires:     gwenview-unstable
Requires:     kmix-unstable
Requires:     plasmoid-networkmanagement-unstable
Requires:       dolphin-unstable
Requires:       kdebase4-session-unstable
Requires:       kdebase-workspace-unstable
Requires:       kwin-unstable
Requires:       kwrite-unstable
Requires:       plasmoid-folderview-unstable

%description basis
This package is installed if a pattern is selected to have a working update path

%prep

%build

%install

%files
%defattr(-,root,root)

%files basis
%defattr(-,root,root)

%changelog
