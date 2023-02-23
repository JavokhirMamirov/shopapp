import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from ux import main_ux
from libs.extra_functions import MENU_SELECTED_STYLESHEET, InsertItemToTable, TableStretchAndHide, ClearTableWidget
from components import add_client, action_button, product_components, dollor_components, search_product_frame
import sqlite3
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from db.database_tables import DataBaseTableCreate
import datetime
#create a database or connect
conn = sqlite3.connect('store.db')
cur = conn.cursor()
DataBaseTableCreate(cur)

class ShopApp(QMainWindow, main_ux.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ShopApp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_stack.setCurrentWidget(self.page_savdo)
        self.PageChanged()
        self.main_stack.currentChanged.connect(self.PageChanged)
        self.menuButtonClicked()
        self.tableWidgetSettings()
        self.pushButton_5.clicked.connect(self.openAddClientWindow)
        self.lineEdit_2.textChanged.connect(self.searchClient)
        self.listClient()
        self.listProducts()
        self.search_product_frame = search_product_frame.SearchProduct(self)
        self.pushButton_6.clicked.connect(self.openAddProductWidow)
        self.lineEdit_3.textChanged.connect(self.searchProduct)
        self.pushButton_7.clicked.connect(self.openDollorKursiForm)
        self.setDollorKursi()
        self.lineEdit.textChanged.connect(self.searchSavdoProduct)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            if self.main_stack.currentWidget() == self.page_savdo:
                self.lineEdit.setFocus()
                self.search_product_frame.hide()
        if event.key() == QtCore.Qt.Key.Key_Down:
            if self.main_stack.currentWidget() == self.page_savdo  and  self.search_product_frame.isVisible() and self.lineEdit.hasFocus():
                self.search_product_frame.table_search.selectRow(0)
                self.search_product_frame.table_search.setFocus()


    def searchSavdoProduct(self, value):
        if value != "":
            cur.execute("""select * from product where (name like (?) or brend like (?) or model like (?) or factory like (?)) limit 20""", (f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%"))
            data = cur.fetchall()
            self.search_product_frame.search_product_handler(data)
        else:
            self.search_product_frame.hide()
    
    def openDollorKursiForm(self):
        form = dollor_components.DollorKursiFormWindow(parent=self)
        form.closeapp.connect(self.closeDollorKursiForm)
        form.exec()

    def setDollorKursi(self):
        cur.execute("""select * from dollor""")
        row = cur.fetchone()
        self.label_23.setText(str(row[3])+" Сўм")
        self.label_22.setText(str(row[4]))
        self.label_20.setText(str(row[1])+" Сўм")
        self.label_21.setText(str(row[2]))

    def closeDollorKursiForm(self, price):
        cur.execute("""select * from dollor""")
        data = cur.fetchall()
        date = datetime.datetime.today().date()
        if len(data)>0:
            row = data[0]
            cur.execute("""update dollor set now_summa=?, now_date=?, old_summa=?, old_date=?""", (price, date, row[1], row[2]))
            conn.commit()
        else:
            cur.execute("""insert into dollor (now_summa, now_date) values (?,?)""",(price, date))
            conn.commit()
        self.setDollorKursi()


    
    def listProducts(self):
        cur.execute("""select * from product""")
        data = cur.fetchall()
        i = 0
        for dt in data:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.productEditClick)
            actionButtons.btn_delete.clicked.connect(self.productDeleteClick)
            lists = [
                dt[0],
                i+1,
                dt[1],
                dt[2],
                dt[3],
                dt[4],
                dt[5],
                dt[6],
                actionButtons,
            ]
            self.tableWidget_3.insertRow(i)
            InsertItemToTable(self.tableWidget_3, i, lists, list_widget=[8])
            i += 1


    def searchProduct(self, value):
        cur.execute("""select * from product where (name like (?) or brend like (?) or model like (?) or factory like (?) )""", (f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%"))
        data = cur.fetchall()
        ClearTableWidget(self.tableWidget_3)
        i = 0
        for dt in data:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.productEditClick)
            actionButtons.btn_delete.clicked.connect(self.productDeleteClick)
            lists = [
                dt[0],
                i+1,
                dt[1],
                dt[2],
                dt[3],
                dt[4],
                dt[5],
                dt[6],
                actionButtons,
            ]
            self.tableWidget_3.insertRow(i)
            InsertItemToTable(self.tableWidget_3, i, lists, list_widget=[8])
            i += 1
    
    def productEditClick(self):
        row = self.tableWidget_3.indexAt(self.sender().parent().pos()).row()
        id = self.tableWidget_3.item(row, 0).text()
        index = self.tableWidget_3.item(row, 1).text()
        name = self.tableWidget_3.item(row, 2).text()
        brend = self.tableWidget_3.item(row, 3).text()
        model = self.tableWidget_3.item(row, 4).text()
        factory = self.tableWidget_3.item(row, 5).text()
        price_box = self.tableWidget_3.item(row, 6).text()
        price_one = self.tableWidget_3.item(row, 7).text()
        data = {
            "id":id,
            "row":row,
            "index":index,
            "name":name,
            "brend":brend,
            "model":model,
            "factory":factory,
            "price_box":price_box,
            "price_one":price_one,
        }
        editClientWindow = product_components.EditProductWindow(data=data, parent=self)
        editClientWindow.closeapp.connect(self.closeEditProductWindow)
        editClientWindow.exec()
    

    def productDeleteClick(self):
        row = self.tableWidget_3.indexAt(self.sender().parent().pos()).row()
        id = self.tableWidget_3.item(row, 0).text()
        reply = QMessageBox.question(self, 'Ўчириш', "Сиз ушбу махсулотни ўчирмоқчимисиз?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            cur.execute("""delete from product where id=?""", id)
            conn.commit()
            ClearTableWidget(self.tableWidget_3)
            self.listProducts()
        else:
            pass

    def closeEditProductWindow(self, data):
        if data:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.productEditClick)
            actionButtons.btn_delete.clicked.connect(self.productDeleteClick)
            lists = [   
                data['id'],
                data['index'],
                data['name'],
                data['brend'],
                data['model'],
                data['factory'],
                data['price_box'],
                data['price_one'],
                actionButtons
            ]
            InsertItemToTable(self.tableWidget_3, data['row'], lists, list_widget=[8] )
            
    
    def openAddProductWidow(self):
        addProductWindow = product_components.AddProductWindow(parent=self)
        addProductWindow.closeapp.connect(self.closeAddProductWindow)
        addProductWindow.exec()

    def closeAddProductWindow(self, refresh):
        if refresh:
            ClearTableWidget(self.tableWidget_3)
            self.listProducts()

    def searchClient(self, value):
        cur.execute("""select * from client where (name like (?) or company like (?) or phone like (?) )""", (f"%{value}%", f"%{value}%", f"%{value}%"))
        data = cur.fetchall()
        ClearTableWidget(self.tableWidget_2)
        i = 0
        for dt in data:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.clientEditClick)
            actionButtons.btn_delete.clicked.connect(self.clientDeleteClick)
            lists = [
                dt[0],
                i+1,
                dt[1],
                dt[2],
                dt[3],
                actionButtons,
            ]
            self.tableWidget_2.insertRow(i)
            InsertItemToTable(self.tableWidget_2, i, lists, list_widget=[5])
            i += 1

    def clientEditClick(self):
        row = self.tableWidget_2.indexAt(self.sender().parent().pos()).row()
        id = self.tableWidget_2.item(row, 0).text()
        index = self.tableWidget_2.item(row, 1).text()
        name = self.tableWidget_2.item(row, 2).text()
        company = self.tableWidget_2.item(row, 3).text()
        phone = self.tableWidget_2.item(row, 4).text()
        data = {
            "id":id,
            "row":row,
            "index":index,
            "name":name,
            "company":company,
            "phone":phone
        }
        editClientWindow = add_client.EditClientWindow(data=data, parent=self)
        editClientWindow.closeapp.connect(self.closeEditClientWindow)
        editClientWindow.exec()

    def closeEditClientWindow(self, list):
        if list:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.clientEditClick)
            actionButtons.btn_delete.clicked.connect(self.clientDeleteClick)
            lists = [   
                list['id'],
                list['index'],
                list['name'],
                list['company'],
                list['phone'],
                actionButtons
            ]
            InsertItemToTable(self.tableWidget_2,list['row'], lists, list_widget=[5] )

    def clientDeleteClick(self):
        row = self.tableWidget_2.indexAt(self.sender().parent().pos()).row()
        id = self.tableWidget_2.item(row, 0).text()
        reply = QMessageBox.question(self, 'Ўчириш', "Сиз ушбу мижозни ўчирмоқчимисиз?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            cur.execute("""delete from client where id=?""", id)
            conn.commit()
            ClearTableWidget(self.tableWidget_2)
            self.listClient()
        else:
            pass


    def listClient(self):
        cur.execute("""select * from client""")
        data = cur.fetchall()
        i = 0
        for dt in data:
            actionButtons = action_button.ActionButtons(edit=True, delete=True)
            actionButtons.btn_edit.clicked.connect(self.clientEditClick)
            actionButtons.btn_delete.clicked.connect(self.clientDeleteClick)
            lists = [
                dt[0],
                i+1,
                dt[1],
                dt[2],
                dt[3],
                actionButtons,
            ]
            self.tableWidget_2.insertRow(i)
            InsertItemToTable(self.tableWidget_2, i, lists, list_widget=[5])
            i += 1

    
    def closeAddClientWindow(self, refresh):
        if refresh:
            ClearTableWidget(self.tableWidget_2)
            self.listClient()

    def openAddClientWindow(self):
        addClientWindow = add_client.AddClientWindow(parent=self)
        addClientWindow.closeapp.connect(self.closeAddClientWindow)
        addClientWindow.exec()


    def menuButtonClicked(self):
        self.btn_savdo.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_savdo))
        self.btn_client.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_client))
        self.btn_product.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_maxsulotlar))
        self.btn_savdolar.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_savdolar))
        self.btn_dollor.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_dollor))

    
    def tableWidgetSettings(self):
        self.tableWidget_5.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setVisible(True)

        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget_2.setColumnWidth(1,50)
        self.tableWidget_3.setColumnWidth(1,50)
        self.tableWidget_4.setColumnWidth(1,50)
        self.tableWidget_5.setColumnWidth(1,50)

        TableStretchAndHide(self.tableWidget, lists_column=[2,6],sizeContent=[3,4,5,7,8,9,10], hide_column=[0])
        TableStretchAndHide(self.tableWidget_5, lists_column=[2,6],sizeContent=[3,4,5,7,8,9,10], hide_column=[0])
        TableStretchAndHide(self.tableWidget_2, lists_column=[2,3],hide_column=[0])
        TableStretchAndHide(self.tableWidget_3, lists_column=[2, 5],hide_column=[0], sizeContent=[6,7,8])
        TableStretchAndHide(self.tableWidget_4, lists_column=[2],hide_column=[0])


    def PageChanged(self):
        widget = self.main_stack.currentWidget()
        if widget == self.page_savdo:
            self.set_active_menu(self.btn_savdo)
        elif widget == self.page_client:
            self.set_active_menu(self.btn_client)
        elif widget == self.page_maxsulotlar:
            self.set_active_menu(self.btn_product)
        elif widget == self.page_savdolar:
            self.set_active_menu(self.btn_savdolar)
        elif widget == self.page_dollor:
            self.set_active_menu(self.btn_dollor)


    def set_active_menu(self, btn):
        self.resetStyle(btn.objectName())
        btn.setStyleSheet(
            self.selectMenu(btn.styleSheet(), btn.objectName()))

    def selectMenu(self, getStyle, btnName):
        select = getStyle + "\n" + MENU_SELECTED_STYLESHEET
        Image = getStyle.split('QPushButton')
        newImage = Image[2].replace(":hover", "")
        select = select + "\n" + "#" + btnName + newImage
        return select
    
    def deselectMenu(self, getStyle, btnName):
        deselect = getStyle.replace("\n"+MENU_SELECTED_STYLESHEET, "")
        Image = getStyle.split('QPushButton')
        newImage = Image[2].replace(":hover", "")
        deselect = deselect.replace("\n" + "#" + btnName + newImage[:-1],'')
        return deselect
    
    def resetStyle(self, widget):
        
        for w in self.sidebar_menu_frame.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet(), w.objectName()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShopApp()
    window.show()
    sys.exit(app.exec_())
    