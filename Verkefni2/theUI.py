from PyQt4 import QtGui
from ui.window import Ui_MainWindow
import sys
from google import search
import webbrowser

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
        #self.ui.genTop10.clicked.connect(self.genTop10_Clicked)
        self.ui.genTop10.clicked.connect(self.genTopX_Clicked)
        self.ui.Gen_rating_btn.clicked.connect(self.Gen_rating_btn_Clicked)
        self.ui.Gen_ran_btn.clicked.connect(self.Gen_ran_btn_Clicked)
        self.ui.Gen_Random_Movie_btn.clicked.connect(self.Gen_Random_Movie_btn_Clicked)
        self.mydb = mydb


        catagories = ["Pick a genre", "Action", "Adventure",    "Animation",    "Children",   "Comedy",   "Crime",    "Documentary",  "Drama",    "Fantasy",  "Film-Noir",    "Horror",   "Musical",  "Mystery",  "Romance",  "Sci-Fi",   "Thriller", "War",  "Western"]
        self.dropdowns = [self.ui.Genre_1_dropdown,self.ui.Genre_2_dropdown,self.ui.Genre_3_dropdown]

        for dropdown in self.dropdowns:
            for catagorie in catagories:
                dropdown.addItem(catagorie)


    def genTopX_Clicked(self):
        print('button clicked')
        toplist = str(self.ui.Top_x_dropdown.currentText())
        num = toplist.split()[1]
        genres = []
        for dropdown in self.dropdowns:
            genres.append(dropdown.currentText())
        genres = [item for item in genres if item != "Pick a genre"]
        print('genres:',genres)

        topX = self.mydb.getTopX(genres,num)




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
        self.mydb.getRandomMovie()
        if num == 0:
            self.ui.textBrowser.append("Here's your general "+toplist+" list:")
        if num >= 1:
            self.ui.textBrowser.append("\nHere's your "+toplist+" list:")

        # self.mydb.cursor.execute("SELECT * FROM ratings")
        # count = 0
        # while True:
        #     row = self.mydb.cursor.fetchone()
            
        #     if row == None or count == 10:
        #         break
        #     print(row)
        #     count += 1

    def Gen_rating_btn_Clicked(self):
        UserID = self.ui.User_Line.text()
        Movie = self.ui.Movie_line.text()
        self.ui.textBrowser.append("Looks like "+UserID+" Will rate "+Movie+"10/10 !")
    def Gen_ran_btn_Clicked(self):
        self.ui.User_Line.setText('Arnar Ingi')
        self.ui.Movie_line.setText('Backdoor sluts 9 ')

    def Gen_Random_Movie_btn_Clicked(self):
        genre1 = str(self.ui.Genre_1_dropdown_2.currentText())
        genre2 = str(self.ui.Genre_2_dropdown_2.currentText())
        genre3 = str(self.ui.Genre_3_dropdown_2.currentText())
        genre4 = self.ui.User_Line_2.text()
        print(genre4)
        print(genre1)
        print(genre2)
        print(genre3)

        RandMovie = self.mydb.getRandomMovie(genre1, genre2, genre3, genre4)
        if RandMovie == 'Nope':
            self.ui.textBrowser.append("Try Again Bitch")
        else:
            self.ui.textBrowser.append('The random movie is: ' + RandMovie)
            UrlList = []
            youtubeList = []
            for url in search(RandMovie, stop = 5):
                UrlList.append(url)
            imdbList = [s for s in UrlList if 'imdb' in s]
            youtubeList = [s for s in UrlList if 'youtube' in s]

            if not imdbList:
                self.ui.textBrowser.append('No imdb link was found for %s' % RandMovie)
            else:
                self.ui.textBrowser.append('Imdb link for %s is %s ' %(RandMovie,imdbList[0]))
                webbrowser.open(imdbList[0])

            if not youtubeList:
                self.ui.textBrowser.append('No youtube link was found for %s' % RandMovie)
            else:
                self.ui.textBrowser.append('Youtube link for %s is %s' %(RandMovie, youtubeList[0]))



    #def loadCatagories(self,listOfCatagories):