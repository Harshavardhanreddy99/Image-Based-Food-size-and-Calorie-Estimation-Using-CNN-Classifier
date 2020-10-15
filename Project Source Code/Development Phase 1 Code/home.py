# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Food2019\home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from adminloginaction import AdminLoginCheck
from userloginaction import UserLoginCheck
from adminhome import AdminHome
# from userhome import UserHome
from registeraction import RegisterAction
import re
import sys


class Home(object):

    def ulogindef(self):
        try:
            uidvar = self.uid.text()
            pwdvar = self.upwd.text()
            self.uid.setText("")
            self.upwd.setText("")
            al = UserLoginCheck()
            res = al.datacheck(uidvar, pwdvar)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif UserLoginCheck.logincheck(uidvar, pwdvar):
                self.showAlertBox2("Success", "Login Success")


            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def signupdef(self):
        EMAIL_REGEX = "^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$"
        try:
            print("signup")
            namevar = self.sname.text()
            emailvar = self.semail.text()
            contactvar = self.sph.text()
            cityvar = self.saddr.text()
            pwdvar = self.spwd.text()

            al = RegisterAction()
            if namevar == "" or namevar == "null" or emailvar == "" or emailvar == "null" or pwdvar == "" or pwdvar == "null" or contactvar == "" or contactvar == "null":
                self.showAlertBox("Information", "Please fill out all fields")
            elif not self.is_email_valid(emailvar):
                self.showAlertBox("Information", "Invalid Email id")
            elif len(contactvar) != 10:
                self.showAlertBox("Information", "Invalid mobile number")

            elif al.datacheck(namevar, emailvar, contactvar, cityvar, pwdvar):
                self.showAlertBox("Alert", "Fill the Fields")

            elif RegisterAction.signup(namevar, emailvar, contactvar, cityvar, pwdvar):
                self.sname.setText("")
                self.semail.setText("")
                self.sph.setText("")
                self.saddr.setText("")
                self.spwd.setText("")

                self.showAlertBox2("Information", "Register Success")

            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def adminlogin(self):
        try:
            print("adminlogin")
            auidvar = self.auid.text()
            apwdvar = self.apwd.text()
            self.auid.setText("")
            self.apwd.setText("")
            al = AdminLoginCheck()
            res = al.datacheck(auidvar, apwdvar)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif AdminLoginCheck.logincheck(auidvar, apwdvar):
                self.u = QtWidgets.QDialog()
                self.ui = AdminHome()
                self.ui.setupUi(self.u)
                self.u.show()


            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    #
    ##Alert Winwow
    #

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def showAlertBox2(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def is_email_valid(self, str):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return bool(re.match(email_regex, str))



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(804, 554)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame.setStyleSheet("background-image: url(calorie.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame_2.setStyleSheet("background-image: url(caloriep.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(230, 220, 380, 280))
        self.frame_3.setStyleSheet("background-image: url(wbg.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(120, -10, 150, 50))
        self.label.setStyleSheet("font: 14pt \"Verdana\";")
        self.label.setObjectName("label")
        self.auid = QtWidgets.QLineEdit(self.frame_3)
        self.auid.setGeometry(QtCore.QRect(40, 70, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.auid.setFont(font)
        self.auid.setStyleSheet("")
        self.auid.setText("")
        self.auid.setObjectName("auid")
        self.alogin = QtWidgets.QPushButton(self.frame_3)
        self.alogin.setGeometry(QtCore.QRect(40, 170, 90, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.alogin.setFont(font)
        self.alogin.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 208, 131);")
        self.alogin.setObjectName("alogin")

        self.alogin.clicked.connect(self.adminlogin)

        self.apwd = QtWidgets.QLineEdit(self.frame_3)
        self.apwd.setGeometry(QtCore.QRect(40, 120, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.apwd.setFont(font)
        self.apwd.setStyleSheet("")
        self.apwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apwd.setObjectName("apwd")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame_4.setStyleSheet("background-image: url(caloriep.jpg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(230, 220, 380, 280))
        self.frame_5.setStyleSheet("background-image: url(wbg.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(130, -10, 150, 50))
        self.label_2.setStyleSheet("font: 14pt \"Verdana\";")
        self.label_2.setObjectName("label_2")
        self.uid = QtWidgets.QLineEdit(self.frame_5)
        self.uid.setGeometry(QtCore.QRect(40, 70, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.uid.setFont(font)
        self.uid.setStyleSheet("")
        self.uid.setText("")
        self.uid.setObjectName("uid")
        self.ulogin = QtWidgets.QPushButton(self.frame_5)
        self.ulogin.setGeometry(QtCore.QRect(40, 170, 90, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ulogin.setFont(font)
        self.ulogin.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 208, 131);")
        self.ulogin.setObjectName("ulogin")

        self.ulogin.clicked.connect(self.ulogindef)

        self.upwd = QtWidgets.QLineEdit(self.frame_5)
        self.upwd.setGeometry(QtCore.QRect(40, 120, 310, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.upwd.setFont(font)
        self.upwd.setStyleSheet("")
        self.upwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.upwd.setObjectName("upwd")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame_6 = QtWidgets.QFrame(self.tab_4)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 941, 541))
        self.frame_6.setStyleSheet("background-image: url(caloriep.jpg);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(230, 220, 380, 280))
        self.frame_7.setStyleSheet("background-image: url(wbg.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(130, -10, 150, 50))
        self.label_3.setStyleSheet("font: 14pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.sname = QtWidgets.QLineEdit(self.frame_7)
        self.sname.setGeometry(QtCore.QRect(40, 40, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sname.setFont(font)
        self.sname.setStyleSheet("")
        self.sname.setText("")
        self.sname.setObjectName("sname")
        self.signup = QtWidgets.QPushButton(self.frame_7)
        self.signup.setGeometry(QtCore.QRect(230, 240, 120, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.signup.setFont(font)
        self.signup.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 208, 131);")
        self.signup.setObjectName("signup")

        self.signup.clicked.connect(self.signupdef)

        self.semail = QtWidgets.QLineEdit(self.frame_7)
        self.semail.setGeometry(QtCore.QRect(40, 80, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.semail.setFont(font)
        self.semail.setStyleSheet("")
        self.semail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.semail.setObjectName("semail")
        self.sph = QtWidgets.QLineEdit(self.frame_7)
        self.sph.setGeometry(QtCore.QRect(40, 120, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.sph.setFont(font)
        self.sph.setStyleSheet("")
        self.sph.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.sph.setObjectName("sph")
        self.saddr = QtWidgets.QLineEdit(self.frame_7)
        self.saddr.setGeometry(QtCore.QRect(40, 160, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.saddr.setFont(font)
        self.saddr.setStyleSheet("")
        self.saddr.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.saddr.setObjectName("saddr")
        self.spwd = QtWidgets.QLineEdit(self.frame_7)
        self.spwd.setGeometry(QtCore.QRect(40, 200, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.spwd.setFont(font)
        self.spwd.setStyleSheet("")
        self.spwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.spwd.setObjectName("spwd")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "Admin Login"))
        self.auid.setToolTip(_translate("Dialog", "Enter UserId"))
        self.auid.setPlaceholderText(_translate("Dialog", "Enter Userid"))
        self.alogin.setText(_translate("Dialog", "Login"))
        self.apwd.setStatusTip(_translate("Dialog", "Enter Password"))
        self.apwd.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.apwd.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.apwd.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.apwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Admin"))
        self.label_2.setText(_translate("Dialog", "User Login"))
        self.uid.setToolTip(_translate("Dialog", "Enter UserId"))
        self.uid.setPlaceholderText(_translate("Dialog", "Enter Userid"))
        self.ulogin.setText(_translate("Dialog", "Login"))
        self.upwd.setStatusTip(_translate("Dialog", "Enter Password"))
        self.upwd.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.upwd.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.upwd.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.upwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "User"))
        self.label_3.setText(_translate("Dialog", "User Signup"))
        self.sname.setToolTip(_translate("Dialog", "Enter UserId"))
        self.sname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.signup.setText(_translate("Dialog", "Signup"))
        self.semail.setStatusTip(_translate("Dialog", "Enter Password"))
        self.semail.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.semail.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.semail.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.semail.setPlaceholderText(_translate("Dialog", "Enter Email"))
        self.sph.setStatusTip(_translate("Dialog", "Enter Password"))
        self.sph.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.sph.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.sph.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.sph.setPlaceholderText(_translate("Dialog", "Enter Contact No"))
        self.saddr.setStatusTip(_translate("Dialog", "Enter Password"))
        self.saddr.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.saddr.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.saddr.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.saddr.setPlaceholderText(_translate("Dialog", "Enter Address"))
        self.spwd.setStatusTip(_translate("Dialog", "Enter Password"))
        self.spwd.setWhatsThis(_translate("Dialog", "Enter Password"))
        self.spwd.setAccessibleName(_translate("Dialog", "Enter Password"))
        self.spwd.setAccessibleDescription(_translate("Dialog", "Enter Password"))
        self.spwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Signup"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

