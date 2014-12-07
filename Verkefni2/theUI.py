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
        self.ui.Gen_rating_btn.clicked.connect(self.Gen_rating_btn_Clicked)
        self.ui.Gen_ran_btn.clicked.connect(self.Gen_ran_btn_Clicked)
        self.ui.Gen_Random_Movie_btn.clicked.connect(self.Gen_Random_Movie_btn_Clicked)
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

    def Gen_rating_btn_Clicked(self):
        UserID = self.ui.User_Line.text()
        Movie = self.ui.Movie_line.text()
        self.ui.textBrowser.append("Looks like "+UserID+" Will rate "+Movie+"10/10 !")
    def Gen_ran_btn_Clicked(self):
        self.ui.User_Line.setText('Arnar Ingi')
        self.ui.Movie_line.setText('Backdoor sluts 9 ')

    def Gen_Random_Movie_btn_Clicked(self):
        print('He')

    #def loadCatagories(self,listOfCatagories):