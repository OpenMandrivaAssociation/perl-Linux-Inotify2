%define upstream_name	 Linux-Inotify2
%define upstream_version 1.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Scalable directory/file change notification
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
Requires:	perl(common::sense)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements an interface to the Linux 2.6.13 and later
Inotify file/directory change notification sytem.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.220.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.220.0-1
+ Revision: 685329
- update to new version 1.22

* Sun Aug 15 2010 Anssi Hannula <anssi@mandriva.org> 1.210.0-3mdv2011.0
+ Revision: 570211
- add missing requires on perl(common::sense)

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-2mdv2011.0
+ Revision: 555998
- rebuild for perl 5.12

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.0
+ Revision: 448258
- update to 1.21

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2-2mdv2010.0
+ Revision: 440606
- rebuild

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2009.1
+ Revision: 292196
- update to new version 1.2

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 1.1-1mdv2008.1
+ Revision: 176899
- initial Mandriva release

