# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name validations-common
%global srcname validations_common

Name:           validations-common
Summary:        A collection of Ansible libraries and Plugins for the Validation Framework
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://opendev.org/openstack/validations-common
Source0:        https://tarballs.opendev.org/openstack/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-oslotest >= 1.0.0
BuildRequires:  python%{pyver}-testrepository >= 0.0.18
BuildRequires:  python%{pyver}-testscenarios >= 0.4
BuildRequires:  python%{pyver}-testtools >= 2.2.0
%if %{pyver} == 2
BuildRequires:  ansible >= 2
%else
BuildRequires:  python3dist(ansible) >= 2
BuildRequires:  /usr/bin/pathfix.py
%endif

%if %{pyver} == 2
Requires:       ansible >= 2
Requires:       PyYAML
%else
Requires:       python3dist(ansible) >= 2
Requires:       python%{pyver}-PyYAML
%endif
Requires:       python%{pyver}-pbr >= 3.1.1

%description
A collection of Ansible librairies and Plugins for the Validation Framework

%package -n validations-common-tests
Summary:        Tests for validations-common
Requires:       %{name} = %{version}-%{release}

BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-oslotest >= 1.0.0
BuildRequires:  python%{pyver}-testrepository >= 0.0.18
BuildRequires:  python%{pyver}-testscenarios >= 0.4
BuildRequires:  python%{pyver}-testtools >= 2.2.0
%if %{pyver} == 2
BuildRequires:  ansible >= 2
%else
BuildRequires:  python3dist(ansible) >= 2
%endif

Requires:       python%{pyver}-subunit
Requires:       python%{pyver}-oslotest >= 1.0.0
Requires:       python%{pyver}-testrepository >= 0.0.18
Requires:       python%{pyver}-testscenarios >= 0.4
Requires:       python%{pyver}-testtools >= 2.2.0

%if %{pyver} == 2
Requires:       ansible >= 2
Requires:       PyYAML
%else
Requires:       python3dist(ansible) >= 2
Requires:       python%{pyver}-PyYAML
%endif

%description -n validations-common-tests
This package contains the validations-common test files.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%if %{pyver} == 3
# Fix shebangs for Python 3-only distros
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{name}/library/
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{name}/lookup_plugins/
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{name}/callback_plugins/
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/%{name}/roles/
%endif

%check
PYTHON=%{pyver_bin} %{pyver_bin} setup.py testr

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{_datadir}/%{name}
%exclude %{pyver_sitelib}/validations_common/test*

%files -n validations-common-tests
%license LICENSE
%{pyver_sitelib}/validations_common/tests

%changelog
