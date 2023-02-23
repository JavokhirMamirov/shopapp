from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import add_product, edit_product
from PyQt5.QtCore import pyqtSignal
import sqlite3

#create a database or connect
conn = sqlite3.connect('store.db')
cur = conn.cursor()

class AddProductWindow(QDialog, add_product.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(AddProductWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)


    def save(self):
        name = self.lineEdit_8.text()
        brend = self.lineEdit_7.text()
        model = self.lineEdit_9.text()
        factory = self.lineEdit_10.text()
        price_box = self.doubleSpinBox.value()
        price_one = self.doubleSpinBox_2.value()
        if name != "" and price_box != 0 and price_one != 0:
            cur.execute("""insert into product (name, brend, model,factory, price_box, price_one) values (?,?,?,?,?,?)""", (name, brend, model,factory,price_box, price_one))
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
        self.lineEdit_10.setText(data['factory'])
        self.doubleSpinBox.setValue(float(data['price_box']))
        self.doubleSpinBox_2.setValue(float(data['price_one']))

    def save(self):
        name = self.lineEdit_8.text()
        brend = self.lineEdit_7.text()
        model = self.lineEdit_9.text()
        factory = self.lineEdit_10.text()
        price_box = self.doubleSpinBox.value()
        price_one = self.doubleSpinBox_2.value()
        if name != "" and price_box != 0 and price_one != 0:
            cur.execute("""update product set name=?, brend=?, model=?, factory=?, price_box=?, price_one=? where id=?""", (name, brend, model,factory, price_box,price_one, self.data['id']))
            conn.commit()
            self.close()
            self.data['name'] = name
            self.data['brend'] = brend
            self.data['model'] = model
            self.data['factory'] = factory
            self.data['price_box'] = price_box
            self.data['price_one'] = price_one
            self.closeapp.emit(self.data)