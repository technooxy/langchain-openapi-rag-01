import sqlite3
import numpy as np



conn= sqlite3.connect('vecotr-db.db')

cursor =conn.cursor()

#create a VECTOR tables
cursor.execute(
    """CREATE TABLE IF NOT EXISTS vectorstbl(
        id INTEGER PRIMARY KEY,
        vector BLOB NOT NULL)
    """
)

#generate some sample vectore

vect1=np.array([1.2,3.4,2.1,0.8])
vect2=np.array([2.7,1.5,3.9,2.3])
# numpy array to bytestream
# print(vect1.tobytes())
# print(vect2.tobytes())

#insert vector data in the tbale
# cursor.execute(
#     "INSERT INTO vectorstbl (vector) VALUES (?)",
#     (sqlite3.Binary(vect1.tobytes()),))
# cursor.execute(
#     "INSERT INTO vectorstbl (vector) VALUES (?)",
#     (sqlite3.Binary(vect2.tobytes()), ))

#retrieve 
cursor.execute(
    "SELECT vector FROM vectorstbl"
)
rows =cursor.fetchall()
print(rows)
print ("=================")

#deserialize
#vector = np.frombuffer(rows[1][0], dtype=np.float64)
vectors=[]
for row in rows:
    vector=np.frombuffer(row[0],dtype=np.float64)
    vectors.append(vector)
    
print(vectors)


#VECTOR SIMILARITY SEARCH - SQLITE IS NOT FOR SIMILARITY SEARCH , BUT LEVERAG TO DO FOR UNDERSATDNING
query_vector=(np.array([1.2,3.4,3.9,0.8]))

#TO FIND THE CLOSES VECCTOR FOR UNDERSATDNING - abs to calculate absolute distance.
cursor.execute(
    "SELECT vector FROM vectorstbl ORDER BY abs(vector- ?) ASC",(sqlite3.Binary(query_vector.tobytes()),))

closestvectorresult=cursor.fetchone()

closestvector=np.frombuffer(closestvectorresult[0], dtype=np.float64)

print(closestvector)

conn.commit()
conn.close()
