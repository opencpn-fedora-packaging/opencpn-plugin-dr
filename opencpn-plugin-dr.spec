%global commit 90c7022f648dc142344add98979665fc0d413970
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner Rasbats
%global project DR_pi
%global plugin DR

Name: opencpn-plugin-dr
Summary: Route plotting plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
Plots great circle routes, limited circle routes, and rhumb lines in OpenCPN.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so
