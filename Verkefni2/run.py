import psycopg2
import sys
import theUI
from manage_db import manage_db
from import_data import import_data


if __name__ == '__main__':
    mydb = manage_db('localhost','verkefni2', 'postgres', 'postgres')
    mydb.createAverageRatingsTable()
    if mydb.missingData():
    	data = import_data()
    	#mydb.insertTables(data)
        
    window = theUI.loadUI(mydb)
