%define major		7
%define oldlibname	%mklibname %{name} 6
%define libname		%mklibname %{name}
%define develname	%mklibname %{name} -d

Name:		rtmidi
Version:	6.0.0
Release:	1
Summary:	C++ library for realtime MIDI input/ouput
License:	MIT
Group:		Sound/Utilities
URL:		https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:	http://www.music.mcgill.ca/~gary/rtmidi/release/rtmidi-%{version}.tar.gz
Patch0:		rtmidi-4.0.0-pkgconfig.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)

%description
RtMidi is a set of C++ classes (RtMidiIn, RtMidiOut and API-specific
classes) that provides a common API (Application Programming Interface) for
realtime MIDI input/output across ALSA & JACK.

#------------------------------------------------

%package -n	%{libname}
Summary:	C++ library for realtime MIDI input/ouput
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
RtMidi is a set of C++ classes (RtMidiIn, RtMidiOut and API-specific
classes) that provides a common API (Application Programming Interface) for
realtime MIDI input/output across ALSA & JACK.

This package provides the shared library.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

#install -Dm 0755 %{name}-config %{buildroot}%{_bindir}/%{name}-config

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%license README.md
#{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/rtmidi
%{_datadir}/rtmidi/*.cmake
