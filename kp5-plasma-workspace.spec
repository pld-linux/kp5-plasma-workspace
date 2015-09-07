# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
# * KF5Prison (required version >= 1.2.0) , Prison library , <http://projects.kde.org/prison>
#   Needed to create mobile barcodes from clipboard data (no stable release currently)
%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		plasma-workspace

Summary:	KDE Plasma Workspace
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	4
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	0bb91a876188f98791358017c85ccec8
Source1:	kde.pam
Patch0:		kp5-plasma-workspace-absolute-path.patch
Patch1:		kp5-plasma-workspace-scripts.patch
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gpsd-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesu-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kjsembed-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kxmlrpcclient-devel
BuildRequires:	kf5-networkmanager-qt-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	kp5-libksysguard-devel
BuildRequires:	libqalculate-devel
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
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

install -m455 -p -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/kde

%find_lang %{kpname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
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
%attr(755,root,root) %{_bindir}/plasmashell
%attr(755,root,root) %{_bindir}/plasmawindowed
%attr(755,root,root) %{_bindir}/startkde
%attr(755,root,root) %{_bindir}/startplasmacompositor
%attr(755,root,root) %{_bindir}/systemmonitor
%attr(755,root,root) %{_libdir}/startplasma
%attr(755,root,root) %{_libdir}/drkonqi
%attr(755,root,root) %{_libdir}/kcheckpass
%attr(755,root,root) %{_libdir}/kscreenlocker_greet
%attr(755,root,root) %{_libdir}/ksyncdbusenv
%attr(755,root,root) %{_libdir}/libkdeinit5_kcminit.so
%attr(755,root,root) %{_libdir}/libkdeinit5_kcminit_startup.so
%attr(755,root,root) %{_libdir}/libkdeinit5_klipper.so
%attr(755,root,root) %{_libdir}/libkdeinit5_ksmserver.so
%attr(755,root,root) %{_libdir}/libkdeinit5_kuiserver5.so
%attr(755,root,root) %ghost %{_libdir}/libkworkspace5.so.5
%attr(755,root,root) %{_libdir}/libkworkspace5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasma-geolocation-interface.so.5
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtaskmanager.so.5
%attr(755,root,root) %{_libdir}/libtaskmanager.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libweather_ion.so.7
%attr(755,root,root) %{_libdir}/libweather_ion.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_kill.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_desktopnotifier.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_freespacenotifier.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_ksysguard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_ktimezoned.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_remotedirnotify.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_solidautoeject.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_soliduiserver.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_statusnotifierwatcher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/desktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kio_applications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kio_remote.so
%dir %{_libdir}/qt5/plugins/kpackage
%dir %{_libdir}/qt5/plugins/kpackage/packagestructure
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_layoutemplate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_plasmashell.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaper.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_packagestructure_wallpaperimages.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_activities.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_baloosearchrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_bookmarksrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_calculatorrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_kill.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_locations.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_placesrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_powerdevil.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_recentdocuments.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_services.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_sessions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_shell.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_webshortcuts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_windowedwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_windows.so
%dir %{_libdir}/qt5/plugins/phonon_platform
%attr(755,root,root) %{_libdir}/qt5/plugins/phonon_platform/kde.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma-geolocation-gps.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma-geolocation-ip.so
%dir %{_libdir}/qt5/plugins/plasma/dataengine
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/ion_noaa.so
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
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_share.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_soliddevice.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_systemmonitor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_tasks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_time.so
%dir %{_libdir}/qt5/plugins/plasma/packagestructure
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/packagestructure/plasma_packagestructure_share.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_applet_notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_applauncher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_contextmenu.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_paste.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_switchactivity.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_switchdesktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma_containmentactions_switchwindow.so
%attr(755,root,root) %{_libdir}/qt5/plugins/screenlocker_kcm.so
%dir %{_libdir}/qt5/qml/org/kde/plasma
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/libdigitalclockplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/icon
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/icon/libiconplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/icon/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/notifications
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/notifications/libnotificationshelperplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/notifications/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/shell
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/shell/libplasmashellprivateplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/shell/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers
%dir %{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/wallpapers/image/libplasma_wallpaper_imageplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/workspace
%dir %{_libdir}/qt5/qml/org/kde/private
%dir %{_libdir}/qt5/qml/org/kde/private/systemtray
%{_libdir}/qt5/qml/org/kde/private/systemtray/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/private/systemtray/libsystemtrayplugin.so
%{_desktopdir}/org.kde.klipper.desktop
%{_desktopdir}/plasma-windowed.desktop
%{_datadir}/config.kcfg/freespacenotifier.kcfg
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSplash.xml
%{_datadir}/dbus-1/interfaces/org.kde.PlasmaShell.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/kf5_org.kde.kuiserver.service
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/desktop-directories/kf5-*.directory
%{_datadir}/drkonqi
%dir %{_datadir}/kconf_update
%{_datadir}/kconf_update/kscreenlocker.upd
%{_datadir}/kconf_update/ksreenlocker_5_3_separate_autologin.pl
%{_datadir}/kio_desktop
%{_datadir}/knotifications5/freespacenotifier.notifyrc
%{_datadir}/knotifications5/ksmserver.notifyrc
%{_datadir}/knotifications5/phonon.notifyrc
%{_datadir}/kservices5/applications.protocol
%{_datadir}/kservices5/desktop.protocol
%{_datadir}/kservices5/ion-noaa.desktop
%{_datadir}/kservices5/kded
%{_datadir}/kservices5/kuiserver.desktop
%{_datadir}/kservices5/plasma-*.desktop
%{_datadir}/kservices5/programs.protocol
%{_datadir}/kservices5/recentdocuments.desktop
%{_datadir}/kservices5/remote.protocol
%{_datadir}/kservices5/screenlocker.desktop
%{_datadir}/kservicetypes5/phononbackend.desktop
%{_datadir}/kservicetypes5/plasma-geolocationprovider.desktop
%{_datadir}/kservicetypes5/plasma-layout-template.desktop
%{_datadir}/kservicetypes5/plasma_shareprovider.desktop
%{_datadir}/ksmserver
%{_datadir}/ksplash
%{_datadir}/kstyle
%{_datadir}/plasma
%{_datadir}/sddm
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/xsessions/plasma.desktop
/etc/xdg/autostart/krunner.desktop
/etc/xdg/autostart/org.kde.klipper.desktop
/etc/xdg/autostart/plasmashell.desktop
/etc/xdg/plasmoids.knsrc
/etc/xdg/taskmanagerrulesrc
/etc/xdg/wallpaper.knsrc
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kde

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDE/Plasma
%{_includedir}/kworkspace5
%{_includedir}/plasma
%{_includedir}/taskmanager
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/ScreenSaverDBusInterface
%attr(755,root,root) %{_libdir}/libkworkspace5.so
%attr(755,root,root) %{_libdir}/libplasma-geolocation-interface.so
%attr(755,root,root) %{_libdir}/libtaskmanager.so
%attr(755,root,root) %{_libdir}/libweather_ion.so

