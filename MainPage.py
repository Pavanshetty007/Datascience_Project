# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from RegisterPage import Ui_Details
from ReportMaking import Ui_Analyse


class Ui_Form(object):
    def setupUi(self, Form):
        self.run = QTimer()
        self.run.setInterval(200)
        self.run.timeout.connect(self.checkstatus)
        self.run.start()
        Form.setObjectName("Form")
        Form.resize(580, 640)
        Form.setFixedSize(QtCore.QSize(583,640))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 581, 641))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.mngif=QMovie("Gui-Images/Doctor.gif")
        self.label.setMovie(self.mngif)
        self.mngif.start()
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 451, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 60, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 600, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def register(self):
        print("Button pressed")
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Details()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()
        
    def checkstatus(self):
        if Ui_Details.Registered==1:
            self.window = QtWidgets.QWidget()
            print(Ui_Details.Name,Ui_Details.Age,Ui_Details.Number,Ui_Details.Mail)
            self.ui = Ui_Analyse(Ui_Details.Name,Ui_Details.Age,Ui_Details.Number,Ui_Details.Mail)
            self.ui.setupUi(self.window)
            self.window.show()
            Ui_Details.Registered=0
        if Ui_Analyse.home==1:
            self.window.close()
            Form.show()
            Ui_Analyse.home=0
            
    
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Auto Analyser"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#5353ff;\">Brain Tumor Classification</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#aa0000;\">Dr.B.B. Hegde First Grade College</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Get Started"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

