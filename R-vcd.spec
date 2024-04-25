#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-vcd
Version  : 1.4.12
Release  : 56
URL      : https://cran.r-project.org/src/contrib/vcd_1.4-12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vcd_1.4-12.tar.gz
Summary  : Visualizing Categorical Data
Group    : Development/Tools
License  : GPL-2.0
Requires: R-colorspace
Requires: R-lmtest
BuildRequires : R-colorspace
BuildRequires : R-lmtest
BuildRequires : buildreq-R

%description
procedures aimed particularly at categorical data. Special
        emphasis is given to highly extensible grid graphics. The
        package was package was originally inspired by the book 
	"Visualizing Categorical Data" by Michael Friendly and is 
	now the main support package for a new book, 
	"Discrete Data Analysis with R" by Michael Friendly and 
	David Meyer (2015).

%prep
%setup -q -n vcd
pushd ..
cp -a vcd buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703881956

%install
export SOURCE_DATE_EPOCH=1703881956
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vcd/CITATION
/usr/lib64/R/library/vcd/DESCRIPTION
/usr/lib64/R/library/vcd/INDEX
/usr/lib64/R/library/vcd/Meta/Rd.rds
/usr/lib64/R/library/vcd/Meta/data.rds
/usr/lib64/R/library/vcd/Meta/demo.rds
/usr/lib64/R/library/vcd/Meta/features.rds
/usr/lib64/R/library/vcd/Meta/hsearch.rds
/usr/lib64/R/library/vcd/Meta/links.rds
/usr/lib64/R/library/vcd/Meta/nsInfo.rds
/usr/lib64/R/library/vcd/Meta/package.rds
/usr/lib64/R/library/vcd/Meta/vignette.rds
/usr/lib64/R/library/vcd/NAMESPACE
/usr/lib64/R/library/vcd/NEWS.Rd
/usr/lib64/R/library/vcd/R/vcd
/usr/lib64/R/library/vcd/R/vcd.rdb
/usr/lib64/R/library/vcd/R/vcd.rdx
/usr/lib64/R/library/vcd/data/Rdata.rdb
/usr/lib64/R/library/vcd/data/Rdata.rds
/usr/lib64/R/library/vcd/data/Rdata.rdx
/usr/lib64/R/library/vcd/demo/discrete.R
/usr/lib64/R/library/vcd/demo/hcl.R
/usr/lib64/R/library/vcd/demo/hls.R
/usr/lib64/R/library/vcd/demo/hsv.R
/usr/lib64/R/library/vcd/demo/hullternary.R
/usr/lib64/R/library/vcd/demo/mondrian.R
/usr/lib64/R/library/vcd/demo/mosaic.R
/usr/lib64/R/library/vcd/demo/strucplot.R
/usr/lib64/R/library/vcd/demo/twoway.R
/usr/lib64/R/library/vcd/doc/index.html
/usr/lib64/R/library/vcd/doc/residual-shadings.R
/usr/lib64/R/library/vcd/doc/residual-shadings.Rnw
/usr/lib64/R/library/vcd/doc/residual-shadings.pdf
/usr/lib64/R/library/vcd/doc/strucplot.R
/usr/lib64/R/library/vcd/doc/strucplot.Rnw
/usr/lib64/R/library/vcd/doc/strucplot.pdf
/usr/lib64/R/library/vcd/help/AnIndex
/usr/lib64/R/library/vcd/help/aliases.rds
/usr/lib64/R/library/vcd/help/paths.rds
/usr/lib64/R/library/vcd/help/vcd.rdb
/usr/lib64/R/library/vcd/help/vcd.rdx
/usr/lib64/R/library/vcd/html/00Index.html
/usr/lib64/R/library/vcd/html/R.css
/usr/lib64/R/library/vcd/tests/demos.R
