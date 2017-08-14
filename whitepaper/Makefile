PAPER = LSST_Observing_Strategy_White_Paper.pdf
TEXFILES = *.tex */*.tex
BIBFILES = references.bib

all: pdf

metric_tables:
	python metrics_table.py

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
	tcsh gen_version.csh --version 1.0

run: $(ARG)_standalone.tex LSST_Observing_Strategy_White_Paper.sty  $(BIBFILES) $(TEXFILES)
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
	bibtex  LSST_Observing_Strategy_White_Paper
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
