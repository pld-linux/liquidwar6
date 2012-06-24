Summary:	A unique multiplayer wargame
Summary(fr):	Un "wargame" multijoueur in�dit
Summary(de):	Ein einzigartiges Kriegspiel f�r mehrere Spieler
Summary(pl):	Unikalna gra wojenna dla wielu graczy
Name:		liquidwar
Version:	5.6.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://liquidwar.sunsite.dk/archive/%{name}-%{version}.tar.gz
# Source0-md5:	981c5f00ddf2364c7b9d31fea82852be
Patch0:		%{name}-man_fix.patch
URL:		http://www.ufoot.org/liquidwar/
BuildRequires:	allegro-devel
BuildRequires:	allegro-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-modules
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liquid War is a unique multiplayer wargame. Its rules are truely
original and have been invented by Thomas Colcombet. You control an
army of liquid and have to try and eat your opponents. A single player
mode is available, but the game is definitely designed to be
multiplayer, and has network support.

%description -l de
Liquid War ist ein einzigartiges Kriegsspiel f�r mehrere Spieler. Die
Regeln sind wahrhaft neuartig und wurden von Thomas Colcombet
entwickelt. Man steuert eine fl�ssige Armee und muss versuchen die
Gegner aufzufressen. Es gibt einen Einzelspielermodus, aber das Spiel
ist eindeutig auf mehrere Spieler ausgelegt und unterst�tzt das
Spielen �ber Netzwerk.

%description -l dk
Liquid war er et unikt multiplayer krigsspil. Reglerne er uhyre
originale og er opfundet af Thomas Colcombet. Du styrer en h�r af
v�ske og skal pr�ve at �de dine modstandere. Liquid War kan spilles
alene, men er helt afgjort designet til multiplayer, og har
netv�rks-support.

%description -l fr
Liquid War est un "wargame" multijoueur in�dit. Ses r�gles sont
vraiment originales et ont �t� invent�es par Thomas Colcombet. L'id�e
est de contr�ler une arm�e de liquide et d'essayer de "manger" ses
adversaires. Il est possible de jouer seul, mais le jeux est con�u
pour se jouer � plusieurs, un mode r�seau �tant disponible.

%description -l pl
Liquid War jest unikaln� gr� dla wielu graczy. Jej zasady, wymy�lone
przez Thomasa Colcombeta s� naprawd� nowatorskie. Kontrolujesz armi�
p�ynu i musisz spr�bowa� stawi� czo�a i wch�on�� swoich przeciwnik�w.
Mo�na wprawdzie gra� w pojedynk�, ale gra jest zaprojektowana dla
wielu graczy, te� graj�cych przez sie�.

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
