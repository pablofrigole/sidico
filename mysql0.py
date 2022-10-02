import pymysql
class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='prueba'
    )
        self.cursor = self.connection.cursor()
    print("Conección establecida exitosamente.")
def select_user(self, id):
    sql = 'SELECT id, nombre, telefono FROM datosnombre WHERE id = {}'.format(id)

    try:
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        print("Id: ", user[0])
        print("Nombre: ", user[1])
        print("Teléfono: ", user[2])

    except Exception as e:
        raise
database = DataBase()
database.select_user(1)