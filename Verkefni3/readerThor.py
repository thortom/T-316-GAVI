import pandas as pd
import csv as csv

def getUsEconomicConstant(fileName):
    csvIn = open(fileName, newline='')
    dialect = csv.Sniffer().sniff(csvIn.read(1024))
    csvIn.seek(0)
    # TODO: use this...
    # data = pd.read_csv(fileName, dialect=dialect, header=None, engine='python', encoding='ISO-8859-2')
    # print('data', data)

    lines = csv.reader(csvIn, dialect)
    lines = list(lines)

    for i in lines:
        print(i)
    csvIn.close()


if __name__ == '__main__':
    fileName = "data/us_economic_constant.csv"
    getUsEconomicConstant(fileName)