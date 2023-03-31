Name:		texlive-draftcopy
Version:	15878
Release:	2
Summary:	Identify draft copies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/draftcopy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
