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
#   -v --version        Manual version number
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
set version = 0.0

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
   case -v:
      shift argv
      set version = $argv[1]
      shift argv
      breaksw
   case --{version}:
      shift argv
      set version = $argv[1]
      shift argv
      breaksw
   endsw
end

if ($help) then
  more $0
  goto FINISH
endif

# # Get most recent tag name:
# set version = `git describe --tags | cut -d'-' -f1`
# set version_url = "https://github.com/LSSTScienceCollaborations/ObservingStrategy/releases/tag/${version}"
# Abandoning this - the problem is that when we make a new release,
# it won't update the tags until *after we've made it, at which
# point the PDF has already become part of the release. I think we have
# to set the Version number by hand.

# Get most recent commit ID and its date:
set SHA = `git show | head -1 | cut -d' ' -f2`
set short_SHA = `echo $SHA | cut -c1-7`
set date = `git log --date=rfc | head -3 | grep Date | cut -d':' -f2-`

# Get URL of latest commit:
set commit_url = "https://github.com/LSSTScienceCollaborations/ObservingStrategy/commit/${SHA}?diff=split"

# Append commit ID to version number:
set version = "${version}.${short_SHA}"

# Write tex file for input into paper:
set texfile = "thisversion.tex"
set template = "version.tex"
\rm -f $texfile ; touch $texfile

cat $template | \
    sed s%XX%"${version}"%g | \
    sed s%URL%"${commit_url}"%g | \
    sed s%SHA%"${short_SHA}"%g | \
    sed s%DATE%"${date}"%g > $texfile

cat $texfile

# ======================================================================
FINISH:
# ======================================================================
