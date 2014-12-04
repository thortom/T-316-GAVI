import csv as csv
import pandas as pd
import numpy as np

class ReadCSVRowHeader:

    def __init__(self, fileName, sizeOfHeader, numbDataRow, numbDataCol):

        # Creates empty list of lists to store arrays of data in one list
        self.data = [[]]
        # This one assumes the first rows are summers
        for i in range((numbDataRow-1)+1):
            self.data.append([])

        csvFile = open(fileName)
        textInFile = csv.reader(csvFile)
        for idx, line in enumerate(textInFile):
            if idx < numbDataRow:
                self.data[numbDataRow].append(line[sizeOfHeader::])
                continue
            for i in range(numbDataRow):
                if idx%numbDataRow == i:
                    self.data[i].append(line[sizeOfHeader::])

        for i in range(numbDataRow):
            self.data[i] = self.splitforCol(self.data[i], numbDataCol)
        csvFile.close()

    # Splits every other column for Gistinætur and Gestakomur
    def splitforCol(self, data, numbDataCol):
        splitData = [[]]
        for i in range(numbDataCol-1):
            splitData.append([])

        for i in range(len(data)):
            tempData = []
            for k in range(numbDataCol):
                tempData.append([])

            for j in range(len(data[0])):
                for k in range(numbDataCol):
                    if j%numbDataCol == k:
                        tempData[k].append(self.fixForNaNValues(data[i][j]))

            for k in range(numbDataCol):
                splitData[k].append(tempData[k])

        # Sets each independent data matrix to a panda DataFrame
        for k in range(numbDataCol):
            splitData[k] = pd.DataFrame(splitData[k])

        return  splitData


    def fixForNaNValues(self, dataPoint):
        data = 0
        try:
            data = float(dataPoint)
        except ValueError:
            data = 0                                                    # Sets the Nan values to 0
        return data

    def getDataArray(self):
        return self.data

    def getData(self):
        # TODO: This is old, delete this function
        dfUtlendingarGesta, dfUtlendingarGisti = self.data[2][0], self.data[2][1]
        dfIslendingarGesta, dfIslendingarGisti = self.data[1][0], self.data[1][1]

        return dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti

    def getSumData(self):
        # TODO: This is old, delete this function
        dfAllsGesta, dfAllsGisti = self.data[0][0], self.data[0][1]
        dfAllMonthsGesta, dfAllMonthsGisti = self.data[3][0], self.data[3][1]

        return dfAllsGesta, dfAllMonthsGesta, dfAllsGisti, dfAllMonthsGisti

if __name__ == '__main__':
    test = ReadCSVRowHeader('SAM01103cm.csv', 2,  3, 2)
    data = test.getDataArray()
    print(data)

    fileName = 'SAM01601cm.csv'
    reader = ReadCSVRowHeader(fileName, 2, 1, 2);
    data = reader.getDataArray()
    print(data)