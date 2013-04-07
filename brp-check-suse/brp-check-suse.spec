#
# spec file for package brp-check-suse
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


Name:           brp-check-suse
AutoReqProv:    off
Summary:        Build root policy check scripts
License:        GPL-2.0+
Group:          Development/Tools/Building
# we need the full perl because of XML Parsing and utf-8 
Requires:       perl
Version:        1.0
Release:        0
Url:            http://gitorious.org/opensuse/brp-check-suse/
#
# Note: don't rebuild this manually. Instead submit your patches
# for inclusion in the git repo!
#
# git clone git://gitorious.org/opensuse/brp-check-suse.git
# cd post-build-checks
# make package
#
Source0:        %{name}-%{version}.tar.bz2
Patch0:         check-broken-symlinks.diff
Patch1:         add-unstable-path.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global provfind sh -c "grep -v 'brp-desktop.data' | %__find_provides"
%global __find_provides %provfind

%description
This package contains all suse scripts called in the 
build root checking or in parts implemeting SUSE policies.


%prep
%setup -q
%ifnarch x86_64 s390x ppc64
rm brp-65-lib64-linux
%endif
%patch0 -p1
%patch1 -p1

%build
# nothing to do

%install
install -d $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d
mv brp*data $RPM_BUILD_ROOT/usr/lib/rpm/
cp -a brp-* $RPM_BUILD_ROOT/usr/lib/rpm/brp-suse.d

%files
%defattr(-, root, root)
%doc COPYING
/usr/lib/rpm/*

%changelog
