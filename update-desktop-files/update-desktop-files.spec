#
# spec file for package update-desktop-files
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


Name:           update-desktop-files
Version:        12.1
Release:        0
Summary:        A Build Tool to Update Desktop Files
License:        GPL-2.0+
Group:          Development/Tools/Building
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         suse_update_desktop_file.sh
Source1:        map-desktop-category.sh
Source2:        macro
Source4:        brp-trim-desktop.sh
# This is not true technically, but we do that to make the rpm macros from
# desktop-file-utils available to most packages that ship a .desktop file
# (since they already have a update-desktop-files BuildRequires).
Requires:       desktop-file-utils
BuildArch:      noarch

%description
This package provides further translations and a shell script to update
desktop files. It is used by the %%suse_update_desktop_file rpm macro.

%package -n brp-trim-desktopfiles
Summary:        Trim translations from .deskop files
Group:          Development/Tools/Building

%description -n brp-trim-desktopfiles
Trim translations from all .deskop files found in build root

%prep
%setup -q -n . -D -T 0
mkdir %name
cd %name

%build

%install
mkdir -p $RPM_BUILD_ROOT%_rpmconfigdir
install -m0755 %SOURCE0 %SOURCE1 $RPM_BUILD_ROOT%_rpmconfigdir
install -m0644 -D %SOURCE2 $RPM_BUILD_ROOT/etc/rpm/macros.%name
install -m0755 -D %SOURCE4 $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d/brp-70-trim-desktopfiles

%files
%defattr(-,root,root)
%_rpmconfigdir/*
%exclude %_rpmconfigdir/brp-suse.d
/etc/rpm/*

%files -n brp-trim-desktopfiles
%defattr(-,root,root)
%_rpmconfigdir/brp-suse.d

%changelog
