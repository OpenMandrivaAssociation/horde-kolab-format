%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: A package for reading/writing Kolab data formats
Name: 		horde-kolab-format
Version:		1.0.1
Release: 	7
License: 	LGPLv2.1
Group:		Networking/Mail
Source0:		http://pear.horde.org/get/Kolab_Format-%{version}.tgz
URL: 		http://pear.horde.org/package/Kolab_Format
BuildRequires: 	php-pear >= 1.4.7
BuildRequires: 	php-pear-channel-horde
Requires: 	horde-dom >= 0.1.0
Requires: 	horde-nls 
Requires: 	horde-util
Requires: 	php-pear >= 1.4.0b1
Requires:	php-pear-channel-horde
BuildArch: noarch

%description
This package allows to convert Kolab data objects from
 XML to hashes.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
rm -rf %{buildroot}
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock

mv %{buildroot}/docs .


# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/Kolab_Format.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/Kolab_Format.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/Kolab_Format
fi

%files
%defattr(-,root,root)
%doc docs/Kolab_Format/*
%{peardir}/*
%{xmldir}/Kolab_Format.xml


%changelog
* Sun Feb 26 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-6mdv2012.0
+ Revision: 780928
+ rebuild (emptylog)

* Sun Feb 26 2012 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-5
+ Revision: 780783
+ rebuild (emptylog)

* Tue Dec 27 2011 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-4
+ Revision: 745814
- added define _requires_exceptions for none existent pear(PHPUnit/Framework)

* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-3mdv2011.0
+ Revision: 564038
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 524853
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 2

* Mon Mar 01 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 512856
- replaced PreReq with Requires(pre)
- removed BuildRequires: horde-framework
- import horde-kolab-format


