import numpy as np
import pylab as plt
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import FuncFormatter

class SlidePlot:
    xticklabels = ['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des']

    def __init__(self, data, title, monthPlayed):
        self.data = data
        self.title = title
        self.monthPlayed = monthPlayed
        self.yearMin = 1998
        self.yearMax = self.yearMin
        for i in self.data:
            self.yearMax += 1
        self.yearMax = self.yearMax-1                                               # The for loop does one to many

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
        self.slideYear = Slider(yearAxis, 'Year', self.yearMin, self.yearMax, valinit=self.yearMin, valfmt='%0.0f')

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
            self.slideYear.set_val(self.slideYear.val + 1)                          # .set_val calls() the update() function for the slider
        else:
            self.slideYear.set_val(self.yearMax)

    def prev(self,val):
        if self.slideYear.val > self.yearMin:
            self.slideYear.set_val(self.slideYear.val - 1)                          # .set_val calls() the update() function for the slider
        else:
            self.slideYear.set_val(self.yearMin)

    def colorBar(self, ax, year):
        month = self.monthPlayed.get(year, False)
        if month:
            ax.bar(month, self.data[self.yearDict[year]][month], color='black')

    
