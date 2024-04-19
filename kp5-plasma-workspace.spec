#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	5.27.11
%define		qtver		5.15.2
%define		kf5ver		5.102.0
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp5-%{kpname}
Version:	5.27.11
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ae751485c237143987f987191064ddfd
Source1:	kde.pam
Patch0:		kp5-plasma-workspace-absolute-path.patch
Patch1:		kp5-plasma-workspace-scripts.patch
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt5-devel >= 1.0.2
BuildRequires:	NetworkManager-devel >= 1.4
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5WaylandClient-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5XkbCommonSupport-devel >= %{qtver}
BuildRequires:	cmake >= 3.22
BuildRequires:	fontconfig-devel
BuildRequires:	gpsd-devel
BuildRequires:	iso-codes
BuildRequires:	ka5-kio-extras-devel
BuildRequires:	ka5-libkexiv2-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kf5ver}
BuildRequires:	kf5-kactivities-devel >= %{kf5ver}
BuildRequires:	kf5-kactivities-stats-devel >= %{kf5ver}
BuildRequires:	kf5-karchive-devel >= %{kf5ver}
BuildRequires:	kf5-kauth-devel >= %{kf5ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf5ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kcrash-devel >= %{kf5ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf5ver}
BuildRequires:	kf5-kded-devel
BuildRequires:	kf5-kdoctools-devel >= %{kf5ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf5ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-ki18n-devel >= %{kf5ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf5ver}
BuildRequires:	kf5-kidletime-devel >= %{kf5ver}
BuildRequires:	kf5-kio-devel >= %{kf5ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf5ver}
BuildRequires:	kf5-kitemmodels-devel >= %{kf5ver}
BuildRequires:	kf5-knewstuff-devel >= %{kf5ver}
BuildRequires:	kf5-knotifications-devel >= %{kf5ver}
BuildRequires:	kf5-knotifyconfig-devel >= %{kf5ver}
BuildRequires:	kf5-kpackage-devel >= %{kf5ver}
BuildRequires:	kf5-kpeople-devel >= %{kf5ver}
BuildRequires:	kf5-kquickcharts-devel >= %{kf5ver}
BuildRequires:	kf5-krunner-devel >= %{kf5ver}
BuildRequires:	kf5-ktexteditor-devel >= %{kf5ver}
BuildRequires:	kf5-ktextwidgets-devel >= %{kf5ver}
BuildRequires:	kf5-kunitconversion-devel >= %{kf5ver}
BuildRequires:	kf5-kwallet-devel >= %{kf5ver}
BuildRequires:	kf5-kwayland-devel >= %{kf5ver}
BuildRequires:	kf5-networkmanager-qt-devel >= %{kf5ver}
BuildRequires:	kf5-plasma-framework-devel >= %{kf5ver}
BuildRequires:	kf5-plasma-wayland-protocols-devel >= 1.6
BuildRequires:	kf5-prison-devel >= %{kf5ver}
BuildRequires:	kp5-breeze-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kpipewire-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kscreenlocker-devel >= 5.13.80
BuildRequires:	kp5-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp5-layer-shell-qt-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libkscreen-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libksysguard-devel >= %{kdeplasmaver}
BuildRequires:	kuserfeedback-devel
BuildRequires:	libdrm-devel
BuildRequires:	libicu-devel
BuildRequires:	libqalculate-devel > 2.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel >= 4.6.60
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	polkit-qt5-1-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.31
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
Requires:	kp5-plasma-workspace-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Workspace.

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

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}
#%%patch0 -p1
#%%patch1 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -p -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kde

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/tok

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
/etc/xdg/autostart/gmenudbusmenuproxy.desktop
%attr(755,root,root) %{_bindir}/gmenudbusmenuproxy
%ghost %{_libdir}/libcolorcorrect.so.5
%attr(755,root,root) %{_libdir}/libcolorcorrect.so.5.*.*
%{_libdir}/qt5/plugins/kf5/kded/colorcorrectlocationupdater.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/holidays
%{_libdir}/qt5/plugins/plasmacalendarplugins/holidays/HolidaysConfig.qml
%{_libdir}/qt5/plugins/plasmacalendarplugins/holidaysevents.so
%dir %{_libdir}/qt5/qml/org/kde/colorcorrect
%{_libdir}/qt5/qml/org/kde/colorcorrect/libcolorcorrectplugin.so
%{_libdir}/qt5/qml/org/kde/colorcorrect/qmldir
%dir %{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin
%{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin/libholidayeventshelperplugin.so
%{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin/qmldir
%attr(755,root,root) %{_prefix}/libexec/baloorunner
%attr(755,root,root) %{_prefix}/libexec/ksmserver-logout-greeter
/etc/xdg/autostart/klipper.desktop
/etc/xdg/autostart/xembedsniproxy.desktop
/etc/xdg/taskmanagerrulesrc
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplashqml
%attr(755,root,root) %{_bindir}/plasma_waitforname
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/systemmonitor
%attr(755,root,root) %{_bindir}/xembedsniproxy
%{_libdir}/libkworkspace5.so.5
%{_libdir}/libkworkspace5.so.5.*.*
%{_libdir}/libplasma-geolocation-interface.so.5
%{_libdir}/libplasma-geolocation-interface.so.5.*.*
%{_libdir}/libtaskmanager.so.5.*.*
%{_libdir}/libtaskmanager.so.6
%{_libdir}/libweather_ion.so.7
%{_libdir}/libweather_ion.so.7.0.0
%{_libdir}/qt5/plugins/kf5/kded/appmenu.so
%{_libdir}/qt5/plugins/kf5/kded/desktopnotifier.so
%{_libdir}/qt5/plugins/kf5/kded/freespacenotifier.so
%{_libdir}/qt5/plugins/kf5/kded/ksysguard.so
%{_libdir}/qt5/plugins/kf5/kded/ktimezoned.so
%{_libdir}/qt5/plugins/kf5/kded/soliduiserver.so
%{_libdir}/qt5/plugins/kf5/kded/statusnotifierwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/desktop.so
%dir %{_libdir}/qt5/plugins/phonon_platform
%{_libdir}/qt5/plugins/phonon_platform/kde.so
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/applets
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.private.systemtray.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.systemtray.so
%dir %{_libdir}/qt5/plugins/plasma/dataengine
%{_libdir}/qt5/plugins/plasma/dataengine/ion_bbcukmet.so
%{_libdir}/qt5/plugins/plasma/dataengine/ion_envcan.so
%{_libdir}/qt5/plugins/plasma/dataengine/ion_noaa.so
%{_libdir}/qt5/plugins/plasma/dataengine/ion_wettercom.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_activities.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_applicationjobs.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_apps.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_clipboard.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_devicenotifications.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_dict.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_executable.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_favicons.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_filebrowser.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_geolocation.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_hotplug.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_keystate.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mouse.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_mpris2.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_notifications.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_packagekit.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_places.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_powermanagement.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_soliddevice.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_statusnotifieritem.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_systemmonitor.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_time.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_weather.so
%dir %{_libdir}/qt5/qml/org/kde/plasma
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/appmenu
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/libappmenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/sessions
%{_libdir}/qt5/qml/org/kde/plasma/private/sessions/libsessionsprivateplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/sessions/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/shell
%{_libdir}/qt5/qml/org/kde/plasma/private/shell/libplasmashellprivateplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/shell/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/libplasma_wallpaper_imageplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/components
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/BatteryIcon.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout
%{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout/libkeyboardlayoutplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/keyboardlayout/qmldir
%dir %{_libdir}/qt5/qml/org/kde/taskmanager
%{_libdir}/qt5/qml/org/kde/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/taskmanager/qmldir
/etc/xdg/autostart/org.kde.plasmashell.desktop
/etc/xdg/plasmanotifyrc
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kde-systemd-start-condition
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/lookandfeeltool
%attr(755,root,root) %{_bindir}/plasma-shutdown
%attr(755,root,root) %{_bindir}/plasma_session
%attr(755,root,root) %{_bindir}/startplasma-wayland
%attr(755,root,root) %{_bindir}/startplasma-x11
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
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerglobalshortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerhistory
%ghost %{_libdir}/libkfontinst.so.5
%{_libdir}/libkfontinst.so.5.*.*
%ghost %{_libdir}/libkfontinstui.so.5
%{_libdir}/libkfontinstui.so.5.*.*
%ghost %{_libdir}/libnotificationmanager.so.1
%{_libdir}/libnotificationmanager.so.5.*.*
%{_libdir}/qt5/plugins/kf5/kio/applications.so
# AppStream 0.x is required to build this
#%{_libdir}/qt5/plugins/kf5/krunner/krunner_appstream.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_bookmarksrunner.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_kill.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_placesrunner.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_powerdevil.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_recentdocuments.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_services.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_sessions.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_shell.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_webshortcuts.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_windowedwidgets.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.panelspacer.so
%dir %{_libdir}/qt5/plugins/plasma/containmentactions
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_applauncher.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_contextmenu.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_paste.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchdesktop.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchwindow.so
%dir %{_libdir}/qt5/qml/org/kde/notificationmanager
%{_libdir}/qt5/qml/org/kde/notificationmanager/libnotificationmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/notificationmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/BasicAppletContainer.qml
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/ConfigOverlayWithHandles.qml
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/PlaceHolder.qml
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/libcontainmentlayoutmanagerplugin.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/private
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/private/BasicResizeHandle.qml
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/qmldir
%attr(755,root,root) %{_prefix}/libexec/kauth/fontinst
%attr(755,root,root) %{_prefix}/libexec/kauth/fontinst_helper
%attr(755,root,root) %{_prefix}/libexec/kauth/fontinst_x11
%attr(755,root,root) %{_prefix}/libexec/kfontprint
%attr(755,root,root) %{_prefix}/libexec/plasma-changeicons
%attr(755,root,root) %{_prefix}/libexec/plasma-dbus-run-session-if-needed
%attr(755,root,root) %{_prefix}/libexec/plasma-sourceenv.sh
%attr(755,root,root) %{_bindir}/plasma-apply-colorscheme
%attr(755,root,root) %{_bindir}/plasma-apply-cursortheme
%attr(755,root,root) %{_bindir}/plasma-apply-desktoptheme
%attr(755,root,root) %{_bindir}/plasma-apply-lookandfeel
%attr(755,root,root) %{_bindir}/plasma-apply-wallpaperimage
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/calculator.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/locations.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/KeyboardLayoutSwitcher.qml
%attr(755,root,root) %{_bindir}/plasma-interactiveconsole
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/kio_fonts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/kfontviewpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_layouttemplate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_shell.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_wallpaper.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/wallpaper_images.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchactivity.so
%dir %{_libdir}/qt5/plugins/plasma/geolocationprovider
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/geolocationprovider/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/geolocationprovider/plasma-geolocation-ip.so
%{systemduserunitdir}/plasma-ksplash.service
%{systemduserunitdir}/plasma-workspace-wayland.target
%{systemduserunitdir}/plasma-workspace-x11.target
%{systemduserunitdir}/plasma-workspace.target
%{_libdir}/qt5/plugins/kf5/krunner/helprunner.so
%dir %{_libdir}/qt5/plugins/kf5/krunner/kcms
%{_libdir}/qt5/plugins/kf5/krunner/kcms/kcm_krunner_kill.so
%{_libdir}/qt5/plugins/plasma/dataengine/ion_dwd.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_fonts_init.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_style_init.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_colors.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_icons.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_nightcolor.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_style.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_users.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/lookandfeel
%{_libdir}/qt5/qml/org/kde/plasma/lookandfeel/liblookandfeelqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/lookandfeel/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/SystemDialog.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/examples
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/examples/test.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/dialogs/qmldir
%{_libdir}/qt5/plugins/kf5/kded/plasma_accentcolor_service.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.appmenu.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.calendar.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.icon.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.notifications.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.systemmonitor.so
%attr(755,root,root) %{_bindir}/plasma-localegen-helper
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_feedback.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/CalendarToolbar.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/DayDelegate.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/DaysCalendar.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/InfiniteList.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/MonthMenu.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/MonthView.qml
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/libcalendarplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/BadgeOverlay.qml
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasmashell-5.27-use-panel-thickness-in-default-group
%{_libdir}/qt5/plugins/kf5/thumbcreator/fontthumbnail.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller
%{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller/libmediacontrollerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/workspace/calendar/MonthViewHeader.qml
%dir %{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter
%{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter/libtrianglemousefilterplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/trianglemousefilter/qmldir

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.systemmonitor.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/WallpaperFader.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.xml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/timer.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%{_datadir}/sddm/themes/breeze/components/WallpaperFader.qml
%dir %{_datadir}/sddm/themes/breeze/faces
%{_datadir}/sddm/themes/breeze/faces/.face.icon
%{_desktopdir}/org.kde.klipper.desktop
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/dbus-1/interfaces/com.canonical.AppMenu.Registrar.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSplash.xml
%{_datadir}/dbus-1/interfaces/org.kde.PlasmaShell.xml
%{_datadir}/dbus-1/interfaces/org.kde.kappmenu.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/dbus-1/services/org.kde.plasma.Notifications.service
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
%dir %{_datadir}/kio_desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/knotifications5/freespacenotifier.notifyrc
%{_datadir}/knotifications5/phonon.notifyrc
%{_datadir}/kservicetypes5/plasma-layouttemplate.desktop
%dir %{_datadir}/kstyle
%dir %{_datadir}/kstyle/themes
%{_datadir}/kstyle/themes/qtcde.themerc
%{_datadir}/kstyle/themes/qtcleanlooks.themerc
%{_datadir}/kstyle/themes/qtgtk.themerc
%{_datadir}/kstyle/themes/qtmotif.themerc
%{_datadir}/kstyle/themes/qtplastique.themerc
%{_datadir}/kstyle/themes/qtwindows.themerc
%{_datadir}/metainfo/org.kde.breeze.desktop.appdata.xml
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
%{_datadir}/metainfo/org.kde.plasma.mediacontroller.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.notifications.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskactivity.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.diskusage.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.memory.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.net.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemtray.appdata.xml
%{_datadir}/metainfo/org.kde.slideshow.appdata.xml
%dir %{_datadir}/plasma/look-and-feel
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/ActionButton.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/Battery.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/Clock.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/SessionManagementScreen.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/UserDelegate.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/UserList.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/VirtualKeyboard.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/README.txt
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/logout_primary.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/restart_primary.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/shutdown_primary.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/defaults
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/desktopswitcher
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/desktopswitcher/DesktopSwitcher.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockOsd.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockScreen.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockScreenUi.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/MainBlock.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/MediaControls.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/Logout.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/LogoutButton.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/Osd.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/OsdItem.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/desktopswitcher.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/lockscreen.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/loginmanager.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/runcommand.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/splash.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/userswitcher.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/windowdecoration.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/windowswitcher.png
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/Splash.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/busywidget.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/kde.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/plasma.svgz
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowswitcher
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowswitcher/WindowSwitcher.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
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
%dir %{_datadir}/plasma/wallpapers/org.kde.color
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents/config
%{_datadir}/plasma/wallpapers/org.kde.color/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.color/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.color/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.image
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/config
%{_datadir}/plasma/wallpapers/org.kde.image/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.image/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/metadata.json
%dir %{_datadir}/sddm/themes/breeze
%{_datadir}/sddm/themes/breeze/Background.qml
%{_datadir}/sddm/themes/breeze/KeyboardButton.qml
%{_datadir}/sddm/themes/breeze/Login.qml
%{_datadir}/sddm/themes/breeze/Main.qml
%{_datadir}/sddm/themes/breeze/SessionButton.qml
%dir %{_datadir}/sddm/themes/breeze/components
%{_datadir}/sddm/themes/breeze/components/ActionButton.qml
%{_datadir}/sddm/themes/breeze/components/Battery.qml
%{_datadir}/sddm/themes/breeze/components/Clock.qml
%{_datadir}/sddm/themes/breeze/components/SessionManagementScreen.qml
%{_datadir}/sddm/themes/breeze/components/UserDelegate.qml
%{_datadir}/sddm/themes/breeze/components/UserList.qml
%{_datadir}/sddm/themes/breeze/components/VirtualKeyboard.qml
%dir %{_datadir}/sddm/themes/breeze/components/artwork
%{_datadir}/sddm/themes/breeze/components/artwork/logout_primary.svgz
%{_datadir}/sddm/themes/breeze/components/artwork/restart_primary.svgz
%{_datadir}/sddm/themes/breeze/components/artwork/shutdown_primary.svgz
%{_datadir}/sddm/themes/breeze/metadata.desktop
%{_datadir}/sddm/themes/breeze/preview.png
%{_datadir}/sddm/themes/breeze/theme.conf
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/wayland-sessions/plasmawayland.desktop
%{_datadir}/xsessions/plasma.desktop
%{_desktopdir}/org.kde.kcolorschemeeditor.desktop
%{_desktopdir}/org.kde.kfontview.desktop
%{_datadir}/config.kcfg/colorssettings.kcfg
%{_datadir}/config.kcfg/cursorthemesettings.kcfg
%{_datadir}/config.kcfg/fontssettings.kcfg
%{_datadir}/config.kcfg/iconssettingsbase.kcfg
%{_datadir}/config.kcfg/lookandfeelsettings.kcfg
%{_datadir}/config.kcfg/stylesettings.kcfg
%{_datadir}/dbus-1/services/org.kde.KSplash.service
%{_datadir}/dbus-1/services/org.kde.Shutdown.service
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/services/org.kde.runners.baloo.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/desktop-directories/kf5-network.directory
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
%attr(755,root,root) %{_datadir}/kconf_update/delete_cursor_old_default_size.pl
%{_datadir}/kconf_update/delete_cursor_old_default_size.upd
%{_datadir}/kconf_update/icons_remove_effects.upd
%{_datadir}/kconf_update/krunnerhistory.upd
%attr(755,root,root) %{_datadir}/kconf_update/style_widgetstyle_default_breeze.pl
%{_datadir}/kconf_update/style_widgetstyle_default_breeze.upd
%dir %{_datadir}/kfontinst
%dir %{_datadir}/kfontinst/icons
%dir %{_datadir}/kfontinst/icons/hicolor
%dir %{_datadir}/kfontinst/icons/hicolor/16x16
%dir %{_datadir}/kfontinst/icons/hicolor/16x16/actions
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/fontstatus.png
%dir %{_datadir}/kfontinst/icons/hicolor/22x22
%dir %{_datadir}/kfontinst/icons/hicolor/22x22/actions
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/fontstatus.png
%dir %{_datadir}/knsrcfiles
%{_datadir}/knsrcfiles/colorschemes.knsrc
%{_datadir}/knsrcfiles/gtk_themes.knsrc
%{_datadir}/knsrcfiles/icons.knsrc
%{_datadir}/knsrcfiles/kfontinst.knsrc
%{_datadir}/knsrcfiles/lookandfeel.knsrc
%{_datadir}/knsrcfiles/plasma-themes.knsrc
%{_datadir}/knsrcfiles/plasmoids.knsrc
%{_datadir}/knsrcfiles/wallpaper.knsrc
%{_datadir}/knsrcfiles/wallpaperplugin.knsrc
%{_datadir}/knsrcfiles/xcursor.knsrc
%dir %{_datadir}/konqsidebartng
%dir %{_datadir}/konqsidebartng/virtual_folders
%dir %{_datadir}/konqsidebartng/virtual_folders/services
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%dir %{_datadir}/kpackage/kcms
%dir %{_datadir}/kpackage/kcms/kcm_colors
%dir %{_datadir}/kpackage/kcms/kcm_colors/contents
%dir %{_datadir}/kpackage/kcms/kcm_colors/contents/ui
%{_datadir}/kpackage/kcms/kcm_colors/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme/contents
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/Delegate.qml
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/Hand.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/ThemePreview.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_fonts
%dir %{_datadir}/kpackage/kcms/kcm_fonts/contents
%dir %{_datadir}/kpackage/kcms/kcm_fonts/contents/ui
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/FontWidget.qml
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui
%{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_style
%dir %{_datadir}/kpackage/kcms/kcm_style/contents
%dir %{_datadir}/kpackage/kcms/kcm_style/contents/ui
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/EffectSettingsPopup.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/GtkStylePage.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/main.qml
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%dir %{_datadir}/kxmlgui5/kfontview
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpucore.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/qlogging-categories5/klipper.categories
%{_datadir}/qlogging-categories5/libnotificationmanager.categories
%{_datadir}/qlogging-categories5/plasma-workspace.categories
%{_datadir}/sddm/themes/breeze/default-logo.svg

%{_desktopdir}/kcm_autostart.desktop
%{_desktopdir}/kcm_colors.desktop
%{_desktopdir}/kcm_cursortheme.desktop
%{_desktopdir}/kcm_fontinst.desktop
%{_desktopdir}/kcm_fonts.desktop
%{_desktopdir}/kcm_icons.desktop
%{_desktopdir}/kcm_lookandfeel.desktop
%{_desktopdir}/kcm_nightcolor.desktop
%{_desktopdir}/kcm_notifications.desktop
%{_desktopdir}/kcm_style.desktop
%{_desktopdir}/kcm_users.desktop
%{_desktopdir}/org.kde.plasmawindowed.desktop
%dir %{_datadir}/kpackage/kcms/kcm_icons
%dir %{_datadir}/kpackage/kcms/kcm_icons/contents
%dir %{_datadir}/kpackage/kcms/kcm_icons/contents/ui
%{_datadir}/kpackage/kcms/kcm_icons/contents/ui/IconSizePopup.qml
%{_datadir}/kpackage/kcms/kcm_icons/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_users
%dir %{_datadir}/kpackage/kcms/kcm_users/contents
%dir %{_datadir}/kpackage/kcms/kcm_users/contents/ui
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/ChangePassword.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/ChangeWalletPassword.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/CreateUser.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/FingerprintDialog.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/FingerprintProgressCircle.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/UserDetailsPage.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/main.qml
%{_datadir}/kxmlgui5/kfontview/kfontviewpart.rc
%{_datadir}/plasma/avatars
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/systemdialog
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/systemdialog/SystemDialog.qml
%{_datadir}/qlogging-categories5/kcmusers.categories
%{_datadir}/kconf_update/krunnerglobalshortcuts2.upd
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/knotifications5/devicenotifications.notifyrc
%{_datadir}/knsrcfiles/wallpaper-mobile.knsrc
%dir %{_datadir}/kpackage/kcms/kcm_autostart
%dir %{_datadir}/kpackage/kcms/kcm_autostart/contents
%dir %{_datadir}/kpackage/kcms/kcm_autostart/contents/ui
%{_datadir}/kpackage/kcms/kcm_autostart/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor/contents
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/LocationsFixedView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/NumberField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimeField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimingsView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_notifications
%dir %{_datadir}/kpackage/kcms/kcm_notifications/contents
%dir %{_datadir}/kpackage/kcms/kcm_notifications/contents/ui
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ApplicationConfiguration.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/PopupPositionPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ScreenPositionSelector.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/SourcesPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/main.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/VirtualKeyboard_wayland.qml
%{_datadir}/qlogging-categories5/myproject.categories
%{_datadir}/sddm/themes/breeze/components/VirtualKeyboard_wayland.qml
%{_datadir}/metainfo/org.kde.breezedark.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezetwilight.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.manage-inputmethod.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui/MoreOptions.qml
%{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui/SimpleOptions.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/animation
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/animation/RejectPasswordAnimation.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/animation/RejectPasswordPathAnimation.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/layouts
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/NoPasswordUnlock.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ThumbnailsComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/SlideshowComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ThumbnailsComponent.qml
%dir %{_datadir}/sddm/themes/breeze/components/animation
%{_datadir}/sddm/themes/breeze/components/animation/RejectPasswordAnimation.qml
%{_datadir}/sddm/themes/breeze/components/animation/RejectPasswordPathAnimation.qml
%{_desktopdir}/kcm_feedback.desktop
%{_desktopdir}/kcm_regionandlang.desktop
%{_datadir}/config.kcfg/feedbacksettings.kcfg
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/kio/servicemenus/setaswallpaper.desktop
%dir %{_datadir}/kpackage/kcms/kcm_feedback
%dir %{_datadir}/kpackage/kcms/kcm_feedback/contents
%dir %{_datadir}/kpackage/kcms/kcm_feedback/contents/ui
%{_datadir}/kpackage/kcms/kcm_feedback/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_regionandlang
%dir %{_datadir}/kpackage/kcms/kcm_regionandlang/contents
%dir %{_datadir}/kpackage/kcms/kcm_regionandlang/contents/ui
%{_datadir}/kpackage/kcms/kcm_regionandlang/contents/ui/AdvancedLanguageSelectPage.qml
%{_datadir}/kpackage/kcms/kcm_regionandlang/contents/ui/main.qml
%dir %{_datadir}/plasma/nightcolor
%{_datadir}/plasma/nightcolor/worldmap.png
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/StaticImageComponent.qml
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/StaticImageComponent.qml
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_datadir}/qlogging-categories5/kcm_regionandlang.categories
%{_desktopdir}/org.kde.plasmashell.desktop
%{_datadir}/dbus-1/services/org.kde.LogoutPrompt.service

%{_datadir}/config.kcfg/launchfeedbacksettings.kcfg
%{_datadir}/kconf_update/plasmashell-5.27-use-panel-thickness-in-default-group.upd
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/LaunchFeedbackDialog.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/Debouncer.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/PicturesSheet.qml
%dir %{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/base.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/base.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-index-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-index-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-little-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-little-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-middle-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-middle-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-ring-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-ring-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-thumb.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/left-thumb.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/palm.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/palm.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-index-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-index-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-little-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-little-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-middle-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-middle-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-ring-finger.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-ring-finger.svg.license
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-thumb.svg
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/hand-images/right-thumb.svg.license
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BlurComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BlurComponent.qml
%{zsh_compdir}/_plasmashell


%files devel
%defattr(644,root,root,755)
%{_includedir}/kworkspace5
%{_includedir}/plasma
%{_includedir}/taskmanager
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libkworkspace5.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libweather_ion.so
%{_includedir}/colorcorrect
%{_libdir}/cmake/LibColorCorrect
%{_libdir}/libcolorcorrect.so
%{_includedir}/notificationmanager
%{_libdir}/cmake/LibNotificationManager
%{_libdir}/libkfontinst.so
%{_libdir}/libkfontinstui.so
%{_libdir}/libnotificationmanager.so
%{_libdir}/libkrdb.so
