################################
## XML to CSV File Conversion ##
## Logan Grim & Steve Moors ####
## 2018 ########################
################################

from xml.dom import minidom

class xmlToCSV:

    def __init__(self, inputFile, outputFile, isRunningFile):

        ########################
        ## Instance Variables ##
        ########################

        # Open the output file for writing
        self.outputFile = open(outputFile, "w")

        # save the inputFile name
        self.inputFile = inputFile

        # save the boolean that represents whether or not the
        # input file is a running file or a biking file
        self.isRunningFile = isRunningFile

        ########################

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

        # Heart Rate Tags
        # Note these contain sub tags named "value"
        heartRateBPMs = xmlInfo.getElementsByTagName('HeartRateBpm')

        # Grab the numerical Heart Rate values and put them in a list
        heartRateValues = []

        for tag in heartRateBPMs:
            heartRateValues.append(tag.getElementsByTagName("Value")[0].firstChild.nodeValue)

        # Speed tags
        speedTags = xmlInfo.getElementsByTagName('ns3:Speed')

        # Grab the numerical speed values and put them in a list
        speeds = []

        for tag in speedTags:
            speeds.append(tag.firstChild.nodeValue)

        # Only grab this data if it is a running file
        if self.isRunningFile:
            # Run cadence tags
            runCadenceTags = xmlInfo.getElementsByTagName('ns3:RunCadence')

            # Grab the numerical run cadence values and put them in a list

            runCadences = []

            for tag in runCadenceTags:
                runCadences.append(tag.firstChild.nodeValue)

        # Only grab this data if it is a biking file
        if not self.isRunningFile:

            # Bike Cadence Tags
            bikeCadenceTags = xmlInfo.getElementsByTagName("Cadence")

            # Grab the numerical bike cadence values and put them in a list
            bikeCadences = []

            for tag in bikeCadenceTags:
                bikeCadences.append(tag.firstChild.nodeValue)

            # Power tags
            powerTags = xmlInfo.getElementsByTagName("ns3:Watts")

            # Grab the numerical tag values and put them in a list
            powers = []

            for tag in powerTags:
                powers.append(tag.firstChild.nodeValue)


        # Write the data to the output file
        # Each column is an attribute
        # The structure is as follows:
        #   Heart Rate BPM, Speed, Run Cadence
        #   NOTE: The bike files have a different third column (bike cadence) and a 4th column (power) :
        #   Heart Rate BPM, Speed, Bike Cadence, Power

        # Handle the case where there is not an equal number of each attribute
        if self.isRunningFile:
            numberOfObjects = min(len(heartRateValues), len(speeds), len(runCadences))
        else:
            numberOfObjects = min(len(heartRateValues), len(speeds), len(bikeCadences), len(powers))

        for i in range(numberOfObjects):
            if self.isRunningFile:
                self.outputFile.write(heartRateValues[i] + ", " + speeds[i] + ", " + runCadences[i] + "\n" )
            else:
                self.outputFile.write(heartRateValues[i] + ", " + speeds[i] + ", " + bikeCadences[i] + ", " + powers[i] + "\n")

##########
## Test ##
##########

obj = xmlToCSV("MoorsFTP_run.txt", "runningOutput.csv", True)

obj1 = xmlToCSV("MooneyBikeFTP.txt", "bikingOutput.csv", False)

