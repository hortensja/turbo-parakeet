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

        self.all_params = [old_params.get_params(), old_params.get_globals(), old_params.get_inits()]
        self.names = old_params.get_inits_names()

        self.manage_layout()
        self.sbox_list = {}
        self.layouts = [QVBoxLayout(), QVBoxLayout(), QVBoxLayout()]
        self.descr_layouts = QVBoxLayout(), QVBoxLayout(), QVBoxLayout()
        self.manage_paramboxes()
        self.manage_buttons()

        self.comp = None

        self.setVisible(True)

    def randomize(self):
#        self.all_params[0] = Parameters.randomize_params(self.all_params[0])
#        self.update_paramboxes(self.all_params[0])
#        self.show()
        print('randomization')


    def manage_layout(self):
        self.layout = QGridLayout(self)
        for i in range(3):
            self.layout.setColumnMinimumWidth(2*i, 50)
            self.layout.setColumnStretch(2*i, 0.5)
            self.layout.setColumnMinimumWidth(2*i+1, 150)
            self.layout.setColumnStretch(2*i+1, 1)

    def manage_buttons(self):
        buttons = QDialogButtonBox(Qt.Horizontal, self)

        button_randomize = QPushButton("&Losuj")
        button_cancel = QPushButton("&Anuluj")
        button_replace = QPushButton("&Zast\u0105p")
        button_compare = QPushButton("&Por\u00F3wnaj")
        buttons.addButton(button_randomize, QDialogButtonBox.ActionRole)
        buttons.addButton(button_cancel, QDialogButtonBox.RejectRole)
        buttons.addButton(button_replace, QDialogButtonBox.AcceptRole)
        buttons.addButton(button_compare, QDialogButtonBox.AcceptRole)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        button_randomize.clicked.connect(self.randomize)
        button_compare.clicked.connect(self.compare)

        self.layout.addWidget(buttons, 1, 3)

    def manage_paramboxes(self):
        for i in range(3):
            try:
                for name, param in self.all_params[i].iteritems():
                    print(i, name, param)
                    try:
                        self.add_parambox(name, param, i)
                    except TypeError:
                        pass
            except AttributeError:
                for j in range(len(self.names)):
                    name = self.names[j]
                    param = self.all_params[i][j]
                    print(j, name, self.all_params[i][j])
                    self.add_parambox(name, param, i)
            self.layout.addLayout(self.descr_layouts[i], 0, 2 * i)
            self.layout.addLayout(self.layouts[i], 0, 2 * i + 1)

    def add_parambox(self, name, param, layout_no):
        sbox = ParamBox(name, param)
        self.sbox_list[name] = sbox
        self.layouts[layout_no].addWidget(sbox)
        self.descr_layouts[layout_no].addWidget(QLabel(name))

    def update_paramboxes(self, p_dict):
        for name, p in p_dict:
            self.sbox_list[name].update(p)


    def get_all_params(self, parent=None):
        p = Parameters(self.names, *self.all_params)
        #print(p)
        result = self.exec_()
        for name, sbox in self.sbox_list.iteritems():
            p.update_one(name, sbox.get_value())
            #print(name, sbox.get_value())
        p.update()
        print("self result: ", result)
        return (p, result == QDialog.Accepted, self.comp)

    def compare(self):
        self.comp = 69
        print(self.comp)
        self.close()