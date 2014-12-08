import psycopg2
import sys
import theUI
from manage_db import manage_db
from import_data import import_data


if __name__ == '__main__':
    mydb = manage_db('localhost','verkefni2', 'postgres', 'postgres')
    if mydb.missingData():
    	data = import_data()
    	mydb.insertTable(data)

    ##########################
    # Testing
    con = mydb.getConnection()
    cur = con.cursor()
    cur.execute("SELECT tag FROM tags")
    count = 0
    while True:
        row = cur.fetchone()
            
        if row == None or count == 10:
            break
        print(row)
        count += 1
    ##########################

    window = theUI.loadUI(mydb)
