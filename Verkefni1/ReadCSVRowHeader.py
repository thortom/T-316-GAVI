import csv as csv
import pandas as pd
import numpy as np

class ReadCSVRowHeader:

    def __init__(self, fileName, numbDataRow, numbDataCol):
        islendingar = []
        utlendingar = []
        alls        = []
        allMonths   = []
        csvFile = open(fileName)
        textInFile = csv.reader(csvFile)
        # TODO: make it dependent on numbDataRow, not hard coded for isl, utl. alls and allMonths
        for idx, line in enumerate(textInFile):
            if idx < numbDataRow:
                allMonths.append(line[2::])
                continue
            if idx%numbDataRow == 0:
                alls.append(line[2::])
            if  idx%numbDataRow == 1:
                islendingar.append(line[2::])
            if idx%numbDataRow == 2:
                utlendingar.append(line[2::])

        self.dfUtlendingarGesta, self.dfUtlendingarGisti = self.splitforCol(utlendingar, numbDataCol)
        self.dfIslendingarGesta, self.dfIslendingarGisti = self.splitforCol(islendingar, numbDataCol)
        self.dfAllsGesta, self.dfAllsGisti               = self.splitforCol(alls, numbDataCol)
        self.dfAllMonthsGesta, self.dfAllMonthsGisti     = self.splitforCol(allMonths, numbDataCol)

    # TODO: make it dependent on numbDataCol, not hard coded for Gesta and Gisti
    # This function splits every other column for Gistinætur and Gestakomur
    def splitforCol(self, data, numbDataCol):
        gesta = []
        gisti = []
        for i in range(len(data)):
            tempGesta = []
            tempGisti = []
            for j in range(len(data[0])):
                if j%2 == 0:
                    tempGesta.append(self.fixForNaNValues(data[i][j]))
                else:
                    tempGisti.append(self.fixForNaNValues(data[i][j]))
            gesta.append(tempGesta)
            gisti.append(tempGisti)
        return pd.DataFrame(gesta), pd.DataFrame(gisti)


    def fixForNaNValues(self, dataPoint):
        data = 0
        try:
            data = float(dataPoint)
        except ValueError:
            data = 0                                                    # Sets the Nan values to 0
        return data

    def getData(self):
        return self.dfIslendingarGesta, self.dfUtlendingarGesta, self.dfIslendingarGisti, self.dfUtlendingarGisti

    def getSumData(self):
        return self.dfAllsGesta, self.dfAllMonthsGesta, self.dfAllsGisti, self.dfAllMonthsGisti

if __name__ == '__main__':
    test = ReadCSVRowHeader('SAM01103cm.csv', 3, 2)