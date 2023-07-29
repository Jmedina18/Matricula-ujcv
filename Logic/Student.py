from Data.Conexion import connection

def create_student(student):
    query = "INSERT INTO Estudiante (ID_Estudiante, NombreCompleto, FechaNacimiento, Genero, Direccion, CorreoElectronico, TelefonoContacto, CarreraPrograma, AnioIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (
        student['ID_Estudiante'],
        student['NombreCompleto'],
        student['FechaNacimiento'],
        student['Genero'],
        student['Direccion'],
        student['CorreoElectronico'],
        student['TelefonoContacto'],
        student['CarreraPrograma'],
        student['AnioIngreso']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

# Métodos similares para consultar, actualizar y eliminar estudiantes.

def read_student():
   
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Estudiante")
    estudiantes = cursor.fetchall()
    return estudiantes

# Métodos similares para consultar, actualizar y eliminar cursos.

def update_student(student):
    
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE Estudiante SET NombreCompleto=?, FechaNacimiento=?, Genero=?, Direccion=?, CorreoElectronico=?, "
                       "TelefonoContacto=?, CarreraPrograma=?, AnioIngreso=? WHERE ID_Estudiante=?",
                       student['NombreCompleto'], student['FechaNacimiento'], student['Genero'],
                       student['Direccion'], student['CorreoElectronico'], student['TelefonoContacto'],
                       student['CarreraPrograma'], student['AnioIngreso'], student['ID_Estudiante'])
        connection.commit()
        print("Estudiante actualizado exitosamente.")
    except Exception as e:
        print("Error al actualizar el estudiante:", str(e))



def delete_student(id_student):

    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Estudiante WHERE ID_Estudiante=?", id_student)
        connection.commit()
        print("Estudiante eliminado exitosamente.")
    except Exception as e:
        print("Error al eliminar el estudiante:", str(e))


