%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name XStatic-DataTables

Name:           python-%{pypi_name}
Version:        1.10.15.1
Release:        1%{?dist}
Summary:        DataTables jquery javascript framework (XStatic packaging standard)

License:        ASL 2.0
URL:            https://datatables.net/
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python2-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python-XStatic
Requires:       xstatic-datatables-common

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 2 build of %{pypi_name}.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-datatables-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.
%endif

%package -n xstatic-datatables-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-datatables-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/datatables'|" xstatic/pkg/datatables/__init__.py

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
mkdir -p %{buildroot}%{_jsdir}/datatables
mv %{buildroot}%{python2_sitelib}/xstatic/pkg/datatables/data/* %{buildroot}%{_jsdir}/datatables
rmdir %{buildroot}%{python2_sitelib}/xstatic/pkg/datatables/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/datatables/js/*.js

%if 0%{?with_python3}
%py3_install
# Remove static files, already created by the python2 subpkg
rm -rf %{buildroot}%{python3_sitelib}/xstatic/pkg/datatables/data
%endif

%files -n python2-%{pypi_name}
%doc README.txt
%{python2_sitelib}/xstatic/pkg/datatables
%{python2_sitelib}/XStatic_DataTables-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/XStatic_DataTables-%{version}-py%{python2_version}-nspkg.pth

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/datatables
%{python3_sitelib}/XStatic_DataTables-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_DataTables-%{version}-py%{python3_version}-nspkg.pth
%endif

%files -n xstatic-datatables-common
%doc README.txt
%{_jsdir}/datatables

%changelog
* Sun Apr 23 2017 David Moreau Simard <dmsimard@redhat.com> - 1.10.15.1
- Initial version of the package
