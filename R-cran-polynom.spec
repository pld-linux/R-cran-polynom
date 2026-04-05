%define		fversion	%(echo %{version} |tr r -)
%define		modulename	polynom
%undefine	_debugsource_packages
Summary:	A collection of functions to implement a class for univariate polynomial manipulations
Summary(pl.UTF-8):	Kolekcja funkcji do implementacji klas do operacji na wielomianach jednowymiarowych
Name:		R-cran-%{modulename}
Version:	1.4r1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	5511178c91fd6eb33fdeefc64deb0546
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of functions to implement a class for univariate
polynomial manipulations.

%description -l pl.UTF-8
Kolekcja funkcji do implementacji klas do operacji na wielomianach
jednowymiarowych.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,ChangeLog}
%{_libdir}/R/library/%{modulename}
