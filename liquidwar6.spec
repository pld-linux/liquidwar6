%define	_beta	beta
Summary:	A unique multiplayer wargame
Summary(fr.UTF-8):	Un "wargame" multijoueur inédit
Summary(de.UTF-8):	Ein einzigartiges Kriegspiel für mehrere Spieler
Summary(pl.UTF-8):	Unikalna gra wojenna dla wielu graczy
Name:		liquidwar6
Version:	0.0.3
Release:	0.%{_beta}.1
Epoch:		1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://download.savannah.gnu.org/releases/liquidwar6/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	92c4fe0e0bc781ca1bdd0ec22a4c64e3
URL:		http://www.ufoot.org/liquidwar/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	guile-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
Obsoletes:	liquidwar
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
%setup -q -n %{name}-%{version}%{_beta}
%{__sed} -i -e 's#ncurses.h#ncurses/ncurses.h#' configure.ac

find . -name Makefile.am | xargs %{__sed} -i -e 's#@PACKAGE_TARNAME@-@PACKAGE_VERSION@#@PACKAGE_TARNAME@#'

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README  doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/liquidwar6.6*
%{_infodir}/liquidwar6.info*
