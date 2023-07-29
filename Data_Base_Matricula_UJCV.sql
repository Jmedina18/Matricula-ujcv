-- Creación de la base de datos
CREATE DATABASE Matricula_UJCV;

-- Uso de la base de datos
USE Matricula_UJCV;

-- Tabla Estudiante
CREATE TABLE Estudiante (
  ID_Estudiante INT PRIMARY KEY,
  NombreCompleto VARCHAR(100),
  FechaNacimiento DATE,
  Genero VARCHAR(10),
  Direccion VARCHAR(200),
  CorreoElectronico VARCHAR(100),
  TelefonoContacto VARCHAR(20),
  CarreraPrograma VARCHAR(100),
  AnioIngreso INT
);

-- Tabla Curso
CREATE TABLE Curso (
  ID_Curso INT PRIMARY KEY,
  NombreCurso VARCHAR(100),
  CodigoCurso VARCHAR(20),
  DescripcionCurso VARCHAR(200),
  Creditos INT,
  HorarioCurso VARCHAR(100),
  ProfesorAsignado VARCHAR(100)
);

-- Tabla Profesor
CREATE TABLE Profesor (
  ID_Profesor INT PRIMARY KEY,
  NombreCompleto VARCHAR(100),
  FechaNacimiento DATE,
  Genero VARCHAR(10),
  Direccion VARCHAR(200),
  CorreoElectronico VARCHAR(100),
  TelefonoContacto VARCHAR(20),
  AreaEspecializacion VARCHAR(100)
);

-- Tabla Matricula
CREATE TABLE Matricula (
  ID_Matricula INT PRIMARY KEY,
  EstudianteID INT,
  CursoID INT,
  FechaMatriculacion DATE,
  EstadoMatricula VARCHAR(20),
  NotaFinal DECIMAL(4, 2),
  FOREIGN KEY (EstudianteID) REFERENCES Estudiante(ID_Estudiante),
  FOREIGN KEY (CursoID) REFERENCES Curso(ID_Curso)
);

-- Tabla Plan de Estudios
CREATE TABLE PlanDeEstudios (
  ID_PlanDeEstudios INT PRIMARY KEY,
  CarreraProgramaAsociado VARCHAR(100)
);

-- Tabla de Relación entre Plan de Estudios y Curso
CREATE TABLE PlanDeEstudios_Curso (
  PlanDeEstudiosID INT,
  CursoID INT,
  PRIMARY KEY (PlanDeEstudiosID, CursoID),
  FOREIGN KEY (PlanDeEstudiosID) REFERENCES PlanDeEstudios(ID_PlanDeEstudios),
  FOREIGN KEY (CursoID) REFERENCES Curso(ID_Curso)
);