%define oname	cssutils
%define name	python-%{oname}

%define prerel b3

Name:		%{name}
Version:	0.9.7
Release:	%mkrel -c %prerel 1
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		http://code.google.com/p/cssutils/
Source0:	http://cssutils.googlecode.com/files/%{oname}-%{version}%prerel.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root 
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%{py_requires}
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
  
%prep
%setup -q -n %{oname}-%{version}%prerel

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
%defattr(755,root,root,-)
%{py_puresitedir}/%{oname}-%{version}%prerel-py%{pyver}.egg-info
