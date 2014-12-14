import psycopg2
import sys
import theUI
from manage_db import manage_db
from import_data import import_data

if __name__ == '__main__':
    mydb = manage_db('localhost','verkefni3', 'postgres', 'postgres')
    if mydb.missingData():
        data = import_data(mydb)
    window = theUI.loadUI(mydb)
    