import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", 
passwd="", database="sidico"
)
#print(cnn)

cur = cnn.cursor()
cur.execute("SELECT * FROM parabot ")
datos = cur.fetchall()
for fila in datos:
    print(fila)
