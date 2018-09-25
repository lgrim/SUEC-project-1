##############################
## Copyright 2018 ############
## Logan Grim & Steve Moors ##
##############################

from xml.dom import minidom

class ConvertXMLToCSV():
    def __init__(self):
        """Convert training peaks data files from XML to CSV"""
        pass

    def XML_to_CSV(self, input_file_name, output_file_name, is_running_file=True):
        """Convert training peaks data files from XML to CSV"""

        output_file = open(output_file_name, "w")
        xml_info = minidom.parse(input_file_name)

        # Heart Rate
        heart_rate_tags = xml_info.getElementsByTagName('HeartRateBpm')
        heart_rates = [tag.getElementsByTagName("Value")[0].firstChild.nodeValue for tag in heart_rate_tags]

        # Speed
        speed_tags = xml_info.getElementsByTagName('ns3:Speed')
        speeds = [tag.firstChild.nodeValue for tag in speed_tags]

        # Run and bike specific tags
        if is_running_file:
            # Run cadences
            run_cadence_tags = xml_info.getElementsByTagName('ns3:RunCadence')
            run_cadences = [tag.firstChild.nodeValue for tag in run_cadence_tags]
        else:
            # Bike cadences
            bike_cadence_tags = xml_info.getElementsByTagName("Cadence")
            bike_cadences = [tag.firstChild.nodeValue for tag in bike_cadence_tags]

            # Power readings
            power_tags = xml_info.getElementsByTagName("ns3:Watts")
            powers = [tag.firstChild.nodeValue for tag in power_tags]

        # Handle the case where there is not an equal number of each attribute
        if is_running_file:
            number_of_objects = min(len(heart_rates), len(speeds), len(run_cadences))
        else:
            number_of_objects = min(len(heart_rates), len(speeds), len(bike_cadences), len(powers))

        # Write the new
        for i in range(number_of_objects):
            if is_running_file:
                output_file.write(heart_rates[i] + ", " + speeds[i] + ", " + run_cadences[i] + "\n")
            else:
                output_file.write(
                    heart_rates[i] + ", " + speeds[i] + ", " + bike_cadences[i] + ", " + powers[i] + "\n")
