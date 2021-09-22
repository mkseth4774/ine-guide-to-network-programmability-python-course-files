##
##
import sqlite3
from os import system

def dbcreate(c):
    try:
        c.execute("""CREATE TABLE proddb (serial TEXT PRIMARY KEY NOT NULL, 
                                                     hostname TEXT, 
                                                     ios TEXT, 
                                                     location TEXT)""")
    except sqlite3.OperationalError as opError:
        print('Database already exists!')
        print('Exception caught: ---> ', opError)

def dbinsert(c, connection, serial, hostname, ios, location):
    try:
        with connection:
            c.execute("INSERT INTO proddb values(?, ?, ?, ?);", (serial, hostname, ios, location))
    except sqlite3.IntegrityError as sqlite3Error:
        print('Entry exists!!! SQLite3 Error: ---> ', sqlite3Error)

def dbselect(c):
    try:
        sqltable = "SELECT * from proddb"
        result = c.execute(sqltable)
        fulltable = c.fetchall()
        print(fulltable)
    except Exception as dbException:
        print('Could not access DB: ---> ', dbException)

def dbremove(c, connection, serial):
    try:
        with connection:
            c.execute("DELETE FROM proddb WHERE serial = ?", (serial,))
    except:
        print('We have an issue deleting...')
    #removal = 'DELETE FROM proddb WHERE serial = ?'
    #c.execute(removal, (serial,))
    # Don't forget to commit the DB changes if you use this code!!!

def main():
    '''This is the program main function'''
    system('clear')
    print()
    print('Welcome to the Python SQLite3 Database Inventory Program!')
    print()

    dbpath = '/Users/travispbonfigli/bin/PYTHON/INE/proddb'
    connection = sqlite3.connect(dbpath)
    c = connection.cursor()
    
    while True:
        print('''Please make your selection from the options below:
        
        1. Create a the prod.db database
        2. Insert an entry into the database
        3. Display the database contents
        4. Remove an entry from the database
        5. Exit...
        ''')
        
        answer = input('Which option would you like to select: ')
        
        if answer == '1':
            dbcreate(c)
        elif answer == '2':
            serial = input('Enter serial number: ')
            hostname = input('Enter hostname: ')
            ios = input('Enter IOS version: ')
            location = input('Enter device location: ')
            dbinsert(c, connection, serial, hostname, ios, location)
        elif answer == '3':
            dbselect(c)
        elif answer == '4':
            serial = input('Enter the serial number of the device to remove: ')
            dbremove(c, connection, serial)
        elif answer == '5':
            exit(99)
        else:
            print('You need to pick an option from above - please try again!')

if __name__ == '__main__':
    main()

##
## End of file...