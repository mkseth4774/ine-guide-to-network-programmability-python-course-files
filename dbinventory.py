##
## Our sqlite database program!
import sqlite3

dbpath = '/Users/travispbonfigli/bin/PYTHON/INE/dbinventorytable'

connection = sqlite3.connect(dbpath)
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS dbinventorytable
             (serial VARCHAR(20) PRIMARY KEY NOT NULL,
              hostname VARCHAR(20),
              ios VARCHAR(15),
              location VARCHAR(30))""")

serialNumber = input('Enter serial number: ')
hostname = input('Enter hostname: ')
ios = input('Enter IOS version: ')
location = input('Enter the location: ')

c.execute("INSERT INTO dbinventorytable VALUES(?, ?, ?, ?);", (serialNumber, 
                                                               hostname,
                                                               ios,
                                                               location))
connection.commit()

select = "SELECT * FROM dbinventorytable"
retreive = c.execute(select)
for row in retreive:
	print(row)

##
## End of file