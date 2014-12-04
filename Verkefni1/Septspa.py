import ReadCSVRowHeader as csvReader
import numpy as np
import os
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, read_csv
os.system('cls')

#Hver dálkur í gagnaskrám eru gestakomur/gistinaetur fyrr það ár
#Hver lína er mánuður
#Ætla að reikna fyrir hvert ár hvernig okt og nóv myndu líta út ef vöxtur í þeim mánuðum
#Væri sá sami og var í september.
#Þarf að taka hlutfall septnýr/septgamall og segja oktnýr = hlutfall * oktgamall. eins fyrir nov
#Bara skoda utlendingar gistinaetur
#Get klarad 2014 likanid - profa seinna
#Skoðum trend fyrir okt rauntölur vs okt septemberspá. eins fyrir nóv.
#Til þess þarf ég array bara með októbertölum og annað bara með nóvembertölum, samtals 4 array
class septoktspa:
    def __init__(self,dF,manudur1,manudur2,spa_manudur):
        self.dF = dF
        self.manudur1 = manudur1
        self.manudur2 = manudur2
        self.spa_manudur = spa_manudur
        self.test(dF,manudur1,manudur2,spa_manudur)

    def test(self,dF,manudur1,manudur2,spa_manudur):

        array0,array1,array2,array3,array4 = self.Dataforplot(dF,manudur1,manudur2,spa_manudur)
        self.plotter(array0,array1,array2,array3,array4,manudur1,manudur2,spa_manudur)

    def plotter(self,array0,array1,array2,array3,array4,manudur1,manudur2,spa_manudur):

        yMax1 = np.amax(array1)
        yMax2 = np.amax(array2)
        yMax3 = np.amax(array3)
        yMax4 = np.amax(array4)

        def max2(num1,num2):
            if(num1 >= num2):
                return num1
            if(num2 > num1):
                return num2

        yMaxf = max2(yMax1,yMax2)
        yMaxs = max2(yMax3,yMax4)
        yMax = max2(yMaxf,yMaxs)
        yMax *= 1.1

        plt.figure(figsize=(12,8))
        sub1 = plt.subplot(2,1,1)
        b1, = sub1.plot(array0,array1,'ro-')
        b2, = sub1.plot(array0,array2,'go-')
        plt.title('Gistinætur í ' + manudur1 + ' eftir árum')
        plt.ylabel('Gistinætur')
        plt.xlabel('Ár')
        sub1.set_ybound(0, yMax)
        sub1.legend([b1,b2],['Rauntölur','Spá byggð á ' + spa_manudur],loc=0,bbox_to_anchor=(0, 0, 1, 1))
        leg = plt.gca().get_legend()
        ltext  = leg.get_texts()
        plt.setp(ltext, fontsize='small') 

        sub2 = plt.subplot(2,1,2)
        b3, = sub2.plot(array0,array3,'ko-')
        b4, = sub2.plot(array0,array4,'bo-')
        plt.title('Gistinætur í ' + manudur2 + ' eftir árum')
        plt.ylabel('Gistinætur')
        plt.xlabel('Ár')
        sub2.set_ybound(0, yMax)
        sub2.legend([b3,b4],['Rauntölur','Spá byggð á ' + spa_manudur],loc=0,bbox_to_anchor=(0, 0, 1, 1))
        plt.subplots_adjust(hspace=.5)
        leg = plt.gca().get_legend()
        ltext  = leg.get_texts()
        plt.setp(ltext, fontsize='small') 
        plt.show()

    def Dataforplot(self,dF,manudur1,manudur2,spa_manudur):
        i = 0
        man1 = []
        man1_spa = []
        man2 = []
        man2_spa = []
        ar = 1998
        arlisti = []
        def manudur_i_tolu(manudur):
            if manudur == 'janúar':
                return 0
            if manudur == 'febrúar':
                return 1
            if manudur == 'mars':
                return 2
            if manudur == 'apríl':
                return 3
            if manudur == 'maí':
                return 4
            if manudur == 'júní':
                return 5
            if manudur == 'júlí':
                return 6
            if manudur == 'ágúst':
                return 7
            if manudur == 'september':
                return 8
            if manudur == 'október':
                return 9
            if manudur == 'nóvember':
                return 10
            if manudur == 'desember':
                return 11
            print('Skrifaðu mánuðinn á íslensku í lágstöfum')
            return 0   
        man1tala = manudur_i_tolu(manudur1)
        man2tala = manudur_i_tolu(manudur2)
        spamantala = manudur_i_tolu(spa_manudur)
        dftest = dF.copy()
        for num in range(0,16):
            num2 = num+1
            hlutfall = dftest[num2][spamantala] / dftest[num][spamantala]
            dftest[num2][man1tala] = hlutfall * dftest[num][man1tala]
            dftest[num2][man2tala] = hlutfall * dftest[num][man2tala]
            man1_spa.append(dftest[num][man1tala])
            man2_spa.append(dftest[num][man2tala])
            man1.append(dF[num][man1tala])
            man2.append(dF[num][man2tala])
            arlisti.append(ar)
            ar += 1

        array0 = np.asarray(arlisti)
        array1 = np.asarray(man1)
        array2 = np.asarray(man1_spa)
        array3 = np.asarray(man2)
        array4 = np.asarray(man2_spa)

        pdarray1 = pd.DataFrame(array1,columns=[manudur1 + ' rauntölur'],index=array0)
        pdarray2 = pd.DataFrame(array2,columns=[manudur1 + ' spá'],index=array0)
        pdarray3 = pd.DataFrame(array3,columns=[manudur2 + ' rauntölur'],index=array0)
        pdarray4 = pd.DataFrame(array4,columns=[manudur2 + ' spá'],index=array0)

        array5 = pd.concat([pdarray1,pdarray2,pdarray3,pdarray4],axis=1)
        print('--------------------------------------')
        print(array5)
        print('--------------------------------------')

        return array0,array1,array2,array3,array4

if __name__ == '__main__':
    fileName = "SAM01103cm.csv"
    reader = csvReader.ReadCSVRowHeader(fileName, 3, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
    

