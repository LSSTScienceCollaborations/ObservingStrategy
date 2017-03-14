#!/bin/tcsh
#=======================================================================
#+
# NAME:
#   gen_version
#
# PURPOSE:
#   Find out the most recent commit ID, and write a small tex file
#   for input into the white paper.
#
# COMMENTS:
#
# INPUTS:
#   None
#
# OPTIONAL INPUTS:
#   -h --help           Print this header
#
# OUTPUTS:
#   version.tex         Tex file for input into white paper
#
# EXAMPLES:
#
# BUGS:
#
#-
# ======================================================================

set help = 0

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
   endsw
end

if ($help) then
  more $0
  goto FINISH
endif

# Get most recent tag name:
set version = `git describe --tags | cut -d'-' -f1`
set version_url = "https://github.com/LSSTScienceCollaborations/ObservingStrategy/releases/tag/${version}"

# Get most recent commit ID and its date:
set SHA = `git show | head -1 | cut -d' ' -f2`
set short_SHA = `echo $SHA | cut -c1-7`
set date = `git log --date=rfc | head -3 | grep Date | cut -d':' -f2-`

# Get URL of latest commit:
set commit_url = "https://github.com/LSSTScienceCollaborations/ObservingStrategy/commit/${SHA}?diff=split"

# Write tex file for input into paper:
set texfile = "version.tex"
\rm -f $texfile ; touch $texfile

echo "\begin{center}{" >> $texfile
echo "    Most recent commit: \href{${commit_url}}{\texttt{$short_SHA}}\\ " >> $texfile
echo "    \vspace*{\stretch{0.1}}" >> $texfile
echo "    (${date}, building on release \href{${version_url}}{$version})}\\ " >> $texfile
echo "\end{center}" >> $texfile

cat $texfile

# ======================================================================
FINISH:
# ======================================================================
