# Skoda fylgni milli ara


import ReadCSVRowHeader as csvReader 
import numpy as np
import matplotlib.pyplot as plt

monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}                     # 'Oktober' == 10-1

FILENAME = "SAM01103cm.csv" 

# Get The Data
def get_Data():
	Data = csvReader.ReadCSVRowHeader(FILENAME,3,2)
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

	return year, GistiUt_AirW, GistiIs_AirW

# The Method of Least Sqaures

def Least_Squares(year, GistiData):
	A = np.vstack([year, np.ones(len(year))]).T
	w  = np.linalg.lstsq(A,GistiData)[0] # Get Beta1 and Beta2 or y = a*x + b
	year_np_array = np.array(year) 
	line = w[0]*year_np_array + w[1] # Cal the line 
	return line, w 


def plot1(year, GistiData, line, title):
	plt.figure(1)
	plt.title('The Method of Least Squares: ' + title)
	plt.plot(year,GistiData,'o', label = 'Original data', markersize = 5)
	plt.plot(year, line, 'r', label = 'Fitted line')
	plt.legend(loc = 2)
	plt.show()


# Plot the Data together
def plot2(year, GistiData1, GistiData2, line1, line2, title1, title2):
	plt.figure(1)
	plt.subplot(211)
	plt.title('The Method of Least Squares: ' + title1)
	plt.plot(year,GistiData1,'o', label = 'Original data', markersize = 5)
	plt.plot(year, line1, 'r', label = 'Fitted line')
	plt.legend(loc = 2)

	plt.subplot(212)
	plt.title('The Method of Least Squares: ' + title2)
	plt.plot(year,GistiData2,'o', label = 'Original data', markersize = 5)
	plt.plot(year, line2, 'r', label = 'Fitted line')
	plt.legend(loc = 2)
	plt.show()

# Correlation
def Corre_Data(year, GistiData):
	Corr = np.corrcoef(year,GistiData) # How good does the data fit the line
	return Corr

year, GistiUt_AirW, GistiIs_AirW = get_Data()
LineIs, wIS = Least_Squares(year, GistiIs_AirW)
LineUt, wUt = Least_Squares(year, GistiUt_AirW)

plot1(year, GistiIs_AirW, LineIs, 'Fyrir íslendinga')
plot1(year, GistiUt_AirW, LineUt, 'Fyrir útlendinga')

plot2(year, GistiIs_AirW, GistiUt_AirW,LineIs, LineUt, 'Fyrir íslendinga', 'Fyrir útlendinga' )



