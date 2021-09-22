##
##
import sqlite3

dbpath = '/Users/travispbonfigli/bin/PYTHON/INE/db3table'

connection = sqlite3.connect(dbpath)
conn = connection.cursor()

##
## Create SQL database table!
##
conn.execute("""CREATE TABLE IF NOT EXISTS db3table
                       (serial VARCHAR(20) PRIMARY KEY NOT NULL,
                        hostname VARCHAR(20),
                        ios VARCHAR (15))""")
##
## Insert some stuff...
##
serialNumber = input('Serial Number: ')
hostname = input('Hostname: ')
ios = input('IOS Version: ')

conn.execute("INSERT INTO db3table VALUES(?, ?, ?);", (serialNumber, hostname, ios))
connection.commit()

##
## Retrieve information...
select = "SELECT * FROM db3table"
receive = conn.execute(select)
for row in receive:
    print(row)

##
## End of file...
