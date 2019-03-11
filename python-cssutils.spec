%define oname	cssutils

Name:		python-%{oname}
Version:	1.0.2
Release:	1
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		https://pypi.org/project/cssutils/
Source0:	https://files.pythonhosted.org/packages/5c/0b/c5f29d29c037e97043770b5e7c740b6252993e4b57f029b3cd03c78ddfec/cssutils-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
 
%package -n python2-%{oname}
Summary:	Python 2 module for parsing and building CSS 
Group:		Development/Python

%description -n python2-%{oname}
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).

%prep
%setup -q -n %{oname}-%{version}
cp -a . %{py2dir}

%build 

%install 
pushd %{py2dir}
python2 setup.py install --root=%{buildroot} --compile --optimize=2
popd

python setup.py install --root=%{buildroot} --compile --optimize=2

%files  
%{_bindir}/css*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/encutils
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info
# %{py_puresitedir}/tests/*py
# %{py_puresitedir}/tests/test_encutils/*py

%files -n python2-%{oname}
%{py2_puresitedir}/%{oname}
%{py2_puresitedir}/encutils
%{py2_puresitedir}/%{oname}-%{version}-py%{py2_ver}.egg-info
