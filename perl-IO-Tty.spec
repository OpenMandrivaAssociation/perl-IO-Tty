%define module  IO-Tty
%define name    perl-%{module}
%define version 1.08
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release} 
Summary:        Pseudo TTY object class
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The IO::Tty and IO::Pty modules provide an interface to pseudo tty's.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/auto/IO
%{perl_vendorarch}/IO
%{_mandir}/*/*

