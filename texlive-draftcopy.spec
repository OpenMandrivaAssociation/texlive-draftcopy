# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/draftcopy
# catalog-date 2009-09-25 22:54:35 +0200
# catalog-license lppl
# catalog-version 2.16
Name:		texlive-draftcopy
Version:	2.16
Release:	2
Summary:	Identify draft copies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/draftcopy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Places the word DRAFT (or other words) in light grey diagonally
across the background (or at the bottom) of each (or selected)
pages of the document. The package uses PostScript \special
commands, and may not therefore be used with PDFLaTeX. For that
usage, consider the wallpaper or draftwatermark packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/draftcopy/draftcopy.cfg
%{_texmfdistdir}/tex/latex/draftcopy/draftcopy.sty
%doc %{_texmfdistdir}/doc/latex/draftcopy/README
%doc %{_texmfdistdir}/doc/latex/draftcopy/THIS-IS-VERSION-2.16
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-1.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-10.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-11.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-12.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-13.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-14.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-15.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-16.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-2.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-3.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-4.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-5.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-6.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-7.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-8.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-9.tex
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy.doc
%doc %{_texmfdistdir}/doc/latex/draftcopy/draftcopy.pdf
#- source
%doc %{_texmfdistdir}/source/latex/draftcopy/Makefile
%doc %{_texmfdistdir}/source/latex/draftcopy/draftcopy.dtx
%doc %{_texmfdistdir}/source/latex/draftcopy/draftcopy.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.16-2
+ Revision: 751086
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.16-1
+ Revision: 718258
- texlive-draftcopy
- texlive-draftcopy
- texlive-draftcopy
- texlive-draftcopy

