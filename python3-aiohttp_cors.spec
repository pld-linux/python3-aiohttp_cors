#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	CORS support for aiohttp
Summary(pl.UTF-8):	Obsługa CORS dla aiohttp
Name:		python3-aiohttp_cors
Version:	0.7.0
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aiohttp_cors/
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp_cors/aiohttp-cors-%{version}.tar.gz
# Source0-md5:	de3940a901b269be82c8bd9f28d53ff0
URL:		https://pypi.org/project/aiohttp_cors/
BuildRequires:	python3-modules >= 1:3.4.1
BuildRequires:	python3-setuptools >= 1:20.8.1
%if %{with tests}
BuildRequires:	python3-aiohttp >= 1.1
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-selenium
%if "%{py3_ver}" == "3.4"
BuildRequires:	python3-typing
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aiohttp_cors library implements CORS (Cross Origin Resource Sharing)
support for aiohttp asyncio-powered asynchronous HTTP server.

%description -l pl.UTF-8
Biblioteka aiohttp_cors implementuje obsługę CORS (Cross Origin
Resource Sharing - współdzielenie zasobów z innych źródeł) dla
asynchronicznego serwera HTTP aiohttp, opartego na asyncio.

%prep
%setup -q -n aiohttp-cors-%{version}

%build
%py3_build

%if %{with tests}
# disabled tests don't match current aiohttp error reporting (3.7.x)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="aiohttp.pytest_plugin,pytest_cov.plugin" \
%{__python3} -m pytest tests -k 'not (test_add_options_route or test_static_resource)'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/aiohttp_cors
%{py3_sitescriptdir}/aiohttp_cors-%{version}-py*.egg-info
