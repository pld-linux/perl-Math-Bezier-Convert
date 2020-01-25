#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Bezier-Convert
Summary:	Math::Bezier::Convert - convert cubic and quadratic bezier each other
Summary(pl.UTF-8):	Math::Bezier::Convert - konwersja krzywych Beziera stopnia 2 i 3 na inne
Name:		perl-Math-Bezier-Convert
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fb5237be267b594ae9849fcdd389ed11
URL:		http://search.cpan.org/dist/Math-Bezier-Convert/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Bezier::Convert provides functions to convert quadratic bezier
to cubic, to approximate cubic bezier to quadratic, and to approximate
cubic and quadratic bezier to polyline.

%description -l pl.UTF-8
Moduł Math::Bezier::Convert udostępnia funkcje do przeliczania
kwadratowych krzywych Beziera na kubiczne, aproksymacji kubicznych
krzywych Beziera kwadratowymi oraz aproksymacji kubicznych i
kwadratowych krzywych Beziera wielomianami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p samples/bezier.plx $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Bezier
%{perl_vendorlib}/Math/Bezier/Convert.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
