%define oname	cssutils
%define name	python-%{oname}

Name:		%{name}
Version:	0.9.10
Release:	3
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		http://code.google.com/p/cssutils/
Source0:	https://pypi.python.org/packages/source/c/cssutils/cssutils-%{version}.zip
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


%changelog
* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.7-0.b3.2mdv2011.0
+ Revision: 590376
- rebuild for python-2.7

* Sat Jul 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.7-0.b3.1mdv2011.0
+ Revision: 550341
- update to 0.9.7b3

* Fri Dec 04 2009 Michael Scherer <misc@mandriva.org> 0.9.5.1-3mdv2010.1
+ Revision: 473354
- do not let world writable file, fix #56186

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.5.1-2mdv2010.0
+ Revision: 442089
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.5.1-1mdv2009.1
+ Revision: 319513
- rebuild with python 2.6
- new release 0.9.5.1

* Wed Jul 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.5-1mdv2009.0
+ Revision: 255575
- import python-cssutils



