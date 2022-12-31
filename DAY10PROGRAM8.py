import sqlite3 as lite
con=lite.connect('mtca.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE Cars(Id INT,Name TEXT,Price INT)''')
print("Table Cars Created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',4000000)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',8000000)")
cur.execute("INSERT INTO Cars VALUES(3,'Skoda',500000)")
cur.execute("INSERT INTO Cars VALUES(4,'Bentley',800000)")
cur.execute("INSERT INTO Cars VALUES(5,'Citroen',700000)")
cur.execute("INSERT INTO Cars VALUES(6,'Volkswagen',1000000)")
cur.execute("INSERT INTO Cars VALUES(7,'Volvo',10000000)")
con.commit()
print("Values in table car inserted.")


































