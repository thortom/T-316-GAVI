import sys
import os
import csv
import numpy as np
import pandas as pd
import re
import psycopg2
import shutil

class import_data():
    mainTable = "world_info"

    def __init__(self, mydb):
        self.mydb = mydb

    def findData(self):
        # This should collect panda DataFrames
        # self.usEconomicConstant = self.getUsEconomicConstant("data/us_economic_constant.csv")
        # self.usMilitaryConstant = self.getUsMilitaryConstant("data/us_military_constant.csv")
        self.worldDevelopmentIndicators = self.getWorldDevelopmentIndicators("data/20_Topic_en_csv_v2.csv")
        #self.worldBankEdu = self.getWorldBankEdu("data/worldbank_data_education.csv")

        self.worldBankDev = self.getWorldBankDev("data/WDI_Data.csv")

        self.createTable(self.worldBankDev)
        self.createNoteTable('data/WDI_CS_Notes.csv', 'data/WDI_Data.csv')
        self.createWorldTable('data/country.txt')

        # self.addData(self.usEconomicConstant)

    def createWorldTable(self,fileName):
        tempFile = 'C:/country.txt'
        shutil.copyfile(fileName, tempFile)
        lableTable = 'Country'

        self.mydb.cursor.execute("SET CLIENT_ENCODING TO 'LATIN1';")
        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %lableTable)
        self.mydb.cursor.execute("CREATE TABLE %s (name varchar(50));" %(lableTable))
        self.mydb.cursor.execute("COPY Country from '%s';" %tempFile)

        os.remove(tempFile)

    def createNoteTable(self, noteFile, wdiDataFile):
        tempFile = 'C:/test.csv'

        lableTable = 'lable'
        shutil.copyfile(wdiDataFile, tempFile)
        wdiDataFile = tempFile

        # Country Name  Country Code    Indicator Name  Indicator Code
        self.mydb.cursor.execute("SET CLIENT_ENCODING TO 'LATIN1';")
        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %lableTable)
        columns = '(country TEXT, country_code TEXT , series_code_text TEXT, series_code TEXT, '
        for year in range(1960, 2015):
            columns += '_' + str(year) + ' real, '
        columns = columns[:-2] + ')'

        self.mydb.cursor.execute("CREATE TABLE %s %s" %(lableTable, columns))
        # # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(lableTable, wdiDataFile))

        for year in range(1960, 2015):
            self.mydb.cursor.execute("ALTER TABLE %s DROP COLUMN %s" %(lableTable, '_'+str(year)))
        self.mydb.cursor.execute("ALTER TABLE %s DROP COLUMN country" %lableTable)
        self.mydb.cursor.execute("ALTER TABLE %s DROP COLUMN country_code" %lableTable)      

        self.mydb.cursor.execute('''CREATE TABLE tmp (series_code_text TEXT, series_code TEXT);
        INSERT INTO tmp SELECT DISTINCT lable.series_code_text, lable.series_code FROM lable;
        DROP TABLE lable;
        ALTER TABLE tmp RENAME TO lable;''')

        self.mydb.cursor.execute("ALTER TABLE %s ADD COLUMN description TEXT" %lableTable)

        noteTable = 'notes'
        shutil.copyfile(noteFile, tempFile)
        noteFile = tempFile

        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %noteTable)
        columns = '(country_code TEXT, series_code TEXT ,description TEXT)'
        self.mydb.cursor.execute("CREATE TABLE %s %s" %(noteTable, columns))
        # # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(noteTable, noteFile))


        self.mydb.cursor.execute('''UPDATE lable SET description=notes.description from notes
                                WHERE lable.series_code=notes.series_code;''')

        os.remove(tempFile)

    def createTable(self, dataFrame):
        fileName = 'C:/temp.csv'
        stacked = dataFrame.stack()
        data = stacked
        print('data', data)
        data.to_csv(fileName)

        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %self.mainTable)
        columns = '(country TEXT, series TEXT, year INT, value real)'
        self.mydb.cursor.execute("CREATE TABLE %s %s" %(self.mainTable, columns))
        # # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(self.mainTable, fileName))
        # TODO: index
        self.mydb.cursor.execute("CREATE INDEX world_idx ON %s (country, series, year);" %self.mainTable)

        os.remove(fileName)

    # TODO: refactor this function
    def addData(self, fileName):
        dataFrame = self.getNewData(fileName)
        tmpfile = 'C:/temp.csv'
        dataFrame.to_csv(tmpfile)
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(self.mainTable, tmpfile))
        os.remove(tmpfile)

    def getNewData(self, fileName):
        dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])
        data.dropna(axis=0, how='all', inplace=True)
        data.columns = [re.sub('\D','',x) for x in data.columns]
        data = data.stack()
        return data

    def getWorldBankDev(self, fileName):
        # dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, delimiter=',', encoding='ascii',index_col=[0,3])
        data.dropna(axis=0, how='all', inplace=True)
        data.drop('Country Code', axis=1, inplace=True)
        data.drop('Indicator Name', axis=1, inplace=True)
        return data

    def getWorldBankEdu(self, fileName):
        dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG',thousands=',',error_bad_lines=False, index_col=False)
        return data

    def getUsEconomicConstant(self, fileName):
        dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

        data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
        data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
        return data

    def getUsMilitaryConstant(self, fileName):
        dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=0)

        data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
        data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
        data.drop('', axis=1, inplace=True)                                                     # Drop unused columns
        return data

    def getWorldDevelopmentIndicators(self, fileName):
        # Used chardetect module to detect encoding
        dialect = self.sniffDialect(fileName)
        data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG', skiprows=2, thousands=',', header=0, index_col=[0, 2])

        data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
        data.dropna(axis=1, how='all', inplace=True)                                            # Drop nan columns
        data.drop('Country Code', axis=1, inplace=True)                                         # Drop unused columns
        data.drop('Indicator Code', axis=1, inplace=True)                                       # Drop unused columns
        return data

    def getGDPgrowth(self, fileName):
        # The CSV sniffer did not work
        data = pd.read_csv(fileName, delimiter=',', encoding='ISO-8859-1', header=0, index_col=0, error_bad_lines=False)

        data[data=='n/a'] = np.nan                                                              # Change n/a string to NaN pandas value
        data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
        data.dropna(axis=1, how='all', inplace=True)                                            # Drop nan columns
        return data

    def sniffDialect(self, fileName):
        csvIn = open(fileName, newline='')
        dialect = csv.Sniffer().sniff(csvIn.read(1024))
        csvIn.seek(0)
        csvIn.close()
        return dialect

    def removeData(self, category):
        # TODO: Remove a category from world_info table
        pass
