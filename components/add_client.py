from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import add_client_ux
from PyQt5.QtCore import pyqtSignal
import sqlite3

#create a database or connect
conn = sqlite3.connect('store.db')
cur = conn.cursor()

class AddClientWindow(QDialog, add_client_ux.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, *args, **kwargs):
        super(AddClientWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)


    def save(self):
        name = self.lineEdit_8.text()
        company = self.lineEdit_7.text()
        phone = self.lineEdit_9.text()
        if name != "":
            cur.execute("""insert into client (name, company, phone) values (?,?,?)""", (name, company, phone))
            conn.commit()
            self.close()
            self.closeapp.emit(True)


