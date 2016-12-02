# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from gui.plot_widget import StaticPlotCanvas, DynamicPlotCanvas
from model_solver import ModelSolver



class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Modelowanie i symulacje ED")

        self.init_menu()

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QHBoxLayout(self.main_widget)


        self.left = StaticPlotCanvas(self.main_widget, width=8, height=8, dpi=100)
        dc = DynamicPlotCanvas(self.main_widget, width=8, height=8, dpi=100)

        l.addWidget(self.left)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        #self.statusBar().showMessage("Joanna Cichowska", 2016)

    def about(self):
        QtGui.QMessageBox.about(self, "O programie",
                                """Praca in\u017cynierska
                                Joanna Cichowska 2016"""
                                )

    def init_menu(self):
        self.file_menu = QtGui.QMenu('&Plik', self)
        self.file_menu.addAction('&Wyjście', self.file_quit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)

        self.model_menu = QtGui.QMenu('&Model', self)
        self.sabr_menu = self.model_menu.addMenu('&SABR')
        self.sabr_menu.addAction('&Deterministyczny', self.run_sabr_deterministic)
        self.sabr_menu.addAction('&Stochastyczny', self.run_sabr_stochastic)
        self.sabr_menu.addAction('&Edytuj parametry...')

        self.sbbh_menu = self.model_menu.addMenu('&SB\u2081B\u2082H')
        self.sbbh_menu.addAction('&Deterministyczny', self.run_sbbh_deterministic)
        self.sbbh_menu.addAction('&Stochastyczny', self.run_sbbh_stochastic)
        self.sbbh_menu.addAction('&Edytuj parametry...')

        self.help_menu = QtGui.QMenu('&Pomoc', self)
        self.help_menu.addAction('&O programie', self.about)

        self.menuBar().addMenu(self.file_menu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.model_menu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

    def file_quit(self):
        self.close()

    def closeEvent(self, ce):
        self.file_quit()

    def run_sabr_deterministic(self):
        model_solver = ModelSolver(modelType='SABR')
        x, y = model_solver.solve()
        self.left.plot_model(x, y, model_solver.get_legend())
        print("SABR deterministic")

    def run_sabr_stochastic(self):
        print("SABR stochastic")


    def run_sbbh_deterministic(self):
        print("SBBH deterministic")

    def run_sbbh_stochastic(self):
        print("SBBH stochastic")

qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()