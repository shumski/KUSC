#
# spec file for package oxygen-icon-theme
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


Name:           oxygen-icon-theme-unstable
Version:        4.8.95
Release:        0
Summary:        Oxygen Icon Theme
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source0:        oxygen-icons-%{version}.tar.xz
Source1:        22x22-package-manager-icon.png
Source2:        32x32-package-manager-icon.png
Source3:        48x48-package-manager-icon.png
Source4:        22x22_folder-html.png
Source5:        32x32_folder-html.png
Source6:        48x48_folder-html.png
Source7:        64x64_folder-html.png
Source8:        128x128_folder-html.png
Source9:        256x256_folder-html.png
Source10:       16x16_folder-html.png
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kde-unstable-filesystem
BuildRequires:  libqt4-devel
BuildRequires:  xz
Requires:       hicolor-icon-theme
Recommends:     oxygen-icon-theme-unstable-large
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the non-scalable icons of the Oxygen icon theme.

%prep
%setup -q -n oxygen-icons-%{version}

%build
  %cmake_kde_unstable -d build
  %make_jobs

%install
  cd build
  %kde_unstable_makeinstall
  install -D -m 0644 %{SOURCE1} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/22x22/apps/package-manager-icon.png
  install -D -m 0644 %{SOURCE2} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/32x32/apps/package-manager-icon.png
  install -D -m 0644 %{SOURCE3} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/48x48/apps/package-manager-icon.png
  install -D -m 0644 %{SOURCE4} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/22x22/places/folder-html.png
  install -D -m 0644 %{SOURCE5} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/32x32/places/folder-html.png
  install -D -m 0644 %{SOURCE6} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/48x48/places/folder-html.png
  install -D -m 0644 %{SOURCE7} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/64x64/places/folder-html.png
  install -D -m 0644 %{SOURCE8} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/128x128/places/folder-html.png
  install -D -m 0644 %{SOURCE9} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/256x256/places/folder-html.png
  install -D -m 0644 %{SOURCE10} %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/16x16/places/folder-html.png

for i in 16x16 22x22 32x32 48x48 64x64 128x128 256x256;
do
install -D -m 0644 %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/${i}/places/folder-html.png %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/${i}/places/folder_html.png
install -D -m 0644 %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/${i}/places/folder-documents.png %{buildroot}%{_kde_unstable_datadir}/icons/oxygen/${i}/apps/document.png;
done

cp -r ../scalable %{buildroot}%{_kde_unstable_datadir}/icons/oxygen

  %fdupes %{buildroot}

%clean
  rm -rf %{buildroot}

%package scalable
Summary:        Oxygen Icon Theme
Group:          System/GUI/KDE
Requires:       oxygen-icon-theme-unstable = %{version}

%description scalable
This package contains the scalable icons of the Oxygen icon theme.

%files scalable
%defattr(-,root,root)
%_kde_unstable_iconsdir/oxygen/scalable

%package large
Summary:        Oxygen Icon Theme
Group:          System/GUI/KDE
Requires:       oxygen-icon-theme-unstable = %{version}

%description large
This package contains the large (128x128 and larger) non-scalable icons of the Oxygen icon theme.

%files large
%defattr(-,root,root)
%_kde_unstable_iconsdir/oxygen/128x128
%_kde_unstable_iconsdir/oxygen/256x256

%files
%defattr(-,root,root)
%exclude %_kde_unstable_iconsdir/oxygen/scalable
%exclude %_kde_unstable_iconsdir/oxygen/128x128
%exclude %_kde_unstable_iconsdir/oxygen/256x256
%_kde_unstable_iconsdir/oxygen

%changelog
