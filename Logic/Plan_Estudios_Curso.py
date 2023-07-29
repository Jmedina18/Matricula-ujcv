from Data.Conexion import connection

def create_plan_estudios_curso(plan_estudios_curso):
    query = "INSERT INTO PlanDeEstudios_Curso (PlanDeEstudiosID, CursoID) VALUES (?, ?)"
    values = (
        plan_estudios_curso['PlanDeEstudiosID'],
        plan_estudios_curso['CursoID']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def read_plan_estudios_curso():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PlanDeEstudios_Curso")
    planes_estudios_curso = cursor.fetchall()
    return planes_estudios_curso

def update_plan_estudios_curso(plan_estudios_curso_actualizado):
    query = "UPDATE PlanDeEstudios_Curso SET CursoID=? WHERE PlanDeEstudiosID=?"
    values = (
        plan_estudios_curso_actualizado['CursoID'],
        plan_estudios_curso_actualizado['PlanDeEstudiosID']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()


def delete_plan_estudios_curso(plan_estudios_id, curso_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PlanDeEstudios_Curso WHERE PlanDeEstudiosID=? AND CursoID=?", (plan_estudios_id, curso_id))
    connection.commit()
    cursor.close()
