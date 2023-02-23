from PyQt5.QtWidgets import QFrame
from ux import search_frame
from libs.extra_functions import TableStretchAndHide, ClearTableWidget, InsertItemToTable
class SearchProduct(QFrame, search_frame.Ui_Frame):
    def __init__(self, obj):
        super(SearchProduct, self).__init__(obj)
        self.setupUi(self)
        self.parent = obj
        self.setParent(obj.page_savdo)
        TableStretchAndHide(self.table_search, lists_column=[1,4], hide_column=[0])
        self.hide()
        self.setGeometry(obj.lineEdit.x() + 20, obj.lineEdit.y() + 110, 800, 300)

    def search_product_handler(self, data):
        if len(data) > 0:
            table = self.table_search
            if not self.isVisible():
                self.show()
            ClearTableWidget(table)
            i = 0
            for dt in data:
                lists = [
                    dt[0],
                    dt[1],
                    dt[2],
                    dt[3],
                    dt[4],
                    f"${dt[5]} / ${dt[6]}"
                ]
                self.table_search.insertRow(i)
                InsertItemToTable(self.table_search, i, lists,)
                i += 1
            
        else:
            self.hide()