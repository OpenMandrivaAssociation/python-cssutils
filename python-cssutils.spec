%define oname	cssutils

Name:		python-%{oname}
Version:	2.11.1
Release:	2
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		https://pypi.org/project/cssutils/
Source0:	https://files.pythonhosted.org/packages/source/c/cssutils/cssutils-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
 
%prep
%autosetup -p1 -n %{oname}-%{version}

%build 
%py_build

%install 
%py_install

%files  
%{_bindir}/css*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/encutils
%{py_puresitedir}/*.dist-info
