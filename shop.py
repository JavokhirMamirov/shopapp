import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from ux import main_ux
from libs.extra_functions import MENU_SELECTED_STYLESHEET, InsertItemToTable, TableStretchAndHide
from components import add_client

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

    

    def openAddClientWindow(self):
        window = add_client.AddClientWindow()
        window.show()


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
        TableStretchAndHide(self.tableWidget_3, lists_column=[2],hide_column=[0])
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
    