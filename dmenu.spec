%define sselp_ver 0.2

Name:           dmenu
Version:        4.6
Release:        1
Summary:        A dynamic menu for X
License:        MIT License
Group:          Graphical desktop/Other
URL:            http://tools.suckless.org/dmenu/

Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:	http://dl.suckless.org/tools/sselp-%{sselp_ver}.tar.gz

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xft)
Requires:       terminus-font
Requires:       sselp

Obsoletes:	dwm-tools
Provides:	dwm-tools

%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages large
numbers of user-defined menu items efficiently.

%package -n	sselp

Version:        0.2
Summary:        Prints X selection to standard out

%description -n sselp
Prints X selection to standard out.

%prep
%setup -q -a1
# No strip for debuginfo, and insert ldflags to enhance the security.
sed -i -e 's|-s ${LIBS}|%{?__global_ldflags} ${LIBS}|' config.mk

%build
%make CC="%{__cc} %{optflags} %{ldflags}" \
    X11INC=%{_includedir} \
    X11LIB=%{_libdir}

pushd sselp-%{sselp_ver}
%make CC="%{__cc} %{optflags} %{ldflags}"
popd

%install
%make install \
     DESTDIR=%{buildroot} \
     PREFIX=%{_prefix} \
     MANPREFIX=%{_mandir}

%makeinstall_std PREFIX=%{_prefix} -C sselp-%{sselp_ver}

%files
%{_bindir}/dmenu*
%{_bindir}/stest
%{_mandir}/man1/*

%files -n sselp
%{_bindir}/sselp
