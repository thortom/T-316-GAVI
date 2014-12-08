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
        # TODO: check if all data is available
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
        # rand = random.randint(0,row)
        # return Title.at[rand,'Title']
        # #print(Title)

        # TODO:
        pass


    def insertTable(self, data):
        cur = self.connection.cursor()
        con = self.connection

        cur.execute("DROP TABLE IF EXISTS Test")

        cur.execute("DROP TABLE IF EXISTS tags")
        cur.execute("CREATE TABLE tags(Index INTEGER PRIMARY KEY, UserID INT, MovieID INT, Tag TEXT, Timestamp INT)")
        for idx, row in data.tagsData.iterrows():
            cur.execute("INSERT INTO tags VALUES(%s, %s, %s, '%s', %s)" %(idx, row['UserID'], row['MovieID'], str(row['Tag']).replace("'","''"), row['Timestamp']))
            print('idx',idx)
            if idx == 11:
                break

        # # ['UserID', 'Gender', 'Age', 'Occupation', 'ZipCode']
        # cur.execute("DROP TABLE IF EXISTS users")
        # cur.execute("CREATE TABLE users(UserID INTEGER PRIMARY KEY, Gender INT, Age INT, Occupation TEXT, Timestamp INT)")
        # for idx, row in data.tagsData.iterrows():
        #     cur.execute("INSERT INTO users VALUES(%s, %s, %s, '%s', %s)" %(row['UserID'], row['Gender'], row['Age'], row['Occupation'], row['ZipCode']))

