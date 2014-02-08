# revision 21385
# category Package
# catalog-ctan /macros/latex/contrib/esdiff
# catalog-date 2011-02-13 18:31:54 +0100
# catalog-license lppl1
# catalog-version 1.2
Name:		texlive-esdiff
Version:	1.2
Release:	3
Summary:	Simplify typesetting of derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esdiff
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esdiff.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751573
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718362
- texlive-esdiff
- texlive-esdiff
- texlive-esdiff
- texlive-esdiff

