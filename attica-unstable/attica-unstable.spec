#
# spec file for package attica
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


%define _soversion 0_4

Name:           attica-unstable
Version:        0.4.2
Release:        0
Summary:        Open Collaboration Service client library
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            https://projects.kde.org/attica
Source:         ftp://ftp.kde.org/pub/kde/stable/attica/attica-git.tar.xz
Source99:       baselibs.conf
BuildRequires:  cmake >= 2.8
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libqt4-devel
Requires:       libattica%{_soversion}-unstable = %{version}
Requires:       libqt4 > 4.7.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Attica is a library to access Open Collaboration Service servers.

%package -n libattica%{_soversion}-unstable
Summary:        Open Collaboration Service client library - development files
Group:          System/GUI/KDE

%description -n libattica%{_soversion}-unstable
Attica is a library to access Open Collaboration Service servers.

%package -n libattica-unstable-devel
Summary:        Open Collaboration Service client library - development files
Group:          Development/Libraries/C and C++
Requires:       libattica%{_soversion}-unstable >= %{version}
Requires:       libqt4-devel

%description -n libattica-unstable-devel
Development files for attica, Attica a library to access Open Collaboration Service servers.

%prep
%setup -q -n attica-git

%build
export RPM_OPT_FLAGS="%optflags -fvisibility-inlines-hidden"
%cmake_kde_unstable -d build
%make_jobs

%install
cd build
make DESTDIR=%{buildroot} install

%post -n libattica%{_soversion}-unstable -p /sbin/ldconfig

%postun -n libattica%{_soversion}-unstable -p /sbin/ldconfig

%files -n libattica%{_soversion}-unstable
%defattr(-,root,root)
%doc README AUTHORS COPYING
%{_kde_unstable_libdir}/libattica*.so.*

%files -n libattica-unstable-devel
%defattr(-,root,root)
%{_kde_unstable_libdir}/libattica*.so
%{_kde_unstable_libdir}/pkgconfig/libattica*.pc
%{_kde_unstable_includedir}/attica

%changelog
