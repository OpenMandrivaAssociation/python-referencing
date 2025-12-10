%global module referencing

Summary:	JSON Referencing + Python
Name:		python-%{module}
Version:	0.37.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/referencing/
Source0:	https://pypi.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
JSON Referencing + Python

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-*.*-info
