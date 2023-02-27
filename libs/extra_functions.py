from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRectF, QPoint
from PyQt5.QtGui import QPainter, QFont, QFontMetrics, QColor
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QLabel


def ClearTableWidget(table):
    while (table.rowCount() > 0):
        table.removeRow(0)


def table_row_index(table):
    rows = table.rowCount()
    for i in range(rows):
        item = QTableWidgetItem(str(i + 1))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        table.setItem(i, 1, item)


def TableStretchAndHide(table, lists_column=None, all=False, sizeContent=None, hide_column=None):
    header = table.horizontalHeader()
    if all:
        for h in range(header.count()):
            header.setSectionResizeMode(h, QHeaderView.Stretch)
    elif lists_column is not None:
        for h in lists_column:
            header.setSectionResizeMode(h, QHeaderView.Stretch)
    if hide_column is not None:
        for hd in hide_column:
            table.hideColumn(hd)
    if sizeContent is not None:
        for h in sizeContent:
            header.setSectionResizeMode(h, QHeaderView.ResizeToContents)


def InsertItemToTable(table, row, lists, list_widget=[], colors=[]):
    i = 0
    for list in lists:
        if i in list_widget:
            table.setCellWidget(row, i, list)
        else:
            if list is None:
                list = ""
            item = QtWidgets.QTableWidgetItem(str(list))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            for cl in colors:
                if i == cl['i']:
                    if cl['bg'] != None:
                        item.setBackground(QColor(cl['bg']))
                    if cl['color'] != None:
                        item.setForeground(QColor(cl['color']))
            table.setItem(row, i, item)
        i += 1


MENU_SELECTED_STYLESHEET = """QPushButton{
    background-color:#006CFE;
	color:#FFF;
}"""
