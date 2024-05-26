import sqlite3

conn= sqlite3.connect('test.db')

cursor =conn.cursor()

#create a tables
cursor.execute(
    """CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT)
    """
)

#insert data in the tbale
cursor.execute(
    "INSERT INTO employees (name,age,department) VALUES (?,?,?)",
    ('Jhon Doe',30,'Sales') 
)


#retrieve 
cursor.execute(
    "SELECT * FROM employees"
)

rows =cursor.fetchall()
print(rows)
conn.commit()
conn.close()
