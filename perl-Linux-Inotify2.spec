%define upstream_name	 Linux-Inotify2
%define upstream_version 2.3

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:	2

Summary:	Scalable directory/file change notification
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Linux-Inotify2
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Linux-Inotify2-2.3.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl(common::sense)

%description
This module implements an interface to the Linux 2.6.13 and later
Inotify file/directory change notification sytem.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%files
%defattr(-,root,root)
%doc README COPYING Changes
%{perl_vendorarch}/Linux
%{perl_vendorarch}/auto/Linux
%{_mandir}/man3/*


