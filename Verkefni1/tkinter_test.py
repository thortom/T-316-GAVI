import tkinter as tk
import ttk as ttk
import newReadCSVRowHeader as csvReader
import statistics as st
import numpy as np
import pylab as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Button
import SlidePlot as plotter
import pandas as pd
import Tolfreadi as Tol
import Septspa as sp

# TODO: read this from file, test for default
monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}
fileName1 = "SAM01103cm.csv"
fileName2 = "SAM01601cm.csv"

class Application(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent

        self.parent.title("Airwaves")
        self.setDataType1(fileName1)
        self.setDataType2(fileName2)
        self.createWidgets()
        self.var1.set(1)

    def createWidgets(self):

        # TODO: Fix layout http://zetcode.com/gui/tkinter/layout/
        self.var1 = tk.IntVar()
        self.dataType1 = tk.Checkbutton(self, text="Data Type 1", variable=self.var1)
        self.dataType1["command"] = self.changeDataType1
        self.dataType1.grid(row=0, column=1)

        self.fileVar1 = tk.StringVar()
        self.fileType1 = tk.Entry(self, textvariable=self.fileVar1)
        self.fileType1.grid(row=0, column=2)

        self.fileVar1.set(fileName1)

        self.var2 = tk.IntVar()
        self.dataType2 = tk.Checkbutton(self, text="Data Type 2", variable=self.var2)
        self.dataType2["command"] = self.changeDataType2
        self.dataType2.grid(row=1, column=1)

        self.fileVar2 = tk.StringVar()
        self.fileType2 = tk.Entry(self, textvariable=self.fileVar2)
        self.fileType2.grid(row=1, column=2)

        self.fileVar2.set(fileName2)

        self.uwotm8 = tk.Button(self)
        self.uwotm8["text"] = "Línurit fyrir gistinætur íslendinga"
        self.uwotm8["command"] = self.linurit1
        self.uwotm8.grid(row=0, column=0)

        self.random = tk.Button(self)
        self.random["text"] = "Línurit fyrir gistinætur útlendinga"
        self.random["command"] = self.linurit2
        self.random.grid(row=1, column=0)

        self.dnolol = tk.Button(self)
        self.dnolol["text"] = "Spá fyrir gistinætum hjá útlendingum yfir Airwaves síðasta ár"
        self.dnolol["command"] = self.rit3
        self.dnolol.grid(row=2, column=0)

        self.immastabyou = tk.Button(self)
        self.immastabyou["text"] = "Spá fyrir gistinætum hjá íslendingum yfir Airwaves síðasta ár"
        self.immastabyou["command"] = self.rit4
        self.immastabyou.grid(row=3, column=0)

        self.ubleednoob = tk.Button(self)
        self.ubleednoob["text"] = "Sliderplot fyrir útlendingar gistikomur öll árin"
        self.ubleednoob["command"] = self.slider1
        self.ubleednoob.grid(row=4, column=0)

        self.udead = tk.Button(self)
        self.udead["text"] = "Sliderplot fyrir útlendingar gestakomur öll árin"
        self.udead["command"] = self.slider2
        self.udead.grid(row=5, column=0)

        self.funeral = tk.Button(self)
        self.funeral["text"] = "Yfirlit fyrir gistinætur útlendinga öll árin"
        self.funeral["command"] = self.linurit4
        self.funeral.grid(row=6, column=0)

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.parent.destroy)
        self.QUIT.grid(row=7, column=0)

        self.pack()

    def changeDataType1(self):
        print('changeDataType1')
        self.var2.set(0)
        fileName = self.fileVar1.get()
        self.setDataType1(fileName)

        self.udead.grid()

    def changeDataType2(self):
        print('changeDataType2')
        self.var1.set(0)
        fileName = self.fileVar2.get()
        self.setDataType2(fileName)
        # self.udead.pack_forget()
        self.udead.grid_remove()

    def setDataType1(self, fileName):
        sizeOfHeader1 = 2
        numbDataInRow1 = 3
        numbDataInCol1 = 2
        reader = csvReader.ReadCSVRowHeader(fileName, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
        data = reader.getDataArray()

        self.alls = data[0]
        self.islendingar = data[1]
        self.utlendingar = data[2]
        self.allMonths = data[3]
        self.dfAllMonthsGesta, self.dfAllMonthsGisti = self.allMonths[0], self.allMonths[1] 
        self.dfAllsGesta, self.dfAllsGisti = self.alls[0], self.alls[1]
        self.dfIslendingarGesta, self.dfIslendingarGisti = self.islendingar[0], self.islendingar[1]
        self.dfUtlendingarGesta, self.dfUtlendingarGisti = self.utlendingar[0], self.utlendingar[1]

    def setDataType2(self, fileName):
        sizeOfHeader2 = 2
        numbDataInRow2 = 1
        numbDataInCol2 = 2
        reader = csvReader.ReadCSVRowHeader(fileName, sizeOfHeader2, numbDataInRow2, numbDataInCol2)
        data = reader.getDataArray()

        self.allMonths = data[1][0]
        self.dfUtlendingar = data[0][0]
        self.dfIslendingar = data[1][0]

    def linurit1(self):
        sp.septoktspa(self.dfIslendingarGisti,'október','nóvember','september')

    def linurit2(self):
        sp.septoktspa(self.dfUtlendingarGisti,'október','nóvember','september')

    def rit3(self):
        Least_Square_Ut_Gisti = Tol.Stats(self.dfUtlendingarGisti,monthPlayed)
        Least_Square_Ut_Gisti.getPrediction()
        Least_Square_Ut_Gisti.plot('Úlendingar gistinætur')

    def rit4(self):
        print(self.dfIslendingarGisti)
        Least_Square_Is_Gisti = Tol.Stats(self.dfIslendingarGisti,monthPlayed)
        Least_Square_Is_Gisti.getPrediction()
        Least_Square_Is_Gisti.plot('Íslendingar gistinætur')

    def slider1(self):
        plotter.SlidePlot(self.dfUtlendingarGisti.T.values, "Útlendingar gistikomur")

    def slider2(self):
        plotter.SlidePlot(self.dfUtlendingarGesta.T.values, "Útlendingar gestakomur")

    def linurit4(self):
        stats = st.statistics()
        print(stats.getAvIncr(self.dfUtlendingar))
        print(stats.getAvIncrMonth(self.dfUtlendingar,3))
        stats.plotAll('Útlendingar gistinætur',self.dfUtlendingar, months = [8,9,10,11])


def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()


if __name__ == '__main__':
    main()