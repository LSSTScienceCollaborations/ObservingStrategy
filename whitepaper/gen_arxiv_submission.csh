#!/bin/tcsh
#=======================================================================
#+
# NAME:
#   gen_arxiv_submission
#
# PURPOSE:
#   Make a gzipped tarball that can be accepted by the arxiv
#
# COMMENTS:
#   Takes the current whitepaper directory, including thisversin.tex,
#   and prepares a folder of source files, reducing figure sizes where
#   needed, and checks that it compiles with pdflatex.
#
# INPUTS:
#   None
#
# OPTIONAL INPUTS:
#   -h --help           Print this header
#   --clobber           Overwrite submission folder
#   --maxsize X         Shrink all images with size greater than X kb
#   --metadata          Skip straight to the metadata
#
# OUTPUTS:
#   arxiv/lsst-obs-str-vX.X.tar.gz
#
# EXAMPLES:
#
# BUGS:
#
#-
# ======================================================================

set help = 0
set fromscratch = 0
set maxsize = 150
set metadata = 0

while ( $#argv > 0 )
   switch ($argv[1])
   case -h:
      shift argv
      set help = 1
      breaksw
   case --{help}:
      shift argv
      set help = 1
      breaksw
   case --{clobber}:
      shift argv
      set fromscratch = 1
      breaksw
   case --{maxsize}:
      shift argv
      set maxsize = $argv[1]
      shift argv
      breaksw
   case --{metadata}:
      shift argv
      set metadata = 1
      breaksw
   endsw
end

if ($help) then
  more $0
  goto FINISH
endif

# Get the version number out of thisversion.tex (which was made last
# time the paper was built)

if ( ! -e thisversion.tex ) then
    make
endif

set Num = `cat thisversion.tex | grep Version | cut -d'}' -f1 | cut -d'n' -f2`
set folder = arxiv/lsst-obs-str-v${Num}

# Make a folder if one doesn't exist (or clobber what's there):

if ( $fromscratch ) then
    rm -f $folder/*.* $folder/*/*.* $folder/*/*/*.*
    rmdir $folder/*
    rmdir $folder
endif

mkdir -p $folder

if ($metadata) then
  goto METADATA
endif

# Start copying stuff in there!

echo "Copying source files to ${folder}:"

# Get tex files from log:
set texfiles = `grep '\.tex' LSST_Observing_Strategy_White_Paper.log | cut -d'(' -f2- | sed s/')'//g | sed s/'('//g`
set texfiles = `ls $texfiles |& grep -v 'No such file' | sort | uniq`
foreach texfile ( $texfiles )
    set texfolder = $folder/$texfile:h
    mkdir -p $texfolder
    cp -v $texfile $texfolder
end
mv $folder/LSST_Observing_Strategy_White_Paper.tex $folder/ms.tex

# Do style files etc by hand
cp -v LSST_Observing_Strategy_White_Paper.sty  $folder/.
cp -v LSST_Observing_Strategy_White_Paper.bbl  $folder/ms.bbl
cp -v deluxetable.sty  $folder/.
cp -v yahapj.bst  $folder/.

# Get figures from log:
set fignames = `grep 'File:' LSST_Observing_Strategy_White_Paper.log | grep figs | cut -d' ' -f2`
set figfiles = ()
foreach figname ( $fignames )
    set thesefigfiles = `ls -1 ${figname}*`
    if ( $#thesefigfiles > 1 ) echo "Warning: copying multiple files $thesefigfiles"
    set figfiles = ( $figfiles $thesefigfiles )
end

# Copy figures, shrinking as required:
foreach figfile ( $figfiles )
    set figfolder = $folder/$figfile:h
    mkdir -p $figfolder
    set size = `du -k $figfile | awk '{print $1}'`
    set target = $figfolder/$figfile:t
    if ( $size > $maxsize ) then
        if ( $figfile:e == pdf ) then
            set intermediate = intermediate.png
            convert $figfile $intermediate
        else
            set ext = $figfile:e
            set intermediate = intermediate.$ext
            convert -geometry 25%x25% -depth 72 -units pixelsperinch $figfile $intermediate
        endif
        mv $intermediate $target
        rm $intermediate
        echo "Reduced file size:"
        du -k $figfile $target
    else
        cp -v $figfile $target
    endif
end

# Compile paper, to check:
cd $folder
    pdflatex ms.tex
    pdflatex ms.tex
cd -

echo ""
echo "Successfully compiled paper:"
set pdffile = $folder:h/${folder:t}.pdf
mv $folder/ms.pdf $pdffile
du -h $pdffile

# Clean up before archiving:
set types = ( out ent log tod toc )
foreach ext ( $types )
    rm -vf $folder/ms.*$ext
end
\rm rm -vf $folder/*.aux

# Now make tarball
cd $folder:h
    tar cvfz ${folder:t}.tar.gz $folder:t
    set tarball = $folder:h/${folder:t}.tar.gz
cd -

echo ""
echo "Successfully made tarball:"
du -h $tarball

# Now make other things:

METADATA:

set metafile = $folder:h/${folder:t}.metadata

echo "LSST Science Collaborations: " > $metafile
grep author authors.tex | grep -v Section | cut -c9- | sed s/'}{'/' '/g | awk '{print $1}' | tail -n +3 | sed s/'\\v{'//g | sed s/"\\'{"//g | sed s/"\\'"//g | sed s/'{\\'//g | sed s/'}'//g | sed s/'~'/' '/g | sed 's/$/,/g' >> $metafile

cat $metafile | awk '{printf "%s", $0}' > junk ; mv junk $metafile
echo "" >> $metafile

echo "" >> $metafile
echo "Science-Driven Optimization of the LSST Observing Strategy" >> $metafile

# Count figures and pages:

chdir $folder
    set Nfigs = `grep 'begin{figure' *tex */*tex | grep -v '%' | wc -l`
chdir -
set Npages = `tail LSST_Observing_Strategy_White_Paper.log | grep 'Output written' | cut -d'(' -f2 | awk '{print $1}'`

set comments = "$Npages pages, $Nfigs figures. Browse the current version at https://github.com/LSSTScienceCollaborations/ObservingStrategy, new contributions welcome!"

echo "" >> $metafile
echo "$comments" >> $metafile

cat $metafile

# ======================================================================
FINISH:
# ======================================================================
