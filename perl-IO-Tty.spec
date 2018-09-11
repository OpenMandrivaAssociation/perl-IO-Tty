%define modname	IO-Tty
%define modver 1.12

Summary:	Pseudo TTY object class

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl-devel

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The IO::Tty and IO::Pty modules provide an interface to pseudo tty's.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/IO
%{_mandir}/man3/*
