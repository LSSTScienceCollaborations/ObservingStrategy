from __future__ import print_function
__author__ = 'fbb'
import os
import sys
import glob

if __name__ == '__main__':
    if not len(sys.argv) > 2:
        print ("""

        Usage: gen_standalone.py <section_name> (<section_name>, <section_name>...) <standalone_name>
this will generate a standalone tex file 
named <standalone_name>_standalone.tex which will include the 
paper Preface and all sections selected via command line.

NOTE: after running this script you must compile the latex into a pdf: Compile the tex file with the command:
$make run ARG=<standalone_name_root>

""")

        sys.exit()
    sec_in = sys.argv[1:-1]
    sa_out = sys.argv[-1]+'_standalone.tex'

    if os.path.isfile(sa_out):
        overwrite = raw_input("standalone file {0:s} already exists. Overwrite? (Y/n)".format(sa_out))
        if overwrite.startswith('n') or  overwrite.startswith('N'):
            print ("ok")
            sys.exit()
    f = open(sa_out, "w")

    f.write("""% ====================================================================

% LSST Observing Strategy White Paper

% Copyright 2015 The LSST Science Collaborations

% ====================================================================

\documentclass[11pt,headsepline,cleardoubleempty,twoside,openright]{scrbook}
% 11pt font
% Draw a line under the header
% Don't draw a line or print page numbers when a page is empty
% Pages are two-sided - so margins alternate
% Chapters start on the righthand side of the page

\usepackage{LSST_Observing_Strategy_White_Paper}

% ====================================================================

\\begin{document}

\\begin{titlepage}
\\begin{center}

\\vspace*{\\stretch{3}}

{\\Huge\\bfseries\\scshape
 Science Driven Optimization \\\\ \\vspace{\\baselineskip}
 of the LSST Observing Strategy}

\\vspace*{\\stretch{2}}

% Version number, to be taken out for published draft

% \\include{VersionDate}

% \\begin{center}
% {\\Large\\bf Version 1.0\\\\
%
% \\vspace*{\\stretch{0.2}}
%
% November 2009}
% \\end{center}

\\vspace*{\\stretch{2.5}}

{\\Large  Prepared by the LSST Science Collaborations,}\\\\
\\vspace*{\\stretch{0.15}}
{\\Large with contributions from the LSST Project. }\\\\
\\vspace*{\\stretch{1}}

\\end{center}
\\end{titlepage}

% --------------------------------------------------------------------

\\clearemptydoublepage
\\include{authors}

% --------------------------------------------------------------------

\\tableofcontents
\\label{toc}

% --------------------------------------------------------------------

\\clearemptydoublepage
\\include{preface}

% --------------------------------------------------------------------

""")
    for sec in sec_in:
        f.write("\\include{"+(sec.strip().replace('.tex',''))+"}")
    f.write("""

\\bibliographystyle{apj}
\\bibliography{references}

% --------------------------------------------------------------------

    \\end{document}

% ====================================================================
""")

    
  
    
