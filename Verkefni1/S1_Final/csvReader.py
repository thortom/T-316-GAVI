import csv as csv
import pandas as pd
import numpy as np

# This CSV reader can handle any csv data that is ordered by the months of the year in the row and ordered by any number of years in the columns
# The number of data items in each row and columns needs to be specified with the parameters numbDataRow and numbDataCol.
# A generalized table is shown here below. The table should not include the column headers when it is suposed to be read from but the table may include the row headers.
# The number of row headrs should be specified whith the parameter sizeOfHeader.
# 
#                       |               |                  First Year                   |                Second Year                ..............                           
#                       |               |_______________________________________________|_______________________________________________|_______...               
#                       |   Data name   |       DataCol1 | DataCol2 |.....| DataColN    |       DataCol1 | DataCol2 |.....| DataColN    | ........
#-------------------------------------------------------------------------------------------------------------------------------
#   Sum of all Months   |   DataRow1    |
#                       |   DataRow2    |
#                       |       .       |
#                       |       .       |
#                       |   DataRowN    |
#   --------------------|---------------|
#   Januar              |   DataRow1    |
#                       |   DataRow2    |
#                       |       .       |
#                       |       .       |
#                       |   DataRowN    |                                           DATA HERE
#   --------------------|---------------|
#   February            |   DataRow1    |
#                       |   DataRow2    |
#                       |       .       |
#                       |       .       |
#                       |   DataRowN    |
#       .
#       .
#       .
#       .
#   --------------------|---------------|
#   Desember            |   DataRow1    |
#                       |   DataRow2    |
#                       |       .       |
#                       |       .       |
#                       |   DataRowN    |
#   --------------------|---------------|
#
# Example of csv file for input whith the parameters sizeOfHeader=2, numbDataRow=1 and numbDataCol=2 thus spaning two years of data
#
# "Höfuðborgarsvæði","Alls",531762,101825,586796,94688
# "Höfuðborgarsvæði","janúar",13719,7605,18018,7569
# "Höfuðborgarsvæði","febrúar",20741,10694,26785,11482
# "Höfuðborgarsvæði","mars",30254,12603,33599,14258
# "Höfuðborgarsvæði","apríl",34319,8747,40782,9842
# "Höfuðborgarsvæði","maí",45823,7903,52462,6311
# "Höfuðborgarsvæði","júní",66860,5321,72918,3744
# "Höfuðborgarsvæði","júlí",93940,5352,97730,4323
# "Höfuðborgarsvæði","ágúst",91983,5501,94752,5039
# "Höfuðborgarsvæði","september",51985,5992,55798,6067
# "Höfuðborgarsvæði","október",34372,12281,40702,9649
# "Höfuðborgarsvæði","nóvember",28733,12654,30784,9773
# "Höfuðborgarsvæði","desember",19033,7172,22466,6631



class ReadCSVRowHeader:

    def __init__(self, fileName, sizeOfHeader, numbDataRow, numbDataCol):

        # Creates empty list of lists to store arrays of data in one list
        self.data = [[]]
        for i in range(numbDataRow):
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