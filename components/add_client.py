from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from ux import add_client_ux


class AddClientWindow(QWidget, add_client_ux.Ui_Form):
    
    def __init__(self, *args, **kwargs):
        super(AddClientWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


