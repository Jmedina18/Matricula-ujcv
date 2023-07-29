from Data.Conexion import connection

def create_curso(curso):
    query = "INSERT INTO Curso (ID_Curso, NombreCurso, CodigoCurso, DescripcionCurso, Creditos, HorarioCurso, ProfesorAsignado) VALUES (?, ?, ?, ?, ?, ?, ?)"
    values = (
        curso['ID_Curso'],
        curso['NombreCurso'],
        curso['CodigoCurso'],
        curso['DescripcionCurso'],
        curso['Creditos'],
        curso['HorarioCurso'],
        curso['ProfesorAsignado']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def read_curso():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Curso")
    cursos = cursor.fetchall()
    return cursos

def update_curso(curso):
    query = "UPDATE Curso SET NombreCurso=?, CodigoCurso=?, DescripcionCurso=?, Creditos=?, HorarioCurso=?, ProfesorAsignado=? WHERE ID_Curso=?"
    values = (
        curso['NombreCurso'],
        curso['CodigoCurso'],
        curso['DescripcionCurso'],
        curso['Creditos'],
        curso['HorarioCurso'],
        curso['ProfesorAsignado'],
        curso['ID_Curso']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def delete_curso(id_curso):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Curso WHERE ID_Curso=?", id_curso)
    connection.commit()
    cursor.close()
