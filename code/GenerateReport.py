##############################
## Copyright 2018 ############
## Logan Grim & Steve Moors ##
##############################

from LoadData import LoadData
from StatisticsAndPlots import StatisticsAndPlots

class GenerateReport():
    def __init__(self):
        """ Generate Automated Running and Biking Reports.
            Creates the .tex file that is compiled into the pdf report."""
        self.number_of_files_created = 0

    # date here is not the latex bit, it should be a string for filenames
    def generate_report(self, input_file_name, output_file_name, athlete_name, is_running_file, date):
        """
        :param input_file_name: Name of the csv file containing data
        :param output_file_name: Name of the tex file that is generated
        :param athlete_name: Name of the athlete separated by an underscore
        :param is_running_file: Boolean, either true or false
        :param date: The date associated with the file in format 'yyyy_mm_dd'
        :return: Nothing

        Generate the tex file that will later be compiled into a pdf.
        """
        data = LoadData().load_csv(input_file_name)
        stats = StatisticsAndPlots()
        self.build_tex(output_file_name, athlete_name, is_running_file, ("%.2f" % stats.get_average_speed(data)),
                       ("%.2f" % stats.get_average_heart_rate(data)), ("%.2f" % stats.get_average_cadence(data)),
                       (None if is_running_file else "%.2f" % stats.get_average_power(data, is_running_file)),
                       stats.make_pace_histogram(data, date, athlete_name),
                       stats.make_zone_histogram(data, date, athlete_name),
                       stats.make_raw_plot(data, date, athlete_name), date)
        self.number_of_files_created += 1

    def build_tex(self, output_file_name, athlete_name, is_running_file,
                   avg_speed, avg_heart_rate, avg_cadence, avg_power,
                   raw_hist_file_name, zone_hist_file_name,
                   raw_plot_file_name,
                   date="\\today"):
        """
        :param output_file_name: Name of the tex file that is generated
        :param athlete_name: Name of the athlete separated by an underscore
        :param is_running_file: Boolean, either true or false
        :param avg_speed: Average speed over the course of the entire file
        :param avg_heart_rate: Average heart rate over the course of the entire file
        :param avg_cadence: Average cadence over the course of the entire file
        :param avg_power: Average power over the course of the entire file
        :param raw_hist_file_name: Name of the raw data histogram file
        :param zone_hist_file_name: Name of the zone histogram file
        :param raw_plot_file_name: Name of the time-series plot file
        :param date: The date associated with the file in format 'yyyy_mm_dd'
        :return: Nothing. Just writes a file.

        Build the tex file and write it.
        """
        output_file = open(output_file_name, "w")
        output_file.write(self.doc_class_and_packages())
        output_file.write(self.title_string(is_running_file))
        output_file.write(self.author_string(athlete_name))
        output_file.write(self.date_string(date))

        output_file.write("\\begin{document}\n")
        output_file.write(self.make_title())

        output_file.write("\\begin{center}\n")
        output_file.write("\\textbf{Averages}\n")
        output_file.write("\\hspace{2in}\n")
        output_file.write("\\textbf{Zones}\n")
        output_file.write("\\end{center}\n")

        output_file.write("\\begin{center}\n")
        output_file.write(self.table_one(avg_speed, avg_heart_rate,
                                         avg_cadence, avg_power,
                                         is_running_file))
        output_file.write("\\hspace{1in}\n")
        output_file.write(self.table_two())
        output_file.write("\\end{center}\n")

        output_file.write("\\begin{center}\n")
        output_file.write(self.place_image(raw_hist_file_name, scale=0.4))
        output_file.write("\\hspace{0.5in}\n")
        output_file.write(self.place_image(zone_hist_file_name, scale=0.4))
        output_file.write("\\end{center}\n")

        output_file.write("\\begin{center}\n")
        output_file.write(self.place_image(raw_plot_file_name, scale=0.8))
        # output_file.write("\\hspace{0.5in}\n")
        # output_file.write(self.place_image(filtered_plot_file_name, scale=0.1))
        output_file.write("\\end{center}\n")

        output_file.write("\\end{document}\n")

        output_file.close()

    def title_string(self, is_running_file):
        """
        :param is_running_file: Boolean, either true or false
        :return: The Title string of the pdf report

        Build the title of the report
        """
        return "\\title{Summit Ultra Endurance Coaching\\\\\n" \
                 + ("Run Outline}\n" if is_running_file else "Bike Outline}\n")

    def author_string(self, athlete_name):
        athlete_name_list = athlete_name.split("_")
        athlete_name = athlete_name_list[0] + " " + athlete_name_list[1]
        return "\\author{" + athlete_name + "}\n"

    def date_string(self, date="\\today"):
        date_list = date.split("_")
        return "\\date{" + date_list[0] + " " \
               + date_list[1] + " " \
               + date_list[2] + "}\n"

    def doc_class_and_packages(self):
        return "\\documentclass{article}\n\\usepackage{graphicx}\n" \
                + "\\usepackage[a4paper,top=1in,bottom=1in,left=1in,right=1in]" \
                + "{geometry}\n"

    def make_title(self):
        return "\\maketitle\n"

    def table_one(self, avg_speed, avg_heart_rate, avg_cadence, avg_power,
                  is_running_file):
        return "\\begin{tabular}{l c c}\n" \
                 + "Average Speed/Pace: & " \
                 + str(avg_speed) \
                 + " \\\\\n" \
                 + "Average Heart Rate: & " \
                 + str(avg_heart_rate) \
                 + " \\\\\n" \
                 + "Average Cadence: & " \
                 + str(avg_cadence)   \
                 + ("" if is_running_file else " \\\\") \
                 + "\n" \
                 + ("" if is_running_file else "Average Power: & ") \
                 + ("" if is_running_file else str(avg_power)) \
                 + ("" if is_running_file else "\n") \
                 + "\\end{tabular}\n"

    def table_two(self):
        return "\\begin{tabular}{l c c}\n" \
               + "Zone & \\% of Average Speed \\\\\n" \
               + "Zone 1 & 0\\% - 70\\% \\\\\n" \
               + "Zone 2 & 70\\% - 80\\% \\\\\n" \
               + "Zone 3 & 80\\% - 90\\% \\\\\n" \
               + "Zone 4 & 90\\% - 100\\% \\\\\n" \
               + "Zone 5a & 100\\% - 110\\% \\\\\n" \
               + "Zone 5b & 110\\% - 120\\% \n" \
               + "\\end{tabular}\n"

    def table_three(self):
        pass

    def place_image(self, image_file_name, scale=0.2):
        return "\\includegraphics[scale=" \
                + str(scale) \
                + "]{" \
                + str(image_file_name) \
                + "}\n"