Summary:	ncurses-based based mp3 player
Summary(pl):	Odtwarzacz plików mp3 bazowany na ncurses
Name:		mp3blaster
Version:	2.0b17
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	ftp://mud.stack.nl/pub/mp3blaster/%{name}-%{version}.tar.gz
Patch0:		mp3blaster-cwd.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3blaster is an interactive text-based mp3player. One of the unique
features of this player is the ability to divide a playlist into groups
(albums). Therefore, the play order can be adjusted with great flexibility.
						
%description -l pl
mp3blaster to interaktywy odtwarzacz plików mp3 pracuj±cy w trybie
tekstowym. Jedn± z wyj±tkowych cech tego odtwarzacza jest mo¿liwo¶æ
dzielenia list odtwarzanych plików na grupy (albumy). Dziêki temu kolejno¶æ
odtwarzania mo¿e byæ dobierana w bardzo elastyczny sposób

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS CREDITS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
