import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from ux import main_ux
from libs.extra_functions import MENU_SELECTED_STYLESHEET, InsertItemToTable, TableStretchAndHide, ClearTableWidget
from components import add_client, action_button, product_components, dollor_components, search_product_frame, basket_components
import sqlite3
from PyQt5 import QtCore, QtGui
from db.database_tables import DataBaseTableCreate
import datetime
from PyQt5 import QtPrintSupport
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
        self.cur = cur
        self.conn = conn
        self.total_summa = 0
        self.savdo_id = None
        self.search_product_frame = search_product_frame.SearchProduct(self)
        self.pushButton_6.clicked.connect(self.openAddProductWidow)
        self.lineEdit_3.textChanged.connect(self.searchProduct)
        self.pushButton_7.clicked.connect(self.openDollorKursiForm)
        self.setDollorKursi()
        self.lineEdit.textChanged.connect(self.searchSavdoProduct)
        self.basketList()
        self.setClientComboboxItems()
        self.btn_save.clicked.connect(self.saveSavdo)
        self.listSavdolar()
        self.lineEdit_4.textChanged.connect(self.listSavdolar)
        self.showSavdoButtons()
        self.tableWidget_4.doubleClicked.connect(self.openSavdoDetail)
        self.btn_clear.clicked.connect(self.clearBasket)  
        self.btn_edit.clicked.connect(self.clickEditButton)  
        self.btn_new.clicked.connect(self.newSavdo)
        self.btn_print.clicked.connect(self.printPerview)


    def printPerview(self):
        self.printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.ScreenResolution)
        self.print_perview_dialog = QtPrintSupport.QPrintPreviewDialog(self.printer)
        self.print_perview_dialog.paintRequested.connect(self.handlePaintRequest)
        self.print_perview_dialog.exec_()


    def handlePaintRequest(self, printer):
        document = self.makeTableDocument()
        document.print_(printer)

    def makeTableDocument(self):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        document.setDocumentMargin(3)
        cur.execute("""select * from savdo where id=?""", (self.savdo_id,))
        savdo = cur.fetchone()

        cur.execute("""select * from client where id=?""", (savdo[1],))
        client = cur.fetchone()
        if self.savdo_id is not None:
            cur.execute("""select * from basket where savdo_id=?;""",(self.savdo_id,))
        else:
            cur.execute("""select * from basket where savdo_id IS NULL;""")
        data = cur.fetchall()
        i = 0
        total_summa = 0
        html_tr=""
        for dt in data:
            total_summa += dt[11]
            html_tr += f"<tr><td>{i+1}</td><td>{dt[3]}</td><td>{dt[4]}</td><td>{dt[5]}</td><td>{dt[6]}</td><td>{dt[7]}</td><td>{dt[10]}</td><td>{dt[9]:,}</td><td>{dt[11]:,}</td></tr>"
            i += 1
        if self.savdo_id is not None:
            cur.execute("""update savdo set summa=? where id=?""",(self.total_summa, self.savdo_id))
            conn.commit()
        html = """<html>
                    <head>
                        <style>
                            #header {
                                border:none;
                                margin-bottom: 20px;
                            }
                            #header th, #header td{
                                border:none;
                                border-style:none;
                                word-wrap: break-word;
                                text-align: left;
                                padding: 5px;
                            }

                            #list {
                                border: 1px solid;
                                border-collapse: collapse;
                                
                            }

                            #list th, #list td {
                                border: 1px solid;
                                word-wrap: break-word;
                                text-align: center;
                                padding: 5px;
                                border-collapse: collapse;
                            }
                        </style>
                    </head>
                    <body>
                        <table id="header" width="100%">
                            <tr>
                                <td>Мижоз</td>
                                <td>106</td>
                                <td>Bizning firma</td>
                            </tr>
                            <tr>
                                <td>"""+str(client[1])+"""</td>
                                <td>Чек № """+str(savdo[0])+"""</td>
                                <td>998989</td>
                            </tr>
                            <tr>
                                <td>"""+str(client[3])+"""</td>
                                <td></td>
                                <td>manzil</td>
                            </tr>
                        </table>
                        <table id="list"  width="100%">
                            <tr>
                                <th>№</th>
                                <th>Махсулот номи</th>
                                <th>Модел</th>
                                <th>Бренд</th>
                                <th>Ишлаб чиқарувчи</th>
                                <th>Бирлиги</th>
                                <th>Сони</th>
                                <th>Нархи</th>
                                <th>Сумма</th>
                            </tr>"""+html_tr+"""
                        </table>
                    </body>
                </html>"""

        cursor.insertHtml(html)
        return document

    def openSavdoDetail(self):
        row = self.tableWidget_4.currentRow()
        if row >= 0:
            id = self.tableWidget_4.item(row, 0).text()
            client_id = self.tableWidget_4.item(row, 1).text()
            self.savdo_id = id
            self.basketList()
            
            self.main_stack.setCurrentWidget(self.page_savdo)
            index = self.comboBox.findData(client_id)
            self.comboBox.setCurrentIndex(index)
            self.lineEdit.setEnabled(False)
            self.comboBox.setEnabled(False)
            
            self.showSavdoButtons()

    def newSavdo(self):
        self.savdo_id = None
        self.basketList()
        self.showSavdoButtons()
        self.lineEdit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.comboBox.setCurrentIndex(0)
    def clearBasket(self):
        if self.tableWidget.rowCount() > 0:
            reply = QMessageBox.question(self, 'Ўчириш', "Сиз саватчадаги барча махсулотларни ўчирмоқчимисиз?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                if self.savdo_id is not None:
                    cur.execute("""delete from basket where savdo_id=?""",(self.savdo_id,))
                else:
                    cur.execute("""delete from basket where savdo_id is null""")
                conn.commit()
                self.basketList()
            else:
                pass
        
    def showSavdoButtons(self):
        if self.savdo_id is None:
            self.btn_edit.setVisible(False)
            self.btn_print.setVisible(False)
            self.btn_new.setVisible(False)
            self.btn_clear.setVisible(True)
            self.btn_save.setVisible(True)
        else:
            self.btn_edit.setVisible(True)
            self.btn_print.setVisible(True)
            self.btn_new.setVisible(True)
            self.btn_clear.setVisible(False)
            self.btn_save.setVisible(False)
    
    def afterSavePermission(self):
        self.lineEdit.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.btn_clear.setVisible(False)
        self.btn_save.setVisible(False)
        self.btn_edit.setVisible(True)
        self.btn_print.setVisible(True)
        self.btn_new.setVisible(True)
    
    def clickEditButton(self):
        self.lineEdit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.btn_clear.setVisible(True)
        self.btn_save.setVisible(True)
        self.btn_edit.setVisible(False)
        self.btn_print.setVisible(False)
        self.btn_new.setVisible(False)

    def listSavdolar(self, value=None):
        if value is not None:
            cur.execute("""select * from savdo where id=? or client like (?) or sana like (?) order by id desc""", (value,f"%{value}%",f"%{value}%"))
        else:
            cur.execute("""select * from savdo order by id desc""")
        
        data = cur.fetchmany(250)
        i = 0
        ClearTableWidget(self.tableWidget_4)
        for dt in data:
            lists = [
                dt[0],
                dt[1],
                i+1,
                dt[2],
                f"{dt[3]:,}",
                dt[4]
            ]
            self.tableWidget_4.insertRow(i)
            InsertItemToTable(self.tableWidget_4, i, lists)
            i += 1
        



    def saveSavdo(self):
        client = self.comboBox.currentData()
        client_name = self.comboBox.currentText()
        rowcount = self.tableWidget.rowCount()
        if rowcount > 0:
            reply = QMessageBox.question(self, 'Сотиш', f"Сиз ушбу махсулотларни << {client_name} >>га сотмоқчимисиз?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
            if reply == QMessageBox.Yes:
                if self.savdo_id is not None:
                    cur.execute("""update savdo set client_id=?, client=?, summa=? where id=?""", (client, client_name, self.total_summa, self.savdo_id))
                    conn.commit()
                else:
                    cur.execute("""insert into savdo (client_id, client, summa, sana) values (?,?,?,?)""",(client, client_name, self.total_summa, datetime.datetime.today().date()))
                    conn.commit()
                    cur.execute("""select * from savdo order by id DESC""")
                    dt = cur.fetchone()
                    cur.execute("""update basket set savdo_id=? where savdo_id is NULL;""", (dt[0],))
                    conn.commit()
                    self.savdo_id = dt[0]
                self.afterSavePermission()
                self.basketList()
            else:
                pass

    def setClientComboboxItems(self):
        cur.execute("""select * from client""")
        data = cur.fetchall()
        self.comboBox.clear()
        for dt in data:
            self.comboBox.addItem(dt[1], dt[0])

    def basketList(self):
        if self.savdo_id is not None:
            cur.execute("""select * from basket where savdo_id=?;""",(self.savdo_id,))
        else:
            cur.execute("""select * from basket where savdo_id IS NULL;""")
        data = cur.fetchall()
        ClearTableWidget(self.tableWidget)
        i = 0
        total_summa = 0
        
        # colors = [
        #     {
        #         'i':3,
        #         'bg':'#92cbdf',
        #         'color':'#fff'
        #     },
        #     {
        #         'i':4,
        #         'bg':'#be4d25',
        #         'color':'#fff'
        #     },
        #     {
        #         'i':5,
        #         'bg':'#6c25be',
        #         'color':'#fff'
        #     },
        #     {
        #         'i':6,
        #         'bg':'#30BE25',
        #         'color':'#fff'
        #     },
        #     {
        #         'i':7,
        #         'bg':'#25a5be',
        #         'color':'#fff'
        #     },
        #     {
        #         'i':8,
        #         'bg':'#92cbdf',
        #         'color':'#fff'
        #     },
        # ]
        for dt in data:
            lists = [
                dt[0],
                dt[2],
                i+1,
                dt[3],
                dt[4],
                dt[5],
                dt[6],
                dt[7],
                dt[10],
                dt[8],
                f"{dt[9]:,}",
                f"{dt[11]:,}"
            ]
            total_summa += dt[11]
            self.tableWidget.insertRow(i)
            InsertItemToTable(self.tableWidget, i, lists)
            i += 1
        self.label_7.setText(f"{total_summa:,} Сўм")
        self.total_summa = total_summa
        if self.savdo_id is not None:
            cur.execute("""update savdo set summa=? where id=?""",(self.total_summa, self.savdo_id))
            conn.commit()


    def deleteProductFromBasket(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            id = self.tableWidget.item(row, 0).text()
            cur.execute("""delete from basket where id=?""",(id))
            conn.commit()
            self.basketList()

    def closeAddBasketWindow(self, refresh):
        if refresh:
            self.search_product_frame.hide()
            self.lineEdit.setText("")
            self.lineEdit.setFocus()
            self.basketList()

    def openAddBasketWindow(self, id):
        window = basket_components.AddBasketWindow(id, parent=self)
        window.closeapp.connect(self.closeAddBasketWindow)
        window.exec()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            if self.main_stack.currentWidget() == self.page_savdo:
                self.lineEdit.setFocus()
                self.search_product_frame.hide()
        if event.key() == QtCore.Qt.Key.Key_Down:
            if self.main_stack.currentWidget() == self.page_savdo  and  self.search_product_frame.isVisible() and self.lineEdit.hasFocus():
                self.search_product_frame.table_search.selectRow(0)
                self.search_product_frame.table_search.setFocus()
        
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            if self.search_product_frame.isVisible() and self.search_product_frame.table_search.hasFocus():
                r = self.search_product_frame.table_search.currentRow()
                id = self.search_product_frame.table_search.item(r, 0).text()
                self.openAddBasketWindow(id)
        if event.key() == QtCore.Qt.Key.Key_Delete:
            if self.tableWidget.hasFocus() and self.main_stack.currentWidget() == self.page_savdo:
                self.deleteProductFromBasket()
        
        if event.key() ==  QtCore.Qt.Key.Key_F2:
            if self.main_stack.currentWidget() == self.page_savdo and self.btn_save.isVisible():
                self.saveSavdo()
        
        if event.key() ==  QtCore.Qt.Key.Key_F6:
            if self.main_stack.currentWidget() == self.page_savdo and self.btn_clear.isVisible() and self.tableWidget.rowCount() > 0:
                self.clearBasket()
        
        if event.key() ==  QtCore.Qt.Key.Key_F5:
            if self.main_stack.currentWidget() == self.page_savdo and self.btn_new.isVisible():
                self.newSavdo()
        
        if event.key() ==  QtCore.Qt.Key.Key_F4:
            if self.main_stack.currentWidget() == self.page_savdo and self.btn_edit.isVisible():
                self.clickEditButton()


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
        self.label_23.setText(f"{row[3]:,} Сўм" )
        self.label_22.setText(str(row[4]))
        self.label_20.setText(f"{row[1]:,} Сўм")
        self.label_21.setText(str(row[2]))
        self.label_5.setText(f"{row[1]:,} Сўм")

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
        self.btn_savdolar.clicked.connect(self.clickbtn_savdolar)
        self.btn_dollor.clicked.connect(lambda: self.main_stack.setCurrentWidget(self.page_dollor))
    
    def clickbtn_savdolar(self):
        self.listSavdolar()
        self.main_stack.setCurrentWidget(self.page_savdolar)

    
    def tableWidgetSettings(self):
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setVisible(True)

        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget_2.setColumnWidth(1,50)
        self.tableWidget_3.setColumnWidth(1,50)
        self.tableWidget_4.setColumnWidth(2,50)

        TableStretchAndHide(self.tableWidget, lists_column=[3,6],sizeContent=[4,5,7,8,9,10, 11], hide_column=[0,1])
        TableStretchAndHide(self.tableWidget_2, lists_column=[2,3],hide_column=[0])
        TableStretchAndHide(self.tableWidget_3, lists_column=[2, 5],hide_column=[0], sizeContent=[6,7,8])
        TableStretchAndHide(self.tableWidget_4, lists_column=[3],hide_column=[0,1])


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
    