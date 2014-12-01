import csv as csv
import pandas as pd
import numpy as np
#import numexpr

class ReadCSVRowHeader:

    def __init__(self, fileName, numbDataRow, numbDataCol):

        test = []
        islendingar = []
        utlendingar = []
        csvFile = open(fileName)
        textInFile = csv.reader(csvFile)
        for idx, line in enumerate(textInFile):
            if idx%2 == 0:
                islendingar.append(line[2::])
            else:
                utlendingar.append(line[2::])
            test.append(line)

        pandaData = pd.DataFrame(test)
        # print(pandaData)

        # print(pandaData.iloc[:,2])

        # print(islendingar)

        islendingarGisti = []
        islendingarGesta = []
        utlendingarGisti = []
        utlendingarGesta = []
        # print(len(utlendingar[0]))
        for i in range(len(utlendingar)):
            tempIsGisti = []
            tempIsGesta = []
            tempUtGisti = []
            tempUtGesta = []
            for j in range(len(utlendingar[0])):
                if j%2 == 0:
                    try:
                        tempIsGesta.append(float(islendingar[i][j]))
                    except ValueError:
                        tempIsGesta.append(0)
                    try:
                        tempUtGesta.append(float(utlendingar[i][j]))
                    except ValueError:
                        tempUtGesta.append(0)
                else:
                    try:
                        tempIsGisti.append(float(islendingar[i][j]))
                    except ValueError:
                        tempIsGisti.append(0)
                    try:
                        tempUtGisti.append(float(utlendingar[i][j]))
                    except ValueError:
                        tempUtGisti.append(0)
            islendingarGesta.append(tempIsGesta)
            utlendingarGesta.append(tempUtGesta)
            islendingarGisti.append(tempIsGisti)
            utlendingarGisti.append(tempUtGisti)

        # print(islendingarGesta)
        self.dfIslendingarGesta = pd.DataFrame(islendingarGesta)
        self.dfUtlendingarGesta = pd.DataFrame(utlendingarGesta)
        self.dfIslendingarGisti = pd.DataFrame(islendingarGisti)
        self.dfUtlendingarGisti = pd.DataFrame(utlendingarGisti)
        

    def getData(self):
        return self.dfIslendingarGesta, self.dfUtlendingarGesta, self.dfIslendingarGisti, self.dfUtlendingarGisti

if __name__ == '__main__':
    test = ReadCSVRowHeader('GistingarAllt-MonthsVsYears.csv', 2, 2)