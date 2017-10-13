#
# Conditional build:
#
%define		_state		stable
%define		orgname		kdelibs
%define		qtver		4.8.5
%define		sopranover	2.9.0
%define		phononver	4.6.0
%define		atticaver	0.4.2

Summary:	K Desktop Environment - libraries
Summary(es.UTF-8):	K Desktop Environment - bibliotecas
Summary(ko.UTF-8):	KDE - 라이브러리
Summary(pl.UTF-8):	K Desktop Environment - biblioteki
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE
Summary(ru.UTF-8):	K Desktop Environment - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment - Бібліотеки
Name:		kde4-kdelibs
Version:	4.14.37
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/applications/17.08.2/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c97d252d7a899ea551fd518c0a89dcfe
Source1:	%{name}-pld_box.png
Patch100:	%{name}-branch.diff
Patch0:		%{name}-branding.patch
Patch1:		%{name}-cacert.patch
Patch2:		%{name}-findlzmafix.patch
Patch3:		%{name}-aboutPLD.patch
Patch4:		%{name}-devicemanager_remove.patch
Patch5:		kde4-kdelibs-sync.patch
Patch6:		kde4-kdelibs-pld-flags.patch
Patch7:		strigi-64bit.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDeclarative-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	acl-devel
BuildRequires:	aspell-devel
BuildRequires:	attica-devel >= %{atticaver}
BuildRequires:	audiofile-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	avahi-devel
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	enchant-devel
BuildRequires:	fam-devel
BuildRequires:	flex
BuildRequires:	giflib-devel
BuildRequires:	grantlee-devel >= 0.1.1
BuildRequires:	heimdal-devel
BuildRequires:	herqq-devel >= 1.0.0-2
BuildRequires:	hspell-devel
BuildRequires:	issue
BuildRequires:	jasper-devel >= 1.600
BuildRequires:	libart_lgpl-devel
BuildRequires:	libdbusmenu-qt-devel >= 0.8.1
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libwmf-devel >= 2:0.2.0
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	lua50-devel
BuildRequires:	media-player-info
BuildRequires:	mdns-bonjour-devel
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	phonon-devel >= %{phononver}
BuildRequires:	pkgconfig
BuildRequires:	polkit-qt-1-gui-devel >= 0.99.0
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.10.0
BuildRequires:	shared-mime-info >= 0.60
BuildRequires:	soprano-devel >= %{sopranover}
BuildRequires:	strigi-devel >= 0.7.0
BuildRequires:	sysstat
BuildRequires:	udev-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildConflicts:	kdelibs
BuildConflicts:	kdelibs-devel
BuildConflicts:	kde4-kde3support
BuildConflicts:	kde4-kde3support-devel
Requires:	QtCore >= %{qtver}
Requires:	attica >= %{atticaver}
Requires:	ca-certificates
Requires:	hicolor-icon-theme
Requires:	kde-common-dirs >= 0.5
Requires:	libxml2-progs
Requires:	phonon >= %{phononver}
Requires:	setup >= 2.4.6-7
Requires:	soprano >= %{sopranover}
Requires:	xdg-menus
Requires:	xorg-app-iceauth
Suggests:	kde4-icons
Provides:	kde4-kdelibs-experimental
Provides:	kde4-kdelibs-shared
Obsoletes:	kde4-kdelibs-experimental
Obsoletes:	kde4-kdelibs-libs
Obsoletes:	kde4-kdelibs-shared
Obsoletes:	kdelibs4
Conflicts:	kdelibs4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# confuses OpenEXR detection
%undefine	configure_cache

%description
This package includes libraries that are central to the development
and execution of a KDE program, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,

%description -l es.UTF-8
Bibliotecas para KDE.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE, różną dokumentację oraz moduły z motywami wyglądu KDE.

Pakiet ten zawiera między innymi:
- kdecore - podstawową bibliotekę KDE,
- kdeui - interfejs użytkownika KDE,
- khtml - obsługę HTML, javascript oraz CSS dla KDE,

%description -l pt_BR.UTF-8
Bibliotecas de fundação do KDE requeridas por todo e qualquer
aplicativo KDE.

%description -l ru.UTF-8
Библиотеки для K Desktop Environment.

Включены библиотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (интерфейс пользователя),
- khtmlw (работа с HTML),
- kimgio (обработка изображений).
- kspell (проверка орфографии),

%description -l uk.UTF-8
Бібліотеки для K Desktop Environment.

Включені такі бібліотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (інтерфейс користувача),
- khtmlw (робота з HTML),
- kimgio (обробка зображень).
- kspell (перевірка орфографії),

%package devel
Summary:	kdelibs - header files and development documentation
Summary(pl.UTF-8):	kdelibs - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação para compilar aplicativos KDE
Summary(ru.UTF-8):	Хедеры и документация для компилляции программ KDE
Summary(uk.UTF-8):	Хедери та документація для компіляції програм KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt3Support-devel >= %{qtver}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtDeclarative-devel >= %{qtver}
Requires:	QtDesigner-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtOpenGL-devel >= %{qtver}
Requires:	QtScript-devel >= %{qtver}
Requires:	QtSvg-devel >= %{qtver}
Requires:	QtTest-devel >= %{qtver}
Requires:	QtUiTools-devel >= %{qtver}
Requires:	QtWebKit-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}
Requires:	acl-devel
Requires:	docbook-dtd42-xml
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	phonon-devel
Requires:	soprano-devel >= %{sopranover}
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	kde4-kdelibs-experimental-devel
Conflicts:	kdelibs-devel


%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdelibs.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
KDE.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для KDE.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p1
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%if "%{pld_release}" == "ti"
sed -i -e 's#PLDLINUX_VERSION#PLD/Titanium#g' kio/kio/kprotocolmanager.cpp
%else
sed -i -e 's#PLDLINUX_VERSION#PLD/3.0 (Th)#g' kio/kio/kprotocolmanager.cpp
%endif


