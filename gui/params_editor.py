from __future__ import unicode_literals

from PyQt4.QtCore import QDateTime
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDateTimeEdit
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QDoubleSpinBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QVBoxLayout

from gui.param_box import ParamBox


class ParamsEditor(QDialog):
    def __init__(self, old_params, parent=None):
        super(ParamsEditor, self).__init__(parent)

        self.setWindowTitle('Edytor parametr\u00f3w')

        self.layout = QGridLayout(self)

        layout_params_descr = QVBoxLayout()
        layout_params = QVBoxLayout()
        layout_globals_descr = QVBoxLayout()
        layout_globals = QVBoxLayout()
        layout_inits = QVBoxLayout()

        self.all_params = old_params
        o_p = self.all_params.get_params()
        g_p = self.all_params.get_globals()

        for name, param in o_p.iteritems():
            print(name, param)
            sbox = ParamBox(name, param)
            layout_params.addWidget(sbox)
            layout_params_descr.addWidget(QLabel(name))

        for name, param in g_p.iteritems():
            print(name, param)
            sbox = ParamBox(name, param)
            layout_globals.addWidget(sbox)
            layout_globals_descr.addWidget(QLabel(name))

        self.layout.addLayout(layout_params_descr, 0, 0)
        self.layout.addLayout(layout_globals_descr, 0, 2)

        self.layout.addLayout(layout_params, 0, 1)
        self.layout.addLayout(layout_globals, 0, 3)
        self.layout.addLayout(layout_inits, 0, 5)

        self.manage_buttons()

        # nice widget for editing the date
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        self.layout.addWidget(self.datetime)



    def dateTime(self):
        return self.datetime.dateTime()

    def randomize(self):
        print('randomization')

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

    def get_all_params(self, parent = None):
        #dialog = ParamsEditor(parent)
        dialog = self
        date = dialog.dateTime()
        result = dialog.exec_()
        return self.all_params
        #return Parameters(params, globals, inits)
        return (date.date(), date.time(), result == QDialog.Accepted)

