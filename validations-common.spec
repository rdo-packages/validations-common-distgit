%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.opendev.org/openstack/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:  git-core
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

Requires:       python3dist(ansible) >= 2
Requires:       python3-PyYAML

Requires:       python3-pbr >= 3.1.1

Requires:       python3-prettytable
Requires:       python3-validations-libs

%description
A collection of Ansible librairies, Plugins and Roles for the Validation Framework

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{upstream_name}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# Create log directory with some default rights/ownership
# In tripleo env, it will be overridden in order to allow the deploy user
# (usually "stack") to write in it
install -d -m 755 %{buildroot}%{_localstatedir}/log/validations

%check
stestr-3 --test-path validations_common/tests run

%files
%doc README* AUTHORS ChangeLog
%license LICENSE
%{_bindir}/validation.py
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/
%exclude %{python3_sitelib}/validations_common/test*
%exclude %{_datadir}/ansible/library/__init__.py

%changelog
