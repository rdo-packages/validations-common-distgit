
%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name validations-common
%global srcname validations_common

Name:           validations-common
Summary:        A collection of Ansible libraries, Plugins and Roles for the Validation Framework
Version:        1.0.0
Release:        1%{?dist}
License:        ASL 2.0
URL:            https://opendev.org/openstack/validations-common
Source0:        https://tarballs.opendev.org/openstack/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-oslotest

BuildRequires:  python3dist(ansible) >= 2
BuildRequires:  python3-PyYAML
BuildRequires:  python3-validations-libs

Requires:       python3dist(ansible) >= 2
Requires:       python3-PyYAML

Requires:       python3-pbr >= 3.1.1

Requires:       python3-prettytable
Requires:       python3-validations-libs

%description
A collection of Ansible librairies, Plugins and Roles for the Validation Framework

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
stestr-3 --test-path validations_common/tests run

%files
%doc README* AUTHORS ChangeLog
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/
%exclude %{python3_sitelib}/validations_common/test*

%changelog
* Mon May 18 2020 RDO <dev@lists.rdoproject.org> 1.0.0-1
- Update to 1.0.0

# REMOVEME: error caused by commit https://opendev.org/openstack/validations-common/commit/bad84e1558f7cac6e2f34697b6417842c0dc148a
