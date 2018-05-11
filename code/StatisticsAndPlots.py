import numpy as np
from matplotlib import pyplot


class StatisticsAndPlots():

    def __init__(self):
        pass

    def get_average_heart_rate(self, data):
        return np.average(data[:,0])

    def get_average_speed(self, data):
        return np.average(data[:,1])

    def get_average_cadence(self, data):
        return np.average(data[:,2])

    def get_average_power(self, data, is_running_file):
        if is_running_file:
            return
        return np.average(data[:,3])

    def make_pace_histogram(self, data, date, athlete_name):
        pyplot.hist(data[:,1], edgecolor="black")
        pyplot.suptitle("Speed Histogram")
        pyplot.xlabel("Speeds")
        pyplot.ylabel("Frequency")
        image_name = "histograms/pace_histogram_" \
                      + date \
                      + "_" \
                      + athlete_name \
                      + ".png"
        pyplot.savefig(image_name)
        pyplot.close()
        return image_name

    def make_zone_histogram(self, data, date, athlete_name):
        avg_speed = self.get_average_speed(data)
        speeds = [speed / avg_speed for speed in data[:,1]]
        speeds = np.asarray(speeds)
        zone_one = speeds[(speeds >= 0) & (speeds < 0.7)]
        zone_two = speeds[(speeds >= 0.7) & (speeds < 0.8)]
        zone_three = speeds[(speeds >= 0.8) & (speeds < 0.9)]
        zone_four = speeds[(speeds >= 0.9) & (speeds < 1)]
        zone_five = speeds[(speeds >= 1) & (speeds < 1.1)]
        zone_six = speeds[speeds >= 1.1]
        zones = [zone_one, zone_two, zone_three, zone_four, zone_five, zone_six]
        pyplot.bar(np.arange(len(zones)), [len(zone) for zone in zones], edgecolor="black")
        pyplot.suptitle("Zone Histogram")
        pyplot.xlabel("Zones")
        pyplot.ylabel("Frequency")
        image_name = "histograms/zone_histogram_" \
                     + date \
                     + "_" \
                     + athlete_name \
                     + ".png"
        pyplot.savefig(image_name)
        pyplot.close()
        return image_name

    def make_raw_plot(self, data, date, athlete_name):
        f, axarr = pyplot.subplots(2, sharex=True)
        axarr[0].plot(data[:,0], color="blue")
        axarr[0].set_title("Raw Speed and Heart Rate vs. Time")
        axarr[0].set_ylabel("Heart Rate")
        axarr[1].plot(data[:,1], color="red")
        axarr[1].set_ylabel("Speed")
        axarr[1].set_xlabel("Time")
        image_name = "plots/speed_heart_rate_raw_" \
                     + date \
                     + "_" \
                     + athlete_name \
                     + ".png"
        pyplot.savefig(image_name)
        pyplot.close()
        return image_name