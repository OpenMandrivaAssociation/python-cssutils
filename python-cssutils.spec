%define oname	cssutils
%define name	python-%{oname}

Name:		%{name}
Version:	0.9.10
Release:	0.1
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		http://code.google.com/p/cssutils/
Source0:	https://pypi.python.org/packages/source/c/cssutils/cssutils-%{version}.zip
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
  
%prep
%setup -q -n %{oname}-%{version}

%build 

%install 
python setup.py install --root=%{buildroot} --compile --optimize=2

%files  
%{_bindir}/css*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/encutils
%defattr(755,root,root,-)
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info
# %{py_puresitedir}/tests/*py
# %{py_puresitedir}/tests/test_encutils/*py
