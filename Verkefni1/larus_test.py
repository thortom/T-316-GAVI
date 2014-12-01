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

array4 = pd.concat([pdarray1,pdarray2,pdarray3,pdarray4],axis=1)
print(array4)

plt.plot(pdarray1)
plt.show()

#Er nuna kominn med arrayin sem mig vantar, naest er ad plotta thetta.