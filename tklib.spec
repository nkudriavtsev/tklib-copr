%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary: Collection of widgets and other packages for Tk
Name: tklib
Version: 0.6
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
Source: http://core.tcl.tk/tklib/tarball/tklib-0.6.tar.gz
URL: http://core.tcl.tk/tklib/
BuildArch: noarch
Requires: tcl(abi) = 8.6 tk tcllib
BuildRequires: tk >= 0:8.3.1 tcllib
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package is intended to be a collection of Tcl packages that provide
Tk utility functions and widgets useful to a large collection of Tcl/Tk
programmers.

%prep
%setup -q
# Remove some execute permission bits on files that aren't executable
# to suppress some rpmlint warnings.
chmod a-x modules/plotchart/*.tcl
chmod a-x modules/swaplist/*.tcl
chmod a-x modules/widget/*.tcl
chmod a-x modules/diagrams/*.tcl
chmod a-x modules/khim/*.tcl
chmod a-x modules/khim/*.msg

iconv --from=ISO-8859-1 --to=UTF-8 modules/ctext/ctext.man > modules/ctext/ctext.man.new
mv -f modules/ctext/ctext.man.new modules/ctext/ctext.man

%build
# Override the setting for 'libdir'.  If this isn't done then the
# platform-independent script files will get installed in an arch-specific
# directory (such as /usr/lib or /usr/lib64).
%configure --libdir=%{tcl_sitelib}
# Don't bother running 'make' because there's nothing to build.

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog license.terms
%{tcl_sitelib}/tklib*
%{_mandir}/*/*
%{_bindir}/bitmap-editor
%{_bindir}/diagram-viewer

%changelog
* Fri Jul 21 2017 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.6-1
- Changed source to http://core.tcl.tk/tklib
- Updated to version 0.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5-11
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Wart <wart at kobold.org> 0.5-3
- Remove patch that was accepted upstream

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Wart <wart at kobold.org> 0.5-1
- Update to 0.5

* Thu Jan 3 2008 Wart <wart at kobold.org> 0.4.1-7
- Rebuild for Tcl 8.5

* Sun Aug 26 2007 Wart <wart at kobold.org> 0.4.1-6
- License tag clarification
- Move to a tcl-specific directory for faster loading

* Mon Aug 28 2006 Wart <wart at kobold.org> 0.4.1-5
- Rebuild for FC-6

* Thu Feb 16 2006 Wart <wart at kobold.org> 0.4.1-4
- Rebuild for FC-5

* Fri Dec 2 2005 Wart <wart at kobold.org> 0.4.1-3
- Minor specfile improvements.

* Thu Dec 1 2005 Wart <wart at kobold.org> 0.4.1-2
- Add check stage after the install, as well as a patch to the check script
  included in the package.

* Sun Nov 27 2005 Wart <wart at kobold.org> 0.4.1-1
- Initial spec file.
