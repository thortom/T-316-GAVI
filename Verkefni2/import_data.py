import sys
import os
import numpy as np
import pandas as pd

class import_data():
    def __init__(self):
        # Empty initialization
        self.moviesData = pd.DataFrame()
        self.tagsData = pd.DataFrame()
        self.usersData = pd.DataFrame()
        self.ratingsData = pd.DataFrame()

        self.findData()
        # print(self.moviesData.head())
        # print(self.tagsData.head())
        # print(self.usersData.head())
        # print(self.ratingsData.head())

    def findData(self):
        #Finds .dat files in the folder /data
        path = os.getcwd()+"\data"
        for file in os.listdir(path):
            if file.endswith(".dat"):
                self.readData(path+'\\'+file)
        pass

    def readMoviesData(self, data):
        data.columns = ['MovieID', 'TitleYear','Genres']
        data.set_index('MovieID', inplace=True)

        thetitle_year = [i for i in data.TitleYear]
        thetitle = [i.rsplit('(',1)[0].strip() for i in thetitle_year]
        theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in thetitle_year]

        data['Title'] = pd.Series(thetitle, index=data.index)
        data['Year'] = pd.Series(theyear, index=data.index)

        data.drop('TitleYear', axis=1, inplace=True)
        self.moviesData = data

    def readTagsData(self, data):
        data.columns = ['UserID', 'MovieID', 'Tag', 'Timestamp']
        # Not sure what should be the index, if there should be an index
        # data.set_index('UserID', inplace=True)
        self.tagsData = data

    def readUsersData(self, data):
        data.columns = ['UserID', 'Gender', 'Age', 'Occupation', 'ZipCode']
        data.set_index('UserID', inplace=True)
        self.usersData = data

    def readRatingsData(self, data):
        data.columns = ['UserID', 'MovieID', 'Rating', 'Timestamp']
        # Not sure what should be the index, if there should be an index
        # data.set_index('UserID', inplace=True)
        self.ratingsData = data

    def readData(self, fileName):
        data = pd.read_csv(fileName, delimiter='::', header=None, engine='python')
        if ('movies.dat' in fileName):
            self.readMoviesData(data)
        elif ('tags.dat' in fileName):
            self.readTagsData(data)
        elif ('users.dat' in fileName):
            self.readUsersData(data)
        elif ('ratings.dat' in fileName):
            self.readRatingsData(data)
        else:
            print('Error: .dat file {} found but not read'.format(fileName))


if __name__ == '__main__':
    import_data()