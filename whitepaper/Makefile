PAPER = LSST_Observing_Strategy_White_Paper.pdf
TEXFILES = *.tex
BIBFILES = references.bib

all: pdf

clean:
	-rm -f *.aux *.log *.dvi *.blg *.bbl *.inx *.aut *.toc *.out $(PAPER)

pdf: $(PAPER)

LSST_Observing_Strategy_White_Paper.pdf: LSST_Observing_Strategy_White_Paper.tex LSST_Observing_Strategy_White_Paper.sty $(BIBFILES) $(TEXFILES)
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	bibtex   LSST_Observing_Strategy_White_Paper
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	pdflatex LSST_Observing_Strategy_White_Paper.tex
	pdflatex LSST_Observing_Strategy_White_Paper.tex

run: $(ARG)_standalone.tex LSST_Observing_Strategy_White_Paper.sty  $(BIBFILES) $(TEXFILES)
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
	bibtex  LSST_Observing_Strategy_White_Paper
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
	pdflatex $(ARG)_standalone.tex
