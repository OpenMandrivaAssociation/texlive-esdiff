%global tl_name esdiff
%global tl_revision 78348

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Simplify typesetting of derivatives
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esdiff
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes writing derivatives very easy. It offers macros for
derivatives, partial derivatives and multiple derivatives, and allows
specification of the point at which the value is calculated. Some
typographic alternatives may be selected by package options

