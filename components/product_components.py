from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import add_product, edit_product
from PyQt5.QtCore import pyqtSignal
import sqlite3

#create a database or connect
conn = sqlite3.connect('store.db')
cur = conn.cursor()

class AddProductWindow(QDialog, add_product.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, *args, **kwargs):
        super(AddProductWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)


    def save(self):
        name = self.lineEdit_8.text()
        brend = self.lineEdit_7.text()
        model = self.lineEdit_9.text()
        price = self.doubleSpinBox.value()
        if name != "" and price != 0:
            cur.execute("""insert into product (name, brend, model, price) values (?,?,?,?)""", (name, brend, model, price))
            conn.commit()
            self.close()
            self.closeapp.emit(True)

class EditProductWindow(QDialog, edit_product.Ui_Dialog):
    closeapp = pyqtSignal(dict)
    def __init__(self, data, parent=None):
        super(EditProductWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)
        self.data = data
        self.lineEdit_7.setText(data['brend'])
        self.lineEdit_8.setText(data['name'])
        self.lineEdit_9.setText(data['model'])
        self.doubleSpinBox.setValue(float(data['price']))

    def save(self):
        name = self.lineEdit_8.text()
        brend = self.lineEdit_7.text()
        model = self.lineEdit_9.text()
        price = self.doubleSpinBox.value()
        if name != "" and price != 0:
            cur.execute("""update product set name=?, brend=?, model=?, price=? where id=?""", (name, brend, model, price, self.data['id']))
            conn.commit()
            self.close()
            self.data['name'] = name
            self.data['brend'] = brend
            self.data['model'] = model
            self.data['price'] = price
            self.closeapp.emit(self.data)