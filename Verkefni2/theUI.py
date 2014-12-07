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
        genre1 = str(self.ui.Genre_1_dropdown.currentText())
        genre2 = str(self.ui.Genre_2_dropdown.currentText())
        genre3 = str(self.ui.Genre_3_dropdown.currentText())
        toplist = str(self.ui.Top_x_dropdown.currentText())

        num = 3
        genre1p = True
        genre2p = True
        genre3p = True
        genrenum = 1

        if genre1 == 'Pick a genre':
           num -= 1
           genre1p = False
        if genre2 == 'Pick a genre':
            num -= 1
            genre2p = False
        if genre3 == 'Pick a genre':
            num -= 1
            genre3p = False

        if num >= 1:
            self.ui.textBrowser.append('You picked '+ str(num) +' genres:')
        for i in range(0,3):
            if eval('genre'+str(i+1)+'p'):

                self.ui.textBrowser.append('Genre '+str(genrenum)+': '+eval('genre'+str((i+1))))
                genrenum +=1
        self.mydb.getTables()
        if num == 0:
            self.ui.textBrowser.append("Here's your general "+toplist+" list:")
        if num >= 1:
            self.ui.textBrowser.append("\nHere's your "+toplist+" list:")

    #def loadCatagories(self,listOfCatagories):