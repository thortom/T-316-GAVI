import numpy as np
import pylab as plt
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import FuncFormatter
# import matplotlib.pyplot as plt


#TODO Make a legend for information

class SlidePlot:
    monthPlayed = {2009: 10-1, 2010: 10-1, 2011: 10-1, 2012: 10-1, 2013: 10-1}         # 'Oktober' == 10-1

    def __init__(self, data, title):
        self.data = data
        self.yearDict = dict(zip(range(1998,2015), range(0, 2015-1998)))
        self.year0 = 1998
        self.title = title

        self.yMaxValue = np.amax(self.data) + np.amax(self.data)*0.1

        self.fig = plt.figure()
        self.ax1 = plt.subplot(2, 1, 1)
        plt.subplots_adjust(left=0.1, bottom=-0.40)

        
        self.x = np.arange(len(self.data[self.yearDict[self.year0]]))
        barPlot = self.ax1.bar(self.x, self.data[self.yearDict[self.year0]])
        # self.ax1.bar(10, self.data[self.yearDict[self.year0]][10], color='black')
        self.colorBar(self.ax1, self.year0)
        self.ax1.set_ybound(0, self.yMaxValue)
        plt.xticks(self.x + 0.5)
        self.ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
        plt.title(self.title + ", " + str(self.year0))

        axcolor = 'lightgoldenrodyellow'
        axYear = plt.axes([0.18, 0.2, 0.65, 0.03], axisbg=axcolor)
        self.slideYear = Slider(axYear, 'Year', 1998, 2014, valinit=1998, valfmt='%0.0f')

        self.slideYear.on_changed(self.update)

        self.axprev = plt.axes([0.4, 0.05, 0.1, 0.075])
        self.axnext = plt.axes([0.51, 0.05, 0.1, 0.075])
        self.bnext = Button(self.axnext, 'Next')
        self.bnext.on_clicked(self.next)
        self.bprev = Button(self.axprev, 'Previous')
        self.bprev.on_clicked(self.prev)
        plt.show()

    def update(self, val):
        # print(slideYear.val)
        self.slideYear.val = int(round(self.slideYear.val))
        year = self.slideYear.val
        self.ax1.cla()                                                               # Clear axis
        barPlot = self.ax1.bar(self.x, self.data[self.yearDict[year]])
        self.ax1.set_ybound(0, self.yMaxValue)
        self.ax1.set_title(self.title + ", " + str(year))
        self.ax1.set_xticks(self.x + 0.5)
        self.ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
        self.colorBar(self.ax1, year)

        self.ax1.set_ybound(0, self.yMaxValue)

        self.fig.show()
        plt.draw()

    def next(self, val):
        if self.slideYear.val != 2014:
            self.slideYear.val = int(round(self.slideYear.val)+1)
            year = self.slideYear.val
            self.ax1.cla()                                                               # Clear axis
            barPlot = self.ax1.bar(self.x, self.data[self.yearDict[year]])
            self.ax1.set_ybound(0, self.yMaxValue)
            self.ax1.set_title(self.title + ", " + str(year))
            self.ax1.set_xticks(self.x + 0.5)
            self.ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
            self.slideYear.set_val(year)
            self.fig.show()
            plt.draw()

    def prev(self,val):
        if self.slideYear.val != 1998:
            self.slideYear.val = int(round(self.slideYear.val)-1)
            year = self.slideYear.val
            self.ax1.cla()                                                               # Clear axis
            barPlot = self.ax1.bar(self.x, self.data[self.yearDict[year]])
            self.ax1.set_ybound(0, self.yMaxValue)
            self.ax1.set_title(self.title + ", " + str(year))
            self.ax1.set_xticks(self.x + 0.5)
            self.ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
            self.slideYear.set_val(year)
            self.fig.show()
            plt.draw()

    def colorBar(self, ax, year):
        month = self.monthPlayed.get(year, 11-1)                                 # Default is 'November' == 11-1
        ax.bar(month, self.data[self.yearDict[year]][month], color='black')

    
