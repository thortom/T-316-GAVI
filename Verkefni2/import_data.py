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


        print("Looking for data")
        self.findData()
        print("Got the data")

        # print(self.moviesData.head())
        # print(self.tagsData.head())
        # print(self.usersData.head())
        # print(self.ratingsData.head())

    def findData(self):
        #Finds .dat files in the folder /data
        dataFiles=[]
        path = os.getcwd()+"\data"
        for file in os.listdir(path):
            if file.endswith(".dat"):
                self.readData(path+'\\'+file)

    def readMoviesData(self, data):
        data.columns = ['movieid', 'titleyear','genres']
        # data.set_index('MovieID', inplace=True)

        thetitle_year = [i for i in data.titleyear]
        thetitle = [i.rsplit('(',1)[0].strip() for i in thetitle_year]
        theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in thetitle_year]

        data['title'] = pd.Series(thetitle, index=data.index)
        data['year'] = pd.Series(theyear, index=data.index)

        data.drop('titleyear', axis=1, inplace=True)
        self.moviesData = data

    def readTagsData(self, data):
        data.columns = ['userid', 'movieid', 'tag', 'timestamp']
        # Not sure what should be the index, if there should be an index
        # data.set_index('UserID', inplace=True)
        self.tagsData = data

    def readUsersData(self, data):
        data.columns = ['userid', 'gender', 'age', 'occupation', 'zipcode']
        # data.set_index('UserID', inplace=True)
        self.usersData = data

    def readRatingsData(self, data):
        data.columns = ['userid', 'movieid', 'rating', 'timestamp']
        # Not sure what should be the index, if there should be an index
        # data.set_index('UserID', inplace=True)
        self.ratingsData = data

    def readData(self, fileName):
        # print('reading',fileName)

        if ('movies.dat' in fileName):
            chunks = pd.read_csv(fileName, delimiter='::', header=None, engine='python', chunksize=1024)
            data = pd.concat(chunk for chunk in chunks)
            self.readMoviesData(data)
        elif ('tags.dat' in fileName):
            chunks = pd.read_csv(fileName, delimiter='::', header=None, engine='python', chunksize=1024)
            data = pd.concat(chunk for chunk in chunks)
            self.readTagsData(data)
        elif ('users.dat' in fileName):
            chunks = pd.read_csv(fileName, delimiter='::', header=None, engine='python', chunksize=1024)
            data = pd.concat(chunk for chunk in chunks)
            self.readUsersData(data)
        elif ('ratings.dat' in fileName):
            #Takes very long to load
            chunks = pd.read_csv(fileName, delimiter='::', header=None, engine='python', chunksize=1024)
            data = pd.concat(chunk for chunk in chunks)
            self.readRatingsData(data)
            # print('ratings not loaded // Remember to uncomment')
            # cur.execute("DROP TABLE IF EXISTS ratings")
            # cur.execute("CREATE TABLE ratings(userid INT, col1 TEXT, movieid INT, col2 TEXT, rating DEC, col3 TEXT, time INT);")
            # cur.execute("COPY ratings FROM 'C:/ratings.dat' Using Delimiters ':';")
            # cur.execute('ALTER TABLE ratings DROP COLUMN col1, DROP COLUMN col2, DROP COLUMN col3, DROP COLUMN time;')

        else:
            print('Error: .dat file {} found but not read'.format(fileName))

    def ReturnMovieData():
    	return self.moviesData


if __name__ == '__main__':
    import_data()