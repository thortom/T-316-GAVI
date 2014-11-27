import csv

class ReadHagstofanCSV:
    validYears = range(1800,2100)

    def __init__(self, fileName):
        csvFile = open('Gistingar.csv')
        textInFile = csv.reader(csvFile)
        for lines in textInFile:
            # TODO
            a = 1
        # TODO
        self.data = 0

    def getData(self):
        # TODO
        return 0

    def isYear(self, year):
        if self.isNumber(year) and (year in self.validYears):
            return True
        else:
            return False

    def isNumber(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    test = ReadHagstofanCSV('Gistingar.csv')
    data = test.getData()
