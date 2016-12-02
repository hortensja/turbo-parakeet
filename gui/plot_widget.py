# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
from PyQt4 import QtGui, QtCore

from numpy import arange, sin, cos, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import legend as legend


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=8, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.axes.hold(False)
        #self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
        pass


class StaticPlotCanvas(PlotCanvas):

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        c = cos(2*pi*t)
        self.axes.plot(t, s, label='a')
        self.axes.plot(t, c, label='f')
        #legend(plt, ['a', 'b'])
        #handles, labels = self.axes.get_legend_handles_labels()
        self.axes.legend(['a', 'b'])

    def plot_model(self, x, y, legend):
        self.axes.plot(x, y)
        self.axes.legend(legend)
        self.draw()



class DynamicPlotCanvas(PlotCanvas):

    def __init__(self, *args, **kwargs):
        PlotCanvas.__init__(self, *args, **kwargs)
        self.axes.hold(False)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()

