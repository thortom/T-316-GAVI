from PyQt4 import QtGui, QtCore
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
        cb = self.ui.checkBox
        cb.toggle()
        cb.stateChanged.connect(self.checkBox)
        self.DATRUTH = True

        catagories = ["Pick a genre", "Action", "Adventure",    "Animation",    "Children",   "Comedy",   "Crime",    "Documentary",  "Drama",    "Fantasy",  "Film-Noir",    "Horror",   "Musical",  "Mystery",  "Romance",  "Sci-Fi",   "Thriller", "War",  "Western"]
        self.dropdowns = [self.ui.Genre_1_dropdown,self.ui.Genre_2_dropdown,self.ui.Genre_3_dropdown]

        for dropdown in self.dropdowns:
            for catagorie in catagories:
                dropdown.addItem(catagorie)


    def checkBox(self,state):
        cb = self.checkBox
        if state == QtCore.Qt.Checked:
            self.DATRUTH = True
        else:
            self.DATRUTH = False

    def genTopX_Clicked(self):
        toplist = str(self.ui.Top_x_dropdown.currentText())
        num = toplist.split()[1]
        genres = []
        for dropdown in self.dropdowns:
            genres.append(dropdown.currentText())
        genres = [item for item in genres if item != "Pick a genre"]

        topX = self.mydb.getTopX(genres,num)
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append(topX)

    def genTop10_Clicked(self):
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


    def Gen_rating_btn_Clicked(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append("Generating the prediction will take some time....")
        print("Generating the prediction will take some time....")
        mainUserID = self.ui.User_Line.text()
        mainMovie = self.ui.Movie_line.text()
        try:
            mainUserID = int(mainUserID)
        except ValueError:
            self.ui.textBrowser.append("Error: The user needs to be inserted as an ID-number")
            return
        try:
            mainMovieID = int(mainMovie)
        except ValueError:
            s = "select movieid from movies where title=%s"
            self.mydb.cursor.execute(s, (mainMovie,))
            mainMovieID = self.mydb.cursor.fetchone()[0]
            if mainMovieID == None:
                self.ui.textBrowser.append("Error: The movie title was not found in library")
                return

        print('mainUserID', mainUserID)
        print('movieID', mainMovieID)

        # Selecting previously rated movies by the mainUserID
        self.mydb.cursor.execute("select movieid from ratings where userid = %s" %mainUserID)

        lines = self.mydb.cursor.fetchall()
        print('lines:', lines)
        print('len(lines)', len(lines))
        size = len(lines)

        mainUserMovies = '('
        margin = 0.5
        maxSize = 20
        count = 0
        for movieid in lines:
            print('movieid', movieid)
            if size < maxSize:
                mainUserMovies += "movieid='"+str(movieid[0])+"'" + " or "
            else:
                mainUserMovies += "movieid='"+str(movieid[0])+"'" + " or "
                # TODO:
                # mainUserMovies += "movieid='"+str(movieid[0])+"' and rating between ...." + " or "
            count += 1
        mainUserMovies = mainUserMovies[:-4] + ')'                                              # Cut of the last redundant " or " expression
        print('mainUserMovies', mainUserMovies)

        # mainUserMovies = '('
        # count = 0
        # while True:
        #     row = self.mydb.cursor.fetchone()
        #     if row == None:
        #         break
        #     mainUserMovies += "movieid='"+str(row[0])+"'" + " or "
        #     count += 1
        # mainUserMovies = mainUserMovies[:-4] + ')'                                              # Cut of the last redundant " or " expression
        # print('mainUserMovies', mainUserMovies)

        print("Starting the long query....")
        print("If the list here above is long then this will take a long time")
        print("A long list is more than 20 items this list is %s items long" %count)
        # Sort by.... TODO: say something clever
        s = '''select distinct ta.userid, count(ta.userid)
                from
                    (
                    select ratings.userid, ratings.movieid, ratings.rating
                        from ratings
                            inner join
                                (
                                    select userid from ratings
                                        where movieid=%s
                                ) as s
                                    on ratings.userid=s.userid
                    ) as ta
                where %s
               group by ta.userid
               order by count(ta.userid) desc''' %(mainMovieID, mainUserMovies)
        self.mydb.cursor.execute(s)
        firstRow = self.mydb.cursor.fetchone()
        maxCommonWatchedMovies = firstRow[1]
        print('maxCommonWatchedMovies', maxCommonWatchedMovies)
        commonUserIDString = "(userid='" + str(firstRow[0]) + "'" + " or "
        while True:
            row = self.mydb.cursor.fetchone()
            if row == None or maxCommonWatchedMovies != row[1]:
                break
            commonUserIDString += "userid='"+str(row[0])+"'" + " or "
        commonUserIDString = commonUserIDString[:-4] + ')'
        print('commonUserIDString', commonUserIDString)

        # Get the average for all users that have similar watching history
        s = "select rating from ratings where movieid=%s and %s" %(mainMovieID, commonUserIDString)
        self.mydb.cursor.execute(s)
        ratings = []
        while True:
            row = self.mydb.cursor.fetchone()
            if row == None:
                break
            ratings.append(float(row[0]))
        avgRating = sum(ratings)/len(ratings)

        self.ui.textBrowser.append('''Looks like user: %s \nWill give the movie with ID-number: %s \nThe rating: %s''' %(str(mainUserID), str(mainMovieID), str(0.5 * ceil(2.0 * avgRating))))

    def Gen_ran_btn_Clicked(self):
        userID, movieTitle = self.mydb.getRandomUserAndMovie()
        self.ui.User_Line.setText(str(userID))
        self.ui.Movie_line.setText(movieTitle)

    def Gen_Random_Movie_btn_Clicked(self):
        self.ui.textBrowser.clear()
        genre1 = str(self.ui.Genre_1_dropdown_2.currentText())
        genre2 = str(self.ui.Genre_2_dropdown_2.currentText())
        genre3 = str(self.ui.Genre_3_dropdown_2.currentText())
        genre4 = self.ui.User_Line_2.text()

        RandMovie = self.mydb.getRandomMovie(genre1, genre2, genre3, genre4)
        if RandMovie == 'Nope':
            self.ui.textBrowser.append("No movie was found: Try Again with diffrent values")
        else:
            self.ui.textBrowser.append('The random movie is: ' + RandMovie)
            UrlList = []
            for url in search(RandMovie, stop = 5):
                UrlList.append(url)
            imdbList = [s for s in UrlList if 'imdb' in s]

            if not imdbList:
                self.ui.textBrowser.append('No imdb link was found for %s' % RandMovie)
            else:
                self.ui.textBrowser.append('Imdb link for %s is %s ' %(RandMovie,imdbList[0]))
                if self.DATRUTH:
                    webbrowser.open(imdbList[0])



    #def loadCatagories(self,listOfCatagories):