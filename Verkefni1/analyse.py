import ReadCSVRowHeader as csvReader
import statistics as st
import numpy as np
import pylab as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Button
# import matplotlib.pyplot as plt



import SlidePlot as plotter

fileName = "GistingarAllt-MonthsVsYears.csv"    


if __name__ == '__main__':
    reader = csvReader.ReadCSVRowHeader(fileName, 2, 2);
    dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti = reader.getData()
    stats = st.statistics(dfIslendingarGesta, dfUtlendingarGesta, dfIslendingarGisti, dfUtlendingarGisti)
    # plotter.SlidePlot(dfUtlendingarGisti.T.values, "Útlendingar gistikomur")
    # plotter.SlidePlot(dfUtlendingarGesta.T.values, "Útlendingar gestakomur")
