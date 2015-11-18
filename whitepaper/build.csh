#!/bin/tcsh
#===============================================================================
#+
# NAME:
#   build
#
# PURPOSE:
#   Make the LSST Observing Strategy white paper, so that the PDF can be downloaded
#   from anywhere.
#
# COMMENTS:
#   To be sent by a cron job like this:
#     ki-ls07 1 * * * 0-6  /u/ki/pjm/public_html/LSST/ObservingStrategy/whitepaper/build.csh
#   Note: the script assumes that it lives in public_html/LSST/ObservingStrategy/whitepaper 
#
# INPUTS:
#   None
#
# OPTIONAL INPUTS:
#   -h --help         Print this header
#
# OUTPUTS:
#   PDF file
#
# EXAMPLES:
#
# BUGS:
#
# REVISION HISTORY:
#   2015-11-13  started Marshall (KIPAC)
#-
# ==============================================================================

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

# ==============================================================================

set LATEX_DIR = /u/ki/pjm/public_html/LSST/ObservingStrategy/whitepaper 
set LOG_FILE = ${LATEX_DIR}/build.log

\rm -f ${LOG_FILE}
echo "build.csh: starting at "`date` >& ${LOG_FILE}

echo "build.csh: moving to white paper directory" >>& ${LOG_FILE}
chdir ${LATEX_DIR} >>& ${LOG_FILE}

echo "build.csh: updating repository" >>& ${LOG_FILE}
git pull http master >>& ${LOG_FILE}

echo "build.csh: making white paper PDF file" >>& ${LOG_FILE}
make >>& ${LOG_FILE}

# ==============================================================================
FINISH:
# ==============================================================================
