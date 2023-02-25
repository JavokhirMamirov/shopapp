from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import add_client_ux, edit_client_ux
from PyQt5.QtCore import pyqtSignal
import sqlite3

class AddClientWindow(QDialog, add_client_ux.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(AddClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)


    def save(self):
        name = self.lineEdit_8.text()
        company = self.lineEdit_7.text()
        phone = self.lineEdit_9.text()
        if name != "":
            self.parent.cur.execute("""insert into client (name, company, phone) values (?,?,?)""", (name, company, phone))
            self.parent.conn.commit()
            self.close()
            self.closeapp.emit(True)


class EditClientWindow(QDialog, edit_client_ux.Ui_Dialog):
    closeapp = pyqtSignal(dict)
    def __init__(self, data, parent=None):
        super(EditClientWindow, self).__init__(parent)
        self.setupUi(self)
        self.id = data['id']
        self.data = data
        self.parent = parent
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)
        self.lineEdit_7.setText(data['company'])
        self.lineEdit_9.setText(data['phone'])
        self.lineEdit_8.setText(data['name'])


    def save(self):
        name = self.lineEdit_8.text()
        company = self.lineEdit_7.text()
        phone = self.lineEdit_9.text()
        if name != "":
            self.parent.cur.execute("""update client set name=?, company=?, phone=? where id=?""", (name, company, phone, self.id))
            self.parent.conn.commit()
            self.close()
            self.data['name'] = name
            self.data['company'] = company
            self.data['phone'] = phone
            self.closeapp.emit(self.data)


