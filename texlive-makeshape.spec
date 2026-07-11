%global tl_name makeshape
%global tl_revision 28973

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Declare new PGF shapes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/makeshape
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package simplifies production of custom shapes with correct anchor
borders, in PGF/TikZ; the only requirement is a PGF path describing the
anchor border. The package also provides macros that help with the
management of shape parameters, and the definition of anchor points.

