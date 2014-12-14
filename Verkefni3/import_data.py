import sys
import os
import csv
import numpy as np
import pandas as pd
import readerThor as th
import readerLarus as li
import re
import psycopg2

class import_data():
    mainTable = "world_info"

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
        self.worldBankDev = li.getWorldBankDev("data/WDI_Data.csv")
        #self.worldBankEdu = li.getWorldBankEdu("data/worldbank_data_education.csv")

        # print(self.worldBankDev)

        # TODO: Do not create table each time
        self.createTable(self.worldBankDev)
        # self.addData(self.worldBankDev)

    def createTable(self, dataFrame):
        fileName = 'C:/temp.csv'
        stacked = dataFrame.stack()
        data = stacked.unstack(1)
        data.to_csv(fileName)

        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %self.mainTable)
        columns = '(country TEXT, year INT, '
        for column in data.columns:
            columns += str(column).replace(".","_") + ' real, '
        columns = columns[:-2] + ')'
        self.mydb.cursor.execute("CREATE TABLE %s %s" %(self.mainTable, columns))
        # # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(self.mainTable, fileName))
        self.mydb.cursor.execute("CREATE INDEX country_idx ON %s (country);" %self.mainTable)
        self.mydb.cursor.execute("CREATE INDEX year_idx ON %s (year);" %self.mainTable)

        os.remove(fileName)


    def addData(self, dataFrame, category=None):
        parentIndex = dataFrame.index[0]

        print('index: ', dataFrame.index)
        print('len(index)', len(dataFrame.index))
        sizeOfIndex = len(dataFrame.index)
        for index in dataFrame.index:
            # print('index:', index)
            # There is not always subIndex
            parentIndex, subIndex = index[0], index[1]
            fixedParentIndex = parentIndex.replace("'","''")
            # print("Add this to table ->", dataFrame.T[parentIndex][subIndex])
            columnName = 'a'+re.sub('\W', '_', subIndex).lower()
            for year, data in dataFrame.T[parentIndex][subIndex].T.iteritems():
                # print('Add this year data: ', year, data)
                # TODO: fix for better solution
                if np.isnan(data):
                    data = 0                            # Put SQL Null value
                s = '''UPDATE %s SET %s=%s WHERE country='%s' and year=%s;
                            INSERT INTO %s (country, year, %s)
                               SELECT '%s', %s, %s
                               WHERE NOT EXISTS (SELECT 1 FROM %s WHERE country='%s' and year=%s);''' %(self.mainTable, columnName, data, fixedParentIndex, year, self.mainTable, columnName, fixedParentIndex, year, data, self.mainTable, fixedParentIndex, year)
                # print('s', s)
                try:
                    self.mydb.cursor.execute(s)
                except psycopg2.ProgrammingError:
                    self.mydb.cursor.execute("ALTER TABLE %s ADD column %s real" %(self.mainTable, columnName))
                    self.mydb.cursor.execute(s)

    def removeData(self, category):
        # TODO: Remove a category from world_info table
        pass
