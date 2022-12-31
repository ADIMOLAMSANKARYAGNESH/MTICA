import sqlite3 as lite
con=lite.connect('mtca.db')
cur=con.cursor()
cur.execute('''
UPDATE Cars
SET Name='Yagnesh' WHERE Id=7
''')
con.commit()
con.close()
print("Data Updated")
