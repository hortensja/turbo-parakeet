from __future__ import unicode_literals

from PyQt4.QtCore import QDateTime
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDateTimeEdit
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QVBoxLayout

from gui.param_box import ParamBox
from parameters import Parameters


class ParamsEditor(QDialog):
    def __init__(self, old_params, parent=None):
        super(ParamsEditor, self).__init__(parent)

        self.setWindowTitle('Edytor parametr\u00f3w')

        self.all_params = old_params.get_params(), old_params.get_globals(), old_params.get_inits()
        self.names = old_params.get_inits_names()

        self.manage_layout()
        self.manage_paramboxes()
        self.manage_buttons()


        self.setVisible(True)
        # nice widget for editing the date
        self.datetime = QDateTimeEdit(self)
        #self.datetime.setDateTime(QDateTime.currentDateTime())
        #self.layout.addWidget(self.datetime)
        #self.show()


    def dateTime(self):
        return self.datetime.dateTime()

    def randomize(self):
        print('randomization')

    def manage_layout(self):
        self.layout = QGridLayout(self)
        for i in range(3):
            self.layout.setColumnMinimumWidth(2*i, 50)
            self.layout.setColumnStretch(2*i, 0.5)
            self.layout.setColumnMinimumWidth(2*i+1, 150)
            self.layout.setColumnStretch(2*i+1, 1)

    def manage_buttons(self):
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok,
            Qt.Horizontal, self)

        button_randomize = QPushButton("&Losuj")
        button_cancel = QPushButton("&Anuluj")
        buttons.addButton(button_randomize, QDialogButtonBox.ActionRole)
        buttons.addButton(button_cancel, QDialogButtonBox.RejectRole)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        button_randomize.clicked.connect(self.randomize)

        self.layout.addWidget(buttons, 1, 3)

    def manage_paramboxes(self):
        self.sbox_list = {}
        layouts = QVBoxLayout(), QVBoxLayout(), QVBoxLayout()
        descr_layouts = QVBoxLayout(), QVBoxLayout(), QVBoxLayout()
        for i in range(3):
            try:
                for name, param in self.all_params[i].iteritems():
                    print(i, name, param)
                    sbox = ParamBox(name, param)
                    self.sbox_list[name] = sbox
                    layouts[i].addWidget(sbox)
                    descr_layouts[i].addWidget(QLabel(name))
            except AttributeError:
                for j in range(len(self.names)):
                    name = self.names[j]
                    param = self.all_params[i][j]
                    print(j, name, self.all_params[i][j])
                    sbox = ParamBox(name, self.all_params[i][j])
                    self.sbox_list[name] = sbox
                    layouts[i].addWidget(sbox)
                    descr_layouts[i].addWidget(QLabel(name))

            self.layout.addLayout(descr_layouts[i], 0, 2 * i)
            self.layout.addLayout(layouts[i], 0, 2 * i + 1)

    def get_all_params(self, parent=None):
        p = Parameters(self.names, *self.all_params)
        print(p)
        result = self.exec_()
        for name, sbox in self.sbox_list.iteritems():
             p.update_one(name, sbox.get_value())
             print(name, sbox.get_value())
        p.update()
        return (p, result == QDialog.Accepted)

