from PyQt4.QtGui import QDoubleSpinBox


class ParamBox(QDoubleSpinBox):

    def __init__(self, name, value = 0.0, parent=None):
        super(ParamBox, self).__init__(parent)
        #QDoubleSpinBox.__init__(parent)
        self.setSingleStep(0.1)
        self.setMaximum(10.0)
        self.setValue(value)
        self.name = name



