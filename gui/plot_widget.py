# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=8, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.axes.hold(False)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def save_plot_canvas(self, filename):
        self.figure.savefig(filename)


class StaticPlotCanvas(PlotCanvas):


    def plot_model(self, x, y, legend, title):
        self.axes.plot(x, y)
        self.axes.legend(legend)
        self.axes.set_title(title)
        self.draw()


