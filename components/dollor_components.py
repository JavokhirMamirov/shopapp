from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import dollor_kursi_form
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore

class DollorKursiFormWindow(QDialog, dollor_kursi_form.Ui_Dialog):
    closeapp = pyqtSignal(int)
    def __init__(self, parent=None):
        super(DollorKursiFormWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)

    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.save()
        
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()

    def save(self):
        price = self.spinBox.value()
        if price != 0:
            self.closeapp.emit(price)
            self.close()