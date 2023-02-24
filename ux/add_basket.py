# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\add_basket.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 517)
        Dialog.setMinimumSize(QtCore.QSize(400, 0))
        Dialog.setMaximumSize(QtCore.QSize(400, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/assets/product-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("#Dialog{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 28))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(0, 28))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_7.addWidget(self.lineEdit_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setMinimumSize(QtCore.QSize(0, 28))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_9.addWidget(self.lineEdit_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setMinimumSize(QtCore.QSize(0, 28))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_10.addWidget(self.lineEdit_10)
        self.verticalLayout_5.addLayout(self.verticalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMinimumSize(QtCore.QSize(0, 28))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 32))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setProperty("showGroupSeparator", True)
        self.doubleSpinBox.setMaximum(999999999.0)
        self.doubleSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMinimumSize(QtCore.QSize(0, 28))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(0, 32))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setStyleSheet("QDoubleSpinBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setProperty("showGroupSeparator", True)
        self.doubleSpinBox_2.setMaximum(999999999.0)
        self.doubleSpinBox_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setMinimumSize(QtCore.QSize(0, 28))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setEnabled(True)
        self.spinBox_3.setMinimumSize(QtCore.QSize(0, 36))
        self.spinBox_3.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid #333;\n"
"}\n"
"\n"
"QSpinBox:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(53, 132, 228);\n"
"}")
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setProperty("showGroupSeparator", True)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(99999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_4.addWidget(self.spinBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    padding:10px;\n"
"    color:#fff;\n"
"    background-color: rgb(224, 27, 36);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(246, 97, 81);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    padding:10px;\n"
"    color:#fff;\n"
"    background-color: rgb(53, 132, 228);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(98, 160, 234);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinBox_3, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.radioButton)
        Dialog.setTabOrder(self.radioButton, self.lineEdit_8)
        Dialog.setTabOrder(self.lineEdit_8, self.lineEdit_7)
        Dialog.setTabOrder(self.lineEdit_7, self.lineEdit_9)
        Dialog.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        Dialog.setTabOrder(self.lineEdit_10, self.doubleSpinBox)
        Dialog.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_2)
        Dialog.setTabOrder(self.doubleSpinBox_2, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_7)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Махсулот қўшиш"))
        self.label_8.setText(_translate("Dialog", "Махсулот номи"))
        self.lineEdit_8.setPlaceholderText(_translate("Dialog", "Махсулот номи"))
        self.label_7.setText(_translate("Dialog", "Бренди"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog", "Бренди"))
        self.label_9.setText(_translate("Dialog", "Модели"))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog", "Модели"))
        self.label_12.setText(_translate("Dialog", "Ишлаб чиқарувчи"))
        self.lineEdit_10.setPlaceholderText(_translate("Dialog", "Ишлаб чиқарувчи"))
        self.label_10.setText(_translate("Dialog", "Нархи комп $"))
        self.label_11.setText(_translate("Dialog", "Нархи дона $"))
        self.radioButton.setText(_translate("Dialog", "Дона"))
        self.radioButton.setShortcut(_translate("Dialog", "F3"))
        self.radioButton_2.setText(_translate("Dialog", "Комп"))
        self.radioButton_2.setShortcut(_translate("Dialog", "F2"))
        self.label_13.setText(_translate("Dialog", "Сони"))
        self.pushButton_6.setText(_translate("Dialog", "Бекор қилиш"))
        self.pushButton_6.setShortcut(_translate("Dialog", "Esc"))
        self.pushButton_7.setText(_translate("Dialog", "Қўшиш"))
        self.pushButton_7.setShortcut(_translate("Dialog", "Return, Enter"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
