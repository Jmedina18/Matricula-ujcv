from Data.Conexion import Conexion

class Profesor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Profesor, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._ID_Profesor = None
        self._NombreCompleto = None
        self._FechaNacimiento = None
        self._Genero = None
        self._Direccion = None
        self._CorreoElectronico = None
        self._TelefonoContacto = None
        self._AreaEspecializacion = None
        self._FechaIngreso = None
        self._conexion = Conexion()

    @property
    def ID_Profesor(self):
        return self._ID_Profesor

    @ID_Profesor.setter
    def ID_Profesor(self, value):
        if isinstance(value, int):
            self._ID_Profesor = value
        else:
            raise ValueError("ID_Profesor debe ser un valor entero.")

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
    def AreaEspecializacion(self):
        return self._AreaEspecializacion

    @AreaEspecializacion.setter
    def AreaEspecializacion(self, value):
        if isinstance(value, str):
            self._AreaEspecializacion = value
        else:
            raise ValueError("AreaEspecializacion debe ser una cadena de texto.")

    @property
    def FechaIngreso(self):
        return self._FechaIngreso

    @FechaIngreso.setter
    def FechaIngreso(self, value):
        if isinstance(value, str):
            self._FechaIngreso = value
        else:
            raise ValueError("FechaIngreso debe ser una cadena de texto.")

    def create_profesor(self, profesor):
        conn = self._conexion._connection

        query = "INSERT INTO Profesor (ID_Profesor, NombreCompleto, FechaNacimiento, Genero, Direccion, CorreoElectronico, TelefonoContacto, AreaEspecializacion, FechaIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (
            profesor['ID_Profesor'],
            profesor['NombreCompleto'],
            profesor['FechaNacimiento'],
            profesor['Genero'],
            profesor['Direccion'],
            profesor['CorreoElectronico'],
            profesor['TelefonoContacto'],
            profesor['AreaEspecializacion'],
            profesor['FechaIngreso']
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def read_profesor(self):
        conn = self._conexion._connection

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Profesor")
        profesores = cursor.fetchall()
        cursor.close()

        return profesores

    def update_profesor(self, profesor):
        conn = self._conexion._connection

        query = "UPDATE Profesor SET NombreCompleto=?, FechaNacimiento=?, Genero=?, Direccion=?, CorreoElectronico=?, TelefonoContacto=?, AreaEspecializacion=?, FechaIngreso=? WHERE ID_Profesor=?"
        values = (
            profesor['NombreCompleto'],
            profesor['FechaNacimiento'],
            profesor['Genero'],
            profesor['Direccion'],
            profesor['CorreoElectronico'],
            profesor['TelefonoContacto'],
            profesor['AreaEspecializacion'],
            profesor['FechaIngreso'],
            profesor['ID_Profesor']
        )

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()

    def delete_profesor(self, id_profesor):
        conn = self._conexion._connection

        query = "DELETE FROM Profesor WHERE ID_Profesor=?"
        values = (id_profesor,)

        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
