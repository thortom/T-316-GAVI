# Skoda fylgni milli ara
import numpy as np
import matplotlib.pyplot as plt

class Stats:

    def __init__(self, DfData, monthPlayed):
        self.Data = []
        self.Counter = 1
        self.year_With2014 = []
        self.yearMin = 1998

        yearCounter = self.yearMin
        for item in DfData.T.iterrows():
            yearCounter += 1
            month = monthPlayed.get(yearCounter, False)
            item = list(item[1])
            if month and item[month] != 0:
                self.Data.append(item[month])
                self.year_With2014.append(yearCounter)

        self.line, self.w = self.Least_Squares()

    # The Method of Least Sqaures
    def Least_Squares(self):
        A = np.vstack([self.year_With2014, np.ones(len(self.year_With2014))]).T
        w = np.linalg.lstsq(A,self.Data)[0]
        year_np = np.array(self.year_With2014)
        line = w[0]*year_np + w[1]
        return line, w

    def getPrediction(self):
        year_np = np.array(self.year_With2014)
        nextYear = year_np[-1]+1
        print('Spá fyrir gistinætum hjá útlendingum yfir Airwaves árið', nextYear)
        print(self.w[0]*nextYear + self.w[1])

    def plot(self, title):
        plt.figure(1)
        plt.title('The Method of least Squares ' + title)
        plt.plot(self.year_With2014, self.Data,'o', label = 'Original data', markersize = 5)
        plt.plot(self.year_With2014, self.line,'r', label = 'Fitted line')
        plt.legend(loc = 2)
        plt.ylabel('Gistinætur')
        plt.xlabel('Ár')
        plt.show()

    # Correlation
    def Corre_Data(self):
        Corr = np.corrcoef(self.year_With2014,self.Data) # How good does the data fit the line
        return Corr[0][1]


    # Basic Statistics
    def Statistics(self):
        Mean = np.mean(self.Data)
        Std = np.std(self.Data)
        Var = np.var(self.Data)
        return Mean, Std, Var
