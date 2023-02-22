from PyQt5.QtWidgets import QDialog, QApplication, QPushButton
from ux import add_client_ux


class AddClientWindow(QDialog, add_client_ux.Ui_Dialog):
    
    def __init__(self, *args, **kwargs):
        super(AddClientWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)


