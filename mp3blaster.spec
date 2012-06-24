Summary:	ncurses-based based mp3 player
Summary(pl):	Odtwarzacz plik�w mp3 bazowany na ncurses
Name:		mp3blaster
Version:	3.1.1
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	ftp://mud.stack.nl/pub/mp3blaster/%{name}-%{version}.tar.gz
URL:		http://www.stack.nl/~brama/mp3blaster/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3blaster is an interactive text-based mp3player. One of the unique
features of this player is the ability to divide a playlist into
groups (albums). Therefore, the play order can be adjusted with great
flexibility.

%description -l pl
mp3blaster to interaktywy odtwarzacz plik�w mp3 pracuj�cy w trybie
tekstowym. Jedn� z wyj�tkowych cech tego odtwarzacza jest mo�liwo��
dzielenia list odtwarzanych plik�w na grupy (albumy). Dzi�ki temu
kolejno�� odtwarzania mo�e by� dobierana w bardzo elastyczny spos�b.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure \
	--with-oggvorbis 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO BUGS FAQ
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mp3blaster
%{_mandir}/man1/*
