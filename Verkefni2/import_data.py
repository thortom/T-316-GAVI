import sys
import os
import csv
import numpy as np
import pandas as pd

class import_data():
    def __init__(self, mydb):
        self.mydb = mydb

        print("Looking for data")
        self.findData()
        print("Got the data")

    #Finds .dat files in the folder /data
    def findData(self):
        dataFiles=[]
        path = os.getcwd()+"\data"
        for file in os.listdir(path):
            if file.endswith(".dat"):
                self.readData(path+'\\'+file)

    def readMoviesData(self, fileName):
        print("start: ", fileName.rsplit('\\')[-1])

        # Need to fix for delimiter
        data = pd.read_csv(fileName, delimiter='::', header=None, engine='python')

        data.columns = ['movieid', 'titleyear','genres']

        thetitle_year = [i for i in data.titleyear]
        thetitle = [i.rsplit('(',1)[0].strip() for i in thetitle_year]
        theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in thetitle_year]

        data['title'] = pd.Series(thetitle, index=data.index)
        data['year'] = pd.Series(theyear, index=data.index)

        data.drop('titleyear', axis=1, inplace=True)

        self.mydb.cursor.execute("DROP TABLE IF EXISTS movies")
        self.mydb.cursor.execute("CREATE TABLE movies(movieid INTEGER PRIMARY KEY, title TEXT, year TEXT,  genres TEXT)")
        for idx, row in data.iterrows():
            self.mydb.cursor.execute("INSERT INTO movies VALUES(%s, '%s', '%s', '%s')" %(row['movieid'], str(row['title']).replace("'","''"), row['year'], str(row['genres']).replace("'","''")))
        print('Saved movies to database')

    def readTagsData(self, fileName):
        print("start: ", fileName.rsplit('\\')[-1])
        self.mydb.cursor.execute("DROP TABLE IF EXISTS tags")
        self.mydb.cursor.execute("CREATE TABLE tags(userid INT, movieid INT, tag TEXT, time INT);")
        # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY tags FROM '%s' Using Delimiters '\t';" %fileName)
        # Tekur lengri tíma en fileName þarf ekki endileg að vera í C:\ möppunni
        # with open(fileName, newline='') as csvfile:
        #     for line in csvfile:
        #         line = line.split('\t')
        #         self.mydb.cursor.execute("INSERT INTO tags(userid, movieid, tag, time) VALUES(%s ,%s ,%s ,%s)", (line[0], line[1], line[2], line[3]))
        self.mydb.cursor.execute("ALTER TABLE tags DROP COLUMN time;")
        self.mydb.cursor.execute("ALTER TABLE tags ADD COLUMN index BIGSERIAL PRIMARY KEY;")
        self.mydb.cursor.execute("ALTER TABLE tags ADD FOREIGN KEY (movieid) REFERENCES movies(movieid);")
        print('Saved tags to database')

    def readRatingsData(self, fileName):
        print("start: ", fileName.rsplit('\\')[-1])
        self.mydb.cursor.execute("DROP TABLE IF EXISTS ratings")
        self.mydb.cursor.execute("CREATE TABLE ratings(userid INT, movieid INT, rating DEC, time INT);")
        # file þarf helst að ver í C:\ möppunni vegna permission sem COPY þarf að hafa
        self.mydb.cursor.execute("COPY ratings FROM '%s' Using Delimiters '\t';" %fileName)
        # Tekur 2-3 tíma en fileName þarf ekki endileg að vera í C:\ möppunni
        # with open(fileName, newline='') as csvfile:
        #     for line in csvfile:
        #         line = line.split('\t')
        #         self.mydb.cursor.execute("INSERT INTO ratings(userid, movieid, rating, time) VALUES(%s ,%s ,%s ,%s)",(line[0], line[1], line[2], line[3]))
        self.mydb.cursor.execute("ALTER TABLE ratings DROP COLUMN time;")
        self.mydb.cursor.execute("ALTER TABLE ratings ADD COLUMN index BIGSERIAL PRIMARY KEY;")
        self.mydb.cursor.execute("ALTER TABLE ratings ADD FOREIGN KEY (movieid) REFERENCES movies(movieid);")
        self.mydb.cursor.execute("CREATE INDEX userid_idx ON ratings (userid);")
        print('Saved ratings to database')

    # Reads .dat files and changes the delimiter :: -> \t
    def fixDelimiterInFile(self, fileName):
        newFileName = fileName.replace('.dat', '.csv')
        with open(fileName, newline='', encoding='utf-8') as dat_file:
            with open(newFileName , 'w', newline='', encoding='utf-8') as out_data:
                for line in dat_file:
                    line = line.replace('\t',' ')
                    lines = line.split('::')
                    out_data.write('\t'.join(lines))
        return newFileName

    def readData(self, fileName):
        if ('movies' in fileName):
            self.readMoviesData(fileName)
        elif ('tags' in fileName):
            fileName = self.fixDelimiterInFile(fileName)
            self.readTagsData(fileName)
        elif ('ratings' in fileName):
            fileName = self.fixDelimiterInFile(fileName)
            self.readRatingsData(fileName)
        else:
            print('Error: .dat file {} found but not read'.format(fileName.rsplit('\\')[-1]))

if __name__ == '__main__':
    import_data()