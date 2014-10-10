%define upstream_name    HTML-Template-Extension
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Basic set operations
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::Template)
BuildArch:	noarch

%description
This module extends HTML::Template to easily support methods and tags not
implemented in parent module. The following plugins are supplied:
- HTML::Template::Extension::DOC
- HTML::Template::Extension::SLASH_VAR
- HTML::Template::Extension::CSTART
- HTML::Template::Extension::HEAD_BODY
- HTML::Template::Extension::DO_NOTHING

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes DISCLAIMER README TODO
%{perl_vendorlib}/HTML
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 403262
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.26-3mdv2009.0
+ Revision: 257209
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.26-1mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2007.0
+ Revision: 133722
- new version

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-2mdv2007.0
- spec cleanup
- fix directory ownership

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.24-1mdk
- initial Mandriva package

