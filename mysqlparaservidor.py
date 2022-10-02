import mysql.connector

cnn = mysql.connector.connect(host="107.152.39.91:3306", user="root", 
passwd="YByOScXImA9tBhwe2^", database="agenda"
)
#print(cnn)

cur = cnn.cursor()
cur.execute("SELECT * FROM usuarios WHERE username='pfrigole' ")
datos = cur.fetchall()
for fila in datos:
    print(fila)