#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_with	localegen	# use Debian-like /etc/locale.gen and locale-gen helper
%bcond_with	packagekit	# use Ubuntu-like check-locale-support helper to get language support packages list

%define		kf_ver		5.102.0
%define		kp_ver		5.27.12
%define		qt_ver		5.15.2
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Summary(pl.UTF-8):	Środowisko KDE Plasma
Name:		kp5-%{kpname}
Version:	5.27.12
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{version}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ae7cb52ab11a032fb4ba29539d1d0499
Source1:	kde.pam
Patch0:		plasma-workspace-appstream1.patch
URL:		https://kde.org/
BuildRequires:	AppStream-qt5-devel >= 1.0.2
BuildRequires:	NetworkManager-devel >= 1.4
%{?with_packagekit:BuildRequires:	PackageKit-qt5-devel}
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5WaylandClient-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5XkbCommonSupport-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.22
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	gpsd-devel
BuildRequires:	iso-codes
BuildRequires:	ka5-libkexiv2-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kactivities-devel >= %{kf_ver}
BuildRequires:	kf5-kactivities-stats-devel >= %{kf_ver}
BuildRequires:	kf5-karchive-devel >= %{kf_ver}
BuildRequires:	kf5-kauth-devel >= %{kf_ver}
BuildRequires:	kf5-kbookmarks-devel >= %{kf_ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf5-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf5-kded-devel
BuildRequires:	kf5-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf5-kidletime-devel >= %{kf_ver}
BuildRequires:	kf5-kio-devel >= %{kf_ver}
BuildRequires:	kf5-kitemmodels-devel >= %{kf_ver}
BuildRequires:	kf5-kjobwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf5-knotifications-devel >= %{kf_ver}
BuildRequires:	kf5-knotifyconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kpackage-devel >= %{kf_ver}
BuildRequires:	kf5-kparts-devel >= %{kf_ver}
BuildRequires:	kf5-kpeople-devel >= %{kf_ver}
BuildRequires:	kf5-krunner-devel >= %{kf_ver}
BuildRequires:	kf5-kservice-devel >= %{kf_ver}
BuildRequires:	kf5-ktexteditor-devel >= %{kf_ver}
BuildRequires:	kf5-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kunitconversion-devel >= %{kf_ver}
BuildRequires:	kf5-kwallet-devel >= %{kf_ver}
BuildRequires:	kf5-kwayland-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-networkmanager-qt-devel >= %{kf_ver}
BuildRequires:	kf5-plasma-framework-devel >= %{kf_ver}
BuildRequires:	kf5-prison-devel >= %{kf_ver}
BuildRequires:	kf5-solid-devel >= %{kf_ver}
BuildRequires:	kp5-breeze-devel >= %{kp_ver}
BuildRequires:	kp5-kpipewire-devel >= %{kp_ver}
BuildRequires:	kp5-kscreenlocker-devel >= 5.13.80
BuildRequires:	kp5-kwin-devel >= %{kp_ver}
BuildRequires:	kp5-layer-shell-qt-devel >= %{kp_ver}
BuildRequires:	kp5-libkscreen-devel >= %{kp_ver}
BuildRequires:	kp5-libksysguard-devel >= %{kp_ver}
BuildRequires:	kuserfeedback-devel
BuildRequires:	libdrm-devel
BuildRequires:	libicu-devel
BuildRequires:	libqalculate-devel > 2.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel >= 4.6.60
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	plasma-wayland-protocols-devel >= 1.6
%{?with_localegen:BuildRequires:	polkit-qt5-1-devel}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.31
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	AppStream-qt5 >= 1.0.2
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5PrintSupport >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5WaylandClient >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	kf5-kactivities >= %{kf_ver}
Requires:	kf5-kactivities-stats >= %{kf_ver}
Requires:	kf5-karchive >= %{kf_ver}
Requires:	kf5-kauth >= %{kf_ver}
Requires:	kf5-kbookmarks >= %{kf_ver}
Requires:	kf5-kcmutils >= %{kf_ver}
Requires:	kf5-kcompletion >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kcrash >= %{kf_ver}
Requires:	kf5-kdbusaddons >= %{kf_ver}
Requires:	kf5-kdeclarative >= %{kf_ver}
Requires:	kf5-kglobalaccel >= %{kf_ver}
Requires:	kf5-kguiaddons >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kiconthemes >= %{kf_ver}
Requires:	kf5-kidletime >= %{kf_ver}
Requires:	kf5-kio >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-kjobwidgets >= %{kf_ver}
Requires:	kf5-knewstuff >= %{kf_ver}
Requires:	kf5-knotifications >= %{kf_ver}
Requires:	kf5-knotifyconfig >= %{kf_ver}
Requires:	kf5-kpackage >= %{kf_ver}
Requires:	kf5-kparts >= %{kf_ver}
Requires:	kf5-kpeople >= %{kf_ver}
Requires:	kf5-kquickcharts >= %{kf_ver}
Requires:	kf5-krunner >= %{kf_ver}
Requires:	kf5-kservice >= %{kf_ver}
Requires:	kf5-ktexteditor >= %{kf_ver}
Requires:	kf5-ktextwidgets >= %{kf_ver}
Requires:	kf5-kwallet >= %{kf_ver}
Requires:	kf5-kwayland >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
Requires:	kf5-networkmanager-qt >= %{kf_ver}
Requires:	kf5-plasma-framework >= %{kf_ver}
Requires:	kf5-prison >= %{kf_ver}
Requires:	kf5-solid >= %{kf_ver}
Requires:	kp5-kpipewire >= %{kp_ver}
Requires:	kp5-kscreenlocker >= 5.13.80
Requires:	kp5-layer-shell-qt >= %{kp_ver}
Requires:	kp5-libkscreen >= %{kp_ver}
Requires:	kp5-libksysguard >= %{kp_ver}
Requires:	kp5-plasma-workspace-data = %{version}-%{release}
Requires:	libqalculate > 2.0
# kf5/kio/thumbnail.so plugin
Suggests:	ka5-kio-extras
Suggests:	appmenu-gtk2-module
Suggests:	appmenu-gtk3-module
Suggests:	kio-fuse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Plasma Workspace.

%description -l pl.UTF-8
Środowisko KDE Plasma.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}
Requires:	Qt5Quick-devel >= %{qt_ver}
Requires:	kf5-kconfig-devel >= %{kf_ver}
Requires:	kf5-kcoreaddons-devel >= %{kf_ver}
Requires:	kf5-kitemmodels-devel >= %{kf_ver}
Requires:	kf5-plasma-framework-devel >= %{kf_ver}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}
%patch -P 0 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
%if %{with localegen} && %{without packagekit}
	-DGLIBC_LOCALE_GEN=ON \
