from Data.Conexion import Conexion

class Plan_de_Estudio:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Plan_de_Estudio, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._ID_PlanDeEstudios = None
        self._NombrePlanEstudio = None
        self._FechaAprobacion = None
        self._conexion = Conexion()

    @property
    def ID_PlanEstudio(self):
        return self._ID_PlanEstudio

    @ID_PlanEstudio.setter
    def ID_PlanEstudio(self, value):
        if isinstance(value, int):
            self._ID_PlanEstudio = value
        else:
            raise ValueError("ID_PlanDeEstudios debe ser un valor entero.")

    @property
    def NombrePlanEstudio(self):
        return self._NombrePlanEstudio

    @NombrePlanEstudio.setter
    def NombrePlanEstudio(self, value):
        if isinstance(value, str):
            self._NombrePlanEstudio = value
        else:
            raise ValueError("NombrePlanEstudio debe ser una cadena de texto.")

    @property
    def FechaAprobacion(self):
        return self._FechaAprobacion

    @FechaAprobacion.setter
    def FechaAprobacion(self, value):
        if isinstance(value, str):
            self._FechaAprobacion = value
        else:
            raise ValueError("FechaAprobacion debe ser una cadena de texto.")


    def create_plan_estudio(self, plan_estudio):
        conn = self._conexion._connection

        query = "INSERT INTO PlanDeEstudios (ID_PlanDeEstudios, NombrePlanEstudio, FechaAprobacion, ) VALUES (?, ?, ?, ?)"
        values = (
            plan_estudio.ID_PlanDeEstudios,
            plan_estudio.NombrePlanEstudio,
            plan_estudio.FechaAprobacion, 
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_plan_estudio(self):
        conn = self._conexion._connection

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PlanDeEstudios")
        planes_estudio = cursor.fetchall()
        cursor.close()

        return planes_estudio

    def update_plan_estudio(self, plan_estudio):
        conn = self._conexion._connection

        query = "UPDATE PlanDeEstudios SET NombrePlanEstudio=?, FechaAprobacion=?, =? WHERE ID_PlanDeEstudios=?"
        values = (
            plan_estudio.NombrePlanEstudio,
            plan_estudio.FechaAprobacion,
            plan_estudio.ID_PlanDeEstudios
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_plan_estudio(self, id_plan_estudio):
        conn = self._conexion._connection

        query = "DELETE FROM PlanDeEstudios WHERE ID_PlanDeEstudios=?"
        values = (id_plan_estudio,)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
