%include	/usr/lib/rpm/macros.perl
Summary:	mysqlsla - MySQL slow log analyzer
Name:		mysqlsla
Version:	2.03
Release:	0.1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://hackmysql.com/scripts/%{name}-%{version}.tar.gz
# Source0-md5:	f620bee7dfcde6a1236be95cf62daa9b
URL:		http://hackmysql.com/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlsla parses, filters, analyzes and sorts MySQL slow, general,
binary and microslow patched logs in order to create a customizable
report of the queries and their meta-property values.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{perl_vendorlib}/%{name}.pm
%{_mandir}/man3/*
