PAPER = paper
TEX = $(wildcard *.tex tex/*.tex *.bib)
BIB = ref.bib
FIGS = $(wildcard graphs/*)

.PHONY: all clean

$(PAPER).pdf: $(TEX) $(FIGS)
	pdflatex $(PAPER).tex
	bibtex $(PAPER).aux
	pdflatex $(PAPER).tex
	pdflatex $(PAPER).tex
	pdflatex $(PAPER).tex

clean:
	rm -f *.aux *.log *.out *.blg *.bbl *.pdf *.synctex.gz *.cut
