# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Thu Dec 11 13:16:03 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1146, 633)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(400, 30, 681, 541))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 40, 261, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Genre_2_dropdown = QtGui.QComboBox(self.gridLayoutWidget)
        self.Genre_2_dropdown.setObjectName(_fromUtf8("Genre_2_dropdown"))
        self.gridLayout.addWidget(self.Genre_2_dropdown, 4, 0, 1, 1)
        self.genTop10 = QtGui.QPushButton(self.gridLayoutWidget)
        self.genTop10.setObjectName(_fromUtf8("genTop10"))
        self.gridLayout.addWidget(self.genTop10, 7, 0, 1, 1)
        self.Top_x_dropdown = QtGui.QComboBox(self.gridLayoutWidget)
        self.Top_x_dropdown.setObjectName(_fromUtf8("Top_x_dropdown"))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.Top_x_dropdown.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Top_x_dropdown, 6, 0, 1, 1)
        self.Genre_1_dropdown = QtGui.QComboBox(self.gridLayoutWidget)
        self.Genre_1_dropdown.setObjectName(_fromUtf8("Genre_1_dropdown"))
        self.gridLayout.addWidget(self.Genre_1_dropdown, 3, 0, 1, 1)
        self.Genre_3_dropdown = QtGui.QComboBox(self.gridLayoutWidget)
        self.Genre_3_dropdown.setObjectName(_fromUtf8("Genre_3_dropdown"))
        self.gridLayout.addWidget(self.Genre_3_dropdown, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 380, 261, 171))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 5, 0, 1, 1)
        self.Genre_1_dropdown_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.Genre_1_dropdown_2.setObjectName(_fromUtf8("Genre_1_dropdown_2"))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_1_dropdown_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.Genre_1_dropdown_2, 1, 0, 1, 1)
        self.User_Line_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.User_Line_2.setObjectName(_fromUtf8("User_Line_2"))
        self.gridLayout_2.addWidget(self.User_Line_2, 4, 0, 1, 1)
        self.Gen_Random_Movie_btn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.Gen_Random_Movie_btn.setObjectName(_fromUtf8("Gen_Random_Movie_btn"))
        self.gridLayout_2.addWidget(self.Gen_Random_Movie_btn, 7, 0, 1, 1)
        self.Genre_2_dropdown_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.Genre_2_dropdown_2.setObjectName(_fromUtf8("Genre_2_dropdown_2"))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_2_dropdown_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.Genre_2_dropdown_2, 2, 0, 1, 1)
        self.Genre_3_dropdown_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.Genre_3_dropdown_2.setObjectName(_fromUtf8("Genre_3_dropdown_2"))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.Genre_3_dropdown_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.Genre_3_dropdown_2, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(70, 210, 261, 148))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Gen_ran_btn = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.Gen_ran_btn.setObjectName(_fromUtf8("Gen_ran_btn"))
        self.gridLayout_3.addWidget(self.Gen_ran_btn, 4, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.Movie_line = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.Movie_line.setObjectName(_fromUtf8("Movie_line"))
        self.gridLayout_3.addWidget(self.Movie_line, 2, 0, 1, 2)
        self.MovieID_checkbox = QtGui.QCheckBox(self.gridLayoutWidget_3)
        self.MovieID_checkbox.setChecked(True)
        self.MovieID_checkbox.setAutoExclusive(False)
        self.MovieID_checkbox.setObjectName(_fromUtf8("MovieID_checkbox"))
        self.gridLayout_3.addWidget(self.MovieID_checkbox, 3, 0, 1, 1)
        self.MovieTitle_checkbox = QtGui.QCheckBox(self.gridLayoutWidget_3)
        self.MovieTitle_checkbox.setObjectName(_fromUtf8("MovieTitle_checkbox"))
        self.gridLayout_3.addWidget(self.MovieTitle_checkbox, 3, 1, 1, 1)
        self.Gen_rating_btn = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.Gen_rating_btn.setObjectName(_fromUtf8("Gen_rating_btn"))
        self.gridLayout_3.addWidget(self.Gen_rating_btn, 5, 0, 1, 2)
        self.User_Line = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.User_Line.setObjectName(_fromUtf8("User_Line"))
        self.gridLayout_3.addWidget(self.User_Line, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.MovieID_checkbox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MovieTitle_checkbox.toggle)
        QtCore.QObject.connect(self.MovieTitle_checkbox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MovieID_checkbox.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie generator", None))
        self.genTop10.setText(_translate("MainWindow", "Generate list", None))
        self.Top_x_dropdown.setItemText(0, _translate("MainWindow", "Top 10", None))
        self.Top_x_dropdown.setItemText(1, _translate("MainWindow", "Top 20", None))
        self.Top_x_dropdown.setItemText(2, _translate("MainWindow", "Top 30", None))
        self.Top_x_dropdown.setItemText(3, _translate("MainWindow", "Top 50", None))
        self.Top_x_dropdown.setItemText(4, _translate("MainWindow", "Top 75", None))
        self.Top_x_dropdown.setItemText(5, _translate("MainWindow", "Top 100", None))
        self.Top_x_dropdown.setItemText(6, _translate("MainWindow", "Top 150", None))
        self.Top_x_dropdown.setItemText(7, _translate("MainWindow", "Top 200", None))
        self.Top_x_dropdown.setItemText(8, _translate("MainWindow", "Top 250", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">Top list generator</span></p></body></html>", None))
        self.checkBox.setText(_translate("MainWindow", "Want to open IMDB in browser?", None))
        self.Genre_1_dropdown_2.setItemText(0, _translate("MainWindow", "Pick a genre", None))
        self.Genre_1_dropdown_2.setItemText(1, _translate("MainWindow", "Action", None))
        self.Genre_1_dropdown_2.setItemText(2, _translate("MainWindow", "Adventure", None))
        self.Genre_1_dropdown_2.setItemText(3, _translate("MainWindow", "Animation", None))
        self.Genre_1_dropdown_2.setItemText(4, _translate("MainWindow", "Children", None))
        self.Genre_1_dropdown_2.setItemText(5, _translate("MainWindow", "Comedy", None))
        self.Genre_1_dropdown_2.setItemText(6, _translate("MainWindow", "Crime", None))
        self.Genre_1_dropdown_2.setItemText(7, _translate("MainWindow", "Documentary", None))
        self.Genre_1_dropdown_2.setItemText(8, _translate("MainWindow", "Drama", None))
        self.Genre_1_dropdown_2.setItemText(9, _translate("MainWindow", "Fantasy", None))
        self.Genre_1_dropdown_2.setItemText(10, _translate("MainWindow", "Film-Noir", None))
        self.Genre_1_dropdown_2.setItemText(11, _translate("MainWindow", "Horror", None))
        self.Genre_1_dropdown_2.setItemText(12, _translate("MainWindow", "Musical", None))
        self.Genre_1_dropdown_2.setItemText(13, _translate("MainWindow", "Mystery", None))
        self.Genre_1_dropdown_2.setItemText(14, _translate("MainWindow", "Romance", None))
        self.Genre_1_dropdown_2.setItemText(15, _translate("MainWindow", "Sci-Fi", None))
        self.Genre_1_dropdown_2.setItemText(16, _translate("MainWindow", "Thriller", None))
        self.Genre_1_dropdown_2.setItemText(17, _translate("MainWindow", "War", None))
        self.Genre_1_dropdown_2.setItemText(18, _translate("MainWindow", "Western", None))
        self.User_Line_2.setText(_translate("MainWindow", "Choose year (ex. >= 1990)", None))
        self.Gen_Random_Movie_btn.setText(_translate("MainWindow", "Generate Random Movie", None))
        self.Genre_2_dropdown_2.setItemText(0, _translate("MainWindow", "Pick a genre", None))
        self.Genre_2_dropdown_2.setItemText(1, _translate("MainWindow", "Action", None))
        self.Genre_2_dropdown_2.setItemText(2, _translate("MainWindow", "Adventure", None))
        self.Genre_2_dropdown_2.setItemText(3, _translate("MainWindow", "Animation", None))
        self.Genre_2_dropdown_2.setItemText(4, _translate("MainWindow", "Children", None))
        self.Genre_2_dropdown_2.setItemText(5, _translate("MainWindow", "Comedy", None))
        self.Genre_2_dropdown_2.setItemText(6, _translate("MainWindow", "Crime", None))
        self.Genre_2_dropdown_2.setItemText(7, _translate("MainWindow", "Documentary", None))
        self.Genre_2_dropdown_2.setItemText(8, _translate("MainWindow", "Drama", None))
        self.Genre_2_dropdown_2.setItemText(9, _translate("MainWindow", "Fantasy", None))
        self.Genre_2_dropdown_2.setItemText(10, _translate("MainWindow", "Film-Noir", None))
        self.Genre_2_dropdown_2.setItemText(11, _translate("MainWindow", "Horror", None))
        self.Genre_2_dropdown_2.setItemText(12, _translate("MainWindow", "Musical", None))
        self.Genre_2_dropdown_2.setItemText(13, _translate("MainWindow", "Mystery", None))
        self.Genre_2_dropdown_2.setItemText(14, _translate("MainWindow", "Romance", None))
        self.Genre_2_dropdown_2.setItemText(15, _translate("MainWindow", "Sci-Fi", None))
        self.Genre_2_dropdown_2.setItemText(16, _translate("MainWindow", "Thriller", None))
        self.Genre_2_dropdown_2.setItemText(17, _translate("MainWindow", "War", None))
        self.Genre_2_dropdown_2.setItemText(18, _translate("MainWindow", "Western", None))
        self.Genre_3_dropdown_2.setItemText(0, _translate("MainWindow", "Rating", None))
        self.Genre_3_dropdown_2.setItemText(1, _translate("MainWindow", "> 0", None))
        self.Genre_3_dropdown_2.setItemText(2, _translate("MainWindow", "> 0.5", None))
        self.Genre_3_dropdown_2.setItemText(3, _translate("MainWindow", "> 1", None))
        self.Genre_3_dropdown_2.setItemText(4, _translate("MainWindow", "> 1.5", None))
        self.Genre_3_dropdown_2.setItemText(5, _translate("MainWindow", "> 2", None))
        self.Genre_3_dropdown_2.setItemText(6, _translate("MainWindow", "> 2.5", None))
        self.Genre_3_dropdown_2.setItemText(7, _translate("MainWindow", "> 3", None))
        self.Genre_3_dropdown_2.setItemText(8, _translate("MainWindow", "> 3.5", None))
        self.Genre_3_dropdown_2.setItemText(9, _translate("MainWindow", "> 4", None))
        self.Genre_3_dropdown_2.setItemText(10, _translate("MainWindow", "> 4.5", None))
        self.label_3.setText(_translate("MainWindow", "Random Movie", None))
        self.Gen_ran_btn.setText(_translate("MainWindow", "Generate random UserID and MovieID", None))
        self.label_2.setText(_translate("MainWindow", "Rating Prediction", None))
        self.Movie_line.setText(_translate("MainWindow", "Please write the title or ID of your movie", None))
        self.MovieID_checkbox.setText(_translate("MainWindow", "MovieID", None))
        self.MovieTitle_checkbox.setText(_translate("MainWindow", "Movie title", None))
        self.Gen_rating_btn.setText(_translate("MainWindow", "Generate rating prediction", None))
        self.User_Line.setText(_translate("MainWindow", "Please enter a UserID", None))

