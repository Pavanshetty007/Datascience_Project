# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QMovie

class Ui_Details(object):
    Registered=0
    Name='SampleName'
    Age=10
    Number=123456789
    Mail='SampleName@gmail.com'
    def setupUi(self, Details):
        Details.setObjectName("Details")
        Details.resize(580, 640)
        Details.setFixedSize(QtCore.QSize(580,640))
        self.label = QtWidgets.QLabel(Details)
        self.label.setGeometry(QtCore.QRect(0, 0, 580, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap())
        self.gif1=QMovie("Gui-Images/Bodyscan.gif")
        self.label.setMovie(self.gif1)
        self.gif1.start()
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Details)
        self.frame.setGeometry(QtCore.QRect(90, 130, 401, 441))
        self.frame.setStyleSheet("background-color: rgba(170, 170, 127, 150);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 145, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(100, 220, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 300, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 141, 131, 21))
        self.lineEdit.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 60);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 180, 131, 21))
        self.lineEdit_2.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 260, 181, 21))
        self.lineEdit_3.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 300, 181, 21))
        self.lineEdit_4.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 220, 131, 21))
        self.lineEdit_5.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 380, 93, 28))
        self.pushButton.clicked.connect(self.submit)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Details)
        QtCore.QMetaObject.connectSlotsByName(Details)

    def submit(self):
        name=self.lineEdit.text()
        age=self.lineEdit_2.text()
        phone=self.lineEdit_5.text()
        email1=self.lineEdit_4.text()
        email2=self.lineEdit_3.text()
        print(name,age,phone,email1,email2)
        if len(name)<1:
            QMessageBox.information(None,'Warning!!','Name not entered, Enter Name')
        elif (len(age)<1):
            QMessageBox.information(None,'Warning!!','Age not entered, Enter Age')
        elif (len(phone)<1):
            QMessageBox.information(None,'Warning!!','Phone Number not entered, Enter Phone Number')
        elif (len(email1)<1 or len(email2)<1):
            QMessageBox.information(None,'Warning!!','Email ID not entered, Enter Email ID')
        elif not(email1 == email2):
            QMessageBox.information(None,'Warning!!','Email IDs not matching, Enter Correct EmailID')
        else:
            QMessageBox.information(None,'Successfull','All Details Entered..!!')
            Ui_Details.Name=name
            Ui_Details.Age=age
            Ui_Details.Number=phone
            Ui_Details.Mail=email1
            Ui_Details.Registered=1
    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Register Patient"))
        self.label_2.setText(_translate("Details", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#005500;\">Patient Details</span></p></body></html>"))
        self.label_3.setText(_translate("Details", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Name:</span></p></body></html>"))
        self.label_4.setText(_translate("Details", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Age:</span></p></body></html>"))
        self.label_5.setText(_translate("Details", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Ph.No:</span></p></body></html>"))
        self.label_6.setText(_translate("Details", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Email-ID:</span></p></body></html>"))
        self.label_7.setText(_translate("Details", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Email-ID:</span></p></body></html>"))
        self.pushButton.setText(_translate("Details", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Details = QtWidgets.QWidget()
    ui = Ui_Details()
    ui.setupUi(Details)
    Details.show()
    sys.exit(app.exec_())

