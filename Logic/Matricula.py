from Data.Conexion import Conexion

class Matricula:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Matricula, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._ID_Matricula = None
        self._EstudianteID = None
        self._CursoID = None
        self._FechaMatricula = None
        self._EstadoMatricula = None  
        self._NotaFinal = None  
        self._conexion = Conexion()

    @property
    def ID_Matricula(self):
        return self._ID_Matricula

    @ID_Matricula.setter
    def ID_Matricula(self, value):
        if isinstance(value, int):
            self._ID_Matricula = value
        else:
            raise ValueError("ID_Matricula debe ser un valor entero.")

    @property
    def EstudianteID(self):
        return self._EstudianteID

    @EstudianteID.setter
    def EstudianteID(self, value):
        if isinstance(value, int):
            self._EstudianteID = value
        else:
            raise ValueError("EstudianteID debe ser un valor entero.")

    @property
    def CursoID(self):
        return self._CursoID

    @CursoID.setter
    def CursoID(self, value):
        if isinstance(value, int):
            self._CursoID = value
        else:
            raise ValueError("CursoID debe ser un valor entero.")

    @property
    def FechaMatricula(self):
        return self._FechaMatricula

    @FechaMatricula.setter
    def FechaMatricula(self, value):
        if isinstance(value, str):
            self._FechaMatricula = value
        else:
            raise ValueError("FechaMatricula debe ser una cadena de texto.")

    @property
    def EstadoMatricula(self):
        return self._EstadoMatricula

    @EstadoMatricula.setter
    def EstadoMatricula(self, value):
        if isinstance(value, str):
            self._EstadoMatricula = value
        else:
            raise ValueError("EstadoMatricula debe ser una cadena de texto.")

    @property
    def NotaFinal(self):
        return self._NotaFinal

    @NotaFinal.setter
    def NotaFinal(self, value):
        if isinstance(value, float):
            self._NotaFinal = value
        else:
            raise ValueError("NotaFinal debe ser un valor decimal (float).")

    def create_matricula(self, matricula):
        conn = self._conexion._connection
        query = "INSERT INTO Matricula (ID_Matricula, EstudianteID, CursoID, FechaMatriculacion, EstadoMatricula, NotaFinal) VALUES (?, ?, ?, ?, ?, ?)"
        values = (
            matricula.ID_Matricula,
            matricula.EstudianteID,
            matricula.CursoID,
            matricula.FechaMatricula,
            matricula.EstadoMatricula,
            matricula.NotaFinal
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_matricula(self):
        conn = self._conexion._connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Matricula")
        matriculas = cursor.fetchall()
        cursor.close()

        return matriculas

    def update_matricula(self, matricula):
        conn = self._conexion._connection
        query = "UPDATE Matricula SET EstudianteID=?, CursoID=?, FechaMatriculacion=?, EstadoMatricula=?, NotaFinal=? WHERE ID_Matricula=?"
        values = (
            matricula.EstudianteID,
            matricula.CursoID,
            matricula.FechaMatricula,
            matricula.EstadoMatricula,
            matricula.NotaFinal,
            matricula.ID_Matricula
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_matricula(self, id_matricula):
        conn = self._conexion._connection
        query = "DELETE FROM Matricula WHERE ID_Matricula=?"
        values = (id_matricula,)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
