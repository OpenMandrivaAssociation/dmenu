%define sselp_ver 0.2

Summary:	A dynamic menu for X
Name:		dmenu
Version:	5.2
Release:	1
License:	MIT License
Group:		Graphical desktop/Other
URL:		http://tools.suckless.org/dmenu/
Source0:	http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:	http://dl.suckless.org/tools/sselp-%{sselp_ver}.tar.gz
Patch0:		dmenu-optflags.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xft)
%rename		dwm-tools

%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages large
numbers of user-defined menu items efficiently.

%package -n sselp
Version:	5.2
Summary:	Prints X selection to standard out

%description -n sselp
Prints X selection to standard out.

%prep
%autosetup -p1 -a1

%build
%set_build_flags

%make_build CC="%{__cc} %{optflags} %{build_ldflags}" \
    X11INC="%{_includedir}" \
    X11LIB="%{_libdir}"

cd sselp-%{sselp_ver}
sed -i -e 's,-L/usr/lib,-L%{_libdir},g' -e 's,-L/usr/X11R6/lib,,g' config.mk
%make_build CC="%{__cc} %{optflags} %{build_ldflags}"
cd ..

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANPREFIX=%{_mandir}

%make_install PREFIX=%{_prefix} -C sselp-%{sselp_ver}

%files
%{_bindir}/dmenu*
%{_bindir}/stest
%{_mandir}/man1/*

%files -n sselp
%{_bindir}/sselp
