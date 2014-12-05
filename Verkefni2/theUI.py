from PyQt4 import QtGui
from ui.window import Ui_MainWindow
import sys

def loadUI(mydb):
    app = QtGui.QApplication(sys.argv)  
    window = Main(mydb)
    window.show()
    sys.exit(app.exec_())
    return window

class Main(QtGui.QMainWindow):
    def __init__(self,mydb):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.genTop10.clicked.connect(self.genTop10_Clicked)
        self.mydb = mydb

    def genTop10_Clicked(self):
        print('button pushed')
        self.mydb.getTables()

    #def loadCatagories(self,listOfCatagories):