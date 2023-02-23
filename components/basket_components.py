from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import add_basket
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
import sqlite3

#create a database or connect
conn = sqlite3.connect('store.db')
cur = conn.cursor()

class AddBasketWindow(QDialog, add_basket.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, id, parent=None):
        super(AddBasketWindow, self).__init__(parent)
        self.setupUi(self)
        self.id = id
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.save)
        self.spinBox_3.selectAll()
        self.setdata()
    def setdata(self):
        cur.execute("""select * from product where id=?""",(self.id))
        data = cur.fetchone()
        self.lineEdit_8.setText(str(data[1]))
        self.lineEdit_9.setText(str(data[3]))
        self.lineEdit_7.setText(str(data[2]))
        self.lineEdit_10.setText(str(data[4]))
        self.doubleSpinBox.setValue(data[5])
        self.doubleSpinBox_2.setValue(data[6])
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or QtCore.Qt.Key.Key_Return == event.key():
            self.save()

    def save(self):
        cur.execute("""select * from product where id=?""",(self.id))
        data = cur.fetchone()
        cur.execute("""select * from dollor""")
        dollor = cur.fetchone()
        count = self.spinBox_3.value()
        dona = self.radioButton.isChecked()
        komp = self.radioButton_2.isChecked()
        if dona:
            birlik = "Dona"
            price = int(data[6]*dollor[1])
            summa = int(price*count)

        if komp:
            birlik = "Komp"
            price = int(data[5]*dollor[1])
            summa = int(price*count)
        print(data[0])
        cur.execute("""select * from basket where (product_id=? and savdo_id IS NULL)""", (self.id))
        pro = cur.fetchone()
        print(pro)
        if pro is not None:
            cur.execute("""update basket set product_id=?, name=?, brend=?, model=?, factory=?, birlik=?,narxi=?, soni=?, summa=? where id=?""", (data[0], data[1], data[2], data[3], data[4], birlik,price, count, summa, pro[0]))
            conn.commit()
        else:
            cur.execute("""insert into basket (product_id, name, brend, model, factory, birlik, narxi, soni, summa) values (?,?,?,?,?,?,?,?,?)""", (data[0], data[1], data[2], data[3], data[4], birlik, price, count, summa ))
            conn.commit()
        self.close()
        self.closeapp.emit(True)
        