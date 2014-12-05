import sys
import os
import numpy as np
import pandas as pd

class import_data():
    def __init__(self):
        self.findData()
        pass

    def findData(self):
        #Finds .dat files in the folder /data
        for file in os.listdir(os.getcwd()+"\data"):
            if file.endswith(".dat"):
                print(file)
        pass

    def readDat(self):
        pass


