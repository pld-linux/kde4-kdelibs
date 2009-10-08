#
# Conditional build:
%bcond_without	kerberos5	# disable kerberos
#
%define		_state		stable
%define		orgname		kdelibs
%define		qtver		4.5.3

Summary:	K Desktop Environment - libraries
Summary(es.UTF-8):	K Desktop Environment - bibliotecas
Summary(ko.UTF-8):	KDE - 라이브러리
Summary(pl.UTF-8):	K Desktop Environment - biblioteki
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE
Summary(ru.UTF-8):	K Desktop Environment - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment - Бібліотеки
Name:		kde4-kdelibs
Version:	4.3.2
Release:	4
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	0564ed8ba804a0f3f1cee9732a3d2d72
Patch100: 	%{name}-branch.diff
Patch0:		%{orgname}4-findqt4.patch
Patch1:		%{name}-findboost.patch
Patch2:		%{name}-branding.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
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
BuildRequires:	audiofile-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	avahi-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.6.3
BuildRequires:	cups-devel
BuildRequires:	enchant-devel
BuildRequires:	fam-devel
BuildRequires:	giflib-devel
BuildRequires:	hspell-devel
BuildRequires:	jasper-devel >= 1.600
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libart_lgpl-devel
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
BuildRequires:	mdns-bonjour-devel
BuildRequires:	openmotif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	shared-mime-info >= 0.18
BuildRequires:	soprano-devel >= 2.3.0
BuildRequires:	strigi-devel >= 0.6.5
BuildRequires:	sysstat
BuildRequires:	utempter-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildConflicts:	kdelibs
BuildConflicts:	kdelibs-devel
Requires:	QtCore >= %{qtver}
Requires:	hicolor-icon-theme
Requires:	kde-common-dirs >= 0.5
Requires:	setup >= 2.4.6-7
Requires:	xdg-menus
Requires:	xorg-app-iceauth
Suggests:	kde4-icons
Provides:	%{name}-shared
Obsoletes:	%{name}-libs
Obsoletes:	%{name}-shared
Obsoletes:	kdelibs4
Conflicts:	kdelibs
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
Requires:	QtOpenGL-devel >= %{qtver}
Requires:	%{name} = %{version}-%{release}
Requires:	acl-devel
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	phonon-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel
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
%patch100 -p0
#%patch0 -p0
#%patch1 -p0
%patch2 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCONFIG_INSTALL_DIR=%{_datadir}/config \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DDATA_INSTALL_DIR=%{_datadir}/apps \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DMIME_INSTALL_DIR=/nogo \
	-DTEMPLATES_INSTALL_DIR=%{_datadir}/templates \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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
	$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \
	$RPM_BUILD_ROOT%{_desktopdir}/kde4 \
	$RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus \

