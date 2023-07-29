import pyodbc

try:
    # Reemplaza 'nombre_servidor', 'usuario', 'contraseña' y 'Matricula_UJCV' con los valores correctos
    connection = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=JM\SQLEXPRESS;'
        'Database=Matricula_UJCV;'
        'UID=javi;'
        'PWD=1234;'
    )

    # Si la conexión es exitosa, puedes realizar operaciones en la base de datos aquí.

    #connection.close()

except pyodbc.Error as error:
    print("Error al conectar con SQL Server:", error)


