from Data.Conexion import Conexion

class Plan_Estudios_Curso:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Plan_Estudios_Curso, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._PlanDeEstudiosID = None
        self._CursoID = None
        self._conexion = Conexion()

    @property
    def PlanDeEstudiosID(self):
        return self._PlanDeEstudiosID

    @PlanDeEstudiosID.setter
    def PlanDeEstudiosID(self, value):
        if isinstance(value, int):
            self._PlanDeEstudiosID = value
        else:
            raise ValueError("PlanDeEstudiosID debe ser un valor entero.")
        
    @property
    def CursoID(self):
        return self._CursoID

    @CursoID.setter
    def CursoID(self, value):
        if isinstance(value, int):
            self._CursoID = value
        else:
            raise ValueError("CursoID debe ser un valor entero.")

    def create_plan_estudios_curso(self, plan_estudios_curso):
        conn = self._conexion._connection
        query = "INSERT INTO PlanDeEstudios_Curso (PlanDeEstudiosID, CursoID) VALUES (?, ?)"
        values = (
            plan_estudios_curso['PlanDeEstudiosID'],
            plan_estudios_curso['CursoID']
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_plan_estudios_curso(self):
        conn = self._conexion._connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PlanDeEstudios_Curso")
        planes_estudios_curso = cursor.fetchall()
        cursor.close()

        return planes_estudios_curso

    def update_plan_estudios_curso(self, plan_estudios_curso):
        conn = self._conexion._connection
        query = "UPDATE PlanDeEstudios_Curso SET PlanDeEstudiosID=? WHERE CursoID=?"
        values = (
            plan_estudios_curso['PlanDeEstudiosID'],
            plan_estudios_curso['CursoID']
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_plan_estudios_curso(self, plan_estudios_id, curso_id):
        conn = self._conexion._connection
        query = "DELETE FROM PlanDeEstudios_Curso WHERE PlanDeEstudiosID=? AND CursoID=?"
        values = (plan_estudios_id, curso_id)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()




