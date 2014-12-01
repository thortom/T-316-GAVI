import ReadCSVRowHeader as csvReader
import numpy as np
import pylab as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Button
# import matplotlib.pyplot as plt

fileName = "GistingarAllt-MonthsVsYears.csv"
monthPlayed = {2009: 'Okt', 2010: 'Okt', 2011: 'Okt', 2012: 'Okt', 2013: 'Okt'}
    


def plotData(data, title):

    yearDict = dict(zip(range(1998,2015), range(0, 2015-1998)))
    # print(yearDict)
    # print(yearDict[1999])

    yMaxValue = np.amax(data) + np.amax(data)*0.1

    fig = plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    plt.subplots_adjust(left=0.1, bottom=-0.40)

    year0 = 1998
    x = np.arange(len(data[yearDict[year0]]))
    barPlot = ax1.bar(x, data[yearDict[year0]])
    ax1.bar(10, data[yearDict[year0]][10], color='black')
    # colorBar(ax1, year, month)
    ax1.set_ybound(0, yMaxValue)
    plt.xticks(x + 0.5)
    ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
    plt.title(title + ", " + str(year0))

    axcolor = 'lightgoldenrodyellow'
    axYear = plt.axes([0.15, 0.2, 0.65, 0.03], axisbg=axcolor)
    slideYear = Slider(axYear, 'Year', 1998, 2014, valinit=1998, valfmt='%0.0f')

    def update(val):
        slideYear.val = int(round(slideYear.val))
        year = slideYear.val
        ax1.cla()                                                               # Clear axis
        barPlot = ax1.bar(x, data[yearDict[year]])
        ax1.set_ybound(0, yMaxValue)
        ax1.set_title(title + ", " + str(year))
        ax1.set_xticks(x + 0.5)
        ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
        fig.show()
        plt.draw()
    def next(val):
        if slideYear.val != 2014:
            slideYear.val = int(round(slideYear.val)+1)
            year = slideYear.val
            ax1.cla()                                                               # Clear axis
            barPlot = ax1.bar(x, data[yearDict[year]])
            ax1.set_ybound(0, yMaxValue)
            ax1.set_title(title + ", " + str(year))
            ax1.set_xticks(x + 0.5)
            ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
            slideYear.set_val(year)
            fig.show()
            plt.draw()
    def prev(val):
        if slideYear.val != 1998:
            slideYear.val = int(round(slideYear.val)-1)
            year = slideYear.val
            ax1.cla()                                                               # Clear axis
            barPlot = ax1.bar(x, data[yearDict[year]])
            ax1.set_ybound(0, yMaxValue)
            ax1.set_title(title + ", " + str(year))
            ax1.set_xticks(x + 0.5)
            ax1.set_xticklabels(['Jan','Feb','Mars','Apríl','Maí','Júní','Júlí','Ágúst','Sept','Okt','Nóv','Des'])
            slideYear.set_val(year)
            fig.show()
            plt.draw()


    axprev = plt.axes([0.4, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.51, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(prev)
    slideYear.on_changed(update)



    plt.show()

    def colorBar(ax, year, month):
        ax.bar(10, data[yearDict[year0]][10], color='black')

if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName, 2, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()

    plotData(dfUtlendingarGisti.T.values, "Útlendingar gistikomur")
    plotData(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")