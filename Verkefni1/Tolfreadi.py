# Skoda fylgni milli ara


import ReadCSVRowHeader as csvReader 
import numpy as np
import matplotlib.pyplot as plt

monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}                     # 'Oktober' == 10-1
year0 =1999

fileName = "GistingarAllt-MonthsVsYears.csv" 
Data = csvReader.ReadCSVRowHeader(fileName,2,2)

DfIsGesta, DfUtGesta, DfIsGisti, DfUtGisti = Data.getData()

GistiUt_AirW_With2014 = []
GistiIs_AirW_With2014 = []
Counter = 1
year_With2014 = []

for k,v in monthPlayed.items():
	GistiIs_AirW_With2014.append(DfIsGisti[Counter][v])
	GistiUt_AirW_With2014.append(DfUtGisti[Counter][v])
	year_With2014.append(k)
	Counter += 1

GistiIs_AirW = GistiIs_AirW_With2014[0:len(GistiIs_AirW_With2014)-1]
GistiUt_AirW = GistiUt_AirW_With2014[0:len(GistiIs_AirW_With2014)-1]
year = year_With2014[0:len(year_With2014)-1]

# The Method of Least Sqaures

A = np.vstack([year, np.ones(len(year))]).T
w  = np.linalg.lstsq(A,GistiIs_AirW)[0] # Get Beta1 and Beta2 or y = a*x + b

w2 = np.linalg.lstsq(A,GistiUt_AirW)[0]
print(w)
print(w2)

year_np_array = np.array(year) 

line = w[0]*year_np_array + w[1] # Cal the line 

line2 = w2[0]*year_np_array + w2[1]




plt.figure(1)
plt.subplot(211)
plt.title('The Method of Least Squares: Fyrir íslendinga')
plt.plot(year,GistiIs_AirW,'o', label = 'Original data', markersize = 5)
plt.plot(year, line, 'r', label = 'Fitted line')
plt.legend(loc = 2)

plt.subplot(212)
plt.title('The Method of Least Squares: Fyrir útlendinga')
plt.plot(year,GistiUt_AirW,'o', label = 'Original data', markersize = 5)
plt.plot(year, line2, 'r', label = 'Fitted line')
plt.legend(loc = 2)
plt.show()

# Correlation

CorrIS = np.corrcoef(year,GistiIs_AirW) # How good does the data fit the line
CorrUT = np.corrcoef(year,GistiUt_AirW) 

print(CorrIS[0][1]) 
print(CorrUT[0][1])

print(w[0]*2014+w[1])
print(w2[0]*2014+w2[1])