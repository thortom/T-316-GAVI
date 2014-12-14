import pandas as pd
import csv as csv
import re                       # imports regular expression


def getWorldBankDev(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(2048))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='ascii',index_col=[0,2])
    #data.dropna(axis=0, how='all', inplace=True)
    return data
def getWorldBankEdu(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG',thousands=',',error_bad_lines=False, index_col=False)
    #print(data.columns)
    return data

if __name__ == '__main__':
    fileName = "data/WDI_Data.csv"
    #testdata = getWorldBankDev(fileName)

    #fileName = "data/worldbank_data_education.csv"
    #testdata2 = getWorldBankEdu(fileName)
