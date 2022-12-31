import sqlite3 as lite
con=lite.connect('mtca.db')
cur=con.cursor()
cur.execute('''
DELETE FROM Cars
WHERE Name='Yagnesh'
''')
con.commit()
con.close()
print("Data Deleted")
