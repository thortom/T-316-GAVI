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
            if len([item for item in self.getTables() if 'ratings' or 'users' or 'movies' or 'tags' in item]) > 1:
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
        g = " where movies.genres like '%"
        for genre in sorted(genres):
            print(genre)
            g += genre+"%' and genres like'%"
        g = g[:-18]
        print("g:",g)
        sql = "select movies.title, averageratings.averagerating from averageratings inner join movies on averageratings.movieid = movies.movieid"
        if len(genres)>0:
            sql += g
        sql += " order by averagerating desc"

        cur.execute(sql+' limit %s'%str(num))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def createAverageRatingsTable(self):
        # Avoid recreating table if not needed
        exists = False
        try:
            self.cursor.execute("select exists(select relname from pg_class where relname='averageratings')")
            exists = self.cursor.fetchone()[0]
        except:
            pass
        if not exists:
            self.cursor.execute("drop table if EXISTS averageratings")
            self.cursor.execute("create table averageratings(title varchar(180),movieid integer PRIMARY KEY,averagerating float)")
            self.cursor.execute("Insert into averageratings(title,movieid,averagerating) select title, movieid, averagerating from(select movies.title, movies.movieid, AVG(ratings.rating)as averagerating, count(ratings.rating) as numberofvotes from movies join ratings on movies.movieid=ratings.movieid group by movies.movieid order by averagerating DESC) as avrat where numberofvotes > 100")
            print('Averageratings table created')
        
    def getRandomMovie(self, genre1, genre2, Rating, Year):
        catagories = ["Pick a genre", "Action", "Adventure",    "Animation",    "Children",   "Comedy",   "Crime",    "Documentary",  "Drama",    "Fantasy",  "Film-Noir",    "Horror",   "Musical",  "Mystery",  "Romance",  "Sci-Fi",   "Thriller", "War",  "Western"]
        if 'Pick' in genre1 and 'Pick' in genre2 and 'Rating' in Rating and 'Choose' in Year:
            Start = 'SELECT m.title From movies m'
        else:
            if not Year or 'Choose' in Year:
                Year = ''
            else:
                if Year[2] == ' ':
                    Year = 'm.year ' + Year[0] + Year[1] + "'" + Year[3:len(Year)] + "'"
                elif Year[1] == ' ':
                    Year = 'm.year ' + Year[0] + "'" + Year[2:len(Year)] + "'"
                elif Year[0] in '12':
                    Year = 'm.year = ' + "'" + Year + "'" 

            if 'Pick' in genre1 and 'Pick' in genre2:
                Start = 'SELECT m.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.title = av.title'
                if not Year:
                    Start = 'SELECT m.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.title = av.title ' + Year
            elif 'Pick' in genre1 and not 'Pick' in genre2:
                if Year == '':
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%'".format(genre2)
                else:
                    print('HAllo')
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%' and {} ".format(genre2, Year)
            elif not 'Pick' in genre1 and 'Pick' in genre2:
                if Year == '':
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%' ".format(genre1)
                else:
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%' and {} ".format(genre1, Year)
            else:
                if Year == '':
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%' and m.genres like '%{}%'".format(genre1,genre2)
                else:
                    Start = "SELECT movies.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid WHERE m.genres like '%{}%' and m.genres like '%{}%' and {} ".format(genre1,genre2,Year)

            if not 'Rating' in Rating:
                if 'Pick' in genre1 and 'Pick' in genre2 and not Year:
                    Start = Start + " av.averagerating {} and RANDOM() < 0.01".format(Rating)
                else:
                    Start = Start + " And av.averagerating {} and RANDOM() < 0.01".format(Rating)
                Start = Start + ' Limit 100'

        print(Start)
        self.cursor.execute(Start)
        row = self.cursor.fetchall()
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
