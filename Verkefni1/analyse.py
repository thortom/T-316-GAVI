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

fileName1 = "SAM01103cm.csv"                                                 # This is the Hagstofu file that we use
sizeOfHeader1 = 2                                                            # All the data provided from Hagstofan is in the file
numbDataInRow1 = 3                                                           # The process was:
numbDataInCol1 = 2                                                           # TEXTASKRÁ -> Afmörkuð textaskrá án hauss -> Komma

fileName2 = "SAM01601cm.csv"
sizeOfHeader2 = 2
numbDataInRow2 = 1
numbDataInCol2 = 2

monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1} 

if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName1, sizeOfHeader1, numbDataInRow1, numbDataInCol1)
    data = reader.getDataArray()


    # Data from file1 split in sub size
    alls = data[0]
    islendingar = data[1]
    utlendingar = data[2]
    allMonths = data[3]
    dfAllsGesta, dfAllsGisti = alls[0], alls[1]
    dfIslendingarGesta, dfIslendingarGisti = islendingar[0], islendingar[1]
    dfUtlendingarGesta, dfUtlendingarGisti = utlendingar[0], utlendingar[1]
    dfAllMonthsGesta, dfAllMonthsGisti = allMonths[0], allMonths[1]
    stats = st.statistics()


    # Plot data with slider plotter
    plotter.SlidePlot(dfUtlendingarGisti.T.values, "Útlendingar gistinætur")
    plotter.SlidePlot(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")

    # Least Squares
    Least_Square_Is_Gisti = Tol.Stats(dfIslendingarGisti,monthPlayed)
    Least_Square_Is_Gisti.plot('Íslendingar gistinætur')
    line, w = Least_Square_Is_Gisti.Least_Squares()
    print('Spá fyrir gistnætum hjá íslendingum yfir Airwaves árið 2014')
    print(w[0]*2014+w[1])

    Least_Square_Ut_Gisti = Tol.Stats(dfUtlendingarGisti,monthPlayed)
    Least_Square_Ut_Gisti.plot('Úlendingar gistinætur')
    lineUt, wUt = Least_Square_Ut_Gisti.Least_Squares()
    print('Spá fyrir gistnætum hjá útlendingum yfir Airwaves árið 2014')
    print(wUt[0]*2014+wUt[1])

    # TODO: fix for hardcoded stuff
    sp.septoktspa(dfUtlendingarGisti,'október','nóvember','september')
    sp.septoktspa(dfIslendingarGisti,'október','nóvember','september')

    print('\n\nÍslendingar gistinætur ')
    print(stats.getAvIncr(dfIslendingarGisti))
    print('\n\nÚtlendingar gistinætur ')
    print(stats.getAvIncr(dfUtlendingarGisti))

    # Other file
    reader = csvReader.ReadCSVRowHeader(fileName2, sizeOfHeader2, numbDataInRow2, numbDataInCol2)
    data = reader.getDataArray()

    
    dfUtlendingarGisti = data[0][0]
    print('\n\nÚtlendingar gistinætur ')
    print(stats.getAvIncr(dfUtlendingarGisti))
    stats.plotAll('Útlendingar gistinætur ',dfUtlendingarGisti, months = [8,9,10,11])
