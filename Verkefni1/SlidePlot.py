import numpy as np
import pylab as plt
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import FuncFormatter
# import matplotlib.pyplot as plt


#TODO Make a legend for information

class SlidePlot:
    monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                    2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                    2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1}                     # 'Oktober' == 10-1
    xticklabels = ['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des']

    def __init__(self, data, title):
        self.data = data
        self.title = title
        self.yearMin = 1998
        self.yearMax = 2014

        self.yearDict = dict(zip(range(self.yearMin, self.yearMax+1), range(0, (self.yearMax+1) - self.yearMin)))
        self.yMaxValue = np.amax(self.data) + np.amax(self.data)*0.1

        self.fig = plt.figure()
        self.barAxis = plt.subplot(2, 1, 1)
        plt.subplots_adjust(left=0.1, bottom=-0.40)
        
        self.x = np.arange(len(self.data[self.yearDict[self.yearMin]]))
        self.setDataOnPlot(self.barAxis, self.yearMin)

        # Create the slider bar
        axcolor = 'lightgoldenrodyellow'
        yearAxis = plt.axes([0.18, 0.2, 0.65, 0.03], axisbg=axcolor)
        self.slideYear = Slider(yearAxis, 'Year', 1998, 2014, valinit=1998, valfmt='%0.0f')

        self.slideYear.on_changed(self.update)                                      # on_changed() method checks for changes in the slider

        # Create the Next and Previous buttons
        self.axprev = plt.axes([0.4, 0.05, 0.1, 0.075])
        self.axnext = plt.axes([0.51, 0.05, 0.1, 0.075])
        self.bnext = Button(self.axnext, 'Next')
        self.bnext.on_clicked(self.next)
        self.bprev = Button(self.axprev, 'Previous')

        self.bprev.on_clicked(self.prev)                                            # on_clicked() method checks for button clicks
        
        plt.show()

    def setDataOnPlot(self, axis, year):
        axis.cla()                                                                  # Clear axis
        axis.bar(self.x, self.data[self.yearDict[year]])

        axis.set_title(self.title + ", " + str(year))
        axis.set_xticks(self.x + 0.5)
        axis.set_xticklabels(self.xticklabels)

        self.colorBar(axis, year)
        b1 = axis.bar([0,0,0],[0,0,0],color = "black", width = 0.4, label ="Bar 2", align = "center")
        b2 = axis.bar([0,0,0],[0,0,0],color = "blue", width = 0.4, label ="Bar 2", align = "center")
        axis.legend([b1,b2], [' Airwaves','!Airwaves'])

        axis.set_ybound(0, self.yMaxValue)

    def update(self, val):
        self.slideYear.val = int(round(self.slideYear.val))
        year = self.slideYear.val

        self.setDataOnPlot(self.barAxis, year)
        self.fig.show()
        plt.draw()

    def next(self, val):
        if self.slideYear.val < self.yearMax:
            self.slideYear.set_val(self.slideYear.val + 1)                          # .set_val calls the update() function for the 
        else:
            self.slideYear.set_val(self.yearMax)

    def prev(self,val):
        if self.slideYear.val > self.yearMin:
            self.slideYear.set_val(self.slideYear.val - 1)                          # .set_val calls the update() function for the slider
        else:
            self.slideYear.set_val(self.yearMin)

    def colorBar(self, ax, year):
        month = self.monthPlayed.get(year, False)
        if month:
            ax.bar(month, self.data[self.yearDict[year]][month], color='black')

    
