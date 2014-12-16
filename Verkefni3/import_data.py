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

        print("Looking for data")
        self.findData()
        print("Got the data")

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


    def createNoteTable2(self, noteFile, wdiDataFile):
        tempFile = 'C:/test.csv'
        noteTable = 'notes'
        shutil.copyfile(noteFile, tempFile)
        noteFile = tempFile

        self.mydb.cursor.execute("SET CLIENT_ENCODING TO 'LATIN1';")
        self.mydb.cursor.execute("DROP TABLE IF EXISTS %s" %noteTable)
        columns = '(country_code TEXT, series_code TEXT ,description TEXT)'
        self.mydb.cursor.execute("CREATE TABLE %s %s" %(noteTable, columns))
        # # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY %s FROM '%s' WITH CSV HEADER Delimiter as ','" %(noteTable, noteFile))

        lableTable = 'lable'
        shutil.copyfile(wdiDataFile, tempFile)
        wdiDataFile = tempFile

        # Country Name  Country Code    Indicator Name  Indicator Code
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

        self.mydb.cursor.execute("ALTER TABLE %s ADD COLUMN series_code_text TEXT" %noteTable)

        # TODO: fix this execute duplicates
        self.mydb.cursor.execute('''INSERT INTO %s (series_code_text, country_code, series_code, description)
            SELECT DISTINCT l.series_code_text, n.country_code, n.series_code, n.description
            FROM %s n, %s l
            WHERE n.series_code = l.series_code'''  %(noteTable, noteTable, lableTable))

        self.mydb.cursor.execute("DELETE FROM notes WHERE series_code_text IS NULL")

        os.remove(tempFile)

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

    # TODO: refactor this function
    def addData(self, dataFrame, category=None):
        parentIndex = dataFrame.index[0]

        sizeOfIndex = len(dataFrame.index)
        for index in dataFrame.index:
            # There is not always subIndex
            if len(index) == 2:
                parentIndex, subIndex = index[0], index[1]

                fixedParentIndex = parentIndex.replace("'","''")
                # print("Add this to table ->", dataFrame.T[parentIndex][subIndex])
                columnName = re.sub('\W', '_', subIndex).lower()
                for year, data in dataFrame.T[parentIndex][subIndex].T.iteritems():
                    # print('Add this year data: ', year, data)
                    if np.isnan(data):
                        data = 'NULL'                            # Put SQL Null value
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
            else:
                # TODO: use the category as added column
                print('Error: in addData() this function is not correctly used or unfinished')

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
