Summary:	A unique multiplayer wargame
Summary(fr.UTF-8):	Un "wargame" multijoueur inédit
Summary(de.UTF-8):	Ein einzigartiges Kriegspiel für mehrere Spieler
Summary(pl.UTF-8):	Unikalna gra wojenna dla wielu graczy
Name:		liquidwar6
Version:	0.0.4
Release:	0.beta.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://www.ufoot.org/download/liquidwar/v6/%{version}beta/%{name}-%{version}beta.tar.gz
# Source0-md5:	8a6b4a6369d5f209a22c0911944bd542
Patch0:		%{name}-readline.patch
URL:		http://www.ufoot.org/liquidwar/v6
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf >= 2.50
#BuildRequires:	csound-devel (http://www.csounds.com/)
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gmp-devel
BuildRequires:	guile-devel >= 5:1.8
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liquid War is a unique multiplayer wargame. Its rules are truely
original and have been invented by Thomas Colcombet. You control an
army of liquid and have to try and eat your opponents. A single player
mode is available, but the game is definitely designed to be
multiplayer, and has network support.

%description -l da.UTF-8
Liquid war er et unikt multiplayer krigsspil. Reglerne er uhyre
originale og er opfundet af Thomas Colcombet. Du styrer en hær af
væske og skal prøve at æde dine modstandere. Liquid War kan spilles
alene, men er helt afgjort designet til multiplayer, og har
netværks-support.

%description -l de.UTF-8
Liquid War ist ein einzigartiges Kriegsspiel für mehrere Spieler. Die
Regeln sind wahrhaft neuartig und wurden von Thomas Colcombet
entwickelt. Man steuert eine flüssige Armee und muss versuchen die
Gegner aufzufressen. Es gibt einen Einzelspielermodus, aber das Spiel
ist eindeutig auf mehrere Spieler ausgelegt und unterstützt das
Spielen über Netzwerk.

%description -l fr.UTF-8
Liquid War est un "wargame" multijoueur inédit. Ses règles sont
vraiment originales et ont été inventées par Thomas Colcombet. L'idée
est de contrôler une armée de liquide et d'essayer de "manger" ses
adversaires. Il est possible de jouer seul, mais le jeux est conçu
pour se jouer à plusieurs, un mode réseau étant disponible.

%description -l pl.UTF-8
Liquid War jest unikalną grą dla wielu graczy. Jej zasady, wymyślone
przez Thomasa Colcombeta są naprawdę nowatorskie. Kontrolujesz armię
płynu i musisz spróbować stawić czoła i wchłonąć swoich przeciwników.
Można wprawdzie grać w pojedynkę, ale gra jest zaprojektowana dla
wielu graczy, też grających przez sieć.

%prep
%setup -q -n %{name}-%{version}beta
%patch0 -p1

%build
cp -f %{_datadir}/automake/config.sub .
%{__autoconf}
CPPFLAGS="-I/usr/include/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/liquidwar6
%attr(755,root,root) %{_libdir}/libliquidwar6-%{version}beta.so
# FIXME: %{_libdir}, not %{_prefix}/lib
%dir %{_prefix}/lib/liquidwar6-%{version}beta
%dir %{_prefix}/lib/liquidwar6-%{version}beta/*
%attr(755,root,root) %{_prefix}/lib/liquidwar6-%{version}beta/*/libmod_*.so
%{_datadir}/liquidwar6-%{version}beta
%{_mandir}/man6/liquidwar6.6*
%{_infodir}/liquidwar6.info*
