Summary:	AMD Accelerated Parallel Processing BLAS Library
Summary(pl.UTF-8):	Akcelerowana, zrównoleglona wersja biblioteki BLAS firmy AMD
Name:		clAmdBlas
Version:	1.8.291
Release:	1
License:	AMD EULA
Group:		Libraries
# download using form at URL
Source0:	%{name}%{version}.tar.gz
# NoSource0-md5:	ad5d5cfbdd8253c9b2b57f3225bbb42d
NoSource:	0
URL:		http://developer.amd.com/tools/heterogeneous-computing/amd-accelerated-parallel-processing-math-libraries/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AMD Accelerated Parallel Processing Math Libraries are software
libraries containing FFT and BLAS functions written in OpenCL and
designed to run on AMD GPUs. The libraries support running on CPU
devices to facilitate debugging and multicore programming.

This package contains BLAS library with complete set of L2 & L3
routines for BLAS.

%description -l pl.UTF-8
AMD APPML (Accelerated Parallel Processing Math Libraries -
akcelerowane, zrównoleglone biblioteki matematyczne) to biblioteki
programowe zawierające funkcje FFT i BLAS napisane z użyciem OpenCL i
zaprojektowane do uruchamiania na procesorach graficznych (GPU) firmy
AMD. Biblioteki obsługują uruchamianie na CPU w celu ułatwienia
diagnostyki i programowania wielordzeniowego.

Ten pakiet zawiera bibliotekę BLAS z pełnym zbiorem procedur BLAS L2 i
L3.

%package devel
Summary:	Header files for OpenCL AMD BLAS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenCL AMD BLAS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenCL-devel

%description devel
Header files for OpenCL AMD BLAS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenCL AMD BLAS.

%prep
%setup -q -c

tar xf %{name}-%{version}-Linux.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}

%ifarch %{ix86}
cp -dp lib32/lib*.so* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{x8664}
cp -dp lib64/lib*.so* $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc clAmdBlas-{EULA,README}.txt
%attr(755,root,root) %{_libdir}/libclAmdBlas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclAmdBlas.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/clAmdBlas.refman.pdf
%attr(755,root,root) %{_libdir}/libclAmdBlas.so
%{_includedir}/clAmdBlas*.h
