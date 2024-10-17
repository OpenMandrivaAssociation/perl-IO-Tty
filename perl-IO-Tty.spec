%define modname	IO-Tty
%define modver 1.12
%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	Pseudo TTY object class
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl-devel

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The IO::Tty and IO::Pty modules provide an interface to pseudo tty's.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build CFLAGS="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/IO
%{_mandir}/man3/*