# DO NOT PACKAGE THIS FILE vvvv - use applnk
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications.menu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_docdir}/kde
# from kde4-kdebase.spec - old common subpackage
%dir %{_desktopdir}/kde4
%attr(755,root,root) %{_bindir}/kjs
%attr(755,root,root) %{_bindir}/kbuildsycoca4
%attr(755,root,root) %{_bindir}/kcookiejar4
%attr(755,root,root) %{_bindir}/kde4-config
%attr(755,root,root) %{_bindir}/kded4
%attr(755,root,root) %{_bindir}/kdeinit4
%attr(755,root,root) %{_bindir}/kdeinit4_shutdown
%attr(755,root,root) %{_bindir}/kdeinit4_wrapper
%attr(755,root,root) %{_bindir}/kjscmd
%attr(755,root,root) %{_bindir}/kross
%attr(755,root,root) %{_bindir}/kshell4
%attr(755,root,root) %{_bindir}/kwrapper4
%attr(755,root,root) %{_bindir}/meinproc4
%attr(755,root,root) %{_bindir}/preparetips
%attr(755,root,root) %{_bindir}/checkXML
%attr(755,root,root) %{_bindir}/kunittestmodrunner
%attr(755,root,root) %{_bindir}/makekdewidgets
%attr(755,root,root) %{_bindir}/nepomuk-rcgen
%{_kdedocdir}/en/sonnet
%{_mandir}/man1/kde4-config.1*
%{_mandir}/man1/kdecmake.1*
%{_mandir}/man1/kjs.1*
%{_mandir}/man1/kjscmd.1*
%{_mandir}/man1/kross.1*
%{_mandir}/man1/makekdewidgets.1*
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
#%{_datadir}/apps/kcertpart
%{_datadir}/apps/khtml/css/presentational.css
%{_datadir}/apps/khtml/domain_info
%{_datadir}/apps/khtml/error.html
%{_datadir}/apps/khtml/khtml.rc
%{_datadir}/apps/khtml/kpartplugins
%{_datadir}/apps/kjava/kjava.policy
%{_datadir}/apps/kjava/pluginsinfo
# %{_datadir}/apps/ktexteditor_docwordcompletion
%{_datadir}/apps/ktexteditor_insertfile
%{_datadir}/apps/ktexteditor_kdatatool
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
%{_datadir}/config/katemoderc
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

%{_datadir}/apps/katepart
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
%{_datadir}/apps/nepomuk
%dir %{_datadir}/config
%dir %{_datadir}/config/ui
%{_datadir}/config/ui/ui_standards.rc
%{_datadir}/config/kdebug.areas
%{_datadir}/config/kdebugrc
%{_datadir}/config/plasmoids.knsrc
%{_datadir}/locale/all_languages
%{_mandir}/man1/checkXML.1*
%lang(en) %{_kdedocdir}/en/common
%lang(en) %{_kdedocdir}/en/kioslave

%attr(755,root,root) %{_libdir}/libkde3support.so.*
%attr(755,root,root) %{_libdir}/libkdecore.so.*
%attr(755,root,root) %{_libdir}/libkdefakes.so.*
%attr(755,root,root) %{_libdir}/libkdesu.so.*
%attr(755,root,root) %{_libdir}/libplasma.so.*
%attr(755,root,root) %{_libdir}/libkpty.so.*
%attr(755,root,root) %{_libdir}/libkdeui.so.*
%attr(755,root,root) %{_libdir}/libkdnssd.so.*
%attr(755,root,root) %{_libdir}/libkhtml.so.*
%attr(755,root,root) %{_libdir}/libkimproxy.so.*
%attr(755,root,root) %{_libdir}/libkio.so.*
%attr(755,root,root) %{_libdir}/libkjs.so.*
%attr(755,root,root) %{_libdir}/libkjsapi.so.*
%attr(755,root,root) %{_libdir}/libkjsembed.so.*
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*
%attr(755,root,root) %{_libdir}/libknewstuff2.so.*
%attr(755,root,root) %{_libdir}/libknotifyconfig.so.*
%attr(755,root,root) %{_libdir}/libkntlm.so.*
%attr(755,root,root) %{_libdir}/libkparts.so.*
%attr(755,root,root) %{_libdir}/libktexteditor.so.*
%attr(755,root,root) %{_libdir}/libkunittest.so.*
%attr(755,root,root) %{_libdir}/libkutils.so.*
%attr(755,root,root) %{_libdir}/libsolid.so.*
%attr(755,root,root) %{_libdir}/libthreadweaver.so.*
%attr(755,root,root) %{_libdir}/libkfile.so.*
%attr(755,root,root) %{_libdir}/libkrosscore.so.*
%attr(755,root,root) %{_libdir}/libkrossui.so.*
%attr(755,root,root) %{_libdir}/libkdeinit4_kbuildsycoca4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kded4.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit4_klauncher.so
%attr(755,root,root) %{_libdir}/libnepomuk.so.*

