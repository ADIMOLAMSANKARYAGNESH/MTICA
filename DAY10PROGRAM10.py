import sqlite3
carData=[
    (1,'Audi',4000000),
    (2, 'Mercedes', 8000000),
    (3, 'Skoda', 500000),
    (4, 'Bentley', 800000),
    (5, 'Citroen', 700000),
    (6, 'Volkswagen', 1000000),
    (7, 'Volvo', 10000000),
    (8, 'Yagnesh', 10000000)
    ]
con=sqlite3.connect('mtca.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("Values inserted.")

