from Data.Conexion import Conexion

class Curso:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Curso, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._ID_Curso = None
        self._NombreCurso = None
        self._CodigoCurso = None
        self._DescripcionCurso = None
        self._Creditos = None
        self._HorarioCurso = None
        self._ProfesorAsignado = None
        self._conexion = Conexion()

    @property
    def ID_Curso(self):
        return self._ID_Curso

    @ID_Curso.setter
    def ID_Curso(self, value):
        if isinstance(value, int):
            self._ID_Curso = value
        else:
            raise ValueError("ID_Curso debe ser un valor entero.")

    @property
    def NombreCurso(self):
        return self._NombreCurso

    @NombreCurso.setter
    def NombreCurso(self, value):
        if isinstance(value, str):
            self._NombreCurso = value
        else:
            raise ValueError("NombreCurso debe ser una cadena de texto.")
    
    @property
    def CodigoCurso(self):
        return self._CodigoCurso

    @CodigoCurso.setter
    def CodigoCurso(self, value):
        if isinstance(value, str):
            self._CodigoCurso = value
        else:
            raise ValueError("CodigoCurso debe ser una cadena de texto.")
    
    @property
    def DescripcionCurso(self):
        return self._DescripcionCurso

    @DescripcionCurso.setter
    def DescripcionCurso(self, value):
        if isinstance(value, str):
            self._DescripcionCurso = value
        else:
            raise ValueError("DescripcionCurso debe ser una cadena de texto.")

    @property
    def Creditos(self):
        return self._Creditos

    @Creditos.setter
    def Creditos(self, value):
        if isinstance(value, int):
            self._Creditos = value
        else:
            raise ValueError("Creditos debe ser un valor entero.")
    
    @property
    def HorarioCurso(self):
        return self._HorarioCurso

    @HorarioCurso.setter
    def HorarioCurso(self, value):
        if isinstance(value, str):
            self._HorarioCurso = value
        else:
            raise ValueError("HorarioCurso debe ser una cadena de texto.")
    
    @property
    def ProfesorAsignado(self):
        return self._ProfesorAsignado

    @ProfesorAsignado.setter
    def ProfesorAsignado(self, value):
        if isinstance(value, str):
            self._ProfesorAsignado = value
        else:
            raise ValueError("ProfesorAsignado debe ser una cadena de texto.")

    def create_curso(self, curso):
        conn = self._conexion._connection

        query = "INSERT INTO Curso (ID_Curso, NombreCurso, CodigoCurso, DescripcionCurso, Creditos, HorarioCurso, ProfesorAsignado) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (
            curso.ID_Curso,
            curso.NombreCurso,
            curso.CodigoCurso,
            curso.DescripcionCurso,
            curso.Creditos,
            curso.HorarioCurso,
            curso.ProfesorAsignado
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_curso(self):
        conn = self._conexion._connection

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Curso")
        cursos = cursor.fetchall()
        cursor.close()

        return cursos

    def update_curso(self, curso):
        conn = self._conexion._connection

        query = "UPDATE Curso SET NombreCurso=?, CodigoCurso=?, DescripcionCurso=?, Creditos=?, HorarioCurso=?, ProfesorAsignado=? WHERE ID_Curso=?"
        values = (
            curso.NombreCurso,
            curso.CodigoCurso,
            curso.DescripcionCurso,
            curso.Creditos,
            curso.HorarioCurso,
            curso.ProfesorAsignado,
            curso.ID_Curso
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_curso(self, id_curso):
        conn = self._conexion._connection

        query = "DELETE FROM Curso WHERE ID_Curso=?"
        values = (id_curso,)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
