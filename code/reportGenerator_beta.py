###########################################
## Practice Report Generator ##############
## Typeset results in LATEX using python ##
## Logan Grim and Steve Moors #############
## 2018 ###################################
###########################################

class reportGenerator_beta:

    def __init__(self):

        # Instance Variables
        self.outputFile = open("testTex.tex", "w")

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

        # Begin Document
        self.outputFile.write("\\begin{document}")

        # Make the title
        self.outputFile.write("\\maketitle\n")

        # End Document
        self.outputFile.write("\\end{document}\n")

# Test
test = reportGenerator_beta()