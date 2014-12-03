# Skoda fylgni milli ara


import ReadCSVRowHeader as csvReader 
import numpy as np
import matplotlib.pyplot as plt



class Stats:

	def __init__(self, DfData, Month):
		self.Data = []
		self.Counter = 1
		self.year_With2014 = []
		for k,v in Month.items():
			self.Data.append(DfData[self.Counter][v])
			self.year_With2014.append(k)
			self.Counter += 1
		if self.Data[len(self.Data)-1] == 0:
			self.Data = self.Data[0:len(self.Data)-1]
			self.year_With2014 = self.year_With2014[0:len(self.year_With2014)-1]
		self.line, self.w = self.Least_Squares()

	# The Method of Least Sqaures

	def Least_Squares(self):
		A = np.vstack([self.year_With2014, np.ones(len(self.year_With2014))]).T
		w = np.linalg.lstsq(A,self.Data)[0]
		year_np = np.array(self.year_With2014)
		line = w[0]*year_np + w[1]
		return line, w

	# Plot

	def plot(self, title):
		plt.figure(1)
		plt.title('The Method of least Sqaures ' + title)
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
