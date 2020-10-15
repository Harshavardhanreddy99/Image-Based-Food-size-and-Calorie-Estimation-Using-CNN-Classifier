from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from DBConnection import DBConnection
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.title = "Calorie's Data"
        self.top = 200
        self.left = 200
        self.width = 440
        self.height = 400

        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
 
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
 
        self.creatingTables()
 
 
        self.show()
 
    def creatingTables(self):

        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select * from dataset ")
        rows = cursor.fetchall()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(rows)+1)
        self.tableWidget.setColumnCount(len(rows[0]))

        tot=len(rows)
        print(rows)


 
        self.tableWidget.setItem(0,0, QTableWidgetItem("Food Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Calorie per Gram"))
        
        
        for s in range(tot):
            print(rows[s][0])
            d=str(rows[s][1])
            self.tableWidget.setItem(s+1,0, QTableWidgetItem(rows[s][0]))
            self.tableWidget.setItem(s+1,1, QTableWidgetItem(d))
            

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
 
        
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
    
    def main(self):
        App = QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())



