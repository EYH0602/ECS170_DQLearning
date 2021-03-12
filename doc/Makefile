CC = pdflatex
PY = python3

all: doc

fig: plotCSV.py
	$(PY) plotCSV.py rewards
	$(PY) plotCSV.py losses

doc: Report.tex # fig
	$(CC) Report.tex

clean:
	rm *.aux *.log 
