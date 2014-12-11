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
        self.sizeOfRatingsTable = None

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
            if len([item for item in self.getTables() if 'ratings' or 'movies' or 'tags' in item]) > 1:
            # if len([item for item in self.getTables() if 'ratings' and 'users' and 'movies' and 'tags' in item]) > 1:
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
            g += genre+"%' and genres like'%"
        g = g[:-18]
        sql = "select movies.title, averageratings.averagerating from averageratings inner join movies on averageratings.movieid = movies.movieid"
        if len(genres)>0:
            sql += g
        sql += " order by averagerating desc"

        cur.execute(sql+' limit %s'%str(num))
        rows = cur.fetchall()
        text ="Rank\tRating\tTitle\n\n"
        r=1
        for row in rows:
            row = list(row)
            #print(row[0],round(row[1],2))
            text += str(r)+'\t'+str(round(row[1],2)) + '\t' + row[0]+'\n'
            r+=1
        return(text[:-1])

    def createAverageRatingsTable(self):
        # Avoid recreating table if not needed
        exists = False
        try:
            self.cursor.execute("select exists(select relname from pg_class where relname='averageratings')")
            exists = self.cursor.fetchone()[0]
        except:
            pass
        if not exists:
            print("start: averageratings", )
            self.cursor.execute("drop table if EXISTS averageratings")
            self.cursor.execute("create table averageratings(title varchar(180),movieid integer PRIMARY KEY,averagerating float)")
            self.cursor.execute("Insert into averageratings(title,movieid,averagerating) select title, movieid, averagerating from(select movies.title, movies.movieid, AVG(ratings.rating)as averagerating, count(ratings.rating) as numberofvotes from movies join ratings on movies.movieid=ratings.movieid group by movies.movieid order by averagerating DESC) as avrat where numberofvotes > 100")
            # self.cursor.execute("Insert into averageratings(title,movieid,averagerating) select movies.title, movies.movieid, AVG(ratings.rating) as a from movies join ratings on movies.movieid=ratings.movieid group by movies.movieid order by a DESC")
            print('Averageratings table created')

    def getRandomUserAndMovie(self):
        if self.sizeOfRatingsTable == None:
            self.cursor.execute("select max(index) from ratings")
            self.sizeOfRatingsTable = self.cursor.fetchone()[0]

        randRatingsRow = random.randint(1, self.sizeOfRatingsTable)
        self.cursor.execute(''' select r.userid, m.title
                                    from ratings r, movies m
                                        where r.index=%s and r.movieid=m.movieid''' %randRatingsRow)
        row = self.cursor.fetchone()
        userID, movieTitle = row[0], row[1]
        return userID, movieTitle
        
    def getRandomMovie(self, genre1, genre2, Rating, Year):
        catagories = ["Pick a genre", "Action", "Adventure",    "Animation",    "Children",   "Comedy",   "Crime",    "Documentary",  "Drama",    "Fantasy",  "Film-Noir",    "Horror",   "Musical",  "Mystery",  "Romance",  "Sci-Fi",   "Thriller", "War",  "Western"]
        Start = 'SELECT m.title FROM movies m Inner Join averageratings av on av.movieid = m.movieid '
        if 'Pick' in genre1 and 'Pick' in genre2 and 'Rating' in Rating and 'Choose' in Year:
            pass
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
                if Year:
                    Start = Start + ' Where ' + Year
            elif not 'Pick' in genre1 and 'Pick' in genre2:
                if not Year:
                    Start = Start + "WHERE m.genres like '%{}%'".format(genre1)
                else:
                    Start = Start + " and m.genres like '%{}%' and {} ".format(genre1, Year)
            elif 'Pick' in genre1 and not 'Pick' in genre2:
                if not Year:
                    Start = Start + "WHERE m.genres like '%{}%'".format(genre2)
                else:
                    Start = Start + " and m.genres like '%{}%' and {} ".format(genre2, Year)
            elif not 'Pick' in genre1 and 'Pick' in genre2:
                if not Year:
                    Start = Start + "WHERE m.genres like '%{}%'".format(genre1)
                else:
                    Start = Start + " and m.genres like '%{}%' and {} ".format(genre1, Year)
            else:
                if Year == '':
                    Start = Start + " Where m.genres like '%{}%' and m.genres like '%{}%'".format(genre1,genre2)
                else:
                    Start = Start + " Where m.genres like '%{}%' and m.genres like '%{}%' and {} ".format(genre1,genre2,Year)

            if not 'Rating' in Rating:
                if 'Pick' in genre1 and 'Pick' in genre2 and not Year:
                    Start = Start + " Where av.averagerating {} and RANDOM() < 1".format(Rating)
                else:
                    Start = Start + " And av.averagerating {} and RANDOM() < 1".format(Rating)
                Start = Start + ' Limit 100'


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
