#
# spec file for package python-kde4
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


Name:           python-kde4-unstable
Version:        4.10.40_20130308
Release:        0
Summary:        Python bindings for KDE 4
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Url:            https://projects.kde.org/projects/kde/kdebindings/pykde4
Source0:        pykde4-git.tar.xz
Patch0:         buildfix.diff
BuildRequires:  fdupes
BuildRequires:  kdebase-workspace-unstable-devel
BuildRequires:  libjasper-devel
BuildRequires:  libkdepimlibs-unstable-devel
#BuildRequires:  okular-devel
BuildRequires:  python-qt4-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%kde_unstable_runtime_requires
%kde_unstable_akonadi_requires

%description
Python KDE bindings using PyQt4 SIP technology.

%package devel
Summary:        Development files of python-kde4
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       python-qt4-devel

%description devel
This package contains development files for the Python bindings for KDE4.

%prep
%setup -q -n pykde4-git
%patch0 -p1

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  %fdupes -s %{buildroot}%{_kde_unstable_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_kde_unstable_py_sitedir}/PyKDE4
%exclude %{_kde_unstable_appsdir}/pykde4/examples
%{_kde_unstable_appsdir}/pykde4
%{_kde_unstable_modulesdir}/kpythonpluginfactory.so
%{_kde_unstable_bindir}/pykdeuic4
%{_kde_unstable_bindir}/pykdeuic4-2.7
%{_kde_unstable_py_sitedir}/PyQt4/uic/widget-plugins
%{_kde_unstable_py_sitedir}/PyQt4/uic/pykdeuic4.*
%dir %{_kde_unstable_libdir}/python2.7
%dir %{_kde_unstable_libdir}/python2.7/site-packages
%dir %{_kde_unstable_libdir}/python2.7/site-packages/PyQt4
%dir %{_kde_unstable_libdir}/python2.7/site-packages/PyQt4/uic


%files devel
%defattr(-,root,root)
%dir %{_kde_unstable_datadir}/sip/
%{_kde_unstable_datadir}/sip/PyKDE4
%{_kde_unstable_appsdir}/pykde4/examples

%changelog
