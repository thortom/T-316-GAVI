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
        print('tables', self.getTables())
        try:
            if 'users' in list(self.getTables()[:][0]):
                print('tafla already in database')
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
        command = "select movieid from movies"
        s = " where genres = "
        for genre in genres:
            if genre == genres[0]:
                command += (s+"'"+genre+"'")
            else:
                command += (" or genres = "+"'"+genre+"'")
        print(command)
        cur = self.connection.cursor()
        
        #cur.execute("select movieid from movies where genres = '%s' limit %s" %(genres[0],num))
        cur.execute(command+" limit %s" %num)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def getRandomMovie(self):
        # engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
        # Title = pd.read_sql_table('tafla', engine, columns = ['Title'])
        # row,col = Title.shape
        # rand = random.randint(0,row)
        # return Title.at[rand,'Title']
        # #print(Title)

        # TODO:
        pass

    def insertTables(self, data):
        cur = self.connection.cursor()
        con = self.connection

        print('doing -> insertTables()')
        cur.execute("DROP TABLE IF EXISTS users")
        cur.execute("CREATE TABLE users(userid INTEGER PRIMARY KEY, gender TEXT, age INT, occupation INT, zipcode INT)")
        for idx, row in data.usersData.iterrows():
            cur.execute("INSERT INTO users VALUES(%s, '%s', %s, %s, %s)" %(row['userid'], row['gender'], row['age'], row['occupation'], row['zipcode']))
        print('Saved users to database')

        cur.execute("DROP TABLE IF EXISTS movies")
        cur.execute("CREATE TABLE movies(movieid INTEGER PRIMARY KEY, title TEXT, year TEXT,  genres TEXT)")
        for idx, row in data.moviesData.iterrows():
            cur.execute("INSERT INTO movies VALUES(%s, '%s', '%s', '%s')" %(row['movieid'], str(row['title']).replace("'","''"), row['year'], str(row['genres']).replace("'","''")))
        print('Saved movies to database')

        cur.execute("DROP TABLE IF EXISTS tags")
        cur.execute("CREATE TABLE tags(index INTEGER PRIMARY KEY, userid INT, movieid INT, tag TEXT)")
        count = 0
        for idx, row in data.tagsData.iterrows():
            cur.execute("INSERT INTO tags VALUES(%s, %s, %s, '%s')" %(count, row['userid'], row['movieid'], str(row['tag']).replace("'","''")))
            count += 1
        print('Saved tags to database')

        cur.execute("DROP TABLE IF EXISTS ratings")
        cur.execute("CREATE TABLE ratings(index INTEGER PRIMARY KEY, userid INT, movieid INT, rating INT)")
        count = 0
        for idx, row in data.ratingsData.iterrows():
            cur.execute("INSERT INTO ratings VALUES(%s, %s, %s, %s)" %(count, row['userid'], row['movieid'], row['rating']))
            count += 1
        print('Saved ratings to database')