%attr(755,root,root) %{_libdir}/kde4/*.so
%dir %{_libdir}/kde4/plugins/designer
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
%attr(755,root,root) %{_libdir}/libkdecore.so
%attr(755,root,root) %{_libdir}/libkdefakes.so
%attr(755,root,root) %{_libdir}/libkpty.so
%attr(755,root,root) %{_libdir}/libkdesu.so
%attr(755,root,root) %{_libdir}/libkdeui.so
%attr(755,root,root) %{_libdir}/libkdnssd.so
%attr(755,root,root) %{_libdir}/libkhtml.so
%attr(755,root,root) %{_libdir}/libkimproxy.so
%attr(755,root,root) %{_libdir}/libkio.so
%attr(755,root,root) %{_libdir}/libkjs.so
%attr(755,root,root) %{_libdir}/libkjsapi.so
%attr(755,root,root) %{_libdir}/libkjsembed.so
%attr(755,root,root) %{_libdir}/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/libknotifyconfig.so
%attr(755,root,root) %{_libdir}/libkntlm.so
%attr(755,root,root) %{_libdir}/libkparts.so
%attr(755,root,root) %{_libdir}/libktexteditor.so
%attr(755,root,root) %{_libdir}/libkunittest.so
%attr(755,root,root) %{_libdir}/libkutils.so
%attr(755,root,root) %{_libdir}/libsolid.so
%attr(755,root,root) %{_libdir}/libthreadweaver.so
%attr(755,root,root) %{_libdir}/libkfile.so
%attr(755,root,root) %{_libdir}/libnepomuk.so
%attr(755,root,root) %{_libdir}/libknewstuff2.so
%attr(755,root,root) %{_libdir}/libkrosscore.so
%attr(755,root,root) %{_libdir}/libkrossui.so
%attr(755,root,root) %{_libdir}/libplasma.so
%{_datadir}/apps/cmake
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
%{_includedir}/KDE/KFileItemActions
%{_includedir}/KDE/KFileItemListProperties
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
%{_includedir}/KDE/K3ProcIO
%{_includedir}/KDE/K3Process
%{_includedir}/KDE/K3ProcessController
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
%{_includedir}/KDE/KACL
%{_includedir}/KDE/KAboutApplicationDialog
%{_includedir}/KDE/KAboutData
%{_includedir}/KDE/KAboutPerson
%{_includedir}/KDE/KAccelGen
%{_includedir}/KDE/KAcceleratorManager
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
%{_includedir}/KDE/KAssistantDialog
%{_includedir}/KDE/KAuthorized
%{_includedir}/KDE/KAutoMount
%{_includedir}/KDE/KAutoUnmount
%{_includedir}/KDE/KAutostart
%{_includedir}/KDE/KBookmark
%{_includedir}/KDE/KBookmarkAction
%{_includedir}/KDE/KBookmarkActionInterface
%{_includedir}/KDE/KBookmarkActionMenu
%{_includedir}/KDE/KBookmarkDomBuilder
%{_includedir}/KDE/KBookmarkExporterBase
%{_includedir}/KDE/KBookmarkGroup
%{_includedir}/KDE/KBookmarkGroupTraverser
%{_includedir}/KDE/KBookmarkImporterBase
%{_includedir}/KDE/KBookmarkManager
%{_includedir}/KDE/KBookmarkMenu
%{_includedir}/KDE/KBookmarkOwner
%{_includedir}/KDE/KBugReport
%{_includedir}/KDE/KBuildSycocaProgressDialog
%{_includedir}/KDE/KButtonGroup
%{_includedir}/KDE/KCModule
%{_includedir}/KDE/KCModuleContainer
%{_includedir}/KDE/KCModuleInfo
%{_includedir}/KDE/KCModuleLoader
%{_includedir}/KDE/KCModuleProxy
%{_includedir}/KDE/KCMultiDialog
%{_includedir}/KDE/KCalendarSystem
%{_includedir}/KDE/KCalendarSystemFactory
%{_includedir}/KDE/KCategorizedSortFilterProxyModel
%{_includedir}/KDE/KCategorizedView
%{_includedir}/KDE/KCategoryDrawer
%{_includedir}/KDE/KCharMacroExpander
%{_includedir}/KDE/KCharSelect
%{_includedir}/KDE/KCharsets
%{_includedir}/KDE/KCmdLineArgs
%{_includedir}/KDE/KCmdLineOptions
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
%{_includedir}/KDE/KCursor
%{_includedir}/KDE/KDBusServiceStarter
%{_includedir}/KDE/KDEDModule
%{_includedir}/KDE/KDEsuClient
%{_includedir}/KDE/KDataTool
%{_includedir}/KDE/KDataToolAction
%{_includedir}/KDE/KDataToolInfo
%{_includedir}/KDE/KDatePicker
%{_includedir}/KDE/KDateTable
%{_includedir}/KDE/KDateTime
%{_includedir}/KDE/KDateTimeWidget
%{_includedir}/KDE/KDateValidator
%{_includedir}/KDE/KDateWidget
%{_includedir}/KDE/KDebug
%{_includedir}/KDE/KDesktopFile
%{_includedir}/KDE/KDialog
%{_includedir}/KDE/KDialogButtonBox
%{_includedir}/KDE/KDirLister
%{_includedir}/KDE/KDirModel
%{_includedir}/KDE/KDirOperator
%{_includedir}/KDE/KDirSelectDialog
%{_includedir}/KDE/KDirSortFilterProxyModel
%{_includedir}/KDE/KDirWatch
%{_includedir}/KDE/KDiskFreeSpace
%{_includedir}/KDE/KDiskFreeSpaceInfo
%{_includedir}/KDE/KDoubleNumInput
%{_includedir}/KDE/KDoubleSpinBox
%{_includedir}/KDE/KDoubleValidator
%{_includedir}/KDE/KEMailSettings
%{_includedir}/KDE/KEditListBox
%{_includedir}/KDE/KEditToolBar
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
%{_includedir}/KDE/KFileItemDelegate
%{_includedir}/KDE/KFileItemList
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
%{_includedir}/KDE/KGenericFactory
%{_includedir}/KDE/KGenericFactoryBase
%{_includedir}/KDE/KGlobal
%{_includedir}/KDE/KGlobalAccel
%{_includedir}/KDE/KGlobalSettings
%{_includedir}/KDE/KGradientSelector
%{_includedir}/KDE/KGuiItem
%{_includedir}/KDE/KHBox
%{_includedir}/KDE/KHE
%{_includedir}/KDE/KHTMLPart
%{_includedir}/KDE/KHTMLSettings
%{_includedir}/KDE/KHTMLView
%{_includedir}/KDE/KHelpMenu
%{_includedir}/KDE/KHistoryComboBox
%{_includedir}/KDE/KHueSaturationSelector
%{_includedir}/KDE/KIEBookmarkExporterImpl
%{_includedir}/KDE/KIEBookmarkImporter
%{_includedir}/KDE/KIEBookmarkImporterImpl
%{_includedir}/KDE/KIMProxy
%{_includedir}/KDE/KIO
%{_includedir}/KDE/KIcon
%{_includedir}/KDE/KIconButton
%{_includedir}/KDE/KIconCanvas
%{_includedir}/KDE/KIconDialog
%{_includedir}/KDE/KIconEffect
%{_includedir}/KDE/KIconLoader
%{_includedir}/KDE/KIconTheme
%{_includedir}/KDE/KImageFilePreview
%{_includedir}/KDE/KImageIO
%{_includedir}/KDE/KInputDialog
%{_includedir}/KDE/KIntNumInput
%{_includedir}/KDE/KIntSpinBox
%{_includedir}/KDE/KIntValidator
%{_includedir}/KDE/KJob
%{_includedir}/KDE/KJobUiDelegate
%{_includedir}/KDE/KKeySequenceWidget
%{_includedir}/KDE/KLanguageButton
%{_includedir}/KDE/KLed
%{_includedir}/KDE/KLibFactory
%{_includedir}/KDE/KLibLoader
%{_includedir}/KDE/KLibrary
%{_includedir}/KDE/KLineEdit
%{_includedir}/KDE/KListWidget
%{_includedir}/KDE/KListWidgetSearchLine
%{_includedir}/KDE/KLocale
%{_includedir}/KDE/KLocalizedString
%{_includedir}/KDE/KLockFile
%{_includedir}/KDE/KMD5
%{_includedir}/KDE/KMacroExpanderBase
%{_includedir}/KDE/KMainWindow
%{_includedir}/KDE/KMakeTypeList
%{_includedir}/KDE/KMediaPlayer
%{_includedir}/KDE/KMenu
%{_includedir}/KDE/KMenuBar
%{_includedir}/KDE/KMessage
%{_includedir}/KDE/KMessageBox
%{_includedir}/KDE/KMessageBoxMessageHandler
%{_includedir}/KDE/KMessageHandler
%{_includedir}/KDE/KMimeType
%{_includedir}/KDE/KMimeTypeChooser
%{_includedir}/KDE/KMimeTypeChooserDialog
%{_includedir}/KDE/KMimeTypeResolver
%{_includedir}/KDE/KMimeTypeTrader
%{_includedir}/KDE/KMimeTypeValidator
%{_includedir}/KDE/KModifierKeyInfo
%{_includedir}/KDE/KMozillaBookmarkImporterImpl
%{_includedir}/KDE/KMultiTabBar
%{_includedir}/KDE/KMultiTabBarButton
%{_includedir}/KDE/KMultiTabBarTab
%{_includedir}/KDE/KNFSShare
%{_includedir}/KDE/KNS
%{_includedir}/KDE/KNSBookmarkExporter
%{_includedir}/KDE/KNSBookmarkExporterImpl
%{_includedir}/KDE/KNSBookmarkImporter
%{_includedir}/KDE/KNSBookmarkImporterImpl
%{_includedir}/KDE/KNTLM
%{_includedir}/KDE/KNetwork
%{_includedir}/KDE/KNotification
%{_includedir}/KDE/KNotificationRestrictions
%{_includedir}/KDE/KNotifyConfigWidget
%{_includedir}/KDE/KNumInput
%{_includedir}/KDE/KOCRDialog
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
%{_includedir}/KDE/KRecentDocument
%{_includedir}/KDE/KRecentFilesAction
%{_includedir}/KDE/KRemoteEncoding
%{_includedir}/KDE/KReplace
%{_includedir}/KDE/KReplaceDialog
%{_includedir}/KDE/KRestrictedLine
%{_includedir}/KDE/KRichTextEdit
%{_includedir}/KDE/KRichTextWidget
%{_includedir}/KDE/KRuler
%{_includedir}/KDE/KRun
%{_includedir}/KDE/KSambaShare
%{_includedir}/KDE/KSaveFile
%{_includedir}/KDE/KScanDialog
%{_includedir}/KDE/KSelectAction
%{_includedir}/KDE/KSelectionOwner
%{_includedir}/KDE/KSelectionWatcher
%{_includedir}/KDE/KSelector
%{_includedir}/KDE/KSeparator
%{_includedir}/KDE/KService
%{_includedir}/KDE/KServiceGroup
%{_includedir}/KDE/KServiceType
%{_includedir}/KDE/KServiceTypeProfile
%{_includedir}/KDE/KServiceTypeTrader
%{_includedir}/KDE/KSessionManager
%{_includedir}/KDE/KSettings
%{_includedir}/KDE/KSharedConfig
%{_includedir}/KDE/KSharedConfigPtr
%{_includedir}/KDE/KSharedPtr
%{_includedir}/KDE/KShell
%{_includedir}/KDE/KShellCompletion
%{_includedir}/KDE/KShortcut
%{_includedir}/KDE/KShortcutsDialog
%{_includedir}/KDE/KShortcutsEditor
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
%{_includedir}/KDE/KStringHandler
%{_includedir}/KDE/KStringListValidator
%{_includedir}/KDE/KStyle
%{_includedir}/KDE/KStyleFactory
%{_includedir}/KDE/KSvgRenderer
%{_includedir}/KDE/KSycoca
%{_includedir}/KDE/KSycocaEntry
%{_includedir}/KDE/KSystemTimeZone
%{_includedir}/KDE/KSystemTimeZoneSource
%{_includedir}/KDE/KSystemTimeZones
%{_includedir}/KDE/KSystemTrayIcon
%{_includedir}/KDE/KTabBar
%{_includedir}/KDE/KTabWidget
%{_includedir}/KDE/KTar
%{_includedir}/KDE/KTempDir
%{_includedir}/KDE/KTemporaryFile
%{_includedir}/KDE/KTextBrowser
%{_includedir}/KDE/KTextEdit
%{_includedir}/KDE/KTextEditor
%{_includedir}/KDE/KTimeZone
%{_includedir}/KDE/KTimeZoneData
%{_includedir}/KDE/KTimeZoneSource
%{_includedir}/KDE/KTimeZoneWidget
%{_includedir}/KDE/KTimeZones
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
%{_includedir}/KDE/KWallet
%{_includedir}/KDE/KWidgetItemDelegate
%{_includedir}/KDE/KWindowInfo
%{_includedir}/KDE/KWindowSystem
%{_includedir}/KDE/KWordMacroExpander
%{_includedir}/KDE/KWordWrap
%{_includedir}/KDE/KXBELBookmarkImporterImpl
%{_includedir}/KDE/KXErrorHandler
%{_includedir}/KDE/KXMLGUIBuilder
%{_includedir}/KDE/KXMLGUIClient
%{_includedir}/KDE/KXMLGUIFactory
%{_includedir}/KDE/KXMessages
%{_includedir}/KDE/KXYSelector
%{_includedir}/KDE/KXmlGuiWindow
%{_includedir}/KDE/KZip
%{_includedir}/KDE/KZipFileEntry
%{_includedir}/KDE/KZoneAllocator
%{_includedir}/KDE/KonqBookmarkMenu
%{_includedir}/KDE/KonqBookmarkOwner
%{_includedir}/KDE/NET
%{_includedir}/KDE/NETRootInfo
%{_includedir}/KDE/NETWinInfo
%{_includedir}/KDE/Nepomuk
%{_includedir}/KDE/OrgKdeKDirNotifyInterface
%{_includedir}/KDE/OrgKdeKLauncherInterface
%{_includedir}/KDE/PtyProcess
%{_includedir}/KDE/Solid
%{_includedir}/KDE/Sonnet
%{_includedir}/KDE/SshProcess
%{_includedir}/KDE/StubProcess
%{_includedir}/KDE/SuProcess
%{_includedir}/KDE/ThreadWeaver
%{_includedir}/KDE/ThumbCreator
%{_includedir}/KDE/kdbgstream
%{_includedir}/KDE/khtml
%{_includedir}/KDE/kndbgstream
%{_includedir}/KDE/Plasma
%dir %{_includedir}/nepomuk
%{_includedir}/nepomuk/*
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
%dir %{_includedir}/kparts
%{_includedir}/kparts/*
%{_includedir}/kross
%dir %{_includedir}/ktexteditor
%{_includedir}/ktexteditor/*
%{_includedir}/*.h
%dir %{_includedir}/solid
%{_includedir}/solid/*
%dir %{_includedir}/sonnet
%{_includedir}/sonnet/*
%dir %{_includedir}/threadweaver
%{_includedir}/threadweaver/*
%{_includedir}/*.tcc
%dir %{_includedir}/ksettings
%{_includedir}/ksettings/*
%dir %{_includedir}/kunittest
%{_includedir}/kunittest/*
