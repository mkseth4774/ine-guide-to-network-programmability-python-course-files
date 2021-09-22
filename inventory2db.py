import sqlite3

def create():
    try:
        c.execute("""CREATE TABLE db2table 
                 (serial, hostname, ios)""")
    except:
        pass

def insert():
    c.execute("""INSERT INTO db2table (serial, hostname, ios)
              values('FTX8675309', 'rtr234', 'IOS-XE')""")

def select(verbose=True):
    sql = "SELECT * FROM db2table"
    recs = c.execute(sql)
    if verbose:
        for row in recs:
            print(row)

db_path = r'/Users/travispbonfigli/bin/PYTHON/INE/db2table'
conn = sqlite3.connect(db_path)
c = conn.cursor()
create()
insert()
conn.commit()
select()
c.close()

##
## End of file...
