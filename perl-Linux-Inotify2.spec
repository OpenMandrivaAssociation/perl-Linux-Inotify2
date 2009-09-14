
%define module	Linux-Inotify2
%define name	perl-%{module}
%define version	1.2
%define rel	2

Summary:	Scalable directory/file change notification
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{module}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	perl-devel

%description
This module implements an interface to the Linux 2.6.13 and later
Inotify file/directory change notification sytem.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING Changes
%{perl_vendorarch}/Linux
%{perl_vendorarch}/auto/Linux
%{_mandir}/man3/*
