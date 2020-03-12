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
Summary:        A collection of Ansible libraries, Plugins and Roles for the Validation Framework
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
%if %{pyver} == 2
BuildRequires:  ansible >= 2
%else
BuildRequires:  python3dist(ansible) >= 2
%endif

%if %{pyver} == 2
Requires:       ansible >= 2
Requires:       PyYAML
%else
Requires:       python3dist(ansible) >= 2
Requires:       python%{pyver}-PyYAML
%endif
Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-validations-libs

%description
A collection of Ansible librairies, Plugins and Roles for the Validation Framework

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README* AUTHORS ChangeLog
%license LICENSE
%{pyver_sitelib}/%{srcname}
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/%{name}/


%changelog
