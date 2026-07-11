%global tl_name draftcopy
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.16
Release:	%{tl_revision}.1
Summary:	Identify draft copies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/draftcopy
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/draftcopy.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Places the word DRAFT (or other words) in light grey diagonally across
the background (or at the bottom) of each (or selected) pages of the
document. The package uses PostScript \special commands, and may not
therefore be used with pdfLaTeX. For that usage, consider the wallpaper
or draftwatermark packages.

