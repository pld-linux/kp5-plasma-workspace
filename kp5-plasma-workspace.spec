# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	582ef2fb97a9020c09d86118c04f3b0a
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
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
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
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -p -D %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/kde

%find_lang %{kpname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde
/etc/xdg/autostart/gmenudbusmenuproxy.desktop
/etc/xdg/klipper.categories
/etc/xdg/plasma-workspace.categories
%attr(755,root,root) %{_bindir}/gmenudbusmenuproxy
%attr(755,root,root) %ghost %{_libdir}/libcolorcorrect.so.5
%attr(755,root,root) %{_libdir}/libcolorcorrect.so.5.*.*
%{_libdir}/qt5/plugins/kf5/kded/colorcorrectlocationupdater.so
%{_libdir}/qt5/plugins/krunner_appstream.so
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
%attr(755,root,root) %{_prefix}/libexec/ksyncdbusenv
%attr(755,root,root) %{_prefix}/libexec/startplasma
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/uiproperties.js
%{_datadir}/sddm/themes/breeze/components/WallpaperFader.qml
%dir %{_datadir}/sddm/themes/breeze/faces
%{_datadir}/sddm/themes/breeze/faces/.face.icon
/etc/xdg/autostart/klipper.desktop
/etc/xdg/autostart/krunner.desktop
#/etc/xdg/autostart/plasmashell.desktop
/etc/xdg/autostart/xembedsniproxy.desktop
/etc/xdg/kuiserver.categories
/etc/xdg/plasmoids.knsrc
/etc/xdg/taskmanagerrulesrc
/etc/xdg/wallpaper.knsrc
%attr(755,root,root) %{_bindir}/kcheckrunning
%attr(755,root,root) %{_bindir}/kcminit
%attr(755,root,root) %{_bindir}/kcminit_startup
%attr(755,root,root) %{_bindir}/kdostartupconfig5
%attr(755,root,root) %{_bindir}/klipper
%attr(755,root,root) %{_bindir}/krunner
%attr(755,root,root) %{_bindir}/ksmserver
%attr(755,root,root) %{_bindir}/ksplashqml
%attr(755,root,root) %{_bindir}/kstartupconfig5
%attr(755,root,root) %{_bindir}/kuiserver5
%attr(755,root,root) %{_bindir}/plasma_waitforname
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/startplasmacompositor
%attr(755,root,root) %{_bindir}/systemmonitor
%attr(755,root,root) %{_bindir}/xembedsniproxy
#%%{_libdir}/drkonqi
%{_libdir}/kconf_update_bin/krunnerplugins
#%%{_libdir}/ksmserver-logout-greeter
#%%{_libdir}/ksmserver-switchuser-greeter
#%%{_libdir}/ksyncdbusenv
%{_libdir}/libkdeinit5_kcminit.so
%{_libdir}/libkdeinit5_kcminit_startup.so
%{_libdir}/libkdeinit5_klipper.so
%{_libdir}/libkdeinit5_ksmserver.so
%{_libdir}/libkdeinit5_kuiserver5.so
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
#%%{_libdir}/qt5/plugins/kf5/kded/solidautoeject.so
%{_libdir}/qt5/plugins/kf5/kded/soliduiserver.so
%{_libdir}/qt5/plugins/kf5/kded/statusnotifierwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/desktop.so
%{_libdir}/qt5/plugins/kio_applications.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_layoutemplate.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_lookandfeel.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_plasmashell.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaper.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaperimages.so
%{_libdir}/qt5/plugins/krunner_activities.so
#%%{_libdir}/qt5/plugins/krunner_baloosearchrunner.so
%{_libdir}/qt5/plugins/krunner_bookmarksrunner.so
%{_libdir}/qt5/plugins/krunner_calculatorrunner.so
%{_libdir}/qt5/plugins/krunner_kill.so
%{_libdir}/qt5/plugins/krunner_locations.so
%{_libdir}/qt5/plugins/krunner_placesrunner.so
%{_libdir}/qt5/plugins/krunner_powerdevil.so
%{_libdir}/qt5/plugins/krunner_recentdocuments.so
%{_libdir}/qt5/plugins/krunner_services.so
%{_libdir}/qt5/plugins/krunner_sessions.so
%{_libdir}/qt5/plugins/krunner_shell.so
%{_libdir}/qt5/plugins/krunner_webshortcuts.so
%{_libdir}/qt5/plugins/krunner_windowedwidgets.so
%{_libdir}/qt5/plugins/krunner_windows.so
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
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_share.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_soliddevice.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_statusnotifieritem.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_systemmonitor.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_time.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_weather.so
%dir %{_libdir}/qt5/plugins/plasma/packagestructure
%{_libdir}/qt5/plugins/plasma/packagestructure/plasma_packagestructure_share.so
%{_libdir}/qt5/plugins/plasma_containmentactions_applauncher.so
%{_libdir}/qt5/plugins/plasma_containmentactions_contextmenu.so
%{_libdir}/qt5/plugins/plasma_containmentactions_paste.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchactivity.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchdesktop.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchwindow.so
%dir %{_libdir}/qt5/qml/org/kde/plasma
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/appmenu
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/libappmenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/notifications
%{_libdir}/qt5/qml/org/kde/plasma/private/notifications/libnotificationshelperplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/notifications/qmldir
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
#%%attr(755,root,root) %{_libdir}/startplasma
%{_desktopdir}/org.kde.klipper.desktop
%{_desktopdir}/plasma-windowed.desktop
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/dbus-1/interfaces/com.canonical.AppMenu.Registrar.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSplash.xml
%{_datadir}/dbus-1/interfaces/org.kde.PlasmaShell.xml
%{_datadir}/dbus-1/interfaces/org.kde.kappmenu.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/kf5_org.kde.kuiserver.service
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
#%%{_datadir}/drkonqi/debuggers/external/gdbrc
#%%{_datadir}/drkonqi/debuggers/external/kdbgrc
#%%{_datadir}/drkonqi/debuggers/internal/dbxrc
#%%{_datadir}/drkonqi/debuggers/internal/gdbrc
#%%{_datadir}/drkonqi/debuggers/internal/kdbgwinrc
#%%{_datadir}/drkonqi/mappings
%{_datadir}/kconf_update/krunnerplugins.upd
%{_datadir}/kdevappwizard/templates/ion-dataengine.tar.bz2
%dir %{_datadir}/kio_desktop
#%%dir %{_datadir}/kio_desktop/DesktopLinks
#%%{_datadir}/kio_desktop/DesktopLinks/Home.desktop
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
%{_datadir}/kservices5/kuiserver.desktop
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
%{_datadir}/kservices5/plasma-containmentactions-applauncher.desktop
%{_datadir}/kservices5/plasma-containmentactions-contextmenu.desktop
%{_datadir}/kservices5/plasma-containmentactions-paste.desktop
%{_datadir}/kservices5/plasma-containmentactions-switchactivity.desktop
%{_datadir}/kservices5/plasma-containmentactions-switchdesktop.desktop
%{_datadir}/kservices5/plasma-containmentactions-switchwindow.desktop
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
%{_datadir}/kservices5/plasma-dataengine-share-addon-im9.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-imgsusepasteorg.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-imgur.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-kde.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-pastebincom.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-pasteopensuseorg.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-pasteubuntucom.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-privatepastecom.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-simplestimagehosting.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-wklej.desktop
%{_datadir}/kservices5/plasma-dataengine-share-addon-wstaw.desktop
%{_datadir}/kservices5/plasma-dataengine-share.desktop
%{_datadir}/kservices5/plasma-dataengine-soliddevice.desktop
%{_datadir}/kservices5/plasma-dataengine-statusnotifieritem.desktop
%{_datadir}/kservices5/plasma-dataengine-systemmonitor.desktop
%{_datadir}/kservices5/plasma-dataengine-time.desktop
%{_datadir}/kservices5/plasma-dataengine-weather.desktop
%{_datadir}/kservices5/plasma-geolocation-gps.desktop
%{_datadir}/kservices5/plasma-geolocation-ip.desktop
%{_datadir}/kservices5/plasma-lookandfeel-org.kde.breeze.desktop.desktop
%{_datadir}/kservices5/plasma-runner-activityrunner.desktop
%{_datadir}/kservices5/plasma-runner-baloosearch.desktop
%{_datadir}/kservices5/plasma-runner-bookmarks.desktop
%{_datadir}/kservices5/plasma-runner-calculator.desktop
%{_datadir}/kservices5/plasma-runner-kill.desktop
%{_datadir}/kservices5/plasma-runner-kill_config.desktop
%{_datadir}/kservices5/plasma-runner-locations.desktop
%{_datadir}/kservices5/plasma-runner-places.desktop
%{_datadir}/kservices5/plasma-runner-powerdevil.desktop
%{_datadir}/kservices5/plasma-runner-services.desktop
%{_datadir}/kservices5/plasma-runner-sessions.desktop
%{_datadir}/kservices5/plasma-runner-shell.desktop
%{_datadir}/kservices5/plasma-runner-webshortcuts.desktop
%{_datadir}/kservices5/plasma-runner-windowedwidgets.desktop
%{_datadir}/kservices5/plasma-runner-windows.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.color.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.image.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.slideshow.desktop
%{_datadir}/kservices5/programs.protocol
#%%{_datadir}/kservices5/recentdocuments.desktop
%{_datadir}/kservicetypes5/phononbackend.desktop
%{_datadir}/kservicetypes5/plasma-geolocationprovider.desktop
%{_datadir}/kservicetypes5/plasma-layouttemplate.desktop
%{_datadir}/kservicetypes5/plasma_shareprovider.desktop
#%%dir %{_datadir}/ksmserver
#%%dir %{_datadir}/ksmserver/themes
#%%dir %{_datadir}/ksmserver/themes/contour
#%%dir %{_datadir}/ksmserver/themes/default
#%%{_datadir}/ksmserver/themes/contour/ContourButton.qml
#%%{_datadir}/ksmserver/themes/contour/main.qml
#%%{_datadir}/ksmserver/themes/contour/metadata.desktop
#%%{_datadir}/ksmserver/themes/contour/screenshot.png
#%%{_datadir}/ksmserver/themes/default/KSMButton.qml
#%%{_datadir}/ksmserver/themes/default/metadata.desktop
#%%{_datadir}/ksmserver/themes/default/screenshot.png
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
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/KeyboardLayoutButton.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/SessionManagementScreen.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/UserDelegate.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/UserList.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/VirtualKeyboard.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/README.txt
#%%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/background.png
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
#%%dir %{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/userswitcher
#%%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/userswitcher/UserSwitcher.qml
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
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock/contents/code/logic.js
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
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/code
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/code/logic.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BadgeOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BatteryItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/BrightnessItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/InhibitionHint.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PopupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/PowerManagementItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/contents/ui/batterymonitor.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/images/mini-calendar.svgz
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/configAgenda.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar/metadata.json
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
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/ActionItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/DeviceItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/contents/ui/devicenotifier.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier/metadata.json
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
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/code
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout/contents/code/data.js
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
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/config
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/config/config.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/ExpandedRepresentation.qml
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents
#%%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/code
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/code/uiproperties.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/JobDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/JobDetailsItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/Jobs.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationIcon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/NotificationPopup.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/Notifications.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/ScreenPositionSelector.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/ThumbnailStrip.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/configNotifications.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/metadata.json
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
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/Applet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/DoublePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/SinglePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/cpu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/contents/ui/cpuConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/Applet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/DoublePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/SinglePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/diskactivity.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/contents/ui/diskactivityConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/Applet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/DoublePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/SinglePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/diskusage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/contents/ui/diskusageConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/Applet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/DoublePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/SinglePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/memory.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/contents/ui/memoryConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/Applet.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/DoublePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/SinglePlotter.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/net.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/contents/ui/netConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net/metadata.json
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
%{_datadir}/plasma/services/share.operations
%{_datadir}/plasma/services/soliddevice.operations
%{_datadir}/plasma/services/statusnotifieritem.operations
%dir %{_datadir}/plasma/shareprovider
%dir %{_datadir}/plasma/shareprovider/im9
%dir %{_datadir}/plasma/shareprovider/im9/contents
%dir %{_datadir}/plasma/shareprovider/im9/contents/code
%{_datadir}/plasma/shareprovider/im9/contents/code/main.js
%{_datadir}/plasma/shareprovider/im9/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/imgsusepasteorg
%dir %{_datadir}/plasma/shareprovider/imgsusepasteorg/contents
%dir %{_datadir}/plasma/shareprovider/imgsusepasteorg/contents/code
%{_datadir}/plasma/shareprovider/imgsusepasteorg/contents/code/main.js
%{_datadir}/plasma/shareprovider/imgsusepasteorg/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/imgur
%dir %{_datadir}/plasma/shareprovider/imgur/contents
%dir %{_datadir}/plasma/shareprovider/imgur/contents/code
%{_datadir}/plasma/shareprovider/imgur/contents/code/main.js
%{_datadir}/plasma/shareprovider/imgur/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/kde
%dir %{_datadir}/plasma/shareprovider/kde/contents
%dir %{_datadir}/plasma/shareprovider/kde/contents/code
%{_datadir}/plasma/shareprovider/kde/contents/code/main.js
%{_datadir}/plasma/shareprovider/kde/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/pastebincom
%dir %{_datadir}/plasma/shareprovider/pastebincom/contents
%dir %{_datadir}/plasma/shareprovider/pastebincom/contents/code
%{_datadir}/plasma/shareprovider/pastebincom/contents/code/main.js
%{_datadir}/plasma/shareprovider/pastebincom/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/pasteopensuseorg
%dir %{_datadir}/plasma/shareprovider/pasteopensuseorg/contents
%dir %{_datadir}/plasma/shareprovider/pasteopensuseorg/contents/code
%{_datadir}/plasma/shareprovider/pasteopensuseorg/contents/code/main.js
%{_datadir}/plasma/shareprovider/pasteopensuseorg/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/pasteubuntucom
%dir %{_datadir}/plasma/shareprovider/pasteubuntucom/contents
%dir %{_datadir}/plasma/shareprovider/pasteubuntucom/contents/code
%{_datadir}/plasma/shareprovider/pasteubuntucom/contents/code/main.js
%{_datadir}/plasma/shareprovider/pasteubuntucom/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/privatepastecom
%dir %{_datadir}/plasma/shareprovider/privatepastecom/contents
%dir %{_datadir}/plasma/shareprovider/privatepastecom/contents/code
%{_datadir}/plasma/shareprovider/privatepastecom/contents/code/main.js
%{_datadir}/plasma/shareprovider/privatepastecom/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/simplestimagehosting
%dir %{_datadir}/plasma/shareprovider/simplestimagehosting/contents
%dir %{_datadir}/plasma/shareprovider/simplestimagehosting/contents/code
%{_datadir}/plasma/shareprovider/simplestimagehosting/contents/code/main.js
%{_datadir}/plasma/shareprovider/simplestimagehosting/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/wklej
%dir %{_datadir}/plasma/shareprovider/wklej/contents
%dir %{_datadir}/plasma/shareprovider/wklej/contents/code
%{_datadir}/plasma/shareprovider/wklej/contents/code/main.js
%{_datadir}/plasma/shareprovider/wklej/metadata.desktop
%dir %{_datadir}/plasma/shareprovider/wstaw
%dir %{_datadir}/plasma/shareprovider/wstaw/contents
%dir %{_datadir}/plasma/shareprovider/wstaw/contents/code
%{_datadir}/plasma/shareprovider/wstaw/contents/code/main.js
%{_datadir}/plasma/shareprovider/wstaw/metadata.desktop
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
%dir %{_datadir}/plasma/wallpapers/org.kde.image/platformcontents
%dir %{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/phone
%dir %{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/phone/ui
%{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/phone/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/phone/ui/config.qml
%{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/phone/ui/customwallpaper.qml
%dir %{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/touch
%dir %{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/touch/ui
%{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/touch/ui/WallpaperDelegate.qml
%{_datadir}/plasma/wallpapers/org.kde.image/platformcontents/touch/ui/config.qml
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
%{_datadir}/sddm/themes/breeze/Clock.qml
%{_datadir}/sddm/themes/breeze/KeyboardButton.qml
%{_datadir}/sddm/themes/breeze/Login.qml
%{_datadir}/sddm/themes/breeze/Main.qml
%{_datadir}/sddm/themes/breeze/SessionButton.qml
%dir %{_datadir}/sddm/themes/breeze/components
%{_datadir}/sddm/themes/breeze/components/ActionButton.qml
%{_datadir}/sddm/themes/breeze/components/Battery.qml
%{_datadir}/sddm/themes/breeze/components/Clock.qml
%{_datadir}/sddm/themes/breeze/components/KeyboardLayoutButton.qml
%{_datadir}/sddm/themes/breeze/components/SessionManagementScreen.qml
%{_datadir}/sddm/themes/breeze/components/UserDelegate.qml
%{_datadir}/sddm/themes/breeze/components/UserList.qml
%{_datadir}/sddm/themes/breeze/components/VirtualKeyboard.qml
%dir %{_datadir}/sddm/themes/breeze/components/artwork
#%%{_datadir}/sddm/themes/breeze/components/artwork/background.png
%{_datadir}/sddm/themes/breeze/components/artwork/logout_primary.svgz
%{_datadir}/sddm/themes/breeze/components/artwork/restart_primary.svgz
%{_datadir}/sddm/themes/breeze/components/artwork/shutdown_primary.svgz
%{_datadir}/sddm/themes/breeze/metadata.desktop
%{_datadir}/sddm/themes/breeze/preview.png
%{_datadir}/sddm/themes/breeze/theme.conf
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/wayland-sessions/plasmawayland.desktop
%{_datadir}/xsessions/plasma.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/tests
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications/contents/tests/test.qml
/etc/xdg/autostart/org.kde.plasmashell.desktop
#%%{_libdir}/baloorunner
#%%{_libdir}/qt5/plugins/appstreamrunner.so
%{_desktopdir}/org.kde.plasmashell.desktop
%{_datadir}/dbus-1/services/org.kde.baloorunner.service
#%%{_datadir}/kservices5/appstreamrunner.desktop
%{_datadir}/kservices5/plasma-runner-appstream.desktop
%{_datadir}/kservices5/plasma-runner-recentdocuments.desktop
%{_datadir}/kservices5/plasma-runner-webshortcuts_config.desktop
/etc/xdg/wallpaperplugin.knsrc
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
