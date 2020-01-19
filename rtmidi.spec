%define major		5
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		rtmidi
Version:	4.0.0
Release:	%mkrel 1
Summary:	C++ library for realtime MIDI input/ouput
License:	MIT
Group:		Sound/Utilities
URL:		https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:	https://www.music.mcgill.ca/~gary/rtmidi/release/%{name}-%{version}.tar.gz
Patch0:		rtmidi-4.0.0-pkgconfig.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
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

%build
%configure \
	--disable-static \
	--with-jack \
	--with-alsa

%make_build V=1

%install
%make_install

install -Dm 0755 %{name}-config %{buildroot}%{_bindir}/%{name}-config

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%license README.md
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
