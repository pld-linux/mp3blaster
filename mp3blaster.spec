Summary:	ncurses-based based mp3 player
Summary(pl):	Odtwarzacz plik�w mp3 bazowany na ncurses
Name:		mp3blaster
Version:	2.0b12
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
License:	GPL
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel >= 5.0
Requires:	ncurses >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%description
mp3blaster is an interactive text-based mp3player. One of
the unique features of this player is the ability to divide
a playlist into groups (albums). Therefore, the play order
can be adjusted with great flexibility.
						
%description -l pl
mp3blaster to interaktywy odtwarzacz plik�w mp3 pracuj�cy w
trybie tekstowym. Jedn� z wyj�tkowych cech tego odtwarzacza jest
mo�liwo�� dzielenia list odtwarzanych plik�w na grupy (albumy).
Dzi�ki temu kolejno�� odtwarzania mo�e by� dobierana w
bardzo elastyczny spos�b

%prep
%setup -q

%build
%configure 
LDFLAGS="-l"; export LDFLAGS
make \
	OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS CREDITS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,CREDITS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
