Name:		texlive-esdiff
Version:	1.2
Release:	1
Summary:	Simplify typesetting of derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esdiff
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package makes writing derivatives very easy. It offers
macros for derivatives, partial derivatives and multiple
derivatives, and allows specification of the point at which the
value is calculated. Some typographic alternatives may be
selected by package options.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/esdiff/esdiff.sty
%doc %{_texmfdistdir}/doc/latex/esdiff/README
%doc %{_texmfdistdir}/doc/latex/esdiff/esdiff.pdf
#- source
%doc %{_texmfdistdir}/source/latex/esdiff/esdiff.dtx
%doc %{_texmfdistdir}/source/latex/esdiff/esdiff.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
