# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Food2019\admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime, xlrd
from DBConnection import DBConnection
import sys
#from ViewData import ViewData


class AdminHome(object):
    def browsefile(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File","E:/", "*.xlsx")
            print(fileName)
            self.textbox.setText(fileName)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)


    def uploadAction(self):
        try:
            fname = self.textbox.text()
            book = xlrd.open_workbook(fname)
            book = xlrd.open_workbook(fname)
            sheet = book.sheet_by_index(0)
            database = DBConnection.getConnection()
            print(database)
            cursor = database.cursor()
            cursor2 = database.cursor()
            cursor.execute("delete from dataset")
            print("deleted")
            database.commit()
            query = "insert into dataset values(%s,%s)"
            print(query)
            for r in range(1, sheet.nrows):
                f0 = sheet.cell(r, 0).value
                f1 = float(sheet.cell(r, 1).value)
                values = (
                    f0, f1)
                print(values)
                try:
                    cursor.execute(query, values)
                except:
                    pass
                database.commit()
                columns = str(sheet.ncols)
                rows=str(sheet.nrows)
                print("inserted")
            self.showAlertBox("Information", "DataSet Loaded Successfully")
            self.auid_2.setText("")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def viewdef(self):
        try:
            import sys
            print("hh")
            
            import subprocess
            import sys

            # Some code here

            pid = subprocess.Popen([sys.executable, "table.py"])



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


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
        self.frame.setStyleSheet("background-image: url(calorie2.jpg);")
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
        self.label.setGeometry(QtCore.QRect(30, -10, 321, 50))
        self.label.setStyleSheet("font: 14pt \"Verdana\";")
        self.label.setObjectName("label")
        self.textbox = QtWidgets.QLineEdit(self.frame_3)
        self.textbox.setGeometry(QtCore.QRect(10, 60, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textbox.setFont(font)
        self.textbox.setStyleSheet("")
        self.textbox.setText("")
        self.textbox.setObjectName("textbox")
        self.upload = QtWidgets.QPushButton(self.frame_3)
        self.upload.setGeometry(QtCore.QRect(10, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.upload.setFont(font)
        self.upload.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 208, 131);")
        self.upload.setObjectName("upload")

        ##########################################
        self.upload.clicked.connect(self.uploadAction)
        ##########################################

        self.browse = QtWidgets.QPushButton(self.frame_3)
        self.browse.setGeometry(QtCore.QRect(330, 60, 30, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.browse.setFont(font)
        self.browse.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 208, 131);")
        self.browse.setObjectName("browse")

        ##########################################
        self.browse.clicked.connect(self.browsefile)
        ###########################################


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
        self.label_2.setGeometry(QtCore.QRect(60, -10, 241, 50))
        self.label_2.setStyleSheet("font: 14pt \"Verdana\";")
        self.label_2.setObjectName("label_2")
        self.View = QtWidgets.QPushButton(self.frame_5)
        self.View.setGeometry(QtCore.QRect(40, 100, 290, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.View.setFont(font)
        self.View.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 208, 131);")
        self.View.setObjectName("View")


        ##########################################
        self.View.clicked.connect(self.viewdef)
        ###########################################



        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Dataset Upload</p></body></html>"))
        self.textbox.setToolTip(_translate("Dialog", "Enter UserId"))
        self.textbox.setPlaceholderText(_translate("Dialog", "Dataset Upload"))
        self.upload.setText(_translate("Dialog", "Upload"))
        self.browse.setText(_translate("Dialog", "----"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Dataset Upload"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">View Dataset</p></body></html>"))
        self.View.setText(_translate("Dialog", "Click to View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "View"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

