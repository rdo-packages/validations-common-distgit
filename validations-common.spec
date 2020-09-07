# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name validations-common
%global srcname validations_common

Name:           validations-common
Summary:        A collection of Ansible libraries, Plugins and Roles for the Validation Framework
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://opendev.org/openstack/validations-common
Source0:        https://tarballs.opendev.org/openstack/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr >= 3.1.1
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-testscenarios
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-oslotest

%if %{pyver} == 2
BuildRequires:  ansible >= 2
BuildRequires:  PyYAML
%else
BuildRequires:  python3dist(ansible) >= 2
BuildRequires:  python%{pyver}-PyYAML
%endif

%if %{pyver} == 2
Requires:       ansible >= 2
Requires:       PyYAML
%else
Requires:       python3dist(ansible) >= 2
Requires:       python%{pyver}-PyYAML
%endif

Requires:       python%{pyver}-pbr >= 3.1.1
Requires:       python%{pyver}-validations-libs

Requires:       python%{pyver}-prettytable

%description
A collection of Ansible librairies, Plugins and Roles for the Validation Framework

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%check
PYTHON=%{pyver_bin} stestr-%{pyver} --test-path validations_common/tests run

%files
%doc README* AUTHORS ChangeLog
%license LICENSE
%{_bindir}/validation.py
%{pyver_sitelib}/%{srcname}
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/%{name}/
%exclude %{pyver_sitelib}/validations_common/test*

%changelog
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/validations-common/commit/?id=946e3a858686564c9c2c2e5cf5b479655a9adfc4
