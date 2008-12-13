%define name	gscan2pdf
%define version	0.9.27
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Producies multipage PDFs from a scan
Version: 	%{version}
Release: 	%{release}

Source:		http://jaist.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.gz
URL:		http://gscan2pdf.sourceforge.net/
License:	GPLv3
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	imagemagick desktop-file-utils
Requires:	perl-Gtk2 perl-Locale-gettext perl-PDF-API2
Requires:	libtiff-progs imagemagick
Requires:	perl-Image-Magick
Requires:	sane-frontends
Requires:	perl-Gtk2-Ex-PodViewer
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-category='Application' \
	%buildroot%_datadir/applications/*.desktop

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.svg $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.svg $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.svg $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc History INSTALL
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
