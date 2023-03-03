import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My PyQt5 App')
        self.setGeometry(100, 100, 300, 200)
        self.button = QPushButton('Click me!', self)
        self.button.setGeometry(100, 70, 100, 30)
        self.button.clicked.connect(self.show_message)
        self.show()

    def closeEvent(self, event):
        os.system('C:\Windows\System32/rundll32 user32.dll, LockWorkStation')
        
    def show_message(self):
        message = QMessageBox()
        message.setWindowTitle('Message')
        message.setText('You clicked the button!')
        message.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
