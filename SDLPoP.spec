Name:           SDLPoP
Version:        1.20
Release:        5%{?dist}
Summary:        An open-source port of Prince of Persia

License:        GPLv3+
URL:            https://github.com/NagyD/SDLPoP
Source0:        https://github.com/NagyD/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        prince.sh
Source2:        prince.appdata.xml
# Fix duplicate symbol errors when building with "-fno-common"
# https://github.com/NagyD/SDLPoP/pull/203
Patch0:         %{name}-1.20-dupl-symbols.patch

BuildRequires:  gcc
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
SDLPoP is an open-source port of Prince of Persia, based on the disassembly 
of the DOS version.


%prep
%autosetup -p1


%build
%set_build_flags
%make_build -C src


%install
# Install wrapper
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/prince

# Install binary
install -d %{buildroot}%{_libexecdir}/%{name}
install -p -m 755 prince %{buildroot}%{_libexecdir}/%{name}

# Install data files
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data mods SDLPoP.ini %{buildroot}%{_datadir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
cp -p src/%{name}.desktop.template src/prince.desktop
desktop-file-install \
  --set-key=Exec \
  --set-value=prince \
  --set-icon=prince \
  --remove-category=Application \
  --remove-key=Path \
  --dir %{buildroot}%{_datadir}/applications \
  src/prince.desktop

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 data/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/prince.png

# Install AppData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/prince.appdata.xml


%files
%{_bindir}/prince
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/prince.desktop
%{_datadir}/icons/hicolor/*/apps/prince.png
%{_metainfodir}/prince.appdata.xml
%license doc/gpl-3.0.txt
%doc doc/Readme.txt doc/ChangeLog.txt doc/bugs.txt


%changelog
* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Andrea Musuruane <musuruan@gmail.com> - 1.20-3
- Added an upstream patch to properly fix duplicate symbol errors when
  building with -fno-common

* Sat May 16 2020 Andrea Musuruane <musuruan@gmail.com> - 1.20-2
- Fixed FTBFS for F32+

* Sun Nov 24 2019 Andrea Musuruane <musuruan@gmail.com> - 1.20-1
- Update to v1.20

* Thu Aug 17 2017 Andrea Musuruane <musuruan@gmail.com> - 1.17-1
- First release

