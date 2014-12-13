import pandas as pd
import csv as csv
import re                       # imports regular expression


def getUnemploymentMen(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG', index_col=[0, 1, 2, 3, 4, 5])
    #print(data.columns)
    return data

if __name__ == '__main__':
    fileName = "data/unemployment_worldbank/men.csv"
    getUnemploymentMen(fileName)