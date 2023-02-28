from PyQt5.QtWidgets import QDialog, QMessageBox
from ux import post_print,add_client_ux
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from libs.extra_functions import PrintChek
from PyQt5 import QtPrintSupport

class PostPrinttWindow(QDialog, post_print.Ui_Dialog):
    closeapp = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(PostPrinttWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.printPos)
        self.setTaxt()
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or QtCore.Qt.Key.Key_Return == event.key():
            self.printPos()
        
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()
       
    def setTaxt(self):
        self.parent.cur.execute("""select * from savdo where id = ?""", (self.parent.savdo_id,))
        savdo = self.parent.cur.fetchone()
        self.parent.cur.execute("""select * from basket where savdo_id = ?""", (self.parent.savdo_id,) )
        baskets = self.parent.cur.fetchall()
        text = f"<h2 style='text-align:center;'>106</h2><p>Чек №: {savdo[0]}</p>"\
            f"<p>Мижоз: {savdo[2]}</p><p>Сана: {savdo[4]}</p><p>Умуми сумма: {savdo[3]:,}</p>"\
        
        self.textEdit.setHtml(text)
        
    def printPos(self):
        # text = self.textEdit.toPlainText()
        # PrintChek(text)
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.ScreenResolution)
        self.textEdit.setContentsMargins(0,0,0,0)
        self.textEdit.print_(printer)
        printer.setPageMargins(0.0, 0.0, 0.0, 0.0, QtPrintSupport.QPrinter.Point)
        printer.setFullPage(True)
        self.closeapp.emit(True)