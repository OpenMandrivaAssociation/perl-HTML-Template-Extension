%define upstream_name    HTML-Template-Extension
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Basic set operations
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::Template)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes DISCLAIMER README TODO
%{perl_vendorlib}/HTML
%{_mandir}/*/*
