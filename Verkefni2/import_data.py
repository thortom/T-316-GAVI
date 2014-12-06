import sys
import os
import numpy as np
import pandas as pd

class import_data():
    def __init__(self):
        dataFiles = self.findData()
        for file in dataFiles:
            self.readDat(file)
        pass

    def findData(self):
        #Finds .dat files in the folder /data
        dataFiles = []
        for file in os.listdir(os.getcwd()+"\data"):
            if file.endswith(".dat"):
                dataFiles.append(file)

        return dataFiles

    def readDat(self,file):
        print(file)
        if file == "movies.dat":
            df = pd.read_csv('data/'+file,delimiter='::', header=None,engine='python')
            #print(df)
            return df
        return None


