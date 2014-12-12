import pandas as pd
import csv as csv
import re                       # imports regular expression

allButNumbers = '''abcdefghijklmnopqrstuvxiz!"#$%&/()=\\-?*+´'^'''

def getUsEconomicConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # use regular expression to replace all non digital values with ''
    # print(data['Country Name']['Afghanistan'])
    # print(data.T['Afghanistan']['Child Survival and Health'])
    # print('data', data.head())
    return data

def getUsMilitaryConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # use regular expression to replace all non digital values with ''
    # print('data', data.head())
    return data

if __name__ == '__main__':
    # fileName = "data/us_economic_constant.csv"
    # getUsEconomicConstant(fileName)
    fileName = "data/us_military_constant.csv"
    getUsMilitaryConstant(fileName)