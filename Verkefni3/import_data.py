import sys
import os
import csv
import numpy as np
import pandas as pd
import readerThor as th
import readerLarus as li

class import_data():
    def __init__(self, mydb):
        self.mydb = mydb

        print("Looking for data")
        self.findData()
        print("Got the data")

    def findData(self):
        # This should collect panda DataFrames
        self.usEconomicConstant = th.getUsEconomicConstant("data/us_economic_constant.csv")
        self.usMilitaryConstant = th.getUsMilitaryConstant("data/us_military_constant.csv")
        self.worldDevelopmentIndicators = th.getWorldDevelopmentIndicators("data/20_Topic_en_csv_v2.csv")
        self.worldBankDev = li.getWorldBankDev("data/worldbank_data_worlddev.csv")
        self.unemploymentMen = li.getUnemploymentMen("data/unemployment_worldbank/men.csv")

    def createTable(self):
    	self.mydb.cursor.execute("DROP TABLE IF EXISTS world_info")
        self.mydb.cursor.execute("CREATE TABLE world_info(country TEXT)")
