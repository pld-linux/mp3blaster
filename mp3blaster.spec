#
# Conditional build:
%bcond_with	lirc	# with LIRC support.
#
Summary:	ncurses-based based MP3 player
Summary(pl):	Odtwarzacz plików MP3 bazowany na ncurses
Name:		mp3blaster
Version:	3.2.3
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3blaster/%{name}-%{version}.tar.gz
# Source0-md5:	0d892d7c99df175eb0efb2bc31086285
Patch0:		%{name}-misc.patch
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

%description -l pl
mp3blaster to interaktywny odtwarzacz plików MP3 pracuj±cy w trybie
tekstowym. Jedn± z wyj±tkowych cech tego odtwarzacza jest mo¿liwo¶æ
dzielenia list odtwarzanych plików na grupy (albumy). Dziêki temu
kolejno¶æ odtwarzania mo¿e byæ dobierana w bardzo elastyczny sposób.

%prep
%setup -q
#%patch0 -p1  # check me!!!

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
