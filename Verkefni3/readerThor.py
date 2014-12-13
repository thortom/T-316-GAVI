import pandas as pd
import csv as csv
import re                       # imports regular expression


def getUsEconomicConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    # TODO: use chardetect module to detect encoding
    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
    # print(data['Country Name']['Afghanistan'])
    # print(data.T['Afghanistan']['Child Survival and Health'])
    # print('data', data.head())
    return data

def getUsMilitaryConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    # TODO: use chardetect module to detect encoding
    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
    # print('data', data.head())
    return data

def getWorldDevelopmentIndicators(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    # TODO: use chardetect module to detect encoding
    data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG', skiprows=2, thousands=',', header=0, index_col=[0, 2])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.dropna(axis=1, how='all', inplace=True)                                            # Drop nan columns
    data.drop('Country Code', axis=1, inplace=True)                                         # Drop unused columns
    data.drop('Indicator Code', axis=1, inplace=True)                                       # Drop unused columns
    # print('data', data.head())
    return data

if __name__ == '__main__':
    # fileName = "data/us_economic_constant.csv"
    # getUsEconomicConstant(fileName)
    # fileName = "data/us_military_constant.csv"
    # getUsMilitaryConstant(fileName)
    fileName = "data/20_Topic_en_csv_v2.csv"
    getWorldDevelopmentIndicators(fileName)