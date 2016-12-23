#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : django_openstack_auth
Version  : 2.4.1
Release  : 30
URL      : http://tarballs.openstack.org/django_openstack_auth/django_openstack_auth-2.4.1.tar.gz
Source0  : http://tarballs.openstack.org/django_openstack_auth/django_openstack_auth-2.4.1.tar.gz
Summary  : Django authentication backend for use with OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: django_openstack_auth-python
BuildRequires : Babel
BuildRequires : Django
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : coverage
BuildRequires : docutils
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8
BuildRequires : hacking
BuildRequires : iso8601
BuildRequires : linecache2
BuildRequires : mccabe
BuildRequires : mox3
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslosphinx
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : prettytable
BuildRequires : pycodestyle-python
BuildRequires : pyflakes
BuildRequires : python-dev
BuildRequires : python-keystoneclient
BuildRequires : python-mimeparse
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : stevedore
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2
BuildRequires : unittest2

%description
=====================
Django OpenStack Auth
=====================
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user against
OpenStack's Keystone Identity API.

%package python
Summary: python components for the django_openstack_auth package.
Group: Default
Requires: oslo.config

%description python
python components for the django_openstack_auth package.


%prep
%setup -q -n django_openstack_auth-2.4.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose; py.test-3.5 --verbose;
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
