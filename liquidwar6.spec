Summary:	A unique multiplayer wargame
Summary(fr.UTF-8):	Un "wargame" multijoueur inédit
Summary(de.UTF-8):	Ein einzigartiges Kriegspiel für mehrere Spieler
Summary(pl.UTF-8):	Unikalna gra wojenna dla wielu graczy
Name:		liquidwar
Version:	5.6.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.savannah.nongnu.org/releases/liquidwar/%{name}-%{version}.tar.gz
# Source0-md5:	a41473c281f214c1ac96ab50f98537c9
Patch0:		%{name}-man_fix.patch
URL:		http://www.ufoot.org/liquidwar/
BuildRequires:	allegro-devel
BuildRequires:	allegro-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-modules
BuildRequires:	tetex-dvips
BuildRequires:	texinfo
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
%setup -q
%patch0 -p1

%build
cp -f %{_datadir}/automake/config.sub .
%{__autoconf}
%configure \
%ifnarch %{ix86}
	--disable-target-opt \
	--disable-asm
%endif

%{__make}

cd doc/man
echo '.so liquidwar.6' > liquidwar-server.6
echo '.so liquidwar.6' > liquidwar-mapgen.6
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc doc/html/*.html doc/txt/*.txt
%attr(755,root,root) %{_prefix}/games/liquidwar*
%attr(755,root,root) %{_bindir}/liquidwar
%attr(755,root,root) %{_bindir}/liquidwar-server
%{_datadir}/games/liquidwar
%{_mandir}/man*/*
%{_infodir}/liquidwar.info*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
