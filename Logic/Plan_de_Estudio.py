from Data.Conexion import connection

def create_plan_estudios(plan_estudios):
    query = "INSERT INTO PlanDeEstudios (ID_PlanDeEstudios, CarreraProgramaAsociado) VALUES (?, ?)"
    values = (
        plan_estudios['ID_PlanDeEstudios'],
        plan_estudios['CarreraProgramaAsociado']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def read_plan_estudios():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PlanDeEstudios")
    planes_estudios = cursor.fetchall()
    return planes_estudios

def update_plan_estudios(plan_estudios):
    query = "UPDATE PlanDeEstudios SET CarreraProgramaAsociado=? WHERE ID_PlanDeEstudios=?"
    values = (
        plan_estudios['CarreraProgramaAsociado'],
        plan_estudios['ID_PlanDeEstudios']
    )

    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def delete_plan_estudios(id_plan_estudios):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PlanDeEstudios WHERE ID_PlanDeEstudios=?", id_plan_estudios)
    connection.commit()
    cursor.close()
