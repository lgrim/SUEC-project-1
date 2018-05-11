import numpy as np

class LoadData():

    def __init__(self):
        pass

    def load_csv(self, file_name):
        return np.loadtxt(file_name, delimiter=",")