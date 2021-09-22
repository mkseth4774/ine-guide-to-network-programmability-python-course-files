##
##
import sqlite3
dbpath = ('/Users/travispbonfigli/bin/PYTHON/INE/inventory.db')

hostname = input('Enter the node hostname: ')
serialnumber = input('Enter the node serial number: ')

#dbconnect = sqlite3.connect(':memory:')
dbconnect = sqlite3.connect(dbpath)
dbcursor = dbconnect.cursor()

dbcursor.execute('''create table if not exists inventory.db
                   (serialnumber varchar(20) primary key not null,
                    hostname varchar(20))''')

#dbconnect = sqlite3.connect(dbpath)
#dbcursor = dbconnect.cursor()
#dbcursor.execute('select * from inventory')

#dbconnect = sqlite3.connect('inventory')
#dbconnect = sqlite3.connect(':memory:')
#dbcursor = dbconnect.cursor()

#dbcmd = '''replace into inventory (serialnumber, hostname) values(serialnumber, hostname)'''
#dbcursor.execute(dbcmd, (serialnumber, hostname))


dbconnect = sqlite3.connect(dbpath)
dbcursor = dbconnect.cursor()

dbcursor.execute('select * from inventory.db')
output = dbcursor.fetchall()
dbconnect.commit()

##
## End of file...
