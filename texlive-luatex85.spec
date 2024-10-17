Name:		texlive-luatex85
Version:	41456
Release:	2
Summary:	pdfTeX aliases for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luatex85
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex85.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex85.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatex85.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides emulation of pdfTeX primitives for LuaTeX
v0.85+.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/luatex85
%{_texmfdistdir}/tex/generic/luatex85
%doc %{_texmfdistdir}/doc/generic/luatex85

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
