################################
## XML to CSV File Conversion ##
## Logan Grim & Steve Moors ####
## 2018 ########################
################################

from xml.dom import minidom

class xmlToCSV:

    def __init__(self, inputFile, outputFile):

        ########################
        ## Instance Variables ##
        ########################

        # Open the output file for writing
        self.outputFile = open(outputFile, "w")

        # save the inputFile name
        self.inputFile = inputFile

        # Parse the XML file
        self.parseXML()

        # Close the output file
        self.outputFile.close()

    #############
    ## Methods ##
    #############

    # The main method for parsing the XML data into CSV format
    def parseXML(self):

        # get the xml info
        xmlInfo = minidom.parse(self.inputFile)

        # Start saving lists of each tag type that we are interested in

        # Heart Rate Tags
        # Note these contain sub tags named "value"
        heartRateBPMs = xmlInfo.getElementsByTagName('HeartRateBpm')

        # Grab the numerical Heart Rate values and put them in a list
        heartRateValues = []

        for tag in heartRateBPMs:
            heartRateValues.append(tag.getElementsByTagName("Value")[0].firstChild.nodeValue)

        print(heartRateValues)

        # Speed tags
        speedTags = xmlInfo.getElementsByTagName('ns3:Speed')

        # Grab the numerical speed values and put them in a list
        speeds = []

        for tag in speedTags:
            speeds.append(tag.firstChild.nodeValue)

        print(speeds)

        # Run cadence tags
        runCadenceTags = xmlInfo.getElementsByTagName('ns3:RunCadence')

        # Grab the numerical run cadence values and put them in a list

        runCadences = []

        for tag in runCadenceTags:
            runCadences.append(tag.firstChild.nodeValue)

        print(runCadences)

        # Write the data to the output file
        # Each column is an attribute
        # The structure is as follows:
        #   Heart Rate BPM, Speed, Run Cadence
        for i in range(len(heartRateValues)):
            self.outputFile.write(heartRateValues[i] + ", " + speeds[i] + ", " + runCadences[i] + "\n" )


##########
## Test ##
##########

obj = xmlToCSV("MoorsFTP_run.txt", "outputFile.csv")

