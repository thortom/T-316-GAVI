# -*- coding: utf-8 -*-
import psycopg2
import sys
from import_data import import_data
import pandas as pd
import sqlalchemy as sqlc 
from pandas.io import sql
import random
import gc



class manage_db():
    def __init__(self,host,database, user, password):
        self.connection = self.connect(host,database, user, password)
        self.engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
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

    def getRandomMovie(self):
        # engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
        # Title = pd.read_sql_table('tafla', engine, columns = ['Title'])
        # row,col = Title.shape
        
        # cur = self.connection.cursor()
        # print(pd.read_sql_query('Select title From tepppi', engine))
        # cur.execute("SELECT Title From tepppi Where Year >= 2007")
        # row = cur.fetchall()
        # print(pd.DataFrame(row))
        # print(len(row))
        # rand = random.randint(0,len(row))
        # # print(row[rand])
        # return row[rand][0]
        # #print(Title)

        # TODO:
        pass



    def insertTables(self, data):
        

        # con = self.connection
        # cur = self.connection.cursor()

        # #cur.execute('DROP TABLE tags')        
        # #Data.to_sql('tepppi', engine)
        # #cur.execute('Drop Table movies')
        # #cur.execute('Drop Table ratings')
        # #cur.execute('Drop Table users')
        # #cur.execute('Drop Table tags')
        # print('HelloWorld')
        # print (gc.collect())

        # df1 = data.ratingsData['userid']
        # df2 = data.ratingsData['movieid']
        # df3 = data.ratingsData['rating']
        # print(gc.collect())
        # print('as')
        # data.ratingsData.to_sql('ratings',self.engine,if_exists = 'append', chunksize = 500)
        # print('asd')
        # data.ratingsData.to_sql('ratings', self.engine, if_exists = 'append')
        # print('asdf')
        # data.ratingsData.to_sql('ratings', self.engine, if_exists = 'append')




        #data.moviesData.to_sql('movies',self.engine)
        #data.ratingsData.to_sql('ratings',self.engine, chunksize = 10)
        #data.tagsData.to_sql('tags', self.engine)
        #data.usersData.to_sql('users',self.engine)

        #gc.collect()
        # print (gc.collect())
        # cur.execute("DROP TABLE IF EXISTS ratings")
        # cur.execute("CREATE TABLE ratings(index INTEGER PRIMARY KEY, userid INT, movieid INT, rating INT)")
        # count = 0
        # for idx, row in data.ratingsData.iterrows():
        #     print('hello')
        #     cur.execute("INSERT INTO ratings VALUES(%s, %s, %s, %s)" %(count, row['userid'], row['movieid'], row['rating']))
        #     count += 1
        # print('Saved ratings to database')






        cur = self.connection.cursor()
        con = self.connection

        print('doing -> insertTables()')
        cur.execute("DROP TABLE IF EXISTS users")
        cur.execute("CREATE TABLE users(userid INTEGER PRIMARY KEY, gender TEXT, age INT, occupation INT, zipcode INT)")
        for idx, row in data.usersData.iterrows():
            cur.execute("INSERT INTO users VALUES(%s, '%s', %s, %s, %s)" %(row['userid'], row['gender'], row['age'], row['occupation'], row['zipcode']))
        print('Saved users to database')

        # cur.execute("DROP TABLE IF EXISTS movies")
        # cur.execute("CREATE TABLE movies(movieid INTEGER PRIMARY KEY, title TEXT, year TEXT,  genres TEXT)")
        # for idx, row in data.moviesData.iterrows():
        #     cur.execute("INSERT INTO movies VALUES(%s, '%s', '%s', '%s')" %(row['movieid'], str(row['title']).replace("'","''"), row['year'], str(row['genres']).replace("'","''")))
        # print('Saved movies to database')

        cur.execute("DROP TABLE IF EXISTS tags")
        cur.execute("CREATE TABLE tags(index INTEGER PRIMARY KEY, userid INT, movieid INT, tag TEXT)")
        count = 0
        for idx, row in data.tagsData.iterrows():
            cur.execute("INSERT INTO tags VALUES(%s, %s, %s, '%s')" %(count, row['userid'], row['movieid'], str(row['tag']).replace("'","''")))
            count += 1
        print('Saved tags to database')

        cur.execute("DROP TABLE ratings")
        cur.execute("CREATE TABLE ratings(index INTEGER PRIMARY KEY, userid INT, movieid INT, rating INT)")
        count = 0
        for idx, row in data.ratingsData.iterrows():
            cur.execute("INSERT INTO ratings VALUES(%s, %s, %s, %s)" %(count, row['userid'], row['movieid'], row['rating']))
            count += 1
        print('Saved ratings to database')
