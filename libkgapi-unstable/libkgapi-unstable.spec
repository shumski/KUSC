#
# spec file for package akonadi-google
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

Name:           libkgapi-unstable
Version:        4.10.40_20130406
Release:        0
License:        GPL-3.0+
Summary:        Extension for accessing your Google data
Url:            http://www.progdan.cz/
Group:          System/GUI/KDE
Source0:        libkgapi-git.tar.xz
BuildRequires:  libkde-unstable-devel
BuildRequires:  libkdepimlibs-unstable-devel
BuildRequires:  libqjson-devel
BuildRequires:  libxslt-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde_unstable_akonadi_requires
%kde_unstable_runtime_requires
%kde_unstable_pimlibs_requires

%description
An extension for accessing some Google services, such as Google Calendar, Google Contacts and Google tasks

%package -n libkgapi1-unstable
Summary:        Akonadi resource to access your Google data
Group:          Development/Libraries/KDE
Provides:       libkgapi0-unstable = %{version}
Obsoletes:      libkgapi0-unstable < %{version}

%description -n libkgapi1-unstable
An extension for accessing some Google services, such as Google Calendar, Google Contacts and Google tasks

%package -n libkgapi2-1-unstable
Summary:        Akonadi resource to access your Google data
Group:          Development/Libraries/KDE

%description -n libkgapi2-1-unstable
An extension for accessing some Google services, such as Google Calendar, Google Contacts and Google tasks

%package -n libkgapi1-unstable-devel
Summary:        Akonadi resource to access your Google data
Group:          Development/Libraries/KDE
Requires:       libkde-unstable-devel
Requires:       libkgapi1-unstable = %{version}
Requires:       libqjson-devel
Requires:       libxslt-devel
Obsoletes:      libkgapi-unstable-devel <= %{version}
Provides:       libkgapi-unstable-devel = %{version}

%description -n libkgapi1-unstable-devel
An extension for accessing some Google services, such as Google Calendar, Google Contacts and Google tasks

%package -n libkgapi2-unstable-devel
Summary:        Akonadi resource to access your Google data
Group:          Development/Libraries/KDE
Requires:       libkde-unstable-devel
Requires:       libkgapi2-1-unstable = %{version}
Requires:       libqjson-devel
Requires:       libxslt-devel

%description -n libkgapi2-unstable-devel
An extension for accessing some Google services, such as Google Calendar, Google Contacts and Google tasks

%lang_package
%prep
%setup -q -n libkgapi-git

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %kde_unstable_post_install
  cd ..

%post -n libkgapi1-unstable -p /sbin/ldconfig

%postun -n libkgapi1-unstable -p /sbin/ldconfig

%post -n libkgapi2-1-unstable -p /sbin/ldconfig

%postun -n libkgapi2-1-unstable -p /sbin/ldconfig

%files -n libkgapi1-unstable
%defattr(-,root,root)
%doc LICENSE README
%{_kde_unstable_libdir}/libkgapi.so.*

%files -n libkgapi2-1-unstable
%defattr(-,root,root)
%doc LICENSE README
%{_kde_unstable_libdir}/libkgapi2.so.*

%files -n libkgapi1-unstable-devel
%defattr(-,root,root)
%doc LICENSE README
%{_kde_unstable_libdir}/libkgapi.so
%{_kde_unstable_libdir}/pkgconfig/libkgapi.pc
%{_kde_unstable_includedir}/libkgapi/
%{_kde_unstable_libdir}/cmake/LibKGAPI/

%files -n libkgapi2-unstable-devel
%defattr(-,root,root)
%doc LICENSE README
%{_kde_unstable_libdir}/libkgapi2.so
%{_kde_unstable_libdir}/pkgconfig/libkgapi2.pc
%{_kde_unstable_includedir}/libkgapi2/
%{_kde_unstable_includedir}/LibKGAPI2/
%{_kde_unstable_libdir}/cmake/LibKGAPI2/

%changelog
