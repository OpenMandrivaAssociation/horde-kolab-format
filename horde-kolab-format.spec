%define _requires_exceptions pear(PHPUnit/Framework.php)
%define prj Kolab_Format

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-kolab-format
Version:       1.0.1
Release:       %mkrel 5
Summary:       A package for reading/writing Kolab data formats
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-dom
Requires:      horde-nls
Requires:      horde-prefs
Requires:      horde-date
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
This package allows to convert Kolab data objects from XML to hashes.

%prep
%setup -q -n %{prj}-%{version}
%__cp %{SOURCE0} %{prj}-%{version}.tgz

%build

%install
pear install --packagingroot %{buildroot} --nodeps --offline %{prj}-%{version}.tgz

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp %{_builddir}/package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Kolab
%dir %{peardir}/tests/Kolab_Format/Horde/Kolab/Format
%{peardir}/Horde/Kolab/Format.php
%{peardir}/Horde/Kolab/Format/Date.php
%dir %{peardir}/Horde/Kolab/Format
%dir %{peardir}/Horde/Kolab/Format/XML
%{peardir}/Horde/Kolab/Format/XML.php
%{peardir}/Horde/Kolab/Format/XML/annotation.php
%{peardir}/Horde/Kolab/Format/XML/contact.php
%{peardir}/Horde/Kolab/Format/XML/distributionlist.php
%{peardir}/Horde/Kolab/Format/XML/event.php
%{peardir}/Horde/Kolab/Format/XML/hprefs.php
%{peardir}/Horde/Kolab/Format/XML/note.php
%{peardir}/Horde/Kolab/Format/XML/task.php
%dir %{peardir}/tests/Kolab_Format
%dir %{peardir}/tests/Kolab_Format/Horde
%dir %{peardir}/tests/Kolab_Format/Horde/Kolab
%dir %{peardir}/tests/Kolab_Format/Horde/Kolab/Format/fixtures
%{peardir}/tests/Kolab_Format/Horde/Kolab/Format/*.php
%{peardir}/tests/Kolab_Format/Horde/Kolab/Format/fixtures/*.xml
%dir %{peardir}/docs/Kolab_Format
%dir %{peardir}/docs/Kolab_Format/Horde
%dir %{peardir}/docs/Kolab_Format/Horde/Kolab
%dir %{peardir}/docs/Kolab_Format/Horde/Kolab/Format
%{peardir}/docs/Kolab_Format/COPYING
%{peardir}/docs/Kolab_Format/Horde/Kolab/Format/event.php
%{peardir}/docs/Kolab_Format/Horde/Kolab/Format/new_type.php
%{peardir}/docs/Kolab_Format/Horde/Kolab/Format/usage.txt
