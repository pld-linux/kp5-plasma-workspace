# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	5.22.3
%define		qtver		5.9.0
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp5-%{kpname}
Version:	5.22.3
Release:	3
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	b058dfeaadc25efe97412dc174b17a4a
Source1:	kde.pam
Patch0:		kp5-plasma-workspace-absolute-path.patch
Patch1:		kp5-plasma-workspace-scripts.patch
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gpsd-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.50
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kded-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesu-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kjsembed-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-ktexteditor-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kxmlrpcclient-devel
BuildRequires:	kf5-networkmanager-qt-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kf5-prison-devel
BuildRequires:	kp5-kscreenlocker-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libkscreen-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libksysguard-devel >= %{kdeplasmaver}
BuildRequires:	libdbusmenu-qt5-devel
BuildRequires:	libqalculate-devel >= 2.8.2
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Workspace.

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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -p -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kde

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
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
%{_desktopdir}/org.kde.systemmonitor.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/WallpaperFader.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/lockscreen/config.xml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/logout/timer.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/logic.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/DelegateToolButtons.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ImageItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/TextItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/UrlItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/data.js
%{_datadir}/sddm/themes/breeze/components/WallpaperFader.qml
%dir %{_datadir}/sddm/themes/breeze/faces
%{_datadir}/sddm/themes/breeze/faces/.face.icon
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
%{_libdir}/libkdeinit5_kcminit.so
%{_libdir}/libkdeinit5_kcminit_startup.so
%{_libdir}/libkworkspace5.so.5
%{_libdir}/libkworkspace5.so.5.*.*
%{_libdir}/libplasma-geolocation-interface.so.5
%{_libdir}/libplasma-geolocation-interface.so.5.*.*
%{_libdir}/libtaskmanager.so.5.*.*
%{_libdir}/libtaskmanager.so.6
%{_libdir}/libweather_ion.so.7
%{_libdir}/libweather_ion.so.7.0.0
%{_libdir}/qt5/plugins/kcm_krunner_kill.so
%{_libdir}/qt5/plugins/kf5/kded/appmenu.so
%{_libdir}/qt5/plugins/kf5/kded/desktopnotifier.so
%{_libdir}/qt5/plugins/kf5/kded/freespacenotifier.so
%{_libdir}/qt5/plugins/kf5/kded/ksysguard.so
%{_libdir}/qt5/plugins/kf5/kded/ktimezoned.so
%{_libdir}/qt5/plugins/kf5/kded/soliduiserver.so
%{_libdir}/qt5/plugins/kf5/kded/statusnotifierwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/desktop.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_layoutemplate.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_lookandfeel.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_plasmashell.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaper.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaperimages.so
%dir %{_libdir}/qt5/plugins/phonon_platform
%{_libdir}/qt5/plugins/phonon_platform/kde.so
%{_libdir}/qt5/plugins/plasma-geolocation-gps.so
%{_libdir}/qt5/plugins/plasma-geolocation-ip.so
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/applets
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.private.systemtray.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.systemtray.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_appmenu.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_calendar.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_icon.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_notifications.so
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
%{_desktopdir}/org.kde.klipper.desktop
%{_desktopdir}/plasma-windowed.desktop
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
%{_datadir}/kdevappwizard/templates/ion-dataengine.tar.bz2
%dir %{_datadir}/kio_desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/knotifications5/freespacenotifier.notifyrc
%{_datadir}/knotifications5/phonon.notifyrc
%{_datadir}/kservices5/applications.protocol
%{_datadir}/kservices5/desktop.protocol
%{_datadir}/kservices5/ion-bbcukmet.desktop
%{_datadir}/kservices5/ion-envcan.desktop
%{_datadir}/kservices5/ion-noaa.desktop
%{_datadir}/kservices5/ion-wettercom.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.activitybar.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.analogclock.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.appmenu.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.battery.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.calendar.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.clipboard.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.devicenotifier.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.digitalclock.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.icon.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.lock_logout.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.mediacontroller.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.notifications.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.panelspacer.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.private.systemtray.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.cpu.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.diskactivity.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.diskusage.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.memory.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.net.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemtray.desktop
%{_datadir}/kservices5/plasma-geolocation-gps.desktop
%{_datadir}/kservices5/plasma-geolocation-ip.desktop
%{_datadir}/kservices5/plasma-lookandfeel-org.kde.breeze.desktop.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.color.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.image.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.slideshow.desktop
%{_datadir}/kservices5/programs.protocol
%{_datadir}/kservicetypes5/phononbackend.desktop
%{_datadir}/kservicetypes5/plasma-geolocationprovider.desktop
%{_datadir}/kservicetypes5/plasma-layouttemplate.desktop
%dir %{_datadir}/ksplash
%dir %{_datadir}/ksplash/Themes
%dir %{_datadir}/ksplash/Themes/Classic
%dir %{_datadir}/ksplash/Themes/Classic/images
%{_datadir}/ksplash/Themes/Classic/FadeIn.qml
%{_datadir}/ksplash/Themes/Classic/Preview.png
%{_datadir}/ksplash/Themes/Classic/Theme.rc
%{_datadir}/ksplash/Themes/Classic/images/background.png
%{_datadir}/ksplash/Themes/Classic/images/icon1.png
%{_datadir}/ksplash/Themes/Classic/images/icon2.png
%{_datadir}/ksplash/Themes/Classic/images/icon3.png
%{_datadir}/ksplash/Themes/Classic/images/icon4.png
%{_datadir}/ksplash/Themes/Classic/images/icon5.png
%{_datadir}/ksplash/Themes/Classic/images/rectangle.png
%{_datadir}/ksplash/Themes/Classic/main.qml
%dir %{_datadir}/ksplash/Themes/Minimalistic
%dir %{_datadir}/ksplash/Themes/Minimalistic/images
%{_datadir}/ksplash/Themes/Minimalistic/Preview.png
%{_datadir}/ksplash/Themes/Minimalistic/Theme.rc
%{_datadir}/ksplash/Themes/Minimalistic/images/kdegear.png
%{_datadir}/ksplash/Themes/Minimalistic/images/kdeletter.png
%{_datadir}/ksplash/Themes/Minimalistic/images/kdelogo-contrast.png
%{_datadir}/ksplash/Themes/Minimalistic/images/kdelogo.png
%{_datadir}/ksplash/Themes/Minimalistic/images/kdemask.png
%{_datadir}/ksplash/Themes/Minimalistic/main.qml
%dir %{_datadir}/ksplash/Themes/None
%{_datadir}/ksplash/Themes/None/Theme.rc
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
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/runcommand
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/runcommand/RunCommand.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/Splash.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/busywidget.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/kde.svgz
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/plasma.svgz
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowdecoration
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowdecoration/WindowDecoration.qml
%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowswitcher
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/windowswitcher/WindowSwitcher.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/metadata.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/Hand.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/analogclock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BadgeOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BatteryItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BrightnessItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/InhibitionHint.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PopupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PowerManagementItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/batterymonitor.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/BarcodePage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ClipboardItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/ClipboardPage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/contents/ui/clipboard.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/CalendarView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/DigitalClock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/MonthMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/Tooltip.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configCalendar.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/configTimeZones.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/ui/lockout.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/applet
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/applet/CompactApplet.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigEntries.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/CurrentItemHighLight.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpandedRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/ExpanderArrow.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/HiddenItemsView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/PlasmoidPopupsContainer.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/AbstractItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PlasmoidItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/PulseAnimation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/StatusNotifierItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray/metadata.json
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
%{_datadir}/plasma/wallpapers/org.kde.color/metadata.desktop
%{_datadir}/plasma/wallpapers/org.kde.color/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.color/plasma-wallpaper-color.desktop
%dir %{_datadir}/plasma/wallpapers/org.kde.image
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/config
%{_datadir}/plasma/wallpapers/org.kde.image/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.image/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.image/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.image/metadata.desktop
%{_datadir}/plasma/wallpapers/org.kde.image/metadata.json
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/config/main.xml
%dir %{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/contents/ui/main.qml
%{_datadir}/plasma/wallpapers/org.kde.slideshow/metadata.desktop
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
/etc/xdg/autostart/org.kde.plasmashell.desktop
%{_desktopdir}/org.kde.plasmashell.desktop
%dir %{_libdir}/qt5/plugins/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_translations.so
%{_datadir}/dbus-1/services/org.kde.LogoutPrompt.service
%dir %{_datadir}/kpackage/kcms
%dir %{_datadir}/kpackage/kcms/kcm_translations
%dir %{_datadir}/kpackage/kcms/kcm_translations/contents
%dir %{_datadir}/kpackage/kcms/kcm_translations/contents/ui
%{_datadir}/kpackage/kcms/kcm_translations/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_translations/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_translations/metadata.json
%{_datadir}/kservices5/kcm_translations.desktop
/etc/xdg/plasmanotifyrc
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kde-systemd-start-condition
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/krdb
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
%{systemduserunitdir}/plasma-workspace@.target
%{systemduserunitdir}/plasma-xembedsniproxy.service
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerglobalshortcuts
%attr(755,root,root) %{_libdir}/kconf_update_bin/krunnerhistory
%ghost %{_libdir}/libkfontinst.so.5
%{_libdir}/libkfontinst.so.5.*.*
%ghost %{_libdir}/libkfontinstui.so.5
%{_libdir}/libkfontinstui.so.5.*.*
%ghost %{_libdir}/libnotificationmanager.so.1
%{_libdir}/libnotificationmanager.so.5.*.*
%{_libdir}/qt5/plugins/fontthumbnail.so
%{_libdir}/qt5/plugins/kcms/kcm_colors.so
%{_libdir}/qt5/plugins/kcms/kcm_cursortheme.so
%{_libdir}/qt5/plugins/kcms/kcm_desktoptheme.so
%{_libdir}/qt5/plugins/kcms/kcm_fonts.so
%{_libdir}/qt5/plugins/kcms/kcm_icons.so
%{_libdir}/qt5/plugins/kcms/kcm_lookandfeel.so
%{_libdir}/qt5/plugins/kcms/kcm_style.so
%{_libdir}/qt5/plugins/kf5/kio/applications.so
%{_libdir}/qt5/plugins/kf5/krunner/krunner_appstream.so
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
%{_libdir}/qt5/plugins/kfontviewpart.so
%{_libdir}/qt5/plugins/kio_fonts.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.panelspacer.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_systemmonitor.so
%dir %{_libdir}/qt5/plugins/plasma/containmentactions
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_applauncher.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_contextmenu.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_paste.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchdesktop.so
%{_libdir}/qt5/plugins/plasma/containmentactions/plasma_containmentactions_switchwindow.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchactivity.so
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
%attr(755,root,root) %{_prefix}/libexec/startplasma-waylandsession
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
%dir %{_datadir}/kdisplay
%dir %{_datadir}/kdisplay/app-defaults
%{_datadir}/kdisplay/app-defaults/AAAAAAGeneral.ad
%{_datadir}/kdisplay/app-defaults/AAAMotif.ad
%{_datadir}/kdisplay/app-defaults/AAATk.ad
%{_datadir}/kdisplay/app-defaults/AAAXaw.ad
%{_datadir}/kdisplay/app-defaults/AcroRead.ad
%{_datadir}/kdisplay/app-defaults/Editres.ad
%{_datadir}/kdisplay/app-defaults/Emacs.ad
%{_datadir}/kdisplay/app-defaults/GV.ad
%{_datadir}/kdisplay/app-defaults/ML.ad
%{_datadir}/kdisplay/app-defaults/Nedit.ad
%{_datadir}/kdisplay/app-defaults/Netscape.ad
%{_datadir}/kdisplay/app-defaults/RVPlayer.ad
%{_datadir}/kdisplay/app-defaults/WPerfect.ad
%{_datadir}/kdisplay/app-defaults/XCalc.ad
%{_datadir}/kdisplay/app-defaults/XOsview.ad
%{_datadir}/kdisplay/app-defaults/XTerm.ad
%{_datadir}/kdisplay/app-defaults/XV.ad
%{_datadir}/kdisplay/app-defaults/Xawtv.ad
%{_datadir}/kdisplay/app-defaults/Xdvi.ad
%{_datadir}/kdisplay/app-defaults/Xpdf.ad
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
%dir %{_datadir}/kpackage/kcms/kcm5_icons
%{_datadir}/kpackage/kcms/kcm5_icons/metadata.desktop
%{_datadir}/kpackage/kcms/kcm5_icons/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm5_icons/contents
%dir %{_datadir}/kpackage/kcms/kcm5_icons/contents/ui
%{_datadir}/kpackage/kcms/kcm5_icons/contents/ui/IconSizePopup.qml
%{_datadir}/kpackage/kcms/kcm5_icons/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_colors
%{_datadir}/kpackage/kcms/kcm_colors/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_colors/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_colors/contents
%dir %{_datadir}/kpackage/kcms/kcm_colors/contents/ui
%{_datadir}/kpackage/kcms/kcm_colors/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme
%{_datadir}/kpackage/kcms/kcm_cursortheme/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_cursortheme/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme/contents
%dir %{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/Delegate.qml
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme
%{_datadir}/kpackage/kcms/kcm_desktoptheme/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_desktoptheme/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/Hand.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/ThemePreview.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_fonts
%{_datadir}/kpackage/kcms/kcm_fonts/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_fonts/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_fonts/contents
%dir %{_datadir}/kpackage/kcms/kcm_fonts/contents/ui
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/FontWidget.qml
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel
%{_datadir}/kpackage/kcms/kcm_lookandfeel/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_lookandfeel/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui
%{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_style
%{_datadir}/kpackage/kcms/kcm_style/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_style/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_style/contents
%dir %{_datadir}/kpackage/kcms/kcm_style/contents/ui
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/EffectSettingsPopup.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/GtkStylePage.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/main.qml
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/fontinst.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kservices5/fontthumbnail.desktop
%{_datadir}/kservices5/kcm_colors.desktop
%{_datadir}/kservices5/kcm_cursortheme.desktop
%{_datadir}/kservices5/kcm_desktoptheme.desktop
%{_datadir}/kservices5/kcm_fonts.desktop
%{_datadir}/kservices5/kcm_icons.desktop
%{_datadir}/kservices5/kcm_lookandfeel.desktop
%{_datadir}/kservices5/kcm_style.desktop
%{_datadir}/kservices5/kfontviewpart.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.cpucore.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.systemmonitor.desktop
%{_datadir}/kservices5/plasma-containmentactions-switchactivity.desktop
%{_datadir}/kservices5/plasma-dataengine-activities.desktop
%{_datadir}/kservices5/plasma-dataengine-applicationjobs.desktop
%{_datadir}/kservices5/plasma-dataengine-apps.desktop
%{_datadir}/kservices5/plasma-dataengine-clipboard.desktop
%{_datadir}/kservices5/plasma-dataengine-devicenotifications.desktop
%{_datadir}/kservices5/plasma-dataengine-dict.desktop
%{_datadir}/kservices5/plasma-dataengine-executable.desktop
%{_datadir}/kservices5/plasma-dataengine-favicons.desktop
%{_datadir}/kservices5/plasma-dataengine-filebrowser.desktop
%{_datadir}/kservices5/plasma-dataengine-geolocation.desktop
%{_datadir}/kservices5/plasma-dataengine-hotplug.desktop
%{_datadir}/kservices5/plasma-dataengine-keystate.desktop
%{_datadir}/kservices5/plasma-dataengine-mouse.desktop
%{_datadir}/kservices5/plasma-dataengine-mpris2.desktop
%{_datadir}/kservices5/plasma-dataengine-notifications.desktop
%{_datadir}/kservices5/plasma-dataengine-packagekit.desktop
%{_datadir}/kservices5/plasma-dataengine-places.desktop
%{_datadir}/kservices5/plasma-dataengine-powermanagement.desktop
%{_datadir}/kservices5/plasma-dataengine-soliddevice.desktop
%{_datadir}/kservices5/plasma-dataengine-statusnotifieritem.desktop
%{_datadir}/kservices5/plasma-dataengine-systemmonitor.desktop
%{_datadir}/kservices5/plasma-dataengine-time.desktop
%{_datadir}/kservices5/plasma-dataengine-weather.desktop
%{_datadir}/kservices5/plasma-runner-kill_config.desktop
%{_datadir}/kservices5/plasma-runner-webshortcuts_config.desktop
%dir %{_datadir}/kxmlgui5/kfontinst
%{_datadir}/kxmlgui5/kfontinst/kfontviewpart.rc
%dir %{_datadir}/kxmlgui5/kfontview
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.systemmonitor.cpucore.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images/mini-calendar.svgz
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/main.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/DeviceItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/devicenotifier.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/main.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/Globals.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/PulseAudio.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/global/qmldir
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/SystemTrayState.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/contents/ui/items/ItemLoader.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config/faceproperties
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/FullRepresentation.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/ConfigSensors.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/config/FaceDetails.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor/contents/ui/main.qml
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/qlogging-categories5/klipper.categories
%{_datadir}/qlogging-categories5/libnotificationmanager.categories
%{_datadir}/qlogging-categories5/plasma-workspace.categories
%{_datadir}/sddm/themes/breeze/BreezeMenuStyle.qml
%{_datadir}/sddm/themes/breeze/default-logo.svg

%attr(755,root,root) %{_bindir}/plasma-apply-colorscheme
%attr(755,root,root) %{_bindir}/plasma-apply-cursortheme
%attr(755,root,root) %{_bindir}/plasma-apply-desktoptheme
%attr(755,root,root) %{_bindir}/plasma-apply-lookandfeel
%attr(755,root,root) %{_bindir}/plasma-apply-wallpaperimage
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_formats.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_nightcolor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/calculator.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/locations.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace/components/KeyboardLayoutSwitcher.qml
%{_datadir}/kconf_update/krunnerglobalshortcuts2.upd
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/knotifications5/devicenotifications.notifyrc
%{_datadir}/knsrcfiles/wallpaper-mobile.knsrc
%dir %{_datadir}/kpackage/kcms/kcm_autostart
%dir %{_datadir}/kpackage/kcms/kcm_autostart/contents/ui
%{_datadir}/kpackage/kcms/kcm_autostart/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_autostart/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_autostart/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/LocationsFixedView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/NumberField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimeField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimingsView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_nightcolor/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_notifications
%dir %{_datadir}/kpackage/kcms/kcm_notifications/contents/ui
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ApplicationConfiguration.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/PopupPositionPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ScreenPositionSelector.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/SourcesPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_notifications/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_notifications/metadata.json
%{_datadir}/kservices5/autostart.desktop
%{_datadir}/kservices5/formats.desktop
%{_datadir}/kservices5/kcm_nightcolor.desktop
%{_datadir}/kservices5/kcm_notifications.desktop
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/VirtualKeyboard_wayland.qml
%{_datadir}/qlogging-categories5/kcm_translations.categories
%{_datadir}/qlogging-categories5/myproject.categories
%{_datadir}/sddm/themes/breeze/components/VirtualKeyboard_wayland.qml

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