%build
install -d build
cd build
%cmake \
	-DASPELL_EXECUTABLE="%{_bindir}/aspell" \
	-DCONFIG_INSTALL_DIR=%{_datadir}/config \
	-DDATA_INSTALL_DIR=%{_datadir}/apps \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DMIME_INSTALL_DIR=/nogo \
	-DTEMPLATES_INSTALL_DIR=%{_datadir}/templates \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
	-DKDE4_ENABLE_FINAL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT/etc/security \
	$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
	$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
	$RPM_BUILD_ROOT%{_datadir}/apps/khtml/kpartplugins \
	$RPM_BUILD_ROOT%{_datadir}/apps/desktoptheme \
	$RPM_BUILD_ROOT%{_datadir}/apps/desktoptheme/default \
	$RPM_BUILD_ROOT%{_datadir}/config/magic \
	$RPM_BUILD_ROOT%{_datadir}/config.kcfg \
	$RPM_BUILD_ROOT%{_datadir}/ontology/kde \
	$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
	$RPM_BUILD_ROOT%{_datadir}/apps/plasma/packages \
	$RPM_BUILD_ROOT%{_desktopdir}/kde4 \
	$RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus \

install %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/apps/kdeui/pics/pld_box.png

# DO NOT PACKAGE THIS FILE vvvv - use applnk
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications.menu

# USE ca-certificates
rm -f $RPM_BUILD_ROOT%{_datadir}/apps/kssl/ca-bundle.crt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_docdir}/kde
%dir %{_datadir}/ontology/kde
# DO NOT PACKAGE THIS FILE vvvv - use applnk
#%{_sysconfdir}/xdg/menus/applications.menu
%attr(755,root,root) %{_bindir}/kjs
%attr(755,root,root) %{_bindir}/kbuildsycoca4
%attr(755,root,root) %{_bindir}/kcookiejar4
%attr(755,root,root) %{_bindir}/kde4-config
%attr(755,root,root) %{_bindir}/kded4
%attr(755,root,root) %{_bindir}/kdeinit4
%attr(755,root,root) %{_bindir}/kdeinit4_shutdown
%attr(755,root,root) %{_bindir}/kdeinit4_wrapper
%attr(755,root,root) %{_bindir}/kfilemetadatareader
%attr(755,root,root) %{_bindir}/kjscmd
%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/kross
%attr(755,root,root) %{_bindir}/kshell4
%attr(755,root,root) %{_bindir}/ktelnetservice
%attr(755,root,root) %{_bindir}/kwrapper4
%attr(755,root,root) %{_bindir}/meinproc4
%attr(755,root,root) %{_bindir}/meinproc4_simple
%attr(755,root,root) %{_bindir}/nepomuk-rcgen
%attr(755,root,root) %{_bindir}/preparetips
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/kunittestmodrunner
%attr(755,root,root) %{_bindir}/makekdewidgets
%{_kdedocdir}/en/sonnet
%{_mandir}/man1/kde4-config.1*
#%{_mandir}/man1/kdecmake.1*
%{_mandir}/man1/kjs.1*
%{_mandir}/man1/kjscmd.1*
%{_mandir}/man1/kross.1*
%{_mandir}/man1/makekdewidgets.1*
%{_mandir}/man1/preparetips.1*
%{_mandir}/man7/kdeoptions.7*
%{_mandir}/man7/qtoptions.7*
%{_mandir}/man8/kbuildsycoca4.8*
%{_mandir}/man8/kded4.8*
%{_mandir}/man8/kdeinit4.8*
%{_mandir}/man8/kcookiejar4.8*
%{_mandir}/man8/meinproc4.8*

