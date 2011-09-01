#
# Conditional build:
%bcond_with	lirc	# with LIRC support.
#
Summary:	ncurses-based based MP3 player
Summary(pl.UTF-8):	Odtwarzacz plików MP3 bazowany na ncurses
Name:		mp3blaster
Version:	3.2.5
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3blaster/%{name}-%{version}.tar.gz
# Source0-md5:	edb3bb122553d2d544dfb084010311c6
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-misc.patch
URL:		http://mp3blaster.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libvorbis-devel >= 1:1.0
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3blaster is an interactive text-based MP3 player. One of the unique
features of this player is the ability to divide a playlist into
groups (albums). Therefore, the play order can be adjusted with great
flexibility.

%description -l pl.UTF-8
mp3blaster to interaktywny odtwarzacz plików MP3 pracujący w trybie
tekstowym. Jedną z wyjątkowych cech tego odtwarzacza jest możliwość
dzielenia list odtwarzanych plików na grupy (albumy). Dzięki temu
kolejność odtwarzania może być dobierana w bardzo elastyczny sposób.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1  # check me!!!

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_lirc:--with-lirc} \
	--with-oggvorbis
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README README.lirc TODO BUGS FAQ
%doc AUTHORS CREDITS ChangeLog NEWS README TODO BUGS FAQ
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mp3blaster
%{_mandir}/man1/*
