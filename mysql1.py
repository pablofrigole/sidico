import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", 
passwd="", database="prueba"
)
#print(cnn)

cur = cnn.cursor()
cur.execute("SELECT * FROM datosnombre WHERE nombre='PAblo' ")
datos = cur.fetchall()
for fila in datos:
    print(fila)