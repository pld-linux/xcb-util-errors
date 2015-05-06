Summary:	XCB util-errors module
Summary(pl.UTF-8):	Moduł XCB util-errors
Name:		xcb-util-errors
Version:	1.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	4e389b65eb5a4b5c0d2958d628df87a8
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
Requires:	libxcb >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB errors utility library.

%description -l pl.UTF-8
Biblioteka narzędziowa błędów XCB.

%package devel
Summary:	Header files for XCB util-errors library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-errors
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4

%description devel
Header files for XCB util-errors library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-errors.

%package static
Summary:	Static XCB util-errors library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util-errors
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-errors library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util-errors.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxcb-errors.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libxcb-errors.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-errors.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-errors.so
%{_includedir}/xcb/xcb_errors.h
%{_pkgconfigdir}/xcb-errors.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-errors.a
