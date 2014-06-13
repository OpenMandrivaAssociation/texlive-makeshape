# revision 28973
# category Package
# catalog-ctan /graphics/pgf/contrib/makeshape
# catalog-date 2013-01-28 11:48:01 +0100
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-makeshape
Version:	2.1
Release:	6
Summary:	Declare new PGF shapes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/makeshape
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makeshape.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package simplifies production of custom shapes with correct
anchor borders, in PGF/TikZ; the only requirement is a PGF path
describing the anchor border. The package also provides macros
that help with the management of shape parameters, and the
definition of anchor points.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makeshape/makeshape.sty
%doc %{_texmfdistdir}/doc/latex/makeshape/README
%doc %{_texmfdistdir}/doc/latex/makeshape/makeshape.pdf
%doc %{_texmfdistdir}/doc/latex/makeshape/ontesting.pdf
%doc %{_texmfdistdir}/doc/latex/makeshape/sampleshape.tex
%doc %{_texmfdistdir}/doc/latex/makeshape/testsample.pdf
%doc %{_texmfdistdir}/doc/latex/makeshape/testsample.tex
#- source
%doc %{_texmfdistdir}/source/latex/makeshape/makeshape.dtx
%doc %{_texmfdistdir}/source/latex/makeshape/makeshape.ins
%doc %{_texmfdistdir}/source/latex/makeshape/ontesting.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
