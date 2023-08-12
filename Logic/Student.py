from Data.Conexion import Conexion

class Student:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._ID_Estudiante = None
        self._NombreCompleto = None
        self._FechaNacimiento = None
        self._Genero = None
        self._Direccion = None
        self._CorreoElectronico = None
        self._TelefonoContacto = None
        self._CarreraPrograma = None
        self._AnioIngreso = None
        self._conexion = Conexion()

    @property
    def ID_Estudiante(self):
        return self._ID_Estudiante

    @ID_Estudiante.setter
    def ID_Estudiante(self, value):
        if isinstance(value, int):
            self._ID_Estudiante = value
        else:
            raise ValueError("ID_Estudiante debe ser un valor entero.")

    @property
    def NombreCompleto(self):
        return self._NombreCompleto

    @NombreCompleto.setter
    def NombreCompleto(self, value):
        if isinstance(value, str):
            self._NombreCompleto = value
        else:
            raise ValueError("NombreCompleto debe ser una cadena de texto.")

    @property
    def FechaNacimiento(self):
        return self._FechaNacimiento

    @FechaNacimiento.setter
    def FechaNacimiento(self, value):
        if isinstance(value, str):
            self._FechaNacimiento = value
        else:
            raise ValueError("FechaNacimiento debe ser una cadena de texto.")

    @property
    def Genero(self):
        return self._Genero

    @Genero.setter
    def Genero(self, value):
        if isinstance(value, str):
            self._Genero = value
        else:
            raise ValueError("Genero debe ser una cadena de texto.")

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, value):
        if isinstance(value, str):
            self._Direccion = value
        else:
            raise ValueError("Direccion debe ser una cadena de texto.")

    @property
    def CorreoElectronico(self):
        return self._CorreoElectronico

    @CorreoElectronico.setter
    def CorreoElectronico(self, value):
        if isinstance(value, str):
            self._CorreoElectronico = value
        else:
            raise ValueError("CorreoElectronico debe ser una cadena de texto.")

    @property
    def TelefonoContacto(self):
        return self._TelefonoContacto

    @TelefonoContacto.setter
    def TelefonoContacto(self, value):
        if isinstance(value, str):
            self._TelefonoContacto = value
        else:
            raise ValueError("TelefonoContacto debe ser una cadena de texto.")

    @property
    def CarreraPrograma(self):
        return self._CarreraPrograma

    @CarreraPrograma.setter
    def CarreraPrograma(self, value):
        if isinstance(value, str):
            self._CarreraPrograma = value
        else:
            raise ValueError("CarreraPrograma debe ser una cadena de texto.")

    @property
    def AnioIngreso(self):
        return self._AnioIngreso

    @AnioIngreso.setter
    def AnioIngreso(self, value):
        if isinstance(value, str):
            self._AnioIngreso = value
        else:
            raise ValueError("AnioIngreso debe ser una cadena de texto")

    def create_student(self, student):
        conn = self._conexion._connection

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

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_student(self):
        conn = self._conexion._connection

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Estudiante")
        students = cursor.fetchall()
        cursor.close()

        return students

    def update_student(self, student):
        conn = self._conexion._connection

        query = "UPDATE Estudiante SET NombreCompleto=?, FechaNacimiento=?, Genero=?, Direccion=?, CorreoElectronico=?, TelefonoContacto=?, CarreraPrograma=?, AnioIngreso=? WHERE ID_Estudiante=?"
        values = (
            student['NombreCompleto'],
            student['FechaNacimiento'],
            student['Genero'],
            student['Direccion'],
            student['CorreoElectronico'],
            student['TelefonoContacto'],
            student['CarreraPrograma'],
            student['AnioIngreso'],
            student['ID_Estudiante']
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_student(self, id_estudiante):
        conn = self._conexion._connection

        query = "DELETE FROM Estudiante WHERE ID_Estudiante=?"
        values = (id_estudiante,)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()