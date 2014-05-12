%define modname	IO-Tty
%define modver 1.11

Summary:	Pseudo TTY object class

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel


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