%attr(755,root,root) %{_datadir}/apps/kconf_update/*.pl
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/kconf_update/*.upd.sh
%{_datadir}/apps/kconf_update/move_kio_help_cache.sh
%{_datadir}/apps/LICENSES
%{_datadir}/apps/khtml/css/presentational.css
%{_datadir}/apps/khtml/domain_info
%{_datadir}/apps/khtml/error.html
%{_datadir}/apps/khtml/khtml.rc
%{_datadir}/apps/khtml/kpartplugins
%{_datadir}/apps/kjava/kjava.policy
%{_datadir}/apps/kjava/pluginsinfo
%{_datadir}/apps/proxyscout
%{_datadir}/apps/kcharselect
%{_datadir}/apps/knewstuff

%{_iconsdir}/hicolor/*x*/actions/*.png

%dir %{_datadir}/applnk
%dir %{_datadir}/applnk/.hidden
%dir %{_datadir}/apps/desktoptheme
%dir %{_datadir}/apps/desktoptheme/default
%dir %{_datadir}/services/kconfiguredialog
%{_datadir}/config/accept-languages.codes
%{_datadir}/config/colors
%{_datadir}/config/ksslcalist
%{_datadir}/config/magic
%{_datadir}/mime/packages/*
%{_datadir}/kde4/servicetypes
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/*.protocol
%dir %{_datadir}/kde4/services/kded
%{_datadir}/kde4/services/kded/*
%dir %{_datadir}/kde4/services/qimageioplugins
%{_datadir}/kde4/services/qimageioplugins/*
%dir %{_datadir}/kde4/services/ServiceMenus

%{_datadir}/dbus-1/interfaces/*.xml

# from kde4-kdebase.spec - old common subpackage
%dir %{_desktopdir}/kde4
%{_desktopdir}/kde4/*.desktop

# kauth
%{_datadir}/apps/kauth
/etc/dbus-1/system.d/org.kde.auth.conf

%dir %{_datadir}/apps/plasma
%dir %{_datadir}/apps/plasma/packages
%dir %{_datadir}/apps/plasma/services
%{_datadir}/apps/plasma/services/dataengineservice.operations
%{_datadir}/apps/plasma/services/plasmoidservice.operations
%{_datadir}/apps/plasma/services/storage.operations

%{_datadir}/apps/kcm_componentchooser
%{_datadir}/apps/kdeui
%{_datadir}/apps/kdewidgets
%dir %{_datadir}/apps/khtml
%dir %{_datadir}/apps/khtml/css
%{_datadir}/apps/khtml/css/html4.css
%{_datadir}/apps/khtml/css/quirks.css
%{_datadir}/apps/khtml/khtml_browser.rc
%dir %{_datadir}/apps/kjava
%{_datadir}/apps/kjava/kjava.jar
%{_datadir}/apps/ksgmltools2
%{_datadir}/apps/kssl
%dir %{_datadir}/config
%dir %{_datadir}/config/ui
%{_datadir}/config/ui/ui_standards.rc
%{_datadir}/config/kdebug.areas
%{_datadir}/config/kdebugrc
%{_datadir}/config/khtmlrc
%{_datadir}/config/plasmoids.knsrc
%{_datadir}/locale/all_languages
%{_datadir}/locale/en_US/entry.desktop
%{_mandir}/man1/checkXML.1*
%lang(en) %{_kdedocdir}/en/common
%lang(en) %{_kdedocdir}/en/kioslave

%attr(755,root,root) %ghost %{_libdir}/libkcmutils.so.?
%attr(755,root,root) %{_libdir}/libkcmutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkemoticons.so.?
%attr(755,root,root) %{_libdir}/libkemoticons.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkidletime.so.?
%attr(755,root,root) %{_libdir}/libkidletime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkprintutils.so.?
%attr(755,root,root) %{_libdir}/libkprintutils.so.*.*.*
%attr(755,root,root) %{_libdir}/libkde3support.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkde3support.so.?
%attr(755,root,root) %{_libdir}/libkdeclarative.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeclarative.so.?
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecore.so.?
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefakes.so.?
%attr(755,root,root) %{_libdir}/libkdesu.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdesu.so.?
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeui.so.?
%attr(755,root,root) %{_libdir}/libkdnssd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdnssd.so.?
%attr(755,root,root) %{_libdir}/libkfile.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkfile.so.?
%attr(755,root,root) %{_libdir}/libkhtml.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkhtml.so.?
%attr(755,root,root) %{_libdir}/libkimproxy.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkimproxy.so.?
%attr(755,root,root) %{_libdir}/libkio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkio.so.?
%attr(755,root,root) %{_libdir}/libkjs.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjs.so.?
%attr(755,root,root) %{_libdir}/libkjsapi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjsapi.so.?
%attr(755,root,root) %{_libdir}/libkjsembed.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjsembed.so.?
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmediaplayer.so.?
%attr(755,root,root) %{_libdir}/libknewstuff2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libknewstuff2.so.?
%attr(755,root,root) %{_libdir}/libknewstuff3.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libknewstuff3.so.?
%attr(755,root,root) %{_libdir}/libknotifyconfig.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libknotifyconfig.so.?
%attr(755,root,root) %{_libdir}/libkntlm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkntlm.so.?
%attr(755,root,root) %{_libdir}/libkparts.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkparts.so.?
%attr(755,root,root) %{_libdir}/libkpty.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkpty.so.?
%attr(755,root,root) %{_libdir}/libkrosscore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrosscore.so.?
%attr(755,root,root) %{_libdir}/libkrossui.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrossui.so.?
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libktexteditor.so.?
%attr(755,root,root) %{_libdir}/libkunitconversion.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkunitconversion.so.?
%attr(755,root,root) %{_libdir}/libkunittest.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkunittest.so.?
%attr(755,root,root) %{_libdir}/libkutils.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkutils.so.?
%attr(755,root,root) %{_libdir}/libnepomuk.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomuk.so.?
%attr(755,root,root) %{_libdir}/libnepomukutils.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukutils.so.?
%attr(755,root,root) %{_libdir}/libnepomukquery.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukquery.so.?
%attr(755,root,root) %{_libdir}/libplasma.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasma.so.?
%attr(755,root,root) %{_libdir}/libsolid.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libsolid.so.?
%attr(755,root,root) %{_libdir}/libthreadweaver.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libthreadweaver.so.?
%attr(755,root,root) %{_libdir}/libkdewebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdewebkit.so.?

%attr(755,root,root) %{_libdir}/libkdeinit4_kbuildsycoca4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kded4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit4_klauncher.so

%attr(755,root,root) %{_libdir}/kde4/*.so
%dir %{_libdir}/kde4/plugins/kauth
%dir %{_libdir}/kde4/plugins/kauth/backend
%attr(755,root,root) %{_libdir}/kde4/plugins/kauth/backend/kauth_backend_plugin.so
%dir %{_libdir}/kde4/plugins/kauth/helper
%attr(755,root,root) %{_libdir}/kde4/plugins/kauth/helper/kauth_helper_plugin.so
%dir %{_libdir}/kde4/plugins/designer
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdedeprecated.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdewebkitwidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdewidgets.so
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kde3supportwidgets.so
%dir %{_libdir}/kde4/plugins/imageformats
%attr(755,root,root) %{_libdir}/kde4/plugins/imageformats/kimg*.so
%dir %{_libdir}/kde4/plugins/script
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libkrossqtsplugin.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libkrossqtsplugin.so.?
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libkrossqtsplugin.so
%dir %{_libdir}/kconf_update_bin
%dir %{_libdir}/kde4/libexec
%attr(755,root,root) %{_libdir}/kde4/libexec/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kconfig_compiler
%attr(755,root,root) %{_libdir}/libkde3support.so
%attr(755,root,root) %{_libdir}/libkdeclarative.so
%attr(755,root,root) %{_libdir}/libkdecore.so
%attr(755,root,root) %{_libdir}/libkdefakes.so
%attr(755,root,root) %{_libdir}/libkdesu.so
%attr(755,root,root) %{_libdir}/libkdeui.so
%attr(755,root,root) %{_libdir}/libkdnssd.so
%attr(755,root,root) %{_libdir}/libkfile.so
%attr(755,root,root) %{_libdir}/libkhtml.so
%attr(755,root,root) %{_libdir}/libkimproxy.so
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkjsapi.so
%attr(755,root,root) %{_libdir}/libkjsembed.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libknewstuff2.so
%attr(755,root,root) %{_libdir}/libknewstuff3.so
%attr(755,root,root) %{_libdir}/libknotifyconfig.so
%attr(755,root,root) %{_libdir}/libkntlm.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libkpty.so
%attr(755,root,root) %{_libdir}/libkrosscore.so
%attr(755,root,root) %{_libdir}/libkrossui.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkunitconversion.so
%attr(755,root,root) %{_libdir}/libkunittest.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libnepomuk.so
%attr(755,root,root) %{_libdir}/libnepomukutils.so
%attr(755,root,root) %{_libdir}/libnepomukquery.so
%attr(755,root,root) %{_libdir}/libplasma.so
%attr(755,root,root) %{_libdir}/libsolid.so
%attr(755,root,root) %{_libdir}/libthreadweaver.so
%attr(755,root,root) %{_libdir}/libkdewebkit.so
%attr(755,root,root) %{_libdir}/libkcmutils.so
%attr(755,root,root) %{_libdir}/libkemoticons.so
%attr(755,root,root) %{_libdir}/libkidletime.so
%attr(755,root,root) %{_libdir}/libkprintutils.so

%{_datadir}/apps/cmake
%{_libdir}/cmake/KDeclarative
%{_includedir}/KDE/ConversionCheck
%{_includedir}/KDE/DNSSD
%{_includedir}/KDE/DOM
%{_includedir}/KDE/K3AboutApplication
%{_includedir}/KDE/K3AboutContainer
%{_includedir}/KDE/K3AboutContributor
%{_includedir}/KDE/K3AboutDialog
%{_includedir}/KDE/K3AboutWidget
%{_includedir}/KDE/K3ActiveLabel
%{_includedir}/KDE/K3BookmarkDrag
%{_includedir}/KDE/K3ButtonBox
%{_includedir}/KDE/K3ColorDrag
%{_includedir}/KDE/K3Command
%{_includedir}/KDE/K3CommandHistory
%{_includedir}/KDE/K3DictSpellingHighlighter
%{_includedir}/KDE/K3DockArea
%{_includedir}/KDE/K3DockMainWindow
%{_includedir}/KDE/K3DockManager
%{_includedir}/KDE/K3DockTabGroup
%{_includedir}/KDE/K3DockWidget
%{_includedir}/KDE/K3DockWidgetAbstractHeader
%{_includedir}/KDE/K3DockWidgetAbstractHeaderDrag
%{_includedir}/KDE/K3DockWidgetHeader
%{_includedir}/KDE/K3DockWidgetHeaderDrag
%{_includedir}/KDE/K3FileTreeView
%{_includedir}/KDE/K3FileTreeViewItem
%{_includedir}/KDE/K3Icon
%{_includedir}/KDE/K3IconView
%{_includedir}/KDE/K3IconViewItem
%{_includedir}/KDE/K3IconViewSearchLine
%{_includedir}/KDE/K3ListBox
%{_includedir}/KDE/K3ListView
%{_includedir}/KDE/K3ListViewItem
%{_includedir}/KDE/K3ListViewSearchLine
%{_includedir}/KDE/K3ListViewSearchLineWidget
%{_includedir}/KDE/K3MacroCommand
%{_includedir}/KDE/K3MimeSourceFactory
%{_includedir}/KDE/K3MultipleDrag
%{_includedir}/KDE/K3NamedCommand
%{_includedir}/KDE/K3PopupMenu
%{_includedir}/KDE/K3Process
%{_includedir}/KDE/K3ProcessController
%{_includedir}/KDE/K3ProcIO
%{_includedir}/KDE/K3RFCDate
%{_includedir}/KDE/K3ShellProcess
%{_includedir}/KDE/K3Spell
%{_includedir}/KDE/K3SpellConfig
%{_includedir}/KDE/K3SpellDlg
%{_includedir}/KDE/K3SpellingHighlighter
%{_includedir}/KDE/K3StaticDeleter
%{_includedir}/KDE/K3StaticDeleterBase
%{_includedir}/KDE/K3SyntaxHighlighter
%{_includedir}/KDE/K3TempFile
%{_includedir}/KDE/K3TextEdit
%{_includedir}/KDE/K3URLDrag
%{_includedir}/KDE/K3Wizard
%{_includedir}/KDE/KAboutApplicationDialog
%{_includedir}/KDE/KAboutData
%{_includedir}/KDE/KAboutPerson
%{_includedir}/KDE/KAcceleratorManager
%{_includedir}/KDE/KAccelGen
%{_includedir}/KDE/KACL
%{_includedir}/KDE/KAction
%{_includedir}/KDE/KActionCategory
%{_includedir}/KDE/KActionCollection
%{_includedir}/KDE/KActionMenu
%{_includedir}/KDE/KActionSelector
%{_includedir}/KDE/KAnimatedButton
%{_includedir}/KDE/KApplication
%{_includedir}/KDE/KAr
%{_includedir}/KDE/KArchive
%{_includedir}/KDE/KArchiveDirectory
%{_includedir}/KDE/KArchiveEntry
%{_includedir}/KDE/KArchiveFile
%{_includedir}/KDE/KArrowButton
%{_includedir}/KDE/KAscii
%{_includedir}/KDE/KAssistantDialog
%{_includedir}/KDE/KAuth
%{_includedir}/KDE/KAuthorized
%{_includedir}/KDE/KAutoMount
%{_includedir}/KDE/KAutoSaveFile
%{_includedir}/KDE/KAutostart
%{_includedir}/KDE/KAutoUnmount
%{_includedir}/KDE/KBookmark
%{_includedir}/KDE/KBookmarkAction
%{_includedir}/KDE/KBookmarkActionInterface
%{_includedir}/KDE/KBookmarkActionMenu
%{_includedir}/KDE/KBookmarkDialog
%{_includedir}/KDE/KBookmarkDomBuilder
%{_includedir}/KDE/KBookmarkExporterBase
%{_includedir}/KDE/KBookmarkGroup
%{_includedir}/KDE/KBookmarkGroupTraverser
%{_includedir}/KDE/KBookmarkImporterBase
%{_includedir}/KDE/KBookmarkManager
%{_includedir}/KDE/KBookmarkMenu
%{_includedir}/KDE/KBookmarkOwner
%{_includedir}/KDE/KBreadcrumbSelectionModel
%{_includedir}/KDE/KBugReport
%{_includedir}/KDE/KBuildSycocaProgressDialog
%{_includedir}/KDE/KButtonGroup
%{_includedir}/KDE/KCalendarSystem
%{_includedir}/KDE/KCalendarSystemFactory
%{_includedir}/KDE/KCapacityBar
%{_includedir}/KDE/KCategorizedSortFilterProxyModel
%{_includedir}/KDE/KCategorizedView
%{_includedir}/KDE/KCategoryDrawer
%{_includedir}/KDE/KCharMacroExpander
%{_includedir}/KDE/KCharSelect
%{_includedir}/KDE/KCharsets
%{_includedir}/KDE/KCheckableProxyModel
%{_includedir}/KDE/KCmdLineArgs
%{_includedir}/KDE/KCmdLineOptions
%{_includedir}/KDE/KCModule
%{_includedir}/KDE/KCModuleContainer
%{_includedir}/KDE/KCModuleInfo
%{_includedir}/KDE/KCModuleLoader
%{_includedir}/KDE/KCModuleProxy
%{_includedir}/KDE/KCMultiDialog
%{_includedir}/KDE/KCodecAction
%{_includedir}/KDE/KCodecs
%{_includedir}/KDE/KColor
%{_includedir}/KDE/KColorButton
%{_includedir}/KDE/KColorCells
%{_includedir}/KDE/KColorCollection
%{_includedir}/KDE/KColorCombo
%{_includedir}/KDE/KColorDialog
%{_includedir}/KDE/KColorMimeData
%{_includedir}/KDE/KColorPatch
%{_includedir}/KDE/KColorScheme
%{_includedir}/KDE/KColorTable
%{_includedir}/KDE/KColorUtils
%{_includedir}/KDE/KColorValueSelector
%{_includedir}/KDE/KComboBox
%{_includedir}/KDE/KCompletion
%{_includedir}/KDE/KCompletionBase
%{_includedir}/KDE/KCompletionBox
%{_includedir}/KDE/KCompletionMatches
%{_includedir}/KDE/KComponentData
%{_includedir}/KDE/KCompositeJob
%{_includedir}/KDE/KConfig
%{_includedir}/KDE/KConfigBase
%{_includedir}/KDE/KConfigDialog
%{_includedir}/KDE/KConfigDialogManager
%{_includedir}/KDE/KConfigGroup
%{_includedir}/KDE/KConfigSkeleton
%{_includedir}/KDE/KConfigSkeletonGenericItem
%{_includedir}/KDE/KConfigSkeletonItem
%{_includedir}/KDE/KCrash
%{_includedir}/KDE/KCrashBookmarkImporter
%{_includedir}/KDE/KCrashBookmarkImporterImpl
%{_includedir}/KDE/KCurrencyCode
%{_includedir}/KDE/KCursor
%{_includedir}/KDE/KDataTool
%{_includedir}/KDE/KDataToolAction
%{_includedir}/KDE/KDataToolInfo
%{_includedir}/KDE/KDateComboBox
%{_includedir}/KDE/KDatePicker
%{_includedir}/KDE/KDateTable
%{_includedir}/KDE/KDateTime
%{_includedir}/KDE/KDateTimeEdit
%{_includedir}/KDE/KDateTimeWidget
%{_includedir}/KDE/KDateValidator
%{_includedir}/KDE/KDateWidget
%{_includedir}/KDE/kdbgstream
%{_includedir}/KDE/KDBusServiceStarter
%{_includedir}/KDE/KDebug
%{_includedir}/KDE/KDEDModule
%{_includedir}/KDE/KDEPrintDialog
%{_includedir}/KDE/KDescendantsProxyModel
%{_includedir}/KDE/KDesktopFile
%{_includedir}/KDE/KDEsuClient
%{_includedir}/KDE/KDeviceListModel
%{_includedir}/KDE/KDialog
%{_includedir}/KDE/KDialogButtonBox
%{_includedir}/KDE/KDialogJobUiDelegate
%{_includedir}/KDE/KDirLister
%{_includedir}/KDE/KDirModel
%{_includedir}/KDE/KDirNotify
%{_includedir}/KDE/KDirOperator
%{_includedir}/KDE/KDirSelectDialog
%{_includedir}/KDE/KDirSortFilterProxyModel
%{_includedir}/KDE/KDirWatch
%{_includedir}/KDE/KDiskFreeSpace
%{_includedir}/KDE/KDiskFreeSpaceInfo
%{_includedir}/KDE/KDoubleNumInput
%{_includedir}/KDE/KDoubleValidator
%{_includedir}/KDE/KDualAction
%{_includedir}/KDE/KEditListBox
%{_includedir}/KDE/KEditListWidget
%{_includedir}/KDE/KEditToolBar
%{_includedir}/KDE/KEMailSettings
%{_includedir}/KDE/KEmoticons
%{_includedir}/KDE/KEmoticonsProvider
%{_includedir}/KDE/KEmoticonsTheme
%{_includedir}/KDE/KEncodingFileDialog
%{_includedir}/KDE/KEncodingProber
%{_includedir}/KDE/KExtendableItemDelegate
%{_includedir}/KDE/KFadeWidgetEffect
%{_includedir}/KDE/KFile
%{_includedir}/KDE/KFileDialog
%{_includedir}/KDE/KFileFilterCombo
%{_includedir}/KDE/KFileItem
%{_includedir}/KDE/KFileItemActions
%{_includedir}/KDE/KFileItemDelegate
%{_includedir}/KDE/KFileItemList
%{_includedir}/KDE/KFileItemListProperties
%{_includedir}/KDE/KFileMetaDataWidget
%{_includedir}/KDE/KFileMetaInfo
%{_includedir}/KDE/KFileMetaInfoGroup
%{_includedir}/KDE/KFileMetaInfoItem
%{_includedir}/KDE/KFilePlacesModel
%{_includedir}/KDE/KFilePlacesView
%{_includedir}/KDE/KFilePreviewGenerator
%{_includedir}/KDE/KFileShare
%{_includedir}/KDE/KFileSharePropsPlugin
%{_includedir}/KDE/KFileTreeBranch
%{_includedir}/KDE/KFileTreeView
%{_includedir}/KDE/KFileWidget
%{_includedir}/KDE/KFileWritePlugin
%{_includedir}/KDE/KFilterBase
%{_includedir}/KDE/KFilterDev
%{_includedir}/KDE/KFilterProxySearchLine
%{_includedir}/KDE/KFind
%{_includedir}/KDE/KFindDialog
%{_includedir}/KDE/KFloatValidator
%{_includedir}/KDE/KFontAction
%{_includedir}/KDE/KFontChooser
%{_includedir}/KDE/KFontComboBox
%{_includedir}/KDE/KFontDialog
%{_includedir}/KDE/KFontRequester
%{_includedir}/KDE/KFontSizeAction
%{_includedir}/KDE/KFontUtils
%{_includedir}/KDE/KGenericFactory
%{_includedir}/KDE/KGenericFactoryBase
%{_includedir}/KDE/KGlobal
%{_includedir}/KDE/KGlobalAccel
%{_includedir}/KDE/KGlobalSettings
%{_includedir}/KDE/KGlobalShortcutInfo
%{_includedir}/KDE/KGradientSelector
%{_includedir}/KDE/KGraphicsWebView
%{_includedir}/KDE/KGuiItem
%{_includedir}/KDE/KHBox
%{_includedir}/KDE/KHE
%{_includedir}/KDE/KHelpMenu
%{_includedir}/KDE/KHistoryComboBox
%{_includedir}/KDE/khtml
%{_includedir}/KDE/KHTMLPart
%{_includedir}/KDE/KHTMLSettings
%{_includedir}/KDE/KHTMLView
%{_includedir}/KDE/KHueSaturationSelector
%{_includedir}/KDE/KIcon
%{_includedir}/KDE/KIconButton
%{_includedir}/KDE/KIconCanvas
%{_includedir}/KDE/KIconDialog
%{_includedir}/KDE/KIconEffect
%{_includedir}/KDE/KIconLoader
%{_includedir}/KDE/KIconTheme
%{_includedir}/KDE/KIdentityProxyModel
%{_includedir}/KDE/KIdleTime
%{_includedir}/KDE/KIEBookmarkExporterImpl
%{_includedir}/KDE/KIEBookmarkImporter
%{_includedir}/KDE/KIEBookmarkImporterImpl
%{_includedir}/KDE/KImageCache
%{_includedir}/KDE/KImageFilePreview
%{_includedir}/KDE/KImageIO
%{_includedir}/KDE/KIMProxy
%{_includedir}/KDE/KInputDialog
%{_includedir}/KDE/KIntNumInput
%{_includedir}/KDE/KIntSpinBox
%{_includedir}/KDE/KIntValidator
%{_includedir}/KDE/KIO
%{_includedir}/KDE/KJob
%{_includedir}/KDE/KJobTrackerInterface
%{_includedir}/KDE/KJobUiDelegate
%{_includedir}/KDE/KKeySequenceWidget
%{_includedir}/KDE/KLanguageButton
%{_includedir}/KDE/KLed
%{_includedir}/KDE/KLibFactory
%{_includedir}/KDE/KLibLoader
%{_includedir}/KDE/KLibrary
%{_includedir}/KDE/KLineEdit
%{_includedir}/KDE/KLinkItemSelectionModel
%{_includedir}/KDE/KListWidget
%{_includedir}/KDE/KListWidgetSearchLine
%{_includedir}/KDE/KLocale
%{_includedir}/KDE/KLocalizedDate
%{_includedir}/KDE/KLocalizedString
%{_includedir}/KDE/KLockFile
%{_includedir}/KDE/KMacroExpanderBase
%{_includedir}/KDE/KMainWindow
%{_includedir}/KDE/KMakeTypeList
%{_includedir}/KDE/KMD5
%{_includedir}/KDE/KMediaPlayer
%{_includedir}/KDE/KMenu
%{_includedir}/KDE/KMenuBar
%{_includedir}/KDE/KMessage
%{_includedir}/KDE/KMessageBox
%{_includedir}/KDE/KMessageBoxMessageHandler
%{_includedir}/KDE/KMessageHandler
%{_includedir}/KDE/KMessageWidget
%{_includedir}/KDE/KMimeType
%{_includedir}/KDE/KMimeTypeChooser
%{_includedir}/KDE/KMimeTypeChooserDialog
%{_includedir}/KDE/KMimeTypeResolver
%{_includedir}/KDE/KMimeTypeTrader
%{_includedir}/KDE/KMimeTypeValidator
%{_includedir}/KDE/KModelIndexProxyMapper
%{_includedir}/KDE/KModifierKeyInfo
%{_includedir}/KDE/KMountPoint
%{_includedir}/KDE/KMozillaBookmarkImporterImpl
%{_includedir}/KDE/KMultiTabBar
%{_includedir}/KDE/KMultiTabBarButton
%{_includedir}/KDE/KMultiTabBarTab
%{_includedir}/KDE/KNameAndUrlInputDialog
%{_includedir}/KDE/kndbgstream
%{_includedir}/KDE/KNetwork
%{_includedir}/KDE/KNewFileMenu
%{_includedir}/KDE/KNewPasswordDialog
%{_includedir}/KDE/KNFSShare
%{_includedir}/KDE/KNotification
%{_includedir}/KDE/KNotificationRestrictions
%{_includedir}/KDE/KNotifyConfigWidget
%{_includedir}/KDE/KNS
%{_includedir}/KDE/KNS3
%{_includedir}/KDE/KNSBookmarkExporter
%{_includedir}/KDE/KNSBookmarkExporterImpl
%{_includedir}/KDE/KNSBookmarkImporter
%{_includedir}/KDE/KNSBookmarkImporterImpl
%{_includedir}/KDE/KNTLM
%{_includedir}/KDE/KNumInput
%{_includedir}/KDE/KOCRDialog
%{_includedir}/KDE/KonqBookmarkMenu
%{_includedir}/KDE/KonqBookmarkOwner
%{_includedir}/KDE/KOpenWithDialog
%{_includedir}/KDE/KOperaBookmarkExporterImpl
%{_includedir}/KDE/KOperaBookmarkImporter
%{_includedir}/KDE/KOperaBookmarkImporterImpl
%{_includedir}/KDE/KPageDialog
%{_includedir}/KDE/KPageModel
%{_includedir}/KDE/KPageView
%{_includedir}/KDE/KPageWidget
%{_includedir}/KDE/KPageWidgetItem
%{_includedir}/KDE/KPageWidgetModel
%{_includedir}/KDE/KParts
%{_includedir}/KDE/KPassivePopup
%{_includedir}/KDE/KPassivePopupMessageHandler
%{_includedir}/KDE/KPasswordDialog
%{_includedir}/KDE/KPasteTextAction
%{_includedir}/KDE/KPixmapCache
%{_includedir}/KDE/KPixmapProvider
%{_includedir}/KDE/KPixmapRegionSelectorDialog
%{_includedir}/KDE/KPixmapRegionSelectorWidget
%{_includedir}/KDE/KPixmapSequence
%{_includedir}/KDE/KPixmapSequenceOverlayPainter
%{_includedir}/KDE/KPixmapSequenceWidget
%{_includedir}/KDE/KPlotAxis
%{_includedir}/KDE/KPlotObject
%{_includedir}/KDE/KPlotPoint
%{_includedir}/KDE/KPlotWidget
%{_includedir}/KDE/KPluginFactory
%{_includedir}/KDE/KPluginInfo
%{_includedir}/KDE/KPluginLoader
%{_includedir}/KDE/KPluginSelector
%{_includedir}/KDE/KPopupFrame
%{_includedir}/KDE/KPreviewWidgetBase
%{_includedir}/KDE/KPrintPreview
%{_includedir}/KDE/KProcess
%{_includedir}/KDE/KProgressDialog
%{_includedir}/KDE/KPropertiesDialog
%{_includedir}/KDE/KProtocolInfo
%{_includedir}/KDE/KProtocolManager
%{_includedir}/KDE/KPty
%{_includedir}/KDE/KPtyDevice
%{_includedir}/KDE/KPtyProcess
%{_includedir}/KDE/KPushButton
%{_includedir}/KDE/KRandom
%{_includedir}/KDE/KRandomSequence
%{_includedir}/KDE/KRatingPainter
%{_includedir}/KDE/KRatingWidget
%{_includedir}/KDE/KRecentDocument
%{_includedir}/KDE/KRecentFilesAction
%{_includedir}/KDE/KRecursiveFilterProxyModel
%{_includedir}/KDE/KRegExpEditorInterface
%{_includedir}/KDE/KRemoteEncoding
%{_includedir}/KDE/KReplace
%{_includedir}/KDE/KReplaceDialog
%{_includedir}/KDE/KRestrictedLine
%{_includedir}/KDE/KRichTextEdit
%{_includedir}/KDE/KRichTextWidget
%{_includedir}/KDE/Kross
%{_includedir}/KDE/KRuler
%{_includedir}/KDE/KRun
%{_includedir}/KDE/KSambaShare
%{_includedir}/KDE/KSambaShareData
%{_includedir}/KDE/KSaveFile
%{_includedir}/KDE/KScanDialog
%{_includedir}/KDE/KSelectAction
%{_includedir}/KDE/KSelectionOwner
%{_includedir}/KDE/KSelectionProxyModel
%{_includedir}/KDE/KSelectionWatcher
%{_includedir}/KDE/KSelector
%{_includedir}/KDE/KSeparator
%{_includedir}/KDE/KService
%{_includedir}/KDE/KServiceAction
%{_includedir}/KDE/KServiceGroup
%{_includedir}/KDE/KServiceType
%{_includedir}/KDE/KServiceTypeProfile
%{_includedir}/KDE/KServiceTypeTrader
%{_includedir}/KDE/KSessionManager
%{_includedir}/KDE/KSettings
%{_includedir}/KDE/KSharedConfig
%{_includedir}/KDE/KSharedConfigPtr
%{_includedir}/KDE/KSharedDataCache
%{_includedir}/KDE/KSharedPtr
%{_includedir}/KDE/KShell
%{_includedir}/KDE/KShellCompletion
%{_includedir}/KDE/KShortcut
%{_includedir}/KDE/KShortcutsDialog
%{_includedir}/KDE/KShortcutsEditor
%{_includedir}/KDE/KShortcutWidget
%{_includedir}/KDE/KSocks
%{_includedir}/KDE/KSortableItem
%{_includedir}/KDE/KSortableList
%{_includedir}/KDE/KSpeech
%{_includedir}/KDE/KSplashScreen
%{_includedir}/KDE/KSqueezedTextLabel
%{_includedir}/KDE/KStandardAction
%{_includedir}/KDE/KStandardDirs
%{_includedir}/KDE/KStandardGuiItem
%{_includedir}/KDE/KStandardShortcut
%{_includedir}/KDE/KStartupInfo
%{_includedir}/KDE/KStartupInfoData
%{_includedir}/KDE/KStartupInfoId
%{_includedir}/KDE/KStatusBar
%{_includedir}/KDE/KStatusBarJobTracker
%{_includedir}/KDE/KStatusBarOfflineIndicator
%{_includedir}/KDE/KStatusNotifierItem
%{_includedir}/KDE/KStringHandler
%{_includedir}/KDE/KStringListValidator
%{_includedir}/KDE/KStyle
%{_includedir}/KDE/KStyleFactory
%{_includedir}/KDE/KSvgRenderer
%{_includedir}/KDE/KSycoca
%{_includedir}/KDE/KSycocaEntry
%{_includedir}/KDE/KSystemEventFilter
%{_includedir}/KDE/KSystemTimeZone
%{_includedir}/KDE/KSystemTimeZones
%{_includedir}/KDE/KSystemTimeZoneSource
%{_includedir}/KDE/KSystemTrayIcon
%{_includedir}/KDE/KTabBar
%{_includedir}/KDE/KTabWidget
%{_includedir}/KDE/KTar
%{_includedir}/KDE/KTempDir
%{_includedir}/KDE/KTemporaryFile
%{_includedir}/KDE/KTextBrowser
%{_includedir}/KDE/KTextEdit
%{_includedir}/KDE/KTextEditor
%{_includedir}/KDE/KTimeComboBox
%{_includedir}/KDE/KTimeZone
%{_includedir}/KDE/KTimeZoneData
%{_includedir}/KDE/KTimeZones
%{_includedir}/KDE/KTimeZoneSource
%{_includedir}/KDE/KTimeZoneWidget
%{_includedir}/KDE/KTipDatabase
%{_includedir}/KDE/KTipDialog
%{_includedir}/KDE/KTitleWidget
%{_includedir}/KDE/KToggleAction
%{_includedir}/KDE/KToggleFullScreenAction
%{_includedir}/KDE/KToggleToolBarAction
%{_includedir}/KDE/KToolBar
%{_includedir}/KDE/KToolBarLabelAction
%{_includedir}/KDE/KToolBarPopupAction
%{_includedir}/KDE/KToolBarSpacerAction
%{_includedir}/KDE/KToolInvocation
%{_includedir}/KDE/KTreeWidgetSearchLine
%{_includedir}/KDE/KTreeWidgetSearchLineWidget
%{_includedir}/KDE/KTypeList
%{_includedir}/KDE/KTypeListIndexOf
%{_includedir}/KDE/KTypeListLength
%{_includedir}/KDE/KTzfileTimeZone
%{_includedir}/KDE/KTzfileTimeZoneSource
%{_includedir}/KDE/KUndoStack
%{_includedir}/KDE/KUniqueApplication
%{_includedir}/KDE/KUnitConversion
%{_includedir}/KDE/KUnitTest
%{_includedir}/KDE/KUriFilter
%{_includedir}/KDE/KUriFilterData
%{_includedir}/KDE/KUriFilterPlugin
%{_includedir}/KDE/KUrl
%{_includedir}/KDE/KUrlComboBox
%{_includedir}/KDE/KUrlComboRequester
%{_includedir}/KDE/KUrlCompletion
%{_includedir}/KDE/KUrlLabel
%{_includedir}/KDE/KUrlNavigator
%{_includedir}/KDE/KUrlPixmapProvider
%{_includedir}/KDE/KUrlRequester
%{_includedir}/KDE/KUrlRequesterDialog
%{_includedir}/KDE/KUser
%{_includedir}/KDE/KUserGroup
%{_includedir}/KDE/KVBox
%{_includedir}/KDE/KViewStateMaintainer
%{_includedir}/KDE/KViewStateSaver
%{_includedir}/KDE/KWallet
%{_includedir}/KDE/KWebPage
%{_includedir}/KDE/KWebPluginFactory
%{_includedir}/KDE/KWebView
%{_includedir}/KDE/KWebWallet
%{_includedir}/KDE/KWidgetItemDelegate
%{_includedir}/KDE/KWidgetJobTracker
%{_includedir}/KDE/KWindowInfo
%{_includedir}/KDE/KWindowSystem
%{_includedir}/KDE/KWordMacroExpander
%{_includedir}/KDE/KWordWrap
%{_includedir}/KDE/KXBELBookmarkImporterImpl
%{_includedir}/KDE/KXErrorHandler
%{_includedir}/KDE/KXMessages
%{_includedir}/KDE/KXMLGUIBuilder
%{_includedir}/KDE/KXMLGUIClient
%{_includedir}/KDE/KXMLGUIFactory
%{_includedir}/KDE/KXmlGuiWindow
%{_includedir}/KDE/KXYSelector
%{_includedir}/KDE/KZip
%{_includedir}/KDE/KZipFileEntry
%{_includedir}/KDE/KZoneAllocator
%{_includedir}/KDE/Nepomuk
%{_includedir}/KDE/NET
%{_includedir}/KDE/NETRootInfo
%{_includedir}/KDE/NETWinInfo
%{_includedir}/KDE/OrgKdeKDirNotifyInterface
%{_includedir}/KDE/OrgKdeKLauncherInterface
%{_includedir}/KDE/Plasma
%{_includedir}/KDE/PtyProcess
%{_includedir}/KDE/Solid
%{_includedir}/KDE/Sonnet
%{_includedir}/KDE/SshProcess
%{_includedir}/KDE/StubProcess
%{_includedir}/KDE/SuProcess
%{_includedir}/KDE/ThreadWeaver
%{_includedir}/KDE/ThumbCreator
%dir %{_includedir}/plasma
%{_includedir}/plasma/*
%dir %{_includedir}/dnssd
%{_includedir}/dnssd/*
%dir %{_includedir}/dom
%{_includedir}/dom/*
%dir %{_includedir}/kdesu
%{_includedir}/kdesu/*
%dir %{_includedir}/khexedit
%{_includedir}/khexedit/*
%dir %{_includedir}/kio
%{_includedir}/kio/*
%dir %{_includedir}/kjs
%{_includedir}/kjs/*
%dir %{_includedir}/kmediaplayer
%{_includedir}/kmediaplayer/*
%{_includedir}/knewstuff2
%{_includedir}/knewstuff3
%dir %{_includedir}/kparts
%{_includedir}/kparts/*
%{_includedir}/kross
%dir %{_includedir}/ktexteditor
%{_includedir}/ktexteditor/*
%dir %{_includedir}/nepomuk
%{_includedir}/nepomuk/*
%dir %{_includedir}/solid
%{_includedir}/solid/*
%dir %{_includedir}/sonnet
%{_includedir}/sonnet/*
%dir %{_includedir}/threadweaver
%{_includedir}/threadweaver/*
%{_includedir}/*.tcc
%dir %{_includedir}/ksettings
%{_includedir}/ksettings/*
%dir %{_includedir}/kunitconversion
%{_includedir}/kunitconversion/*
%dir %{_includedir}/kunittest
%{_includedir}/kunittest/*
%{_includedir}/*.h

%{_mandir}/man1/kconfig_compiler.1*
