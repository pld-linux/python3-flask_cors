#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Flask extension adding a decorator for CORS support
Summary(pl.UTF-8):	Rozszerzenie Flaska dodające dekorator do obsługi CORS
Name:		python-flask_cors
# keep 3.x here for python2/Flask 1 support
Version:	3.0.10
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Flask-Cors/
Source0:	https://files.pythonhosted.org/packages/source/F/Flask-Cors/Flask-Cors-%{version}.tar.gz
# Source0-md5:	647ff0632b960ba063a077fb4063077e
URL:		https://pypi.org/project/Flask-Cors/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-flask >= 0.9
BuildRequires:	python-nose
BuildRequires:	python-packaging
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-flask >= 0.9
BuildRequires:	python3-nose
BuildRequires:	python3-packaging
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-sphinx_rtd_theme
BuildRequires:	python-sphinxcontrib-httpdomain >= 1.7.0
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%description -l pl.UTF-8
Rozszerzenie Flaska do obsługi CORS (Cross Origin Resource Sharing),
umożliwiającego działanie AJAX-a między domenami.

%package -n python3-flask_cors
Summary:	Flask extension adding a decorator for CORS support
Summary(pl.UTF-8):	Rozszerzenie Flaska dodające dekorator do obsługi CORS
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-flask_cors
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%description -n python3-flask_cors -l pl.UTF-8
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
%setup -q -n Flask-Cors-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/flask_cors
%{py_sitescriptdir}/Flask_Cors-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-flask_cors
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/flask_cors
%{py3_sitescriptdir}/Flask_Cors-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
