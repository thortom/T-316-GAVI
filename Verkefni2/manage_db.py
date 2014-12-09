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
            if len([item for item in self.getTables() if 'ratings' or 'users' or 'movies' or 'tags' in item]) == 4:
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
            
    def getRandomMovie(self):
        # engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
        # Title = pd.read_sql_table('tafla', engine, columns = ['Title'])
        # row,col = Title.shape
        # rand = random.randint(0,row)
        # return Title.at[rand,'Title']
        # #print(Title)

        # TODO:
        pass
