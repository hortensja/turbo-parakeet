from PyQt4 import QtGui

from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QVBoxLayout


class ParamsDisplay(QtGui.QGridLayout):

    def __init__(self, parameters, parent=None):
        super(ParamsDisplay, self).__init__(parent)

        self.names = QVBoxLayout(), QVBoxLayout()
        self.values = QVBoxLayout(), QVBoxLayout()

        self.set_parameters(parameters)

    def set_parameters(self, parameters):
        self.params = parameters.get_params()
        self.inits = parameters.get_inits()
        self.init_names = parameters.get_inits_names()

        for i in range(2):
            self.addLayout(self.names[i], 0, 2 * i)
            self.addLayout(self.values[i], 0, 2 * i + 1)

        for n, p in self.params.iteritems():
            self.names[0].addWidget(QLabel(n))
            self.values[0].addWidget(QLabel(str(p)))

        for j in range(len(self.init_names)):
            n = self.init_names[j]
            p = self.inits[j]
            self.names[1].addWidget(QLabel(n))
            self.values[1].addWidget(QLabel(str(p)))

    def clear(self):
        for i in range(2):
            while self.values[i].count():
                item = self.values[i].takeAt(0)
                widget = item.widget()
                widget.deleteLater()
            while self.names[i].count():
                item = self.names[i].takeAt(0)
                widget = item.widget()
                widget.deleteLater()
