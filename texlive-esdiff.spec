Name:		texlive-esdiff
Version:	21385
Release:	2
Summary:	Simplify typesetting of derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esdiff
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes writing derivatives very easy. It offers
macros for derivatives, partial derivatives and multiple
derivatives, and allows specification of the point at which the
value is calculated. Some typographic alternatives may be
selected by package options.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