%else
	-DGLIBC_LOCALE_GEN=OFF \
%endif
%if %{without localegen} && %{without packagekit}
	-DGLIBC_LOCALE_PREGENERATED=ON \
%else
	-DGLIBC_LOCALE_PREGENERATED=OFF \
%endif
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
%if %{with packagekit}
	-DUBUNTU_PACKAGEKIT=ON \
%else
	-DUBUNTU_PACKAGEKIT=OFF
%endif

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -p -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kde

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
/etc/xdg/plasmanotifyrc
/etc/xdg/taskmanagerrulesrc
/etc/xdg/autostart/gmenudbusmenuproxy.desktop
/etc/xdg/autostart/klipper.desktop
/etc/xdg/autostart/org.kde.plasmashell.desktop
/etc/xdg/autostart/xembedsniproxy.desktop
%attr(755,root,root) %{_bindir}/gmenudbusmenuproxy
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kde-systemd-start-condition
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplashqml
%attr(755,root,root) %{_bindir}/lookandfeeltool
%attr(755,root,root) %{_bindir}/plasma-apply-colorscheme
%attr(755,root,root) %{_bindir}/plasma-apply-cursortheme
%attr(755,root,root) %{_bindir}/plasma-apply-desktoptheme
%attr(755,root,root) %{_bindir}/plasma-apply-lookandfeel
%attr(755,root,root) %{_bindir}/plasma-apply-wallpaperimage
%attr(755,root,root) %{_bindir}/plasma-interactiveconsole
%if %{with localegen}
%attr(755,root,root) %{_bindir}/plasma-localegen-helper
%endif
%attr(755,root,root) %{_bindir}/plasma-shutdown
%attr(755,root,root) %{_bindir}/plasma_session
%attr(755,root,root) %{_bindir}/plasma_waitforname
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/startplasma-wayland
%attr(755,root,root) %{_bindir}/startplasma-x11
%attr(755,root,root) %{_bindir}/systemmonitor
%attr(755,root,root) %{_bindir}/xembedsniproxy
%attr(755,root,root) %{_libexecdir}/baloorunner
%attr(755,root,root) %{_libexecdir}/kfontprint
%attr(755,root,root) %{_libexecdir}/ksmserver-logout-greeter
%attr(755,root,root) %{_libexecdir}/plasma-changeicons
%attr(755,root,root) %{_libexecdir}/plasma-dbus-run-session-if-needed
%attr(755,root,root) %{_libexecdir}/plasma-sourceenv.sh
%attr(755,root,root) %{_libexecdir}/kauth/fontinst
%attr(755,root,root) %{_libexecdir}/kauth/fontinst_helper
%attr(755,root,root) %{_libexecdir}/kauth/fontinst_x11
%attr(755,root,root) %{_libdir}/libcolorcorrect.so.5.*.*
%ghost %{_libdir}/libcolorcorrect.so.5
%attr(755,root,root) %{_libdir}/libkfontinst.so.*.*.*
%ghost %{_libdir}/libkfontinst.so.5
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*.*.*
%ghost %{_libdir}/libkfontinstui.so.5
%attr(755,root,root) %{_libdir}/libkworkspace5.so.*.*.*
%ghost %{_libdir}/libkworkspace5.so.5
%attr(755,root,root) %{_libdir}/libnotificationmanager.so.*.*.*
%ghost %{_libdir}/libnotificationmanager.so.1
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so.*.*.*
%ghost %{_libdir}/libplasma-geolocation-interface.so.5
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*
%ghost %{_libdir}/libtaskmanager.so.6
%attr(755,root,root) %{_libdir}/libweather_ion.so.*.*.*
%ghost %{_libdir}/libweather_ion.so.7
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerglobalshortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerhistory
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasmashell-5.27-use-panel-thickness-in-default-group
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/appmenu.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/colorcorrectlocationupdater.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/desktopnotifier.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/freespacenotifier.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/ksysguard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/ktimezoned.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/plasma_accentcolor_service.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/soliduiserver.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/statusnotifierwatcher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/applications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/desktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/kio_fonts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/calculator.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/helprunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_appstream.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_kill.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_powerdevil.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_services.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_sessions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_shell.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_windowedwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/locations.so
%dir %{_libdir}/qt5/plugins/kf5/krunner/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/kcms/kcm_krunner_kill.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/kfontviewpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/thumbcreator/fontthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_layouttemplate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_shell.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_wallpaper.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/wallpaper_images.so
%dir %{_libdir}/qt5/plugins/phonon_platform
%attr(755,root,root) %{_libdir}/qt5/plugins/phonon_platform/kde.so
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/applets
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.appmenu.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.calendar.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.icon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.panelspacer.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.private.systemtray.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.systemmonitor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.systemtray.so
%dir %{_libdir}/qt5/plugins/plasma/containmentactions
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_applauncher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_contextmenu.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_paste.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchactivity.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchdesktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchwindow.so
%dir %{_libdir}/qt5/plugins/plasma/dataengine
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_bbcukmet.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_dwd.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_envcan.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_noaa.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_wettercom.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_activities.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_applicationjobs.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_apps.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_clipboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_devicenotifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_dict.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_executable.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_favicons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_filebrowser.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_geolocation.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_hotplug.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_keystate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mouse.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mpris2.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_packagekit.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_places.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_powermanagement.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_statusnotifieritem.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_systemmonitor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_weather.so
%dir %{_libdir}/qt5/plugins/plasma/geolocationprovider
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/geolocationprovider/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/geolocationprovider/plasma-geolocation-ip.so
%dir %{_libdir}/qt5/plugins/plasma/kcminit
# symlinks to modules in ../kcms/systemsettings
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_fonts_init.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_style_init.so
%dir %{_libdir}/qt5/plugins/plasma/kcms
%dir %{_libdir}/qt5/plugins/plasma/kcms/systemsettings
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_colors.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_feedback.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_icons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_nightcolor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_style.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_users.so
%dir %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/plasmacalendarplugins/holidaysevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/holidays
%{_libdir}/qt5/plugins/plasmacalendarplugins/holidays/HolidaysConfig.qml
%dir %{_libdir}/qt5/qml/org/kde/colorcorrect
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/colorcorrect/libcolorcorrectplugin.so
%{_libdir}/qt5/qml/org/kde/colorcorrect/qmldir
%dir %{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin/libholidayeventshelperplugin.so
%{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin/qmldir
%dir %{_libdir}/qt5/qml/org/kde/notificationmanager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/notificationmanager/libnotificationmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/notificationmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma
%dir %{_libdir}/qt5/qml/org/kde/plasma/lookandfeel
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/lookandfeel/liblookandfeelqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/lookandfeel/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/appmenu
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/libappmenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/*.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/libcontainmentlayoutmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/private
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller/libmediacontrollerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/sessions
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/sessions/libsessionsprivateplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/sessions/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/shell
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/shell/libplasmashellprivateplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/shell/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/libplasma_wallpaper_imageplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/*.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/libcalendarplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/components
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/*.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/SystemDialog.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/examples
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/examples/test.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout/libkeyboardlayoutplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter/libtrianglemousefilterplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter/qmldir
%dir %{_libdir}/qt5/qml/org/kde/taskmanager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/taskmanager/qmldir
%{systemduserunitdir}/plasma-baloorunner.service
%{systemduserunitdir}/plasma-core.target
%{systemduserunitdir}/plasma-gmenudbusmenuproxy.service
%{systemduserunitdir}/plasma-kcminit-phase1.service
%{systemduserunitdir}/plasma-kcminit.service
%{systemduserunitdir}/plasma-krunner.service
%{systemduserunitdir}/plasma-ksmserver.service
%{systemduserunitdir}/plasma-ksplash-ready.service
%{systemduserunitdir}/plasma-plasmashell.service
%{systemduserunitdir}/plasma-restoresession.service
%{systemduserunitdir}/plasma-xembedsniproxy.service
%{systemduserunitdir}/plasma-ksplash.service
%{systemduserunitdir}/plasma-workspace-wayland.target
%{systemduserunitdir}/plasma-workspace-x11.target
%{systemduserunitdir}/plasma-workspace.target

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/colorssettings.kcfg
%{_datadir}/config.kcfg/cursorthemesettings.kcfg
%{_datadir}/config.kcfg/feedbacksettings.kcfg
%{_datadir}/config.kcfg/fontssettings.kcfg
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/config.kcfg/iconssettingsbase.kcfg
%{_datadir}/config.kcfg/launchfeedbacksettings.kcfg
%{_datadir}/config.kcfg/lookandfeelsettings.kcfg
%{_datadir}/config.kcfg/stylesettings.kcfg
%{_datadir}/dbus-1/interfaces/com.canonical.AppMenu.Registrar.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSplash.xml
%{_datadir}/dbus-1/interfaces/org.kde.PlasmaShell.xml
%{_datadir}/dbus-1/interfaces/org.kde.kappmenu.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.KSplash.service
%{_datadir}/dbus-1/services/org.kde.LogoutPrompt.service
%{_datadir}/dbus-1/services/org.kde.Shutdown.service
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/dbus-1/services/org.kde.plasma.Notifications.service
%{_datadir}/dbus-1/services/org.kde.runners.baloo.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%if %{with localegen}
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%endif
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%if %{with localegen}
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%endif
%{_datadir}/desktop-directories/kf5-development-translation.directory
%{_datadir}/desktop-directories/kf5-development-webdevelopment.directory
%{_datadir}/desktop-directories/kf5-development.directory
%{_datadir}/desktop-directories/kf5-editors.directory
%{_datadir}/desktop-directories/kf5-edu-languages.directory
%{_datadir}/desktop-directories/kf5-edu-mathematics.directory
%{_datadir}/desktop-directories/kf5-edu-miscellaneous.directory
%{_datadir}/desktop-directories/kf5-edu-science.directory
%{_datadir}/desktop-directories/kf5-edu-tools.directory
%{_datadir}/desktop-directories/kf5-education.directory
%{_datadir}/desktop-directories/kf5-games-arcade.directory
%{_datadir}/desktop-directories/kf5-games-board.directory
%{_datadir}/desktop-directories/kf5-games-card.directory
%{_datadir}/desktop-directories/kf5-games-kids.directory
%{_datadir}/desktop-directories/kf5-games-logic.directory
%{_datadir}/desktop-directories/kf5-games-roguelikes.directory
%{_datadir}/desktop-directories/kf5-games-strategy.directory
%{_datadir}/desktop-directories/kf5-games.directory
%{_datadir}/desktop-directories/kf5-graphics.directory
%{_datadir}/desktop-directories/kf5-internet-terminal.directory
%{_datadir}/desktop-directories/kf5-internet.directory
%{_datadir}/desktop-directories/kf5-main.directory
%{_datadir}/desktop-directories/kf5-more.directory
%{_datadir}/desktop-directories/kf5-multimedia.directory
%{_datadir}/desktop-directories/kf5-network.directory
%{_datadir}/desktop-directories/kf5-office.directory
%{_datadir}/desktop-directories/kf5-science.directory
%{_datadir}/desktop-directories/kf5-settingsmenu.directory
%{_datadir}/desktop-directories/kf5-system-terminal.directory
%{_datadir}/desktop-directories/kf5-system.directory
%{_datadir}/desktop-directories/kf5-toys.directory
%{_datadir}/desktop-directories/kf5-unknown.directory
%{_datadir}/desktop-directories/kf5-utilities-accessibility.directory
%{_datadir}/desktop-directories/kf5-utilities-desktop.directory
%{_datadir}/desktop-directories/kf5-utilities-file.directory
%{_datadir}/desktop-directories/kf5-utilities-peripherals.directory
%{_datadir}/desktop-directories/kf5-utilities-pim.directory
%{_datadir}/desktop-directories/kf5-utilities-xutils.directory
%{_datadir}/desktop-directories/kf5-utilities.directory
%attr(755,root,root) %{_datadir}/kconf_update/delete_cursor_old_default_size.pl
%{_datadir}/kconf_update/delete_cursor_old_default_size.upd
%{_datadir}/kconf_update/icons_remove_effects.upd
%{_datadir}/kconf_update/krunnerglobalshortcuts2.upd
%{_datadir}/kconf_update/krunnerhistory.upd
%{_datadir}/kconf_update/plasmashell-5.27-use-panel-thickness-in-default-group.upd
%attr(755,root,root) %{_datadir}/kconf_update/style_widgetstyle_default_breeze.pl
%{_datadir}/kconf_update/style_widgetstyle_default_breeze.upd
%{_datadir}/kfontinst
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/kio/servicemenus/setaswallpaper.desktop
%dir %{_datadir}/kio_desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/knotifications5/devicenotifications.notifyrc
%{_datadir}/knotifications5/freespacenotifier.notifyrc
%{_datadir}/knotifications5/phonon.notifyrc
%dir %{_datadir}/knsrcfiles
%{_datadir}/knsrcfiles/colorschemes.knsrc
%{_datadir}/knsrcfiles/gtk_themes.knsrc
%{_datadir}/knsrcfiles/icons.knsrc
%{_datadir}/knsrcfiles/kfontinst.knsrc
%{_datadir}/knsrcfiles/lookandfeel.knsrc
%{_datadir}/knsrcfiles/plasma-themes.knsrc
%{_datadir}/knsrcfiles/plasmoids.knsrc
%{_datadir}/knsrcfiles/wallpaper.knsrc
%{_datadir}/knsrcfiles/wallpaper-mobile.knsrc
%{_datadir}/knsrcfiles/wallpaperplugin.knsrc
%{_datadir}/knsrcfiles/xcursor.knsrc
%dir %{_datadir}/konqsidebartng
%dir %{_datadir}/konqsidebartng/virtual_folders
%dir %{_datadir}/konqsidebartng/virtual_folders/services
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/kpackage/kcms/kcm_autostart
%{_datadir}/kpackage/kcms/kcm_colors
%{_datadir}/kpackage/kcms/kcm_cursortheme
%{_datadir}/kpackage/kcms/kcm_desktoptheme
%{_datadir}/kpackage/kcms/kcm_feedback
%{_datadir}/kpackage/kcms/kcm_fonts
%{_datadir}/kpackage/kcms/kcm_icons
%{_datadir}/kpackage/kcms/kcm_lookandfeel
%{_datadir}/kpackage/kcms/kcm_nightcolor
%{_datadir}/kpackage/kcms/kcm_notifications
%{_datadir}/kpackage/kcms/kcm_regionandlang
%{_datadir}/kpackage/kcms/kcm_style
%{_datadir}/kpackage/kcms/kcm_users
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservicetypes5/plasma-layouttemplate.desktop
%dir %{_datadir}/kstyle
%dir %{_datadir}/kstyle/themes
%{_datadir}/kstyle/themes/qtcde.themerc
%{_datadir}/kstyle/themes/qtcleanlooks.themerc
%{_datadir}/kstyle/themes/qtgtk.themerc
%{_datadir}/kstyle/themes/qtmotif.themerc
%{_datadir}/kstyle/themes/qtplastique.themerc
%{_datadir}/kstyle/themes/qtwindows.themerc
%{_datadir}/kxmlgui5/kfontview
%{_datadir}/metainfo/org.kde.breeze.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezedark.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezetwilight.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.color.appdata.xml
%{_datadir}/metainfo/org.kde.image.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activitybar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.analogclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.appmenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.calendar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.clipboard.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.devicenotifier.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.digitalclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.lock_logout.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.manage-inputmethod.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mediacontroller.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.notifications.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpucore.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskactivity.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskusage.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.memory.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.net.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemtray.appdata.xml
%{_datadir}/metainfo/org.kde.slideshow.appdata.xml
%{_datadir}/plasma/avatars
%dir %{_datadir}/plasma/look-and-feel
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop
%{_datadir}/plasma/nightcolor
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%{_datadir}/plasma/services/activities.operations
%{_datadir}/plasma/services/applicationjobs.operations
%{_datadir}/plasma/services/apps.operations
%{_datadir}/plasma/services/hotplug.operations
%{_datadir}/plasma/services/modifierkeystate.operations
%{_datadir}/plasma/services/mpris2.operations
%{_datadir}/plasma/services/notifications.operations
%{_datadir}/plasma/services/org.kde.places.operations
%{_datadir}/plasma/services/org.kde.plasma.clipboard.operations
%{_datadir}/plasma/services/packagekit.operations
%{_datadir}/plasma/services/powermanagementservice.operations
%{_datadir}/plasma/services/soliddevice.operations
%{_datadir}/plasma/services/statusnotifieritem.operations
%dir %{_datadir}/plasma/wallpapers
%{_datadir}/plasma/wallpapers/org.kde.color
%{_datadir}/plasma/wallpapers/org.kde.image
%{_datadir}/plasma/wallpapers/org.kde.slideshow
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%if %{with localegen}
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%endif
%{_datadir}/qlogging-categories5/kcm_regionandlang.categories
%{_datadir}/qlogging-categories5/kcmusers.categories
%{_datadir}/qlogging-categories5/klipper.categories
%{_datadir}/qlogging-categories5/libnotificationmanager.categories
%{_datadir}/qlogging-categories5/myproject.categories
%{_datadir}/qlogging-categories5/plasma-workspace.categories
%{_datadir}/sddm/themes/breeze
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/wayland-sessions/plasmawayland.desktop
%{_datadir}/xsessions/plasma.desktop
%{_desktopdir}/kcm_autostart.desktop
%{_desktopdir}/kcm_colors.desktop
%{_desktopdir}/kcm_cursortheme.desktop
%{_desktopdir}/kcm_feedback.desktop
%{_desktopdir}/kcm_fontinst.desktop
%{_desktopdir}/kcm_fonts.desktop
%{_desktopdir}/kcm_icons.desktop
%{_desktopdir}/kcm_lookandfeel.desktop
%{_desktopdir}/kcm_nightcolor.desktop
%{_desktopdir}/kcm_notifications.desktop
%{_desktopdir}/kcm_regionandlang.desktop
%{_desktopdir}/kcm_style.desktop
%{_desktopdir}/kcm_users.desktop
%{_desktopdir}/org.kde.kcolorschemeeditor.desktop
%{_desktopdir}/org.kde.kfontview.desktop
%{_desktopdir}/org.kde.klipper.desktop
%{_desktopdir}/org.kde.plasmashell.desktop
%{_desktopdir}/org.kde.plasmawindowed.desktop
%{_desktopdir}/org.kde.systemmonitor.desktop
%{_iconsdir}/hicolor/128x128/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/16x16/apps/kfontview.png
%{_iconsdir}/hicolor/16x16/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/22x22/apps/kfontview.png
%{_iconsdir}/hicolor/22x22/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/32x32/apps/kfontview.png
%{_iconsdir}/hicolor/32x32/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/48x48/apps/kfontview.png
%{_iconsdir}/hicolor/48x48/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/64x64/apps/kfontview.png
%{_iconsdir}/hicolor/64x64/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{zsh_compdir}/_plasmashell

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcolorcorrect.so
%{_libdir}/libkfontinst.so
%{_libdir}/libkfontinstui.so
%{_libdir}/libkrdb.so
%{_libdir}/libkworkspace5.so
%{_libdir}/libnotificationmanager.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libweather_ion.so
%{_includedir}/colorcorrect
%{_includedir}/kworkspace5
%{_includedir}/notificationmanager
%{_includedir}/plasma
%{_includedir}/taskmanager
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/LibColorCorrect
%{_libdir}/cmake/LibNotificationManager
