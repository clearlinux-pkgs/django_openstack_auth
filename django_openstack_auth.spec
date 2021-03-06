#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django_openstack_auth
Version  : 3.6.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/41/bd/eff3e06afc36012664d800956a603b7efca29df313f9aaeb5221e1c9639f/django_openstack_auth-3.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/bd/eff3e06afc36012664d800956a603b7efca29df313f9aaeb5221e1c9639f/django_openstack_auth-3.6.1.tar.gz
Summary  : Django authentication backend for use with OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: django_openstack_auth-python3
Requires: django_openstack_auth-license
Requires: django_openstack_auth-python
Requires: Django
Requires: keystoneauth1
Requires: oslo.config
Requires: oslo.policy
Requires: pbr
Requires: python-keystoneclient
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package license
Summary: license components for the django_openstack_auth package.
Group: Default

%description license
license components for the django_openstack_auth package.


%package python
Summary: python components for the django_openstack_auth package.
Group: Default
Requires: django_openstack_auth-python3

%description python
python components for the django_openstack_auth package.


%package python3
Summary: python3 components for the django_openstack_auth package.
Group: Default
Requires: python3-core

%description python3
python3 components for the django_openstack_auth package.


%prep
%setup -q -n django_openstack_auth-3.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532326040
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/django_openstack_auth
cp LICENSE %{buildroot}/usr/share/doc/django_openstack_auth/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/django_openstack_auth/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
