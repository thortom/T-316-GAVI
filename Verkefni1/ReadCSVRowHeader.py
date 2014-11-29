import csv as csv
import pandas as pd
import numpy as np
#import numexpr

class ReadCSVRowHeader:

    def __init__(self, fileName, numbDataRow, numbDataCol):

        data = []
        csvFile = open(fileName)
        textInFile = csv.reader(csvFile)
        for line in textInFile:
            data.append(line[2::])
        dfData = pd.DataFrame(data)
        print(dfData)

        

if __name__ == '__main__':
    test = ReadCSVRowHeader('GistingarAllt-MonthsVsYears.csv', 2, 2)