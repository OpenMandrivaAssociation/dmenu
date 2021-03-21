%define sselp_ver 0.2

Summary:	A dynamic menu for X
Name:		dmenu
Version:	5.0
Release:	1
License:	MIT License
Group:		Graphical desktop/Other
URL:		http://tools.suckless.org/dmenu/
Source0:	http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:	http://dl.suckless.org/tools/sselp-%{sselp_ver}.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xft)
Requires:	terminus-font
Requires:	sselp
%rename		dwm-tools

%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages large
numbers of user-defined menu items efficiently.

%package -n sselp
Version:	0.2
Summary:	Prints X selection to standard out

%description -n sselp
Prints X selection to standard out.

%prep
%setup -q -a1
# Insert optflags + ldflags
sed -i -e 's|-Os|%{optflags}|' config.mk
sed -i -e 's|$(LIBS)|%{build__ldflags} $(LIBS)|' config.mk
# X includedir path fix
sed -i -e 's|X11INC = .*|X11INC = %{_includedir}|' config.mk
# libdir path fix
sed -i -e 's|X11LIB = .*|X11LIB = %{_libdir}|' config.mk

%build
%set_build_flags

%make_build CC="%{__cc} %{optflags} %{build_ldflags}" \
    X11INC=%{_includedir} \
    X11LIB=%{_libdir}

pushd sselp-%{sselp_ver}
%make_build CC="%{__cc} %{optflags} %{build_ldflags}"
popd

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANPREFIX=%{_mandir}

%make_install PREFIX=%{_prefix} -C sselp-%{sselp_ver}

%files
%{_bindir}/dmenu*
%{_bindir}/stest
%{_mandir}/man1/*

%files -n sselp
%{_bindir}/sselp
