import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class statistics:
    def __init__(self, dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti):
        self.dfIGe = dfIslendingarGesta
        self.dfUGe = dfUtlendingarGesta
        self.dfIGi = dfIslendingarGisti
        self.dfUGi = dfUtlendingarGisti

        #print(self.getAvIncr(self.dfUGi))
        #print(self.getAvIncrMonth(self.dfUGi,3))
        #print(self.dfUGi)
        #self.plotLine(self.getMonth(self.dfUGi,9)) 
        self.plotAll(self.dfUGi,months=[8,9,10,11])
    def getAvIncr(self,df):
        #Prints column 0, row 1
        #Prints year 1998, Februar
        #print(df[0][1])

        #Finds average increase for each month
        averageIncrease = []
        for month in df.T:
            percentage = []
            for year in df:
                if year!=15:
                    try:
                        percentage.append(int(100*df[year+1][month]/df[year][month])-100)
                    except:
                        pass
            averageIncrease.append(round(sum(percentage)/len(percentage),1))
        dfAvIncr = pd.DataFrame(data = averageIncrease)
        return(dfAvIncr)

    def getAvIncrMonth(self,df,month):
        dfAvIncr = self.getAvIncr(df)
        return(dfAvIncr[0][month])

    def getMonth(self,df,month,years = None):
        if years == None:
            years = list(range(len(df.columns)))
            #print(years)
        return(df[years][month])

    def plotLine(self,df):
        fig = plt.figure("myFig!")
        plt.plot(df)
        plt.show()

    def plotAll(self,df,months=None,years=None):
        if months == None:
            months = list(range(len(df.index)))
        if years == None:
            years = list(range(len(df.columns)-1))
        
        monthName={0:'Jan', 1:'Feb', 2:'Mars', 3:'April', 4:'May', 5:'Juni', 6:'July', 7:'Agust', 8:'September', 9:'Oktober', 10:'November', 11:'Desember'}
        index=[]
        for i in months:
            index.append(monthName[i])

        #Sniðugt til að sækja rétt gögn
        for year in years:
            pass
            #print(df[year][months])
        for month in months:
            pass
            #print(df.T[month][years])

        plt.figure('my plot', figsize=(15, 9))
        for year in years:
            toPlot = df[year][months]
            toPlot.index=index
            #print(2013-year)
            toPlot.plot()

        years.reverse()
        leg=np.asarray(years)
        leg = 2013-leg
        plt.legend(leg,loc='center left', bbox_to_anchor=(1, 0.5))
        plt.xlabel('Mánuður')
        plt.ylabel('Gistinætur')
        plt.show()