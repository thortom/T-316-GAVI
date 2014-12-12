import sys
import os
import csv
import numpy as np
import pandas as pd

class import_data():
    def __init__(self, mydb):
        self.mydb = mydb

        print("Looking for data")
        self.findData()
        print("Got the data")

    def findData(self):
        #Finds .dat files in the folder /data
        dataFiles=[]
        path = os.getcwd()+"\data"
        for file in os.listdir(path):
            if file.endswith(".dat"):
                self.readData(path+'\\'+file)