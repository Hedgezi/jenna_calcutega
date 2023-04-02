import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QFontDatabase, QRegularExpressionValidator

from calc import Ui_MainWindow

## Main Window class
# Importing the UI file from calc.py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/OpenSans.ttf")
        self.lineEdit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9+-.*/!^]*")))

        # Connect buttons to text input
        self.but_0.clicked.connect(lambda: self.add_symbol("0"))
        self.but_1.clicked.connect(lambda: self.add_symbol("1"))
        self.but_2.clicked.connect(lambda: self.add_symbol("2"))
        self.but_3.clicked.connect(lambda: self.add_symbol("3"))
        self.but_4.clicked.connect(lambda: self.add_symbol("4"))
        self.but_5.clicked.connect(lambda: self.add_symbol("5"))
        self.but_6.clicked.connect(lambda: self.add_symbol("6"))
        self.but_7.clicked.connect(lambda: self.add_symbol("7"))
        self.but_8.clicked.connect(lambda: self.add_symbol("8"))
        self.but_9.clicked.connect(lambda: self.add_symbol("9"))
        self.but_point.clicked.connect(lambda: self.add_symbol("."))
        self.but_plus.clicked.connect(lambda: self.add_symbol("+"))
        self.but_minus.clicked.connect(lambda: self.add_symbol("-"))
        self.but_mult.clicked.connect(lambda: self.add_symbol("*")) # ×
        self.but_div.clicked.connect(lambda: self.add_symbol("/")) # ÷

        self.but_c.clicked.connect(self.clear)
        self.but_bs.clicked.connect(self.backspace)


    def add_symbol(self, symbol):
        self.lineEdit.setText(self.lineEdit.text() + symbol)

    def clear(self):
        self.lineEdit.setText("")
    
    def backspace(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
