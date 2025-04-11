%global octpkg cgi

Summary:	Common Gateway Interface for Octave.
Name:		octave-%{octpkg}
Version:	0.1.2
Release:	3
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}

BuildArch:	noarch

Requires(post): octave
Requires(postun): octave

%description
Common Gateway Interface for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

