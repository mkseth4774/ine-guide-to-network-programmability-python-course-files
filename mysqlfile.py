##
##
import MySQLdb

## Create the connection to the MySQL database...
db = MySQLdb.connect("localhost","testuser","test123","dbtable" )

## Now, create the cursor object for our commands...
cursor = db.cursor()

## Run the command to get the version of MySQL...
cursor.execute("SELECT * from dbtable")

## Fetch all rows and print them out...
data = cursor.fetchall()
print(data)

## Perform good housekeeping...
db.close()
