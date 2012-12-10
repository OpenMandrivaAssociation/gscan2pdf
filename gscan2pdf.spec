%define name	gscan2pdf
%define version	1.0.6
%define release %mkrel 1

Name:		%{name}
Summary:	Produces multipage PDFs from a scan
Version:	%{version}
Release:	%{release}

Source0:	http://downloads.sourceforge.net/project/gscan2pdf/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:		http://gscan2pdf.sourceforge.net/
License:	GPLv3
Group:		Publishing
BuildArch:	noarch
BuildRequires:	imagemagick perl-devel
BuildRequires:	imagemagick desktop-file-utils
Requires:	libtiff-progs imagemagick
Requires:	sane-frontends
Requires:	unpaper
Requires:	xdg-utils
Requires:	djvulibre
Requires:	gocr

%description
A GUI to ease the process of producing a multipage PDF from a scan.

Scanning is handled with SANE via scanimage. PDF conversion is done by
PDF::API2. TIFF export is handled by libtiff (faster and smaller memory
footprint for multipage files).

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
perl -pi -e 's|usr/local|usr||g' Makefile
make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	%{buildroot}%{_datadir}/applications/*.desktop

#icons
mkdir -p %{buildroot}/%{_liconsdir}
convert -resize 48x48 %{name}.svg %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
convert -resize 32x32 %{name}.svg %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
convert -resize 16x16 %{name}.svg %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc History LICENCE COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/pixmaps/*.svg


%changelog
* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.6-1mdv2012.0
+ Revision: 810626
- update to 1.0.6

* Thu Apr 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.4-1
+ Revision: 790356
- update to 1.0.4

* Thu Mar 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.2-1
+ Revision: 788134
- new version 1.0.2

* Tue Feb 07 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0.1-1
+ Revision: 771680
- new version 1.0.1
- spec cleanup
- don't manually specify perl modules requirements

* Tue Nov 01 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.0-1
+ Revision: 709266
- New version 1.0.0

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 0.9.32-4
+ Revision: 669783
- rebuild

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.9.32-3
+ Revision: 658493
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.9.32-2
+ Revision: 657380
- rebuild for updated spec-helper

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.9.32-1
+ Revision: 645231
- update to new version 0.9.32

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 0.9.31-1mdv2011.0
+ Revision: 555540
- update to new version 0.9.31

* Tue May 25 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.30-3mdv2010.1
+ Revision: 545837
- actually resize the icons

* Mon May 24 2010 Emmanuel Andry <eandry@mandriva.org> 0.9.30-2mdv2010.1
+ Revision: 545796
- add missing requires : perl-Set-IntSpan (#59268)
- fix summary

* Tue Feb 02 2010 Frederik Himpe <fhimpe@mandriva.org> 0.9.30-1mdv2010.1
+ Revision: 499763
- update to new version 0.9.30

* Mon May 18 2009 Funda Wang <fwang@mandriva.org> 0.9.29-2mdv2010.0
+ Revision: 376824
- fix requires

* Wed May 06 2009 Funda Wang <fwang@mandriva.org> 0.9.29-1mdv2010.0
+ Revision: 372357
- update to new version 0.9.29

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 0.9.28-2mdv2010.0
+ Revision: 372066
- add more requires (bug#50517)

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.9.28-1mdv2010.0
+ Revision: 370436
- update file list
- New version 0.9.28

* Sat Dec 13 2008 Funda Wang <fwang@mandriva.org> 0.9.27-1mdv2009.1
+ Revision: 313909
- fix file list
- new version 0.9.27

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.9.26-1mdv2009.0
+ Revision: 275708
- update to new version 0.9.26

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 0.9.25-1mdv2009.0
+ Revision: 231939
- update to new version 0.9.25

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 14 2008 Funda Wang <fwang@mandriva.org> 0.9.24-1mdv2009.0
+ Revision: 207237
- update to new version 0.9.24

* Fri Mar 07 2008 Funda Wang <fwang@mandriva.org> 0.9.23-1mdv2008.1
+ Revision: 181297
- update to new version 0.9.23

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 0.9.21-1mdv2008.1
+ Revision: 161382
- update to new version 0.9.21

* Mon Jan 21 2008 Funda Wang <fwang@mandriva.org> 0.9.20-1mdv2008.1
+ Revision: 155531
- New version 0.9.20

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 25 2007 Funda Wang <fwang@mandriva.org> 0.9.19-1mdv2008.1
+ Revision: 111886
- update to new version 0.9.19

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0.9.18-1mdv2008.1
+ Revision: 109798
- update to new version 0.9.18

* Wed Oct 10 2007 Funda Wang <fwang@mandriva.org> 0.9.17-1mdv2008.1
+ Revision: 96809
- New version 0.9.17

* Sat Aug 25 2007 Funda Wang <fwang@mandriva.org> 0.9.16-1mdv2008.0
+ Revision: 71137
- New version 0.9.16

* Wed Jul 25 2007 Austin Acton <austin@mandriva.org> 0.9.15-1mdv2008.0
+ Revision: 55136
- install perl module
- new version

* Mon Jul 09 2007 Austin Acton <austin@mandriva.org> 0.9.13-1mdv2008.0
+ Revision: 50764
- new version

* Sat Jun 09 2007 Austin Acton <austin@mandriva.org> 0.9.10-1mdv2008.0
+ Revision: 37703
- Import gscan2pdf

