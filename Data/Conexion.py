import pyodbc

# try:
#     # Reemplaza 'nombre_servidor', 'usuario', 'contraseña' y 'Matricula_UJCV' con los valores correctos
#     connection = pyodbc.connect(
#         'Driver={SQL Server};'
#         'Server=JM\SQLEXPRESS;'
#         'Database=Matricula_UJCV;'
#         'UID=javi;'
#         'PWD=1234;'
#     )

#     # Si la conexión es exitosa, puedes realizar operaciones en la base de datos aquí.

#     #connection.close()

# except pyodbc.Error as error:
#     print("Error al conectar con SQL Server:", error)


import pyodbc

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        server = 'JM\\SQLEXPRESS'  # Reemplazar con el nombre de tu servidor SQL
        database = 'Matricula_UJCV'  # Reemplazar con el nombre de tu base de datos
        username = 'javi'  # Reemplazar con tu nombre de usuario
        password = '1234'  # Reemplazar con tu contraseña
        driver = '{SQL Server}'  # ODBC Driver para SQL Server

        # Cadena de conexión
        connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        try:
            self._connection = pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            raise ConnectionError("Error al conectar a la base de datos SQL Server" + str(e)) from e

    @property
    def connection(self):
        return self._connection

    def execute_query(self, query, values=None):
        cursor = self._connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        self._connection.commit()
        cursor.close()

    def fetch_data(self, query, values=None):
        cursor = self._connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
def test_database_connection():
    try:
        # Crear una instancia de la clase Conexion
        conexion = Conexion()

        # Ejecutar una consulta simple para obtener la versión del servidor de base de datos
        query = "SELECT @@VERSION"
        data = conexion.fetch_data(query)

        # Mostrar la versión del servidor
        print("Versión del servidor de base de datos:", data[0][0])
        print("La conexión a la base de datos funciona correctamente.")
    except Exception as e:
        print("Error al conectar a la base de datos:", str(e))

if __name__ == "__main__":
    test_database_connection()