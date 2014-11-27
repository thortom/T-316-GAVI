import csv

# Example usage of ReadHagstofanCSV:
#   test = ReadHagstofanCSV('Gistingar.csv')
#   data = test.getData()
#   # then do stuff with data...

class ReadHagstofanCSV:
    validYears = range(1800,2100)
    validMonths = ['Janúar','Febrúar','Mars','Apríl','Maí','Júní','Júlí','Ágúst','September','Október','Nóvember']
    MISSING_VALUE = '..'

    def __init__(self, fileName):
        self.years = []
        self.months = []
        self.data = []

        self.readYearMonthDataFormat(fileName)
        

    def readYearMonthDataFormat(self, fileName):
        csvFile = open(fileName)
        textInFile = csv.reader(csvFile)
        for line in textInFile:
            if self.isYearLine(line):
                for year in line:
                    if self.isYear(year):                                       # Used to filter empty values '' and ' '
                        self.years.append(year)
                        # print('appending -> ', year)
            elif self.isMonthLine(line):
                for idx, month in enumerate(line):
                    if idx >= 12:                                               # Only need the 12 months the rest is repetition
                        break
                    if self.isMonth(month):                                     # Used to filter empty values '' and ' '
                        self.months.append(month)
                        # print('appending -> ', month)
            # The rest should be the data, if the cells are not empty
            # The data is split in groups of 12 (12 months in the year)
            # Here we assume only one line of data
            else:
                dataForYear = []
                for idx, number in enumerate(line):
                    if self.isNumber(number):
                        dataForYear.append(number)
                    elif number == self.MISSING_VALUE:
                        dataForYear.append('nan')
                    else:
                        continue
                    if idx%12 == 0:                                             # Data for one year gathered, make new line
                          self.data.append(dataForYear)
                          # print('appending -> ', dataForYear)
                          dataForYear = []

    def getData(self):
        data = []
        for idx, year in enumerate(self.years):
            temp = self.data[idx]
            temp.insert(0, year)
            data.append(temp)
        return data

    def printData(self, data=None):
        if data == None:
            data = self.getData()
        for item in data:
            print(item[0])
            print(item[1:len(item)])
            print()

    def isYearLine(self, line):
        for item in line:
            if self.isYear(item):
                return True
        return False

    def isYear(self, item):
        if self.isNumber(item) and (int(item) in self.validYears):
            return True
        else:
            return False

    def isMonthLine(self, line):
        for item in line:
            if self.isMonth(item):
                return True
        return False

    def isMonth(self, item):
        if item in self.validMonths:
            return True
        else:
            return False

    def isNumber(self, item):
        try:
            float(item)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    test = ReadHagstofanCSV('Gistingar.csv')
    data = test.getData()
    print(data)
    # TODO: do stuff with data...
    # The data manipulation should be done in another file
