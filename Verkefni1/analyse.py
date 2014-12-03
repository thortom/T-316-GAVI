import ReadCSVRowHeader as csvReader
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

fileName = "SAM01103cm.csv"                                                 # This is the Hagstofu file that we use
                                                                            # All the data provided from Hagstofan is in the file
                                                                            # The process was:
                                                                            # TEXTASKRÁ -> Afmörkuð textaskrá án hauss -> Komma
monthPlayed = {1999: 10-1, 2000: 10-1, 2001: 10-1, 2002: 10-1, 2003: 10-1, 2004: 10-1,\
                2005: 10-1, 2006: 10-1, 2006: 10-1, 2007: 10-1, 2008: 10-1, 2009: 10-1,\
                2010: 10-1, 2011: 10-1, 2012: 11-1, 2013: 11-1, 2014: 11-1} 

if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName, 3, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti  = reader.getData()
    dfAllsGesta, dfAllMonthsGesta, dfAllsGisti, dfAllMonthsGisti = reader.getSumData()

    plotter.SlidePlot(dfUtlendingarGisti.T.values, "Útlendingar gistikomur")
    plotter.SlidePlot(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")

    stats = st.statistics(dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti)

    # Least Squares
    Least_Square_Is_Gisti = Tol.Stats(dfIslendingarGisti,monthPlayed)
    Least_Square_Is_Gisti.plot('Íslendingar Gistinætur')
    Least_Square_Ut_Gisti = Tol.Stats(dfUtlendingarGisti,monthPlayed)
    Least_Square_Ut_Gisti.plot('Útlendingar Gistinætur')
    line, w = Least_Square_Is_Gisti.Least_Squares()
 	
    # 
    sp.septoktspa(dfUtlendingarGisti)
    sp.septoktspa(dfIslendingarGisti)


