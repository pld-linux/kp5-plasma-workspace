#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kf6ver		5.102.0
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	8a837ca69e3bef6296d637bb974dfd37
Source1:	kde.pam
Patch0:		kp5-plasma-workspace-absolute-path.patch
Patch1:		kp5-plasma-workspace-scripts.patch
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt-devel >= 0.10.6
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6WaylandClient-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.22
BuildRequires:	fontconfig-devel
BuildRequires:	gpsd-devel
BuildRequires:	iso-codes
BuildRequires:	ka5-kio-extras-devel
BuildRequires:	ka5-libkexiv2-devel
BuildRequires:	kf5-plasma-wayland-protocols-devel >= 1.6
BuildRequires:	kf6-baloo-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kf6ver}
BuildRequires:	kf6-karchive-devel >= %{kf6ver}
BuildRequires:	kf6-kauth-devel >= %{kf6ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf6ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kcrash-devel >= %{kf6ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kdeclarative-devel >= %{kf6ver}
BuildRequires:	kf6-kded-devel
BuildRequires:	kf6-kdoctools-devel >= %{kf6ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf6ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kholidays-devel
BuildRequires:	kf6-ki18n-devel >= %{kf6ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf6ver}
BuildRequires:	kf6-kidletime-devel >= %{kf6ver}
BuildRequires:	kf6-kio-devel >= %{kf6ver}
BuildRequires:	kf6-kirigami-devel >= %{kf6ver}
BuildRequires:	kf6-kitemmodels-devel >= %{kf6ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf6ver}
BuildRequires:	kf6-knotifications-devel >= %{kf6ver}
BuildRequires:	kf6-knotifyconfig-devel >= %{kf6ver}
BuildRequires:	kf6-kpackage-devel >= %{kf6ver}
BuildRequires:	kf6-kpeople-devel >= %{kf6ver}
BuildRequires:	kf6-kquickcharts-devel >= %{kf6ver}
BuildRequires:	kf6-krunner-devel >= %{kf6ver}
BuildRequires:	kf6-ktexteditor-devel >= %{kf6ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf6ver}
BuildRequires:	kf6-kunitconversion-devel >= %{kf6ver}
BuildRequires:	kf6-kwallet-devel >= %{kf6ver}
BuildRequires:	kf6-networkmanager-qt-devel >= %{kf6ver}
BuildRequires:	kf6-prison-devel >= %{kf6ver}
BuildRequires:	kp5-breeze-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kpipewire-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kscreenlocker-devel >= 5.13.80
BuildRequires:	kp5-kwayland-devel >= 5.93.0
BuildRequires:	kp5-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp5-layer-shell-qt-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libkscreen-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libksysguard-devel >= %{kdeplasmaver}
BuildRequires:	kp5-plasma-activities-devel >= 5.93.0
BuildRequires:	kp5-plasma-activities-stats-devel >= 5.93.0
BuildRequires:	kp5-plasma5support-devel >= 5.93.0
BuildRequires:	kuserfeedback-devel
BuildRequires:	libdrm-devel
BuildRequires:	libicu-devel
BuildRequires:	libqalculate-devel > 2.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel >= 4.6.60
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	polkit-qt6-1-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.31
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

%define		qt6dir		%{_libdir}/qt6

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
sed -i -e 's|/usr/bin/env python3|%{_bindir}/python3|' $RPM_BUILD_ROOT%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
/etc/xdg/autostart/gmenudbusmenuproxy.desktop
/etc/xdg/autostart/org.kde.plasmashell.desktop
/etc/xdg/autostart/xembedsniproxy.desktop
/etc/xdg/menus/plasma-applications.menu
/etc/xdg/plasmanotifyrc
/etc/xdg/taskmanagerrulesrc
%attr(755,root,root) %{_bindir}/gmenudbusmenuproxy
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kde-systemd-start-condition
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
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
%attr(755,root,root) %{_bindir}/plasma-localegen-helper
%attr(755,root,root) %{_bindir}/plasma-shutdown
%attr(755,root,root) %{_bindir}/plasma_session
%attr(755,root,root) %{_bindir}/plasma_waitforname
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/startplasma-wayland
%attr(755,root,root) %{_bindir}/startplasma-x11
%attr(755,root,root) %{_bindir}/xembedsniproxy
%{systemduserunitdir}/plasma-baloorunner.service
%{systemduserunitdir}/plasma-core.target
%{systemduserunitdir}/plasma-gmenudbusmenuproxy.service
%{systemduserunitdir}/plasma-kcminit-phase1.service
%{systemduserunitdir}/plasma-kcminit.service
%{systemduserunitdir}/plasma-krunner.service
%{systemduserunitdir}/plasma-ksmserver.service
%{systemduserunitdir}/plasma-ksplash-ready.service
%{systemduserunitdir}/plasma-ksplash.service
%{systemduserunitdir}/plasma-plasmashell.service
%{systemduserunitdir}/plasma-restoresession.service
%{systemduserunitdir}/plasma-workspace-wayland.target
%{systemduserunitdir}/plasma-workspace-x11.target
%{systemduserunitdir}/plasma-workspace.target
%{systemduserunitdir}/plasma-xembedsniproxy.service
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%ghost %{_libdir}/libcolorcorrect.so.5
%attr(755,root,root) %{_libdir}/libcolorcorrect.so.*.*
%ghost %{_libdir}/libkfontinst.so.5
%attr(755,root,root) %{_libdir}/libkfontinst.so.*.*
%ghost %{_libdir}/libkfontinstui.so.5
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*.*
%ghost %{_libdir}/libkmpris.so.5
%attr(755,root,root) %{_libdir}/libkmpris.so.*.*
%ghost %{_libdir}/libkworkspace6.so.5
%attr(755,root,root) %{_libdir}/libkworkspace6.so.*.*
%ghost %{_libdir}/libnotificationmanager.so.1
%attr(755,root,root) %{_libdir}/libnotificationmanager.so.*.*
%ghost %{_libdir}/libplasma-geolocation-interface.so.5
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so.*.*
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*
%ghost %{_libdir}/libtaskmanager.so.6
%ghost %{_libdir}/libweather_ion.so.7
%attr(755,root,root) %{_libdir}/libweather_ion.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/appmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/colorcorrectlocationupdater.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/desktopnotifier.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/devicenotifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/freespacenotifier.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/ktimezoned.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/mprisservice.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/plasma-session-shortcuts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/plasma_accentcolor_service.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/soliduiserver.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/statusnotifierwatcher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/wallpaperfileitemaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/applications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/desktop.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_fonts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/calculator.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/helprunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_kill.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_kill.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_powerdevil.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_services.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_sessions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_shell.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/locations.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_layouttemplate.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/wallpaper_images.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/kfontviewpart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/fontthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/phonon_platform/kde.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.appmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.calendar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.icon.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.panelspacer.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.private.systemtray.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.systemmonitor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.systemtray.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.applauncher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.contextmenu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.paste.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/org.kde.switchdesktop.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/switchactivity.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/containmentactions/switchwindow.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcminit/kcm_fonts_init.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcminit/kcm_style_init.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_colors.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_icons.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_nightcolor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_soundtheme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_style.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_users.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_wallpaper.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_activities.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_applicationjobs.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_apps.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_bbcukmet.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_clipboard.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_devicenotifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_dict.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_dwd.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_envcan.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_executable.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_favicons.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_filebrowser.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_geolocation.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_hotplug.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_keystate.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_mouse.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_noaa.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_notifications.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_packagekit.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_places.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_powermanagement.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_statusnotifieritem.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_time.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_weather.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/dataengine/plasma_engine_wettercom.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/geolocationprovider/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma5support/geolocationprovider/plasma-geolocation-ip.so
%{_libdir}/qt6/plugins/plasmacalendarplugins/holidays/HolidaysConfig.qml
%attr(755,root,root) %{_libdir}/qt6/plugins/plasmacalendarplugins/holidaysevents.so
%{_libdir}/qt6/qml/org/kde/breeze/components/ActionButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/Battery.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/Clock.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/RejectPasswordAnimation.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/RejectPasswordPathAnimation.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/SessionManagementScreen.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/UserDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/UserList.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboard.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboardLoader.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/VirtualKeyboard_wayland.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/WallpaperFader.qml
%{_libdir}/qt6/qml/org/kde/breeze/components/components.qmltypes
%{_libdir}/qt6/qml/org/kde/breeze/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/breeze/components/libcomponents.so
%{_libdir}/qt6/qml/org/kde/breeze/components/qmldir
%{_libdir}/qt6/qml/org/kde/colorcorrect/colorcorrect.qmltypes
%{_libdir}/qt6/qml/org/kde/colorcorrect/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/colorcorrect/libcolorcorrectplugin.so
%{_libdir}/qt6/qml/org/kde/colorcorrect/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/holidayeventshelperplugin/libholidayeventshelperplugin.so
%{_libdir}/qt6/qml/org/kde/holidayeventshelperplugin/qmldir
%{_libdir}/qt6/qml/org/kde/notificationmanager/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/notificationmanager/libnotificationmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/notificationmanager/notificationmanager.qmltypes
%{_libdir}/qt6/qml/org/kde/notificationmanager/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/lookandfeel/liblookandfeelqmlplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/lookandfeel/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/appmenu/libappmenuplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/appmenu/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/brightnesscontrolplugin/brightnesscontrolplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/brightnesscontrolplugin/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/brightnesscontrolplugin/libbrightnesscontrolplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/brightnesscontrolplugin/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/BasicAppletContainer.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/ConfigOverlayWithHandles.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/PlaceHolder.qml
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/libcontainmentlayoutmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/private/BasicResizeHandle.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/containmentlayoutmanager/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/digitalclock/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/kicker/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mediacontroller/libmediacontrollerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mediacontroller/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/kmpris.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mpris/libkmprisplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/sessions/libsessionsprivateplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/sessions/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/shell/libplasmashellprivateplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/shell/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/image/libplasma_wallpaper_imageplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/wallpapers/image/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/DayDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/DaysCalendar.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/InfiniteList.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/MonthMenu.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/MonthView.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/MonthViewHeader.qml
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/libcalendarplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/calendar/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/BadgeOverlay.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/BatteryIcon.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/KeyboardLayoutSwitcher.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/components/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/SystemDialog.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/examples/test.qml
%{_libdir}/qt6/qml/org/kde/plasma/workspace/dialogs/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/keyboardlayout/libkeyboardlayoutplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/keyboardlayout/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/libtrianglemousefilterplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/workspace/trianglemousefilter/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt6/qml/org/kde/taskmanager/qmldir
%attr(755,root,root) %{_prefix}/libexec/baloorunner
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst_helper
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/fontinst_x11
%attr(755,root,root) %{_prefix}/libexec/kfontprint
%attr(755,root,root) %{_prefix}/libexec/ksmserver-logout-greeter
%attr(755,root,root) %{_prefix}/libexec/plasma-changeicons
%attr(755,root,root) %{_prefix}/libexec/plasma-dbus-run-session-if-needed
%attr(755,root,root) %{_prefix}/libexec/plasma-sourceenv.sh

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/kcm_autostart.desktop
%{_desktopdir}/kcm_colors.desktop
%{_desktopdir}/kcm_cursortheme.desktop
%{_desktopdir}/kcm_desktoptheme.desktop
%{_desktopdir}/kcm_fontinst.desktop
%{_desktopdir}/kcm_fonts.desktop
%{_desktopdir}/kcm_icons.desktop
%{_desktopdir}/kcm_lookandfeel.desktop
%{_desktopdir}/kcm_nightcolor.desktop
%{_desktopdir}/kcm_notifications.desktop
%{_desktopdir}/kcm_regionandlang.desktop
%{_desktopdir}/kcm_soundtheme.desktop
%{_desktopdir}/kcm_style.desktop
%{_desktopdir}/kcm_users.desktop
%{_desktopdir}/kcm_wallpaper.desktop
%{_desktopdir}/org.kde.kcolorschemeeditor.desktop
%{_desktopdir}/org.kde.kfontview.desktop
%{_desktopdir}/org.kde.plasmashell.desktop
%{_desktopdir}/org.kde.plasmawindowed.desktop
%{_datadir}/config.kcfg/colorssettings.kcfg
%{_datadir}/config.kcfg/cursorthemesettings.kcfg
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
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
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
%attr(755,root,root) %{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.upd
%{_datadir}/kconf_update/plasma6.0-remove-dpi-settings.upd
%{_datadir}/kconf_update/plasma6.0-remove-old-shortcuts.upd
%{_datadir}/kconf_update/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels.upd
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/fontstatus.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-disable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/font-enable.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/fontstatus.png
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/kio/servicemenus/installfont.desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/knotifications6/devicenotifications.notifyrc
%{_datadir}/knotifications6/freespacenotifier.notifyrc
%{_datadir}/knotifications6/phonon.notifyrc
%{_datadir}/knsrcfiles/colorschemes.knsrc
%{_datadir}/knsrcfiles/gtk_themes.knsrc
%{_datadir}/knsrcfiles/icons.knsrc
%{_datadir}/knsrcfiles/kfontinst.knsrc
%{_datadir}/knsrcfiles/lookandfeel.knsrc
%{_datadir}/knsrcfiles/plasma-themes.knsrc
%{_datadir}/knsrcfiles/plasmoids.knsrc
%{_datadir}/knsrcfiles/wallpaper-mobile.knsrc
%{_datadir}/knsrcfiles/wallpaper.knsrc
%{_datadir}/knsrcfiles/wallpaperplugin.knsrc
%{_datadir}/knsrcfiles/xcursor.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kstyle/themes/qtcde.themerc
%{_datadir}/kstyle/themes/qtcleanlooks.themerc
%{_datadir}/kstyle/themes/qtgtk.themerc
%{_datadir}/kstyle/themes/qtmotif.themerc
%{_datadir}/kstyle/themes/qtplastique.themerc
%{_datadir}/kstyle/themes/qtwindows.themerc
%{_datadir}/kxmlgui5/kfontview/kfontviewpart.rc
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_datadir}/metainfo/org.kde.breeze.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezedark.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.breezetwilight.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.color.appdata.xml
%{_datadir}/metainfo/org.kde.image.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activitybar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.analogclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.appmenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.brightness.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.calendar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.cameraindicator.appdata.xml
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
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockOsd.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockScreen.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/LockScreenUi.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/MainBlock.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/MediaControls.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/NoPasswordUnlock.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.xml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/Logout.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/LogoutButton.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/timer.js
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/Osd.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/osd/OsdItem.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/lockscreen.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/loginmanager.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/runcommand.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/splash.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/userswitcher.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/previews/windowdecoration.png
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/Splash.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/busywidget.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/kde.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/plasma.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/systemdialog/SystemDialog.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/metadata.json
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.json
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/Hand.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/MenuDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BatteryItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/InhibitionHint.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PopupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PowerManagementItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PowerProfileItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/logic.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/BrightnessItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/NightColorItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/PopupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/logic.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images/mini-calendar.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/BarcodePage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ClipboardItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ClipboardPage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/DelegateToolButtons.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/EditPage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ImageItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/TextItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/UrlItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/DeviceItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/CalendarView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/DigitalClock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/MonthMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/Tooltip.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configCalendar.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configTimeZones.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/data.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/AlbumArtStackView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/DraggableDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/DraggableFileArea.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/EditContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/JobDetails.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/JobItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationHeader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationPopup.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationReplyField.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/SelectableLabel.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/ThumbnailStrip.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/Globals.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/PulseAudio.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/qmldir
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/applet/CompactApplet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigEntries.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/CurrentItemHighLight.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpanderArrow.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/HiddenItemsView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/PlasmoidPopupsContainer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/SystemTrayState.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/AbstractItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/ItemLoader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PlasmoidItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PulseAnimation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/StatusNotifierItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config/faceproperties
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigSensors.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/FaceDetails.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.color/contents/config/main.xml
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.color/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.color/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.image/contents/config/main.xml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/AddFileDialog.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/ThumbnailsComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/BlurComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/mediacomponent/StaticImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.image/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config/main.xml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/AddFileDialog.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ImageStackView.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/SlideshowComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/ThumbnailsComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/AnimatedImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BaseMediaComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/BlurComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/mediacomponent/StaticImageComponent.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/metadata.json
%{_datadir}/plasma5support/services/activities.operations
%{_datadir}/plasma5support/services/applicationjobs.operations
%{_datadir}/plasma5support/services/apps.operations
%{_datadir}/plasma5support/services/hotplug.operations
%{_datadir}/plasma5support/services/modifierkeystate.operations
%{_datadir}/plasma5support/services/notifications.operations
%{_datadir}/plasma5support/services/org.kde.places.operations
%{_datadir}/plasma5support/services/org.kde.plasma.clipboard.operations
%{_datadir}/plasma5support/services/packagekit.operations
%{_datadir}/plasma5support/services/powermanagementservice.operations
%{_datadir}/plasma5support/services/soliddevice.operations
%{_datadir}/plasma5support/services/statusnotifieritem.operations
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_datadir}/qlogging-categories6/kcm_regionandlang.categories
%{_datadir}/qlogging-categories6/kcmusers.categories
%{_datadir}/qlogging-categories6/klipper.categories
%{_datadir}/qlogging-categories6/libnotificationmanager.categories
%{_datadir}/qlogging-categories6/myproject.categories
%{_datadir}/qlogging-categories6/plasma-workspace.categories
%{_datadir}/sddm/themes/breeze/Background.qml
%{_datadir}/sddm/themes/breeze/KeyboardButton.qml
%{_datadir}/sddm/themes/breeze/Login.qml
%{_datadir}/sddm/themes/breeze/Main.qml
%{_datadir}/sddm/themes/breeze/SessionButton.qml
%{_datadir}/sddm/themes/breeze/default-logo.svg
%{_datadir}/sddm/themes/breeze/faces/.face.icon
%{_datadir}/sddm/themes/breeze/metadata.desktop
%{_datadir}/sddm/themes/breeze/preview.png
%{_datadir}/sddm/themes/breeze/theme.conf
%{_datadir}/solid/actions/openWithFileManager.desktop
%{_datadir}/wayland-sessions/plasma.desktop
%{_datadir}/xsessions/plasmax11.desktop
%{zsh_compdir}/_krunner
%{zsh_compdir}/_plasmashell

%files devel
%defattr(644,root,root,755)
%{_includedir}/krdb
%{_includedir}/kworkspace6
%{_includedir}/plasma5support/weather
%{_includedir}/plasma
%{_includedir}/taskmanager
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/libplasma-geolocation-interface.so
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
%{_libdir}/libkmpris.so
%{_libdir}/libkworkspace6.so
