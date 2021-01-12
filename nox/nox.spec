# Created by pyp2rpm-3.3.5
%global pypi_name nox
%define __python %{python3}

Name:           python-%{pypi_name}
Version:        2020.12.31
Release:        1%{?dist}
Summary:        Flexible test automation

License:        Apache Software License
URL:            https://nox.thea.codes
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Nox - Flexible test automation for Python nox is a command-line tool that
automates testing in multiple Python environments, similar to tox_. Unlike tox,
Nox uses a standard Python file for configuration.The latest documentation is
available on Read the Docs_.The source code is available on GitHub_. .. _tox:
.. _Read the Docs: .. _GitHub:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(argcomplete) >= 1.9.4 with python3dist(argcomplete) < 2)
Requires:       (python3dist(colorlog) >= 2.6.1 with python3dist(colorlog) < 5)
%if 0%{?python_version_nodots} < 38
Requires:       python3dist(importlib-metadata)
%endif
Requires:       (python3dist(py) >= 1.4 with python3dist(py) < 2)
Requires:       python3dist(virtualenv) >= 14

Suggests:       python3dist(jinja2)
Suggests:       python3dist(tox)

%description -n python3-%{pypi_name}
Nox - Flexible test automation for Python nox is a command-line tool that
automates testing in multiple Python environments, similar to tox_. Unlike tox,
Nox uses a standard Python file for configuration.The latest documentation is
available on Read the Docs_.The source code is available on GitHub_. .. _tox:
.. _Read the Docs: .. _GitHub:


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/nox
%{_bindir}/tox-to-nox
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 12 2021 Jerzy Drozdz <jerzy.drozdz@jdsieci.pl> - 2020.12.31-1
- Initial package.
