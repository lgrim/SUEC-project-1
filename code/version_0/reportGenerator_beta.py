###########################################
## Practice Report Generator ##############
## Typeset results in LATEX using python ##
## Logan Grim and Steve Moors #############
## 2018 ###################################
###########################################

import sys

class reportGenerator_beta:

    def __init__(self, pacePlot):

        # Instance Variables
        self.outputFile = open("testTex.tex", "w")

        self.pacePlot = pacePlot

        ##########################################

        # Call appropriate methods to configure the tex file
        self.testDoc()

        # Close the output file
        self.outputFile.close()


    #############
    ## Methods ##
    #############

    def testDoc(self):
      
        # Title tag
        self.outputFile.write("\\title{Practice Typesetting from Python}\n")

        # Author tag
        self.outputFile.write("\\author{Logan Grim and Steve Moors}\n")

        # Date tag
        self.outputFile.write("\\date{\\today}\n")

        # Document class
        self.outputFile.write("\\documentclass{article}\n")

        # include the appropriate package
        self.outputFile.write("\\usepackage{graphicx}")

        # Begin Document
        self.outputFile.write("\\begin{document}")

        # Make the title
        self.outputFile.write("\\maketitle\n")

        # Begin a section
        self.outputFile.write("\\section{Introduction}\n")

        # Bring in the PDF
        self.createCenteredPlot(self.pacePlot, "Bryan Mooney Cycling Pace Histogram")

        # Print out the numbers 1 through 10
        #for i in range(100):
        #    self.outputFile.write("" + str(i) + "\\\\" + "\n")

        # End Document
        self.outputFile.write("\\end{document}\n")

    # Create a method to make a centered plot with a given title
    # This method should take the name of the file and the description as arguments
    def createCenteredPlot(self, fileName, description):

        # Center the plot
        self.outputFile.write("\\begin{center}\n" +
                              "\\includegraphics[scale=0.2]{" + fileName + "}\n" +
                              "\\textbf{" + description + "}\n" +
                              "\\end{center}")

# Test
test = reportGenerator_beta("bikingPace_BryanMooney.png")
print("It Worked.")
