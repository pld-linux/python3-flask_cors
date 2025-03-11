#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Flask extension adding a decorator for CORS support
Summary(pl.UTF-8):	Rozszerzenie Flaska dodające dekorator do obsługi CORS
Name:		python3-flask_cors
Version:	4.0.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Flask-Cors/
Source0:	https://files.pythonhosted.org/packages/source/F/Flask-Cors/Flask-Cors-%{version}.tar.gz
# Source0-md5:	0ccfa375e744200243d85719b38cdbc6
URL:		https://pypi.org/project/Flask-Cors/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
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
%setup -q -n Flask-Cors-%{version}

%build
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/flask_cors
%{py3_sitescriptdir}/Flask_Cors-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
