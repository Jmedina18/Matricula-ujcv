from Data.Conexion import connection

def create_matricula(matricula):
    query = "INSERT INTO Matricula (ID_Matricula, EstudianteID, CursoID, FechaMatriculacion, EstadoMatricula, NotaFinal) VALUES (?, ?, ?, ?, ?, ?)"
    values = (
        matricula['ID_Matricula'],
        matricula['EstudianteID'],
        matricula['CursoID'],
        matricula['FechaMatriculacion'],
        matricula['EstadoMatricula'],
        matricula['NotaFinal']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def read_matricula():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Matricula")
    matriculas = cursor.fetchall()
    return matriculas

def update_matricula(matricula):
    query = "UPDATE Matricula SET EstudianteID=?, CursoID=?, FechaMatriculacion=?, EstadoMatricula=?, NotaFinal=? WHERE ID_Matricula=?"
    values = (
        matricula['EstudianteID'],
        matricula['CursoID'],
        matricula['FechaMatriculacion'],
        matricula['EstadoMatricula'],
        matricula['NotaFinal'],
        matricula['ID_Matricula']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def delete_matricula(id_matricula):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Matricula WHERE ID_Matricula=?", id_matricula)
    connection.commit()
    cursor.close()
