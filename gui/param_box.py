from PyQt4.QtGui import QDoubleSpinBox


class ParamBox(QDoubleSpinBox):

    def __init__(self, name, value=0.0, parent=None):
        super(ParamBox, self).__init__(parent)
        self.setSingleStep(0.1)
        self.setMaximum(50.0)
        self.setDecimals(3)
        self.setValue(value)
        self.name = name


    def get_value(self):
        return self.value()

    def get_name(self):
        return self.name

    def update(self, value):
        self.value = value