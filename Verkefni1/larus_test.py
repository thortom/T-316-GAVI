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
#Prósentubundinn vöxtur á ári, gæti hermt með margliðu?
i = 0
okt = []
okt_spa = []
nov = []
nov_spa = []
ar = 1998
arlisti = []
fileName = "GistingarAllt-MonthsVsYears.csv"

if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName, 2, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()

    dftest = dfUtlendingarGisti.copy()

    for num in range(0,16):
            num2 = num+1
            hlutfall = dftest[num2][8] / dftest[num][8]
            dftest[num2][9] = hlutfall * dftest[num][9]
            dftest[num2][10] = hlutfall * dftest[num][10]
            okt_spa.append(dftest[num][9])
            nov_spa.append(dftest[num][10])
            okt.append(dfUtlendingarGisti[num][9])
            nov.append(dfUtlendingarGisti[num][10])
            arlisti.append(ar)
            ar += 1

array0 = np.asarray(arlisti)
array1 = np.asarray(okt)
array2 = np.asarray(okt_spa)
array3 = np.asarray(nov)
array4 = np.asarray(nov_spa)

pdarray1 = pd.DataFrame(array1,columns=['Október rauntölur'],index=array0)
pdarray2 = pd.DataFrame(array2,columns=['Október spá'],index=array0)
pdarray3 = pd.DataFrame(array3,columns=['Nóvember rauntölur'],index=array0)
pdarray4 = pd.DataFrame(array4,columns=['Nóvember spá'],index=array0)

array5 = pd.concat([pdarray1,pdarray2,pdarray3,pdarray4],axis=1)
print(array5)

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


sub1 = plt.subplot(2,1,1)
b1, = sub1.plot(array0,array1,'ro-')
b2, = sub1.plot(array0,array2,'go-')
plt.title('Gistinætur útlendinga í októbermánuði eftir árum')
plt.ylabel('Gistinætur')
plt.xlabel('Ár')
sub1.set_ybound(0, yMax)
sub1.legend([b1,b2],['Rauntölur','Spá'],loc=4)

sub2 = plt.subplot(2,1,2)
b3, = sub2.plot(array0,array3,'ko-')
b4, = sub2.plot(array0,array4,'bo-')
plt.title('Gistinætur útlendinga í nóvembermánuði eftir árum')
plt.ylabel('Gistinætur')
plt.xlabel('Ár')
sub2.set_ybound(0, yMax)
sub2.legend([b3,b4],['Rauntölur','Spá'],loc=4)

plt.show()

#Þarf bara að fiffa legend og eitthvað smá núna