%define _legacy_common_support 1

Name:           SDLPoP
Version:        1.20
Release:        2%{?dist}
Summary:        An open-source port of Prince of Persia

License:        GPLv3+
URL:            https://github.com/NagyD/SDLPoP
Source0:        https://github.com/NagyD/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        prince.sh
Source2:        prince.appdata.xml

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
%autosetup 


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
* Sat May 16 2020 Andrea Musuruane <musuruan@gmail.com> - 1.20-2
- Fixed FTBFS for F32+

* Sun Nov 24 2019 Andrea Musuruane <musuruan@gmail.com> - 1.20-1
- Update to v1.20

* Thu Aug 17 2017 Andrea Musuruane <musuruan@gmail.com> - 1.17-1
- First release

