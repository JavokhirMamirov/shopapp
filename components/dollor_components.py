from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import dollor_kursi_form
from PyQt5.QtCore import pyqtSignal


class DollorKursiFormWindow(QDialog, dollor_kursi_form.Ui_Dialog):
    closeapp = pyqtSignal(int)
    def __init__(self, parent=None):
        super(DollorKursiFormWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)


    def save(self):
        price = self.spinBox.value()
        if price != 0:
            self.closeapp.emit(price)
            self.close()