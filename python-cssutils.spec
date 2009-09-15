%define oname	cssutils
%define name	python-%{oname}

Name:		%{name}
Version:	0.9.5.1
Release:	%mkrel 2
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		http://code.google.com/p/cssutils/
Source0:	http://cssutils.googlecode.com/files/%{oname}-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root 
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%{py_requires}
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
  
%prep
%setup -q -n %{oname}-%{version}

%build 

%install 
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean 
rm -rf %{buildroot}

%files  
%defattr(-,root,root,-)
%{_bindir}/css*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/encutils
%{py_puresitedir}/tests
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info

