##
#  @file main.py
#  @package main
#  @brief Main file for the project

import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QFontDatabase, QRegularExpressionValidator

from middleware import prepare_expression
from mathlib import evaluate

from ui.calc import Ui_MainWindow

## Main Window class
# Importing the UI file from calc.py

##
# @brief Main Window class, importing the UI file from calc.py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ##
    # @brief todo
    # @param self todo
    # @param *args todo
    # @param obj todo
    # @param **kwargs todo
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("ui/fonts/OpenSans.ttf")
        self.lineEdit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9+-.*/!()^%]*")))

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
        self.but_pow.clicked.connect(lambda: self.add_symbol("^"))
        self.but_fact.clicked.connect(lambda: self.add_symbol("!"))
        self.but_bracket_open.clicked.connect(lambda: self.add_symbol("("))
        self.but_bracket_close.clicked.connect(lambda: self.add_symbol(")"))
        self.but_modulo.clicked.connect(lambda: self.add_symbol("%"))

        self.but_sqrt.clicked.connect(self.add_root)

        self.but_c.clicked.connect(self.clear)
        self.but_bs.clicked.connect(self.backspace)

        self.but_equals.clicked.connect(self.calculate)

    ##
    # @brief todo
    # @param self todo
    # @param symbol todo
    def add_symbol(self, symbol):
        self.lineEdit.setText(self.lineEdit.text() + symbol)

    ##
    # @brief todo
    # @param self todo
    def clear(self):
        self.lineEdit.setText("")
    
    ##
    # @brief todo
    # @param self todo
    def backspace(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    ##
    # @brief todo
    # @param self todo
    def add_root(self):
        self.lineEdit.setText(self.lineEdit.text() + "^(1/")

    ##
    # @brief todo
    # @param self todo
    def calculate(self):
        try:
            cur_expr = evaluate(prepare_expression(self.lineEdit.text()))
        except ZeroDivisionError:
            errordialog = QtWidgets.QErrorMessage(self)
            errordialog.showMessage("Dividing by zero is forbidden")
        except Exception as e:
            errordialog = QtWidgets.QErrorMessage(self)
            errordialog.showMessage(str(e))
        else:
            if (int(cur_expr) == cur_expr):
                self.lineEdit.setText(str(int(cur_expr)))
            else:
                self.lineEdit.setText(str(cur_expr))
            self.lineEdit.setCursorPosition(0)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
