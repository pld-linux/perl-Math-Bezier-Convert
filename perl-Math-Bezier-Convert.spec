#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Bezier-Convert
Summary:	Math::Bezier::Convert - convert cubic and quadratic bezier each other
Summary(pl):	Math::Bezier::Convert - konwersja krzywych Beziera stopnia 2 i 3 na inne
Name:		perl-Math-Bezier-Convert
Version:	0.01
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59416829a665fd948faf2782a73837f4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Bezier::Convert provides functions to convert quadratic bezier
to cubic, to approximate cubic bezier to quadratic, and to approximate
cubic and quadratic bezier to polyline.

%description -l pl
Modu³ Math::Bezier::Convert udostêpnia funkcje do przeliczania
kwadratowych krzywych Beziera na kubiczne, aproksymacji kubicznych
krzywych Beziera kwadratowymi oraz aproksymacji kubicznych i
kwadratowych krzywych Beziera wielomianami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install samples/bezier.plx $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Math/Bezier
%{perl_vendorlib}/Math/Bezier/Convert.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
