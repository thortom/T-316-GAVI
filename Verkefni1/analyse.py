import ReadCSVRowHeader as csvReader
import statistics as st
import numpy as np
import pylab as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Button
import SlidePlot as plotter
import pandas as pd

fileName = "SAM01103cm.csv"                                                 # This is the Hagstofu file that we use
                                                                            # All the data provided from Hagstofan is in the file
                                                                            # The process was:
                                                                            # TEXTASKRÁ -> Afmörkuð textaskrá án hauss -> Komma


if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName, 3, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti  = reader.getData()
    dfAllsGesta, dfAllMonthsGesta, dfAllsGisti, dfAllMonthsGisti = reader.getSumData()

    # plotter.SlidePlot(dfUtlendingarGisti.T.values, "Útlendingar gistikomur")
    # plotter.SlidePlot(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")

    st.statistics(dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti)
