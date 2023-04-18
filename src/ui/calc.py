# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from . import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/fx.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: \"Open Sans\";\n"
"    font-size: 22pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(63, 63, 63, 0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(31, 31, 31, 0.7);\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"background-image: url(:/icons/pics/wallpaper.jpg);\n"
"background-position: center;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(44)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font-size: 44pt;\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0.2);")
        self.lineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.but_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_2.sizePolicy().hasHeightForWidth())
        self.but_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_2.setFont(font)
        self.but_2.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_2.setObjectName("but_2")
        self.gridLayout.addWidget(self.but_2, 5, 2, 1, 1)
        self.but_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_5.sizePolicy().hasHeightForWidth())
        self.but_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_5.setFont(font)
        self.but_5.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_5.setObjectName("but_5")
        self.gridLayout.addWidget(self.but_5, 4, 2, 1, 1)
        self.but_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_0.sizePolicy().hasHeightForWidth())
        self.but_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_0.setFont(font)
        self.but_0.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_0.setObjectName("but_0")
        self.gridLayout.addWidget(self.but_0, 6, 2, 1, 1)
        self.but_mult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_mult.sizePolicy().hasHeightForWidth())
        self.but_mult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_mult.setFont(font)
        self.but_mult.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_mult.setObjectName("but_mult")
        self.gridLayout.addWidget(self.but_mult, 3, 4, 1, 1)
        self.but_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_minus.sizePolicy().hasHeightForWidth())
        self.but_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_minus.setFont(font)
        self.but_minus.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_minus.setObjectName("but_minus")
        self.gridLayout.addWidget(self.but_minus, 4, 4, 1, 1)
        self.but_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_4.sizePolicy().hasHeightForWidth())
        self.but_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_4.setFont(font)
        self.but_4.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_4.setObjectName("but_4")
        self.gridLayout.addWidget(self.but_4, 4, 1, 1, 1)
        self.but_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_point.sizePolicy().hasHeightForWidth())
        self.but_point.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_point.setFont(font)
        self.but_point.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_point.setObjectName("but_point")
        self.gridLayout.addWidget(self.but_point, 6, 3, 1, 1)
        self.but_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_9.sizePolicy().hasHeightForWidth())
        self.but_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_9.setFont(font)
        self.but_9.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_9.setObjectName("but_9")
        self.gridLayout.addWidget(self.but_9, 3, 3, 1, 1)
        self.but_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_3.sizePolicy().hasHeightForWidth())
        self.but_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_3.setFont(font)
        self.but_3.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_3.setObjectName("but_3")
        self.gridLayout.addWidget(self.but_3, 5, 3, 1, 1)
        self.but_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_7.sizePolicy().hasHeightForWidth())
        self.but_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_7.setFont(font)
        self.but_7.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_7.setObjectName("but_7")
        self.gridLayout.addWidget(self.but_7, 3, 1, 1, 1)
        self.but_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_1.sizePolicy().hasHeightForWidth())
        self.but_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_1.setFont(font)
        self.but_1.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_1.setObjectName("but_1")
        self.gridLayout.addWidget(self.but_1, 5, 1, 1, 1)
        self.but_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_6.sizePolicy().hasHeightForWidth())
        self.but_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_6.setFont(font)
        self.but_6.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_6.setObjectName("but_6")
        self.gridLayout.addWidget(self.but_6, 4, 3, 1, 1)
        self.but_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_8.sizePolicy().hasHeightForWidth())
        self.but_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_8.setFont(font)
        self.but_8.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_8.setObjectName("but_8")
        self.gridLayout.addWidget(self.but_8, 3, 2, 1, 1)
        self.but_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_plus.sizePolicy().hasHeightForWidth())
        self.but_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_plus.setFont(font)
        self.but_plus.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_plus.setObjectName("but_plus")
        self.gridLayout.addWidget(self.but_plus, 5, 4, 1, 1)
        self.but_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_div.sizePolicy().hasHeightForWidth())
        self.but_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_div.setFont(font)
        self.but_div.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_div.setObjectName("but_div")
        self.gridLayout.addWidget(self.but_div, 2, 4, 1, 1)
        self.but_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_equals.sizePolicy().hasHeightForWidth())
        self.but_equals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_equals.setFont(font)
        self.but_equals.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_equals.setObjectName("but_equals")
        self.gridLayout.addWidget(self.but_equals, 6, 4, 1, 1)
        self.but_fact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_fact.sizePolicy().hasHeightForWidth())
        self.but_fact.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_fact.setFont(font)
        self.but_fact.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_fact.setObjectName("but_fact")
        self.gridLayout.addWidget(self.but_fact, 6, 1, 1, 1)
        self.but_c = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_c.sizePolicy().hasHeightForWidth())
        self.but_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_c.setFont(font)
        self.but_c.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_c.setObjectName("but_c")
        self.gridLayout.addWidget(self.but_c, 1, 3, 1, 1)
        self.but_bs = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_bs.sizePolicy().hasHeightForWidth())
        self.but_bs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_bs.setFont(font)
        self.but_bs.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_bs.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pics/backspace.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.but_bs.setIcon(icon1)
        self.but_bs.setIconSize(QtCore.QSize(38, 38))
        self.but_bs.setObjectName("but_bs")
        self.gridLayout.addWidget(self.but_bs, 1, 4, 1, 1)
        self.but_pow = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_pow.sizePolicy().hasHeightForWidth())
        self.but_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_pow.setFont(font)
        self.but_pow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_pow.setObjectName("but_pow")
        self.gridLayout.addWidget(self.but_pow, 1, 1, 1, 1)
        self.but_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_sqrt.sizePolicy().hasHeightForWidth())
        self.but_sqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_sqrt.setFont(font)
        self.but_sqrt.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_sqrt.setObjectName("but_sqrt")
        self.gridLayout.addWidget(self.but_sqrt, 1, 2, 1, 1)
        self.but_modulo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_modulo.sizePolicy().hasHeightForWidth())
        self.but_modulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_modulo.setFont(font)
        self.but_modulo.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_modulo.setObjectName("but_modulo")
        self.gridLayout.addWidget(self.but_modulo, 2, 3, 1, 1)
        self.but_bracket_open = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_bracket_open.sizePolicy().hasHeightForWidth())
        self.but_bracket_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_bracket_open.setFont(font)
        self.but_bracket_open.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_bracket_open.setObjectName("but_bracket_open")
        self.gridLayout.addWidget(self.but_bracket_open, 2, 1, 1, 1)
        self.but_bracket_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_bracket_close.sizePolicy().hasHeightForWidth())
        self.but_bracket_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        self.but_bracket_close.setFont(font)
        self.but_bracket_close.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.but_bracket_close.setObjectName("but_bracket_close")
        self.gridLayout.addWidget(self.but_bracket_close, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calcutega"))
        self.but_2.setText(_translate("MainWindow", "2"))
        self.but_2.setShortcut(_translate("MainWindow", "2"))
        self.but_5.setText(_translate("MainWindow", "5"))
        self.but_5.setShortcut(_translate("MainWindow", "5"))
        self.but_0.setText(_translate("MainWindow", "0"))
        self.but_0.setShortcut(_translate("MainWindow", "0"))
        self.but_mult.setText(_translate("MainWindow", "×"))
        self.but_mult.setShortcut(_translate("MainWindow", "*"))
        self.but_minus.setText(_translate("MainWindow", "-"))
        self.but_minus.setShortcut(_translate("MainWindow", "-"))
        self.but_4.setText(_translate("MainWindow", "4"))
        self.but_4.setShortcut(_translate("MainWindow", "4"))
        self.but_point.setText(_translate("MainWindow", "."))
        self.but_point.setShortcut(_translate("MainWindow", "."))
        self.but_9.setText(_translate("MainWindow", "9"))
        self.but_9.setShortcut(_translate("MainWindow", "9"))
        self.but_3.setText(_translate("MainWindow", "3"))
        self.but_3.setShortcut(_translate("MainWindow", "3"))
        self.but_7.setText(_translate("MainWindow", "7"))
        self.but_7.setShortcut(_translate("MainWindow", "7"))
        self.but_1.setText(_translate("MainWindow", "1"))
        self.but_1.setShortcut(_translate("MainWindow", "1"))
        self.but_6.setText(_translate("MainWindow", "6"))
        self.but_6.setShortcut(_translate("MainWindow", "6"))
        self.but_8.setText(_translate("MainWindow", "8"))
        self.but_8.setShortcut(_translate("MainWindow", "8"))
        self.but_plus.setText(_translate("MainWindow", "+"))
        self.but_plus.setShortcut(_translate("MainWindow", "+"))
        self.but_div.setText(_translate("MainWindow", "÷"))
        self.but_div.setShortcut(_translate("MainWindow", "/"))
        self.but_equals.setText(_translate("MainWindow", "="))
        self.but_equals.setShortcut(_translate("MainWindow", "Return"))
        self.but_fact.setText(_translate("MainWindow", "n!"))
        self.but_fact.setShortcut(_translate("MainWindow", "!"))
        self.but_c.setText(_translate("MainWindow", "C"))
        self.but_c.setShortcut(_translate("MainWindow", "Del"))
        self.but_bs.setShortcut(_translate("MainWindow", "Backspace"))
        self.but_pow.setText(_translate("MainWindow", "xⁿ"))
        self.but_pow.setShortcut(_translate("MainWindow", "^"))
        self.but_sqrt.setText(_translate("MainWindow", "ⁿ√x"))
        self.but_modulo.setText(_translate("MainWindow", "%"))
        self.but_modulo.setShortcut(_translate("MainWindow", "%"))
        self.but_bracket_open.setText(_translate("MainWindow", "("))
        self.but_bracket_open.setShortcut(_translate("MainWindow", "("))
        self.but_bracket_close.setText(_translate("MainWindow", ")"))
        self.but_bracket_close.setShortcut(_translate("MainWindow", ")"))
