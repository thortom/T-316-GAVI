import pandas as pd
import numpy as np
import csv as csv
import chardet    
import re                       # imports regular expression


def getUsEconomicConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=[0, 1])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
    # print(data.T['Afghanistan']['Child Survival and Health'])
    return data

def getUsMilitaryConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    data = pd.read_csv(fileName, dialect=dialect, encoding='ISO-8859-1', skiprows=6, thousands=',', header=0, index_col=0)

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.columns = [re.sub('\D','',x) for x in data.columns]                                # used regular expression to replace all non digital values with ''
    data.drop('', axis=1, inplace=True)                                                     # Drop unused columns
    return data

def getWorldDevelopmentIndicators(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    csvIn.close()

    # Used chardetect module to detect encoding
    data = pd.read_csv(fileName, dialect=dialect, encoding='UTF-8-SIG', skiprows=2, thousands=',', header=0, index_col=[0, 2])

    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.dropna(axis=1, how='all', inplace=True)                                            # Drop nan columns
    data.drop('Country Code', axis=1, inplace=True)                                         # Drop unused columns
    data.drop('Indicator Code', axis=1, inplace=True)                                       # Drop unused columns
    # print('data', data.head())
    return data

def getGDPgrowth(fileName):
    # The CSV sniffer did not work

    data = pd.read_csv(fileName, delimiter=',', encoding='ISO-8859-1', header=0, index_col=0, error_bad_lines=False)

    data[data=='n/a'] = np.nan                                                              # Change n/a string to NaN pandas value
    data.dropna(axis=0, how='all', inplace=True)                                            # Drop nan rows
    data.dropna(axis=1, how='all', inplace=True)                                            # Drop nan columns
    # print('data', data.head())
    return data

def plotter(x, y):
    plt.plot(x, y)
    plt.show()

def subOptions(data):
    print('Sub options', data.T.index)
    plotThisSub = input('Data to plot:')
    return plotThisSub

if __name__ == '__main__':
    import pylab as plt

    fileName = "data/us_economic_constant.csv"
    usEconomic = getUsEconomicConstant(fileName)
    # print(usEconomic.head())

    fileName = "data/us_military_constant.csv"
    usMilitary = getUsMilitaryConstant(fileName)
    # print(usMilitary.head())

    fileName = "data/20_Topic_en_csv_v2.csv"
    worldDev = getWorldDevelopmentIndicators(fileName)
    # print(worldDev.head())

    fileName = "data/dm-export-20141211.csv"
    gdpGrowth = getGDPgrowth(fileName)
    # print(gdpGrowth.head())

    # options = {'usEconomic': usEconomic, 'usMilitary': usMilitary, 'worldDev': worldDev, 'gdpGrowth': gdpGrowth}

    # while True:
    #     print('options: ', options.keys())
    #     toUse = input('Data to use:')
    #     data = options.get(toUse)
    #     print('Sub options', data.index)
    #     plotThis = input('Data to plot:')
    #     print(data.T[plotThis])
    #     print(list(data.T[plotThis]))
    #     if type(list(data.T[plotThis])[0]) != int:
    #         plotThisSub = subOptions(data.T[plotThis])
    #         plotter([int(x) for x in data.columns], list(data.T[plotThis][plotThisSub]))
    #     else:
    #         plotter([int(x) for x in data.columns], list(data.T[plotThis]))


    # print('gdpGrowth', gdpGrowth.head())
    # timeLine = [int(year) for year in gdpGrowth.columns]
    # print(timeLine)
    # print(gdpGrowth.index)
    # print(gdpGrowth.T['World'])
    # plt.plotbar(timeLine, list(gdpGrowth.T['World']))
    # plt.show()
