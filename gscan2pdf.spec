%define name	gscan2pdf
%define version	0.9.13
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Producies multipage PDFs from a scan
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gscan2pdf.sourceforge.net/
License:	GPL
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	ImageMagick
Requires:	perl-Gtk2 perl-Locale-gettext perl-PDF-API2
Requires:	libtiff-progs ImageMagick
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
perl Makefile.PL
perl -pi -e 's|usr/local|usr||g' Makefile
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm %buildroot/%_datadir/applications/%name.desktop

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GScan2PDF" longtitle="Scan and create PDFs" section="Office/Publishing" xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=GScan2PDF
Comment=Scan and create PDFs
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Graphics;Scanning;X-MandrivaLinux-Office-Publishing;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc History INSTALL
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
