PAPER = LSST_Observing_Strategy_White_Paper.pdf
TEXFILES = *.tex */*.tex
BIBFILES = references.bib

all: pdf

clean:
	-rm -f *.aux LSST*.log *.dvi *.blg *.bbl *.inx *.aut *.toc *.tod *.out

vclean: clean
	-rm LSST_Observing_Strategy_White_Paper.pdf

pdf: $(PAPER)

LSST_Observing_Strategy_White_Paper.pdf: version LSST_Observing_Strategy_White_Paper.tex LSST_Observing_Strategy_White_Paper.sty $(BIBFILES) $(TEXFILES)
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	bibtex   LSST_Observing_Strategy_White_Paper
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	pdflatex LSST_Observing_Strategy_White_Paper.tex

version:
	/bin/tcsh gen_version.csh --version 0.9

run: $(ARG)_standalone.tex LSST_Observing_Strategy_White_Paper.sty  $(BIBFILES) $(TEXFILES)
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
	bibtex  LSST_Observing_Strategy_White_Paper
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
