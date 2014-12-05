import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class statistics:
    def __init__(self):
        pass

    def getAvIncr(self,df):
        #Finds average increase for each month
        print('Average increase per month for all years')
        averageIncrease = []
        self.yearMin = 1998
        self.yearMax = self.yearMin + len(df.T)-1
        for month in df.T:
            percentage = []
            for year in df:
                if year!= (self.yearMax-self.yearMin):   #15
                    try:
                        percentage.append(int(100*df[year+1][month]/df[year][month])-100)
                    except:
                        pass
            averageIncrease.append(round(sum(percentage)/len(percentage),1))
        dfAvIncr = pd.DataFrame(data = averageIncrease)
        monthName={0:'Jan', 1:'Feb', 2:'Mars', 3:'April', 4:'May', 5:'Juni', 6:'July', 7:'Agust', 8:'September', 9:'Oktober', 10:'November', 11:'Desember'}
        index=[]
        for i in list(range(len(dfAvIncr.index))):
            index.append(monthName[i])
        dfAvIncr.index=index
        dfAvIncr.columns=['Average incr (%)']
        return(dfAvIncr)

    def getAvIncrMonth(self,df,month):
        dfAvIncr = self.getAvIncr(df)
        return(dfAvIncr['Average incr (%)'][month])

    def getMonth(self,df,month,years = None):
        if years == None:
            years = list(range(len(df.columns)))
        return(df[years][month])

    def plotLine(self,df):
        fig = plt.figure("myFig!")
        plt.plot(df)
        plt.show()

    def plotAll(self,title,df,months=None,years=None):
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

        plt.figure(title, figsize=(15, 9))
        plt.title(title)
        for year in years:
            toPlot = df[year][months]
            toPlot.index=index
            #print(2013-year)
            toPlot.plot()

        years.reverse()
        leg=np.asarray(years)
        leg = (self.yearMax-1)-leg                                      # Skip the last year missing last months of data
        plt.legend(leg,loc='center left', bbox_to_anchor=(1, 0.5))
        plt.xlabel('Mánuður')
        plt.ylabel('Gistinætur')
        plt.show()