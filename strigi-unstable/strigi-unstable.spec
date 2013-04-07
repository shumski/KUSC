#
# spec file for package strigi
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


%bcond_with ffmpeg

Name:           strigi-unstable
Version:        0.7.7
Release:        0
Summary:        Lightweight and fast desktop search engine
License:        GPL-2.0+ and LGPL-2.1+
Group:          Productivity/Other
Url:            http://www.vandenoever.info/software/strigi/
Source0:        strigi-%{version}.tar.bz2
Source100:      baselibs.conf
Patch1:         add_missing_lib.diff
# PATCH-FIX-UPSTREAM git.diff
# This patch syncs strigi to git snapshot, 
# most of this changes fixed (re)indexing of specifix files. Remove for next release
# See reviews: 105442, 105362, 105242, 105208, 103977, 103961, 103911, 103368
Patch2:         git.diff
#Subject: Fixes indexing of jpegs with 'wrong' isoSpeedRatings, pending upstream
Patch3:         bug_304439.diff
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  c++_compiler
BuildRequires:  clucene-core-devel
BuildRequires:  cmake
BuildRequires:  dbus-1-x11
BuildRequires:  file-devel
%if 0%{?suse_version} > 1210
BuildRequires:  gamin-devel
%else
BuildRequires:  fam-devel
%endif
BuildRequires:  java-devel
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libcppunit-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libexpat-devel
%if %{with ffmpeg}
BuildRequires:  libffmpeg-devel
%endif
BuildRequires:  libbz2-devel
BuildRequires:  libqt4-devel
BuildRequires:  zlib-devel
%if !0%{?sles_version}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
%else
BuildRequires:  dbus-1-devel
BuildRequires:  libxml2-devel
%endif
Requires:       libstrigi0-unstable = %{version}
Provides:       strigi-ui = 0.5.8
Obsoletes:      strigi-ui < 0.5.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
strigi is a very fast crawling, very small memory footprint, no
hammering of the system with pluggable backend desktop search engine.

%package devel
Summary:        Development files for the strigi desktop search engine
Group:          Development/Libraries/C and C++
Requires:       libstrigi0-unstable = %{version}

%description devel
This package contains development files for the strigi desktop search engine.

%package -n libstrigi0-unstable
Summary:        Strigi desktop search engine libraries
Group:          System/Libraries
%requires_ge    libqt4

%description -n libstrigi0-unstable
This package contains the strigi desktop search engine libraries.

%prep
%setup -q -n strigi-%{version}
%if 0%{?suse_version} > 1210
%patch1 -p0
%endif
%patch2 -p1
%patch3 -p1

%build
%cmake_kde_unstable -d build
%make_jobs

%install
cd build
%kde_unstable_makeinstall
cd ..

%post   -n libstrigi0-unstable -p /sbin/ldconfig

%postun -n libstrigi0-unstable -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_kde_unstable_bindir}/deepfind
%{_kde_unstable_bindir}/deepgrep
%if 0%{?suse_version} > 1210
%{_kde_unstable_bindir}/lucene2indexer
%else
%{_kde_unstable_bindir}/luceneindexer
%endif
%{_kde_unstable_bindir}/rdfindexer
%{_kde_unstable_bindir}/strigiclient
%{_kde_unstable_bindir}/strigicmd
%{_kde_unstable_bindir}/strigidaemon
%{_kde_unstable_bindir}/xmlindexer
%dir %{_kde_unstable_libdir}/libsearchclient
%dir %{_kde_unstable_libdir}/libstreamanalyzer
%dir %{_kde_unstable_libdir}/libstreams
%dir %{_kde_unstable_libdir}/strigi
%{_kde_unstable_libdir}/strigi/strigiea_jpeg.so
%{_kde_unstable_libdir}/strigi/strigiea_riff.so
%{_kde_unstable_libdir}/strigi/strigiea_digest.so
%if 0%{?suse_version} > 1210
%{_kde_unstable_libdir}/strigi/strigiindex_cluceneng.so
%else
%{_kde_unstable_libdir}/strigi/strigiindex_clucene.so
%endif
%{_kde_unstable_libdir}/strigi/strigila_cpp.so
%{_kde_unstable_libdir}/strigi/strigila_deb.so
%{_kde_unstable_libdir}/strigi/strigila_namespaceharvester.so
%{_kde_unstable_libdir}/strigi/strigila_txt.so
%{_kde_unstable_libdir}/strigi/strigila_xpm.so
%{_kde_unstable_libdir}/strigi/strigita_au.so
%{_kde_unstable_libdir}/strigi/strigita_avi.so
%{_kde_unstable_libdir}/strigi/strigita_dds.so
%{_kde_unstable_libdir}/strigi/strigita_gif.so
%{_kde_unstable_libdir}/strigi/strigita_ico.so
%{_kde_unstable_libdir}/strigi/strigita_pcx.so
%{_kde_unstable_libdir}/strigi/strigita_rgb.so
%{_kde_unstable_libdir}/strigi/strigita_sid.so
%{_kde_unstable_libdir}/strigi/strigita_wav.so
%{_kde_unstable_libdir}/strigi/strigita_xbm.so
%if %{with ffmpeg}
%{_kde_unstable_libdir}/strigi/strigiea_ffmpeg.so
%endif
%dir %{_kde_unstable_datadir}/dbus-1/services
%{_kde_unstable_datadir}/dbus-1/services/org.freedesktop.xesam.searcher.service
%{_kde_unstable_datadir}/dbus-1/services/vandenoever.strigi.service
%{_kde_unstable_datadir}/strigi/

%files devel
%defattr(-,root,root,-)
%{_kde_unstable_includedir}/strigi/
%{_kde_unstable_libdir}/libsearchclient.so
%{_kde_unstable_libdir}/libstreamanalyzer.so
%{_kde_unstable_libdir}/libstreams.so
%{_kde_unstable_libdir}/libstrigihtmlgui.so
%{_kde_unstable_libdir}/libstrigiqtdbusclient.so
%{_kde_unstable_libdir}/libsearchclient/LibSearchClientConfig.cmake
%{_kde_unstable_libdir}/libstreamanalyzer/LibStreamAnalyzerConfig.cmake
%{_kde_unstable_libdir}/libstreams/LibStreamsConfig.cmake
%{_kde_unstable_libdir}/libstreams/LibStreamsTargets.cmake
%{_kde_unstable_libdir}/libstreams/LibStreamsTargets-release.cmake
%{_kde_unstable_libdir}/pkgconfig/libstreamanalyzer.pc
%{_kde_unstable_libdir}/pkgconfig/libstreams.pc
%{_kde_unstable_libdir}/strigi/StrigiConfig.cmake

%files -n libstrigi0-unstable
%defattr(-,root,root,-)
%{_kde_unstable_libdir}/libsearchclient.so.0*
%{_kde_unstable_libdir}/libstreamanalyzer.so.0*
%{_kde_unstable_libdir}/libstreams.so.0*
%{_kde_unstable_libdir}/libstrigihtmlgui.so.0*
%{_kde_unstable_libdir}/libstrigiqtdbusclient.so.0*

%changelog
