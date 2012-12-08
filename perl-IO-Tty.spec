%define upstream_name    IO-Tty
%define upstream_version 1.10

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        5

Summary:        Pseudo TTY object class
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel


%description
The IO::Tty and IO::Pty modules provide an interface to pseudo tty's.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

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


%changelog
* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-4mdv2012.0
+ Revision: 763893
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead
