import psycopg2
import sys
from import_data import import_data
import pandas as pd
import sqlalchemy as sqlc 
from pandas.io import sql
import random

class manage_db():
    def __init__(self,host,database, user, password):
        self.connection = self.connect(host,database, user, password)
        self.cursor = self.connection.cursor()
        #self.insertTable()
    def connect(self,host,database, user, password):
        print('Connecting to database')
        con = None
        try:
            con = psycopg2.connect(host = host, database=database, user=user, password=password)
            print('Connection established')
            con.autocommit = True                                                   # This is done to skip #con.commit()
            return con

        except psycopg2.DatabaseError as e:
            # if con:                                                               # We either use autocommit or commit and rollback
            #     con.rollback()
            #     print("Roll back")
            print('Error %s' % e)
            sys.exit(1)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            if con:
                con.close()
        finally:
            return con

    def missingData(self):
        #Remember to add for the other files
        try:
            if len([item for item in self.getTables() if 'ratings' or 'users' or 'movies' or 'tags' in item]) == 5:
                print('Tables already in Database')
                return False
        except:
            return True
        return True

    def getConnection(self):
        return self.connection

    def getTables(self):
        cur = self.connection.cursor()
        cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        return cur.fetchall()

    def getTopX(self,genres,num):
        cur = self.cursor
        g = " where genres = '"
        for genre in sorted(genres):
            g += genre
            g += '|'
        g = g[:-1] + "'"
        sql = "select movieid, genres from movies"
        if len(genres)>0:
            sql += g

        cur.execute(sql+' limit %s'%str(num))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def createAverageRatingsTable(self):
        cur = self.connection.cursor()
        cur.execute("drop table if EXISTS averageratings")
        cur.execute("create table averageratings(thetitle varchar(180),movieid integer PRIMARY KEY,averagerating float)")
        cur.execute("Insert into averageratings(thetitle,movieid,averagerating) select movies.title, movies.movieid, AVG(ratings.rating) as a from movies join ratings on movies.movieid=ratings.movieid group by movies.movieid order by a DESC")
        print('Av')

    def getRandomMovie(self, genre1, genre2, Rating, Year):
        catagories = ["Pick a genre", "Action", "Adventure",    "Animation",    "Children",   "Comedy",   "Crime",    "Documentary",  "Drama",    "Fantasy",  "Film-Noir",    "Horror",   "Musical",  "Mystery",  "Romance",  "Sci-Fi",   "Thriller", "War",  "Western"]
        cur = self.connection.cursor()

        if 'Pick' in genre1 and 'Pick' in genre2 and 'Rating' in Rating and 'Choose' in Year:
            Start = 'SELECT title From movies'
        else:
            if '' in Year or 'Choose' in Year:
                Year = ''
            else:
                if Year[2] == ' ':
                    Year = 'year ' + Year[0] + Year[1] + "'" + Year[3:len(Year)] + "'"
                elif Year[1] == ' ':
                    Year = 'year ' + Year[0] + "'" + Year[2:len(Year)] + "'"
                elif Year[0] in '12':
                    Year = 'year = ' + "'" + Year + "'" 

            if 'Pick' in genre1 and 'Pick' in genre2:
                Start = 'SELECT title FROM movies WHERE ' + Year
            elif 'Pick' in genre1 and not 'Pick' in genre2:
                genre2 = "'" + genre2 + "'" 
                if Year == '':
                    Start = "SELECT title FROM movies WHERE " + Year + 'genres = ' + genre2
                else:
                    Start = "SELECT title FROM movies WHERE " + Year + ' And ' + 'genres = ' + genre2
            elif not 'Pick' in genre1 and 'Pick' in genre2:
                genre1 = "'" + genre1 + "'" 
                if Year == '':
                    Start = 'SELECT title FROM movies WHERE ' + Year + 'genres = ' + genre1
                else:
                    Start = 'SELECT title FROM movies WHERE ' + Year + ' And ' + 'genres = ' + genre1
            else:
                genre = "'" + genre1 + "|" + genre2 + "'"
                if Year == '':
                    Start = 'SELECT title FROM movies WHERE ' + Year + 'genres = ' + genre
                else:
                    Start = 'SELECT title FROM movies WHERE ' + Year + ' and ' + 'genres = ' + genre

            if not 'Rating' in Rating:
                Start = 'Select title From ratings, movies where rating ' + Rating + ' and RANDOM() < 0.01'
                if not 'Pick' in genre1 and 'Pick' in genre2:
                    Start = Start + ' And genres = ' + genre1
                elif 'Pick' in genre1 and not 'Pick' in genre2:
                    Start = Start + ' And genres = ' + genre2
                else:
                    Start = Start + ' And genres = ' + genre

                if not Year == '':
                    Start = Start + ' And ' + Year

                Start = Start + ' Limit 100'


        cur.execute(Start)
        row = cur.fetchall()
        if not row:
            return 'Nope'
        else:
            row = pd.DataFrame(row)
            rand = random.randint(0,len(row)-1)
            try: 
                return row.iloc[rand,0]
            except:
                print(row)
                print(rand)
                print(row.iloc[rand,0])



    def insertTables(self, data):
        cur = self.connection.cursor()
        con = self.connection

        print('doing -> insertTables()')
        # cur.execute("DROP TABLE IF EXISTS users")
        # cur.execute("CREATE TABLE users(userid INTEGER PRIMARY KEY, gender TEXT, age INT, occupation INT, zipcode INT)")
        # for idx, row in data.usersData.iterrows():
        #     cur.execute("INSERT INTO users VALUES(%s, '%s', %s, %s, %s)" %(row['userid'], row['gender'], row['age'], row['occupation'], row['zipcode']))
        # print('Saved users to database')

        # cur.execute("DROP TABLE IF EXISTS movies")
        # cur.execute("CREATE TABLE movies(movieid INTEGER PRIMARY KEY, title TEXT, year TEXT,  genres TEXT)")
        # for idx, row in data.moviesData.iterrows():
        #     cur.execute("INSERT INTO movies VALUES(%s, '%s', '%s', '%s')" %(row['movieid'], str(row['title']).replace("'","''"), row['year'], str(row['genres']).replace("'","''")))
        # print('Saved movies to database')

        # cur.execute("DROP TABLE IF EXISTS tags")
        # cur.execute("CREATE TABLE tags(index INTEGER PRIMARY KEY, userid INT, movieid INT, tag TEXT)")
        # count = 0
        # for idx, row in data.tagsData.iterrows():
        #     cur.execute("INSERT INTO tags VALUES(%s, %s, %s, '%s')" %(count, row['userid'], row['movieid'], str(row['tag']).replace("'","''")))
        #     count += 1
        # print('Saved tags to database')

        # cur.execute("DROP TABLE IF EXISTS ratings")
        # cur.execute("CREATE TABLE ratings(index INTEGER PRIMARY KEY, userid INT, movieid INT, rating INT)")
        # count = 0
        # for idx, row in data.ratingsData.iterrows():
        #     cur.execute("INSERT INTO ratings VALUES(%s, %s, %s, %s)" %(count, row['userid'], row['movieid'], row['rating']))
        #     count += 1
        # print('Saved ratings to database')

        # print('Hallo')
        # cur.execute("DROP TABLE IF EXISTS ratings")
        # cur.execute("CREATE TABLE ratings(userid INT, col1 TEXT, movieid INT, col2 TEXT, rating DEC, col3 TEXT, time INT);")
        # cur.execute("COPY ratings FROM 'C:/ratings.dat' Using Delimiters ':';")
        # cur.execute('ALTER TABLE ratings DROP COLUMN col1, DROP COLUMN col2, DROP COLUMN col3, DROP COLUMN time;')
        
        # print('Saved ratings to database')
