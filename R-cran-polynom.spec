%define		fversion	%(echo %{version} |tr r -)
%define		modulename	polynom
Summary:	A collection of functions to implement a class for univariate polynomial manipulations
Summary(pl):	Kolekcja funkcji do implementacji klas do uniwersalnych manipulacji na wielomianach
Name:		R-cran-%{modulename}
Version:	1.1r15
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	bc17210955f5a49834531ba1bdc1b0e9
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of functions to implement a class for univariate
polynomial manipulations.

%description -l pl
Kolekcja funkcji do implementacji klas do uniwersalnych manipulacji na
wielomianach.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,ChangeLog,NOTES}
%{_libdir}/R/library/%{modulename}
