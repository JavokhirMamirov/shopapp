from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QRegion
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem,QWidget
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PyQt5 import QtWidgets
class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Name', 'Age', 'Gender'])
        self.setRowCount(5)
        self.setVerticalHeaderLabels(['Row {}'.format(i) for i in range(1, 6)])
        for i in range(5):
            self.setItem(i, 0, QTableWidgetItem('Person {}'.format(i+1)))
            self.setItem(i, 1, QTableWidgetItem(str(20+i)))
            self.setItem(i, 2, QTableWidgetItem('Male' if i%2==0 else 'Female'))
        
        self.printPreview()

    def printPreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer)
        previewDialog.paintRequested.connect(self.printTable)
        previewDialog.exec_()

    def printTable(self, printer):
        painter = QPainter(printer)
        painter.setRenderHint(QPainter.Antialiasing)
        tableHeight = self.rowHeight(0) * self.rowCount() + self.horizontalHeader().height()
        tableWidth = self.columnWidth(0) * self.columnCount() + self.verticalHeader().width()
        scale = printer.pageRect().width() / tableWidth
        painter.scale(scale, scale)
        self.render(painter, QPoint(0,0), QRegion(), QWidget.DrawChildren)
        painter.end()


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyTable()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())