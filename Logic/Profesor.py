from Data.Conexion import connection

def create_profesor(profesor):
    query = "INSERT INTO Profesor (ID_Profesor, NombreCompleto, FechaNacimiento, Genero, Direccion, CorreoElectronico, TelefonoContacto, AreaEspecializacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = (
        profesor['ID_Profesor'],
        profesor['NombreCompleto'],
        profesor['FechaNacimiento'],
        profesor['Genero'],
        profesor['Direccion'],
        profesor['CorreoElectronico'],
        profesor['TelefonoContacto'],
        profesor['AreaEspecializacion']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def read_profesor():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Profesor")
    profesores = cursor.fetchall()
    return profesores

def update_profesor(profesor):
    query = "UPDATE Profesor SET NombreCompleto=?, FechaNacimiento=?, Genero=?, Direccion=?, CorreoElectronico=?, TelefonoContacto=?, AreaEspecializacion=? WHERE ID_Profesor=?"
    values = (
        profesor['NombreCompleto'],
        profesor['FechaNacimiento'],
        profesor['Genero'],
        profesor['Direccion'],
        profesor['CorreoElectronico'],
        profesor['TelefonoContacto'],
        profesor['AreaEspecializacion'],
        profesor['ID_Profesor']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def delete_profesor(id_profesor):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Profesor WHERE ID_Profesor=?", id_profesor)
    connection.commit()
    cursor.close()
