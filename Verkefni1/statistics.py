import pandas as pd
class statistics:
    def __init__(self, dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti):
        self.dfIGe = dfIslendingarGesta
        self.dfUGe = dfUtlendingarGesta
        self.dfIGi = dfIslendingarGisti
        self.dfUGi = dfUtlendingarGisti

        #print(self.getAvIncr(self.dfUGi))
        #print(self.getAvIncrMonth(self.dfUGi,3))
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