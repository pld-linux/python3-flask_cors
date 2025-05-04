#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

Summary:	Flask extension adding a decorator for CORS support
Summary(pl.UTF-8):	Rozszerzenie Flaska dodające dekorator do obsługi CORS
Name:		python3-flask_cors
Version:	5.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Flask-Cors/
Source0:	https://files.pythonhosted.org/packages/source/F/Flask-Cors/flask_cors-%{version}.tar.gz
# Source0-md5:	786591022a69fc5479c4aa8d71b05abd
URL:		https://pypi.org/project/Flask-Cors/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-flask >= 0.9
BuildRequires:	python3-nose
BuildRequires:	python3-packaging
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-sphinxcontrib-httpdomain >= 1.7.0
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%description -l pl.UTF-8
Rozszerzenie Flaska do obsługi CORS (Cross Origin Resource Sharing),
umożliwiającego działanie AJAX-a między domenami.

%package apidocs
Summary:	API documentation for Python Flask-Cors module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Flask-Cors
Group:		Documentation

%description apidocs
API documentation for Python Flask-Cors module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Flask-Cors.

%prep
%setup -q -n flask_cors-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%if %{with doc}
%{__python3} -m zipfile -e build-3/*.whl build-3-doc
PYTHONPATH=$(pwd)/build-3-doc \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/flask_cors
%{py3_sitescriptdir}/flask_cors-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
