##
##
import sqlite3

def create():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS deviceinventory
                 (SERIALNUMBER VARCHAR(20) PRIMARY KEY NOT NULL, HOSTNAME VARCHAR(20), IOSi VARCHAR(15))""")
    except:
        pass

def insert(serialnumber, hostname, ios):
    c.execute("""REPLACE INTO deviceinventory (SERIALNUMBER, HOSTNAME, IOS)
              values(serialnumber, hostname, ios)""")

def select(verbose=True):
    sql = "SELECT * FROM deviceinventory"
    recs = c.execute(sql)
    if verbose:
        for row in recs:
            print(row)

def main():

    serialnumber = input('Enter the serial number: ')
    hostname = input('Enter the hostname: ')
    ios = input('Enter the IOS type/version: ')

    db_path = '/Users/travispbonfigli/bin/PYTHON/INE/inventory.db'
    conn = sqlite3.connect(db_path)

    c = conn.cursor()
    create()
    insert(serialnumber, hostname, ios)
    conn.commit()
    select()
    c.close()

if __name__ == '__main__':
    main()

##
## End of file...
