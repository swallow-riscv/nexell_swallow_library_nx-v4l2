Name:    nx-v4l2
Version: 0.0.1
Release: 0
License: Apache 2.0
Summary: Nexell v4l2 library
Group: Development/Libraries
Source:  %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig automake autoconf libtool
BuildRequires:  pkgconfig(glib-2.0)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Nexell v4l2 library

%package devel
Summary: Nexell v4l2 library
Group: Development/Libraries
License: Apache 2.0
Requires: %{name} = %{version}-%{release}

%description devel
Nexell v4l2 library (devel)

%prep
%setup -q

%build
autoreconf -v --install || exit 1
%configure
make %{?_smp_mflags}

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -delete

mkdir -p %{buildroot}/usr/include
cp %{_builddir}/%{name}-%{version}/media-bus-format.h %{buildroot}/usr/include
cp %{_builddir}/%{name}-%{version}/nx-v4l2.h %{buildroot}/usr/include

%files
%{_libdir}/libnx_v4l2.so
%{_libdir}/libnx_v4l2.so.*

%files devel
%{_includedir}/media-bus-format.h
%{_includedir}/nx-v4l2.h
