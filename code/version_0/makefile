all: generateTex
	pdflatex testTex.tex

generateTex: generatePlots
	python3 reportGenerator_beta.py

generatePlots: generateDataFile
	Rscript makePlots.R $(outputFile) $(name)

generateDataFile:
	python3 xmlToCSV.py $(inputFile) $(outputFile) $(isRunningFile)
