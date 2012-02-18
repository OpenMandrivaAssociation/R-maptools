%global packname  maptools
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.8_14
Release:          1
Summary:          Tools for reading and handling spatial objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-14.tar.gz
Requires:         R-foreign R-sp R-methods R-lattice 
Requires:         R-spatstat R-PBSmapping R-maps R-rgeos R-gpclib R-RArcInfo 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-foreign R-sp R-methods R-lattice
BuildRequires:    R-spatstat R-PBSmapping R-maps R-rgeos R-gpclib R-RArcInfo 
BuildRequires:    geos-devel
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Set of tools for manipulating and reading geographic data, in particular
ESRI shapefiles; C code used from shapelib. It includes binary access to
GSHHS shoreline files. The package also provides interface wrappers for
exchanging spatial objects with packages such as PBSmapping, spatstat,
maps, RArcInfo, Stata tmap, WinBUGS, Mondrian, and others.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/changes
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/grids
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/old_man
%{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/share
