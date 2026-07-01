%global debug_package %{nil}

Name:           jadens-printer-driver
Version:        3.3.5.497
Release:        %autorelease
Summary:        CUPS support for JADENS thermal printing devices
License:        Proprietary
Requires:       cups
ExclusiveArch:  x86_64 aarch64

# These are the only archs that JADENS provides for that is supported by Fedora.
# JADENS has folder structures and postinst scripts for x86 but no files, so we can't add it sadly.
Source0: https://raw.githubusercontent.com/RdrSeraphim/jadens-printer-driver/sources/jadens-printer-driver-3.3.5.497-x86_64.tar.gz
Source1: https://raw.githubusercontent.com/RdrSeraphim/jadens-printer-driver/sources/jadens-printer-driver-3.3.5.497-aarch64.tar.gz

%description
CUPS support for JADENS thermal printing devices. Converted from Debian package.

%prep
%ifarch x86_64
%setup -q -b 0 -c
%endif

%ifarch aarch64
%setup -q -b 1 -c
%endif

%build
# Nothing needed to build.

%install
mkdir -p %{buildroot}/usr/lib/cups/filter
mkdir -p %{buildroot}%{_datadir}/cups/model/Jadens

cp -p usr/lib/cups/filter/jadens_printer_filter %{buildroot}/usr/lib/cups/filter/
cp -p usr/share/cups/model/Jadens/*.ppd %{buildroot}%{_datadir}/cups/model/Jadens/

chmod 755 %{buildroot}/usr/lib/cups/filter/jadens_printer_filter

%post
%systemd_post cups.service

%files
%dir /usr/lib/cups
%dir /usr/lib/cups/filter
%attr(755,root,root) /usr/lib/cups/filter/jadens_printer_filter
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/Jadens
%{_datadir}/cups/model/Jadens/*.ppd

%changelog
%autochangelog
