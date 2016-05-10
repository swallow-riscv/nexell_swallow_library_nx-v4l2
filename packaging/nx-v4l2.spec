Name:    nx-v4l2
Version: 0.0.1
Release: 0
License: Apache 2.0
Summary: Nexell v4l2 library
Group: Development/Libraries
Source:  %{name}-%{version}.tar.gz

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
make

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/include
cp %{_builddir}/%{name}-%{version}/media-bus-format.h %{buildroot}/usr/include
cp %{_builddir}/%{name}-%{version}/nx-v4l2.h %{buildroot}/usr/include

mkdir -p %{buildroot}/usr/lib
cp %{_builddir}/%{name}-%{version}/libnx-v4l2.so  %{buildroot}/usr/lib

%files
%attr (0644, root, root) %{_libdir}/*.so

%files devel
%attr (0644, root, root) %{_includedir}/*
