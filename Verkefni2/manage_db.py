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
        self.insertTable()
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

    def getTables(self):
        cur = self.connection.cursor()
        # cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        # print(cur.fetchall())
        engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
        Title = pd.read_sql_table('tafla', engine, columns = ['Title'])
        row,col = Title.shape
        rand = random.randint(0,row)
        return Title.at[rand,'Title']
        #print(Title)


    def insertTable(self):
        cur = self.connection.cursor()
        con = self.connection
        Importin = import_data()
        Data = Importin.moviesData

        engine = sqlc.create_engine('postgresql://postgres:postgres@localhost:5432/verkefni2')
        #Data.to_sql('tafla', engine)

        #print(pd.read_sql_table('tafla', engine))
        # cur.execute("SELECT * FROM Tafla", engine)
        # cur.fetchone()
        # # print(pd.read_sql_query('SELECT * FROM Tafla', engine))
        # MovieID = pd.read_sql_table('tafla', engine, columns = ['MovieID'])
        # sql.execute('SELECT Year FROM tafla', engine)
        #print(MovieID)

        #sql.write_frame(Data,'TableWithMovie', con, if_exists = 'append')



        #pass