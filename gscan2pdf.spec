%define name	gscan2pdf
%define version	1.0.6
%define release 3

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
Requires:	unpaper >= 0.4.2
Requires:	xdg-utils
Requires:	djvulibre
Requires:	gocr
Requires:	perl(PDF::API2) >= 2.21.0

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


