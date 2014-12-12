import sys
import os
import csv
import numpy as np
import pandas as pd
import readerThor as th

class import_data():
    def __init__(self, mydb):
        self.mydb = mydb

        print("Looking for data")
        self.findData()
        print("Got the data")

    def findData(self):
        # This should collect panda DataFrames
        self.usEconomicConstant = th.getUsEconomicConstant()