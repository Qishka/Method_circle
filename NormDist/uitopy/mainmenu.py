# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir,QStringListModel
from uitopy.radius import Ui_Form
import sys

g_radius = 0
g_c = []
g_z = []
g_x = []
g_y = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 593)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Download/1eadf4027937d699a83ac0905d82204a-3745024997.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(770, 10, 291, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(900, 70, 161, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(668, 10, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 671, 351))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuChange = QtWidgets.QMenu(self.menubar)
        self.menuChange.setObjectName("menuChange")
        self.menuMethod = QtWidgets.QMenu(self.menubar)
        self.menuMethod.setObjectName("menuMethod")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Open.triggered.connect(self.getfiles)
        self.actionRadius = QtWidgets.QAction(MainWindow)
        self.actionRadius.setObjectName("actionRadius")
        self.rad_window = Rad()
        self.actionRadius.triggered.connect(self.rad_window.show)
        self.actionOther = QtWidgets.QAction(MainWindow)
        self.actionOther.setObjectName("actionOther")
        self.actionChoose_method = QtWidgets.QAction(MainWindow)
        self.actionChoose_method.setObjectName("actionChoose_method")
        self.menu_File.addAction(self.action_Open)
        self.menuChange.addAction(self.actionRadius)
        self.menuChange.addAction(self.actionOther)
        self.menuMethod.addAction(self.actionChoose_method)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuChange.menuAction())
        self.menubar.addAction(self.menuMethod.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Методы круглость"))
        self.label.setText(_translate("MainWindow", "Радиус"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_4.setText(_translate("MainWindow", "Максимум"))
        self.label_5.setText(_translate("MainWindow", "Минимум"))
        self.label_6.setText(_translate("MainWindow", "Отклонение"))
        self.label_7.setText(_translate("MainWindow", "Метод"))
        self.pushButton.setText(_translate("MainWindow", "Показать график"))
        self.pushButton.clicked.connect(ShowGraphic)
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuChange.setTitle(_translate("MainWindow", "Edit"))
        self.menuMethod.setTitle(_translate("MainWindow", "Method"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.actionRadius.setText(_translate("MainWindow", "Radius"))
        self.actionOther.setText(_translate("MainWindow", "Other"))
        self.actionChoose_method.setText(_translate("MainWindow", "Method type"))
    #FileDialog    
    def getfiles(self):
      dlg = QtWidgets.QFileDialog()
      dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
      dlg.setFilter(QDir.Files)
      filenames = QtCore.QStringListModel()
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            data = f.read()
            print(data)

def ShowGraphic():
    print("GraphicShow")

class Rad(QtWidgets.QMainWindow):
    def __init__(self):
        super(Rad,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.close())

        
    