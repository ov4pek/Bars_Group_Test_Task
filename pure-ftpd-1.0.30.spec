#

Summary:	Pure-FTPd package
Name:		pure-ftpd
Version:	1.0.30
Release: 	1
License:	BSD
URL: 		https://www.pureftpd.org/project/pure-ftpd
Group: 		System Environment/Daemons 

Source0: 	%{name}-%{version}.tar.gz
#Patch0:		%{name}-%{version}-1.patch
Buildroot: 	%{_buildrootdir}

%description
If you read this, it means that I`ve finished my task.

%prep
%setup -q
#%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR="${RPM_BUILD_ROOT}"

install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_localstatedir}/ftp
#install -d -m 755 $RPM_BUILD_ROOT/%{name}-%{version}/debugfiles.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ THANKS AUTHORS CONTACT HISTORY NEWS
%doc README README.Authentication-Modules README.Configuration-File
%doc README.Contrib README.Donations README.LDAP README.MySQL
%doc README.PGSQL README.TLS README.Virtual-Users
%doc README.MacOS-X README.Windows README.Debian
%doc contrib/pure-vpopauth.pl pureftpd.schema contrib/pure-stat.pl
%dir /%{_localstatedir}/ftp/
%config /%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/pure-*
%{_sbindir}/pure-*
%{_mandir}/man8/*
#%{_buildrootdir}/%{name}-%{version}/debugfiles.list


%changelog
* Sun Jun 4 2017 Danil Ovchinnikov <danilevgenyevi4@gmail.com> - 1.0.30-1
- Everyone should try this, here I decided
