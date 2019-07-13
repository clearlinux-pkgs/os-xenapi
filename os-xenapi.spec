#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-xenapi
Version  : 0.3.4
Release  : 6
URL      : https://files.pythonhosted.org/packages/ed/af/8fa74f2545518ba725992765a63b2d8cf507b12867380e8f701c44e47587/os-xenapi-0.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/af/8fa74f2545518ba725992765a63b2d8cf507b12867380e8f701c44e47587/os-xenapi-0.3.4.tar.gz
Summary  : XenAPI library for OpenStack projects
Group    : Development/Tools
License  : Apache-2.0
Requires: os-xenapi-bin
Requires: os-xenapi-python3
Requires: os-xenapi-license
Requires: os-xenapi-python
Requires: Babel
Requires: eventlet
Requires: oslo.concurrency
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: paramiko
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : netifaces
BuildRequires : oslo.concurrency
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslotest
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
os-xenapi
        =========
        
        XenAPI library for OpenStack projects
        
        This library provides the support functions needed to connect to and manage a XenAPI-based
        hypervisor, such as Citrix's XenServer.

%package bin
Summary: bin components for the os-xenapi package.
Group: Binaries
Requires: os-xenapi-license

%description bin
bin components for the os-xenapi package.


%package license
Summary: license components for the os-xenapi package.
Group: Default

%description license
license components for the os-xenapi package.


%package python
Summary: python components for the os-xenapi package.
Group: Default
Requires: os-xenapi-python3

%description python
python components for the os-xenapi package.


%package python3
Summary: python3 components for the os-xenapi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-xenapi package.


%prep
%setup -q -n os-xenapi-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534889711
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/os-xenapi
cp LICENSE %{buildroot}/usr/share/doc/os-xenapi/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xenapi_bootstrap

%files license
%defattr(-,root,root,-)
/usr/share/doc/os-xenapi/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
