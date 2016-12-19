# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QPushButton
from PyQt4 import QtGui, QtCore

from gui.params_display import ParamsDisplay
from gui.params_editor import ParamsEditor
from gui.plot_widget import StaticPlotCanvas
from model_solver import ModelSolver



class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Modelowanie i symulacje ED")

        self.init_menu()

        self.main_widget = QtGui.QWidget(self)

        self.layout = QtGui.QGridLayout(self.main_widget)

        self.plot_canvases = StaticPlotCanvas(self.main_widget), StaticPlotCanvas(self.main_widget)

        self.model_solvers = [None, None]
        self.params_displays = [QGridLayout(), QGridLayout()]

        self.layout.addWidget(self.plot_canvases[0], 0, 0, 2, 4)
        self.layout.addWidget(self.plot_canvases[1], 0, 4, 2, 4)

        button_edit = QPushButton("&Edytuj parametry")
        button_edit.clicked.connect(self.edit_parameters)
        self.layout.addWidget(button_edit, 3, 3, 1, 2)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

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
        self.model_menu.addAction('&SABR', self.run_sabr_deterministic)
        self.model_menu.addAction('&SB\u2081B\u2082H', self.run_sbbh_deterministic)

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
        self.run_deterministic(type='SABR')
        print("SABR deterministic")

    def run_sbbh_deterministic(self):
        self.run_deterministic(type='SBBH')
        print("SBBH deterministic")

    def run_deterministic(self, type, which=0):
        for i in range(2):
            self.model_solvers[i] = ModelSolver(model_type=type)
        self.refresh_plot(which)

    def refresh_param_display(self, which=0):
        try:
            self.params_displays[which].clear()
        except AttributeError:
            pass
        self.layout.removeItem(self.params_displays[which])
        self.params_displays[which] = ParamsDisplay(self.model_solvers[which].get_params())
        self.layout.addLayout(self.params_displays[which], 4, 4*which, 2, 4)

    def refresh_plot(self, which=0, name=None):
        if name is None:
            name = "model "
        x, y = self.model_solvers[which].solve()
        self.plot_canvases[which].plot_model(x, y, self.model_solvers[which].get_legend(),
                                      name + self.model_solvers[which].get_title())
        self.refresh_param_display(which)

    def edit_parameters(self, which=0):
        if self.model_solvers[which] is None:
            msg = QtGui.QMessageBox()
            msg.setText("Najpierw wybierz model")
            msg.setWindowTitle("(!)")
            msg.exec_()
        else:
            p_e = ParamsEditor(self.model_solvers[which].get_params())
            all_params, status, comp = p_e.get_all_params()
            if comp == 69:
                which = 1
            if status is True:
                self.model_solvers[which].update_params(all_params)
                #print(self.model_solvers[which].get_params())
                self.refresh_plot(which)


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()