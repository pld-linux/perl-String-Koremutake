#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	String
%define	pnam	Koremutake
Summary:	String::Koremutake - Convert to/from Koremutake Memorable Random Strings
Summary(pl.UTF-8):	String::Koremutake - konwersja z/do Koremutake Memorable Random Strings
Name:		perl-String-Koremutake
Version:	0.30
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b28d2017b98015f5e1b376324673419
URL:		http://search.cpan.org/dist/String-Koremutake/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Error >= 0.15
BuildRequires:	perl-Test-Exception >= 0.15
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Koremutake module converts to and from Koremutake
Memorable Random Strings.

The term "Memorable Random String" was thought up by Sean B. Palmer as
a name for those strings like dopynl, glargen, glonknic, spoopwiddle,
and kebble etc. that don't have any conventional sense, but can be
used as random identifiers, especially in URIs to keep them
persistent. See <http://infomesh.net/2001/07/MeRS/>.

%description -l pl.UTF-8
Moduł String::Koremutake przekształca do i z Koremutake Memorable
Random Strings (zapamiętywalnych losowych łańcuchów znaków).

Określenie "zapamiętywalny łańcuch losowy" (Memorable Random String)
zostało wymyślone przez Seana B. Palmera jako nazwa dla łańcuchów
znaków typu dopynl, glargen, glonknic, spoopwiddle, kebble itp., które
nie mają żadnego umownego sensu, ale mogą być używane jako losowe
identyfikatory, szczególnie w URI, aby utrzymać je stałymi. Patrz
<http://infomesh.net/2001/07/MeRS/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/String/*.pm
%{_mandir}/man3/*
