from Logic import Student, Profesor, Curso, Matricula, Plan_de_Estudio, Plan_Estudios_Curso

# Funciones de los menus principales

def mostrar_menu_principal():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Estudiantes")
    print("2. Profesores")
    print("3. Cursos")
    print("4. Matriculas")
    print("5. Plan de Estudios")
    print("6. Plan de Estudio Curso")
    print("0. Salir")

def mostrar_menu_estudiantes():
    print("\n===== MENÚ ESTUDIANTES =====")
    print("1. Agregar Estudiante")
    print("2. Listar Estudiantes")
    print("3. Actualizar Estudiante")
    print("4. Eliminar Estudiante")
    print("0. Volver al Menú Principal\n")

def mostrar_menu_profesores():
    print("\n===== MENÚ PROFESORES =====")
    print("1. Agregar Profesor")
    print("2. Listar Profesores")
    print("3. Actualizar Profesor")
    print("4. Eliminar Profesor")
    print("0. Volver al Menú Principal\n")

def mostrar_menu_cursos():
    print("\n===== MENÚ CURSOS =====")
    print("1. Agregar Curso")
    print("2. Listar Cursos")
    print("3. Actualizar Curso")
    print("4. Eliminar Curso")
    print("0. Volver al Menú Principal\n")

def mostrar_menu_matriculas():
    print("\n===== MENÚ MATRICULAS =====")
    print("1. Agregar Matricula")
    print("2. Listar Matriculas")
    print("3. Actualizar Matricula")
    print("4. Eliminar Matricula")
    print("0. Volver al Menú Principal\n")

def mostrar_menu_plan_estudios():
    print("\n===== MENÚ PLAN DE ESTUDIOS =====")
    print("1. Agregar Plan de Estudios")
    print("2. Listar Planes de Estudios")
    print("3. Actualizar Plan de Estudios")
    print("4. Eliminar Plan de Estudios")
    print("0. Volver al Menú Principal\n")

def mostrar_menu_plan_estudio_curso():
    print("\n===== MENÚ PLAN DE ESTUDIO CURSO =====")
    print("1. Agregar Curso al Plan de Estudio")
    print("2. Listar Cursos del Plan de Estudio")
    print("3. Actualizar Plan de Estudios")
    print("4. Eliminar Curso del Plan de Estudio")
    print("0. Volver al Menú Principal\n")

# Función para ejecutar el menú principal

def ejecutar_menu_principal():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Ingrese la opción deseada: ")

        if opcion_principal == "1":
            ejecutar_menu_estudiantes()
        elif opcion_principal == "2":
            ejecutar_menu_profesores()
        elif opcion_principal == "3":
            ejecutar_menu_cursos()
        elif opcion_principal == "4":
            ejecutar_menu_matriculas()
        elif opcion_principal == "5":
            ejecutar_menu_plan_estudios()
        elif opcion_principal == "6":
            ejecutar_menu_plan_estudio_curso()
        elif opcion_principal == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Funciones para ejecutar los submenús

def ejecutar_menu_estudiantes():
    while True:
        mostrar_menu_estudiantes()
        opcion_estudiantes = input("Ingrese la opción deseada: ")

        if opcion_estudiantes == "1":
            agregar_estudiante()
        elif opcion_estudiantes == "2":
            listar_estudiantes()
        elif opcion_estudiantes == "3":
            actualizar_estudiante()
        elif opcion_estudiantes == "4":
            eliminar_estudiante()
        elif opcion_estudiantes == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_estudiante():
    nuevo_estudiante = {
        'ID_Estudiante'     : int(input("Ingrese el ID del estudiante:\n")),
        'NombreCompleto'    : input("Ingrese el nombre completo del estudiante:\n"),
        'FechaNacimiento'   : input("Ingrese la fecha de nacimiento del estudiante (YYYY-MM-DD):\n"),
        'Genero'            : input("Ingrese el género del estudiante:\n"),
        'Direccion'         : input("Ingrese la dirección del estudiante:\n"),
        'CorreoElectronico' : input("Ingrese el correo electrónico del estudiante:\n"),
        'TelefonoContacto'  : input("Ingrese el teléfono de contacto del estudiante:\n"),
        'CarreraPrograma'   : input("Ingrese la carrera o programa del estudiante:\n"),
        'AnioIngreso'       : int(input("Ingrese el año de ingreso del estudiante:\n"))
    }
    Student.create_student(nuevo_estudiante)
    print("Estudiante agregado exitosamente.")

def listar_estudiantes():
    estudiantes = Student.read_student()
    for estudiante in estudiantes:
        print(estudiante)

def actualizar_estudiante():
    id_estudiante = int(input("Ingrese el ID del estudiante que desea actualizar: "))
    # Lógica para obtener los datos del estudiante con el ID dado y mostrarlos al usuario
    # Luego, pedir al usuario que ingrese los nuevos datos y actualizar el estudiante en la base de datos
    estudiante_actualizado = {
        'ID_Estudiante'     : id_estudiante,
        'NombreCompleto'    : input("Ingrese el nombre completo del estudiante:\n"),
        'FechaNacimiento'   : input("Ingrese la fecha de nacimiento del estudiante (YYYY-MM-DD):\n"),
        'Genero'            : input("Ingrese el género del estudiante:\n"),
        'Direccion'         : input("Ingrese la dirección del estudiante:\n"),
        'CorreoElectronico' : input("Ingrese el correo electrónico del estudiante:\n"),
        'TelefonoContacto'  : input("Ingrese el teléfono de contacto del estudiante:\n"),
        'CarreraPrograma'   : input("Ingrese la carrera o programa del estudiante:\n"),
        'AnioIngreso'       : int(input("Ingrese el año de ingreso del estudiante:\n"))
    }
    Student.update_student(estudiante_actualizado)
    print("Estudiante actualizado exitosamente.")

def eliminar_estudiante():
    id_estudiante = int(input("Ingrese el ID del estudiante que desea eliminar: "))
    Student.delete_student(id_estudiante)
    print("Estudiante eliminado exitosamente.")

### PROFESOR ###

def ejecutar_menu_profesores():

    while True:
        mostrar_menu_profesores()
        opcion_profesor = input("Ingrese la opción deseada: ")

        if opcion_profesor == "1":
            agregar_profesor()
        elif opcion_profesor == "2":
            listar_profesor()
        elif opcion_profesor == "3":
            actualizar_profesor()
        elif opcion_profesor == "4":
            eliminar_profesor()
        elif opcion_profesor == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_profesor():
    nuevo_profesor = {
        'ID_Profesor'         : int(input("Ingrese el ID del profesor:\n")),
        'NombreCompleto'      : input("Ingrese el nombre completo del profesor:\n"),
        'FechaNacimiento'     : input("Ingrese la fecha de nacimiento del profesor (YYYY-MM-DD):\n"),
        'Genero'              : input("Ingrese el género del profesor:\n"),
        'Direccion'           : input("Ingrese la dirección del profesor:\n"),
        'CorreoElectronico'   : input("Ingrese el correo electrónico del profesor:\n"),
        'TelefonoContacto'    : input("Ingrese el teléfono de contacto del profesor:\n"),
        'AreaEspecializacion' : input("Ingrese la carrera o programa del profesor:\n"),
    }
    Profesor.create_profesor(nuevo_profesor)
    print("Profesor agregado exitosamente.")

def listar_profesor():
    profesores = Profesor.read_profesor()
    for profe in profesores:
        print(profe)

def actualizar_profesor():
    id_profesor = int(input("Ingrese el ID del profesor que desea actualizar:\n"))
    profesor_actualizado = {
        'ID_Profesor'           : id_profesor,
        'NombreCompleto'        : input("Ingrese el nombre completo del profesor:\n"),
        'FechaNacimiento'       : input("Ingrese la fecha de nacimiento del profesor (YYYY-MM-DD):\n"),
        'Genero'                : input("Ingrese el género del profesor:\n"),
        'Direccion'             : input("Ingrese la dirección del profesor:\n"),
        'CorreoElectronico'     : input("Ingrese el correo electrónico del profesor:\n"),
        'TelefonoContacto'      : input("Ingrese el teléfono de contacto del profesor:\n"),
        'AreaEspecializacion'   : input("Ingrese el área de especialización del profesor:\n")
    }
    Profesor.update_profesor(profesor_actualizado)
    print("Profesor actualizado exitosamente.")

def eliminar_profesor():
    id_profesor = int(input("Ingrese el ID del profesor que desea eliminar: "))
    Profesor.delete_profesor(id_profesor)
    print("Profesor eliminado exitosamente.")

### CURSO ###

def ejecutar_menu_cursos():
    
    while True:
        mostrar_menu_cursos()
        opcion_curso = input("Ingrese la opción deseada: ")

        if opcion_curso == "1":
            agregar_curso()
        elif opcion_curso == "2":
            listar_curso()
        elif opcion_curso == "3":
            actualizar_curso()
        elif opcion_curso == "4":
            eliminar_curso()
        elif opcion_curso == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_curso():
    nuevo_curso = {

        'ID_Curso'          : int(input("Ingrese el ID del curso:\n")),
        'NombreCurso'       : input("Ingrese el nombre del curso:\n"),
        'CodigoCurso'       : input("Ingrese el codigo del curso:\n"),
        'DescripcionCurso'  : input("Ingrese la descripcion del curso:\n"),
        'Creditos'          : int(input("Ingrese los creditos del curso:\n")),
        'HorarioCurso'      : input("Ingrese el horario del curso:\n"),
        'ProfesorAsignado'  : input("Ingrese el profesor asignado al curso:\n")
    }
    Curso.create_curso(nuevo_curso)
    print("Curso agregado exitosamente")

def listar_curso():
    cursos = Curso.read_curso()
    for curso in cursos:
        print(curso)

def actualizar_curso():
    id_curso = int(input("Ingrese el ID del curso que desea actualizar:\n"))
    curso_actualizado = {

        'ID_Curso'          : id_curso,
        'NombreCurso'       : input("Ingrese el nombre del curso:\n"),
        'CodigoCurso'       : input("Ingrese el codigo del curso:\n"),
        'DescripcionCurso'  : input("Ingrese la descripcion del curso:\n"),
        'Creditos'          : int(input("Ingrese los creditos del curso:\n")),
        'HorarioCurso'      : input("Ingrese el horario del curso:\n"),
        'ProfesorAsignado'  : input("Ingrese el profesor asignado al curso:\n")
    }
    Curso.update_curso(curso_actualizado)
    print("Curso actualizado exitosamente.")

def eliminar_curso():
    id_curso = int(input("Ingrese el ID del curso que desea eliminar:\n"))
    Curso.delete_curso(id_curso)
    print("Curso eliminado exitosamente")

### MATRICULA ###
def ejecutar_menu_matriculas():
    while True:
        mostrar_menu_matriculas()
        opcion_matriculas = input("Ingrese la opción deseada: ")

        if opcion_matriculas == "1":
            agregar_matricula()
        elif opcion_matriculas == "2":
            listar_martricula()
        elif opcion_matriculas == "3":
            actualizar_matricula()
        elif opcion_matriculas == "4":
            eliminar_matricula()
        elif opcion_matriculas == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_matricula():
    nueva_matricula = {
        'ID_Matricula'          : int(input("Ingrese el ID de la matrícula:\n")),
        'EstudianteID'          : int(input("Ingrese el ID del estudiante:\n")),
        'CursoID'               : int(input("Ingrese el ID del curso:\n")),
        'FechaMatriculacion'    : input("Ingrese la fecha de matriculación (YYYY-MM-DD):\n"),
        'EstadoMatricula'       : input("Ingrese el estado de la matrícula:\n"),
        'NotaFinal'             : float(input("Ingrese la nota final:\n"))
    }
    Matricula.create_matricula(nueva_matricula)
    print("Matrícula agregada exitosamente.")

def listar_martricula():
    matriculas = Matricula.read_matricula()
    for matricula in matriculas:
        print(matricula)

def actualizar_matricula():
    id_matricula = int(input("Ingrese el ID de la matrícula que desea actualizar: "))
    matricula_actualizada = {
        'ID_Matricula'          : id_matricula,
        'EstudianteID'          : int(input("Ingrese el ID del estudiante:\n")),
        'CursoID'               : int(input("Ingrese el ID del curso:\n")),
        'FechaMatriculacion'    : input("Ingrese la fecha de matriculación (YYYY-MM-DD):\n"),
        'EstadoMatricula'       : input("Ingrese el estado de la matrícula:\n"),
        'NotaFinal'             : float(input("Ingrese la nota final:\n"))
    }
    Matricula.update_matricula(matricula_actualizada)
    print("Matrícula actualizada exitosamente.")

def eliminar_matricula():
    id_matricula = int(input("Ingrese el ID de la matrícula que desea eliminar: "))
    Matricula.delete_matricula(id_matricula)
    print("Matrícula eliminada exitosamente.")


### PLAN DE ESTUDIOS ###

def ejecutar_menu_plan_estudios():
    while True:
        mostrar_menu_plan_estudios()
        opcion_plan_estudios = input("Ingrese la opción deseada: ")

        if opcion_plan_estudios == "1":
            agregar_plan_de_estudio()
        elif opcion_plan_estudios == "2":
            listar_plan_de_estudios()
        elif opcion_plan_estudios == "3":
            actualizar_plan_de_estudio()
        elif opcion_plan_estudios == "4":
            eliminar_plan_de_estudio()
        elif opcion_plan_estudios == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_plan_de_estudio():
    nuevo_plan_estudio = {
        'ID_PlanDeEstudios'         : int(input("Ingrese el ID del plan de estudios:\n")),
        'CarreraProgramaAsociado'   : input("Ingrese la carrera o programa asociado al plan de estudios:\n")
    }
    Plan_de_Estudio.create_plan_estudio(nuevo_plan_estudio)
    print("Plan de estudios agregado exitosamente.")

def listar_plan_de_estudios():
    planes_de_estudios = Plan_de_Estudio.read_plan_estudios()
    for plan_estudio in planes_de_estudios:
        print(plan_estudio)

def actualizar_plan_de_estudio():
    id_plan_estudio = int(input("Ingrese el ID del plan de estudios que desea actualizar: \n"))
    plan_estudio_actualizado = {
        'ID_PlanDeEstudios'         : id_plan_estudio,
        'CarreraProgramaAsociado'   : input("Ingrese la carrera o programa asociado al plan de estudios:\n")
    }
    Plan_de_Estudio.update_plan_estudio(plan_estudio_actualizado)
    print("Plan de estudios actualizado exitosamente.")

def eliminar_plan_de_estudio():
    id_plan_estudio = int(input("Ingrese el ID del plan de estudios que desea eliminar: "))
    Plan_de_Estudio.delete_plan_estudio(id_plan_estudio)
    print("Plan de estudios eliminado exitosamente.")

### PLAN DE ESTUDIO CURSO ###

def ejecutar_menu_plan_estudio_curso():
    while True:
        mostrar_menu_plan_estudio_curso()
        opcion_plan_estudio_curso = input("Ingrese la opción deseada: ")

        if opcion_plan_estudio_curso == "1":
            agregar_plan_estudio_curso()
        elif opcion_plan_estudio_curso == "2":
            listar_plan_estudios_curso()
        elif opcion_plan_estudio_curso == "3":
            actualizar_plan_estudios_curso()
        elif opcion_plan_estudio_curso == "4":
            eliminar_plan_estudio_curso()
        elif opcion_plan_estudio_curso == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def agregar_plan_estudio_curso():
    nuevo_plan_estudio_curso = {
        'PlanDeEstudiosID'  : int(input("Ingrese el ID del plan de estudios: \n")),
        'CursoID'           : int(input("Ingrese el ID del curso: \n"))
    }
    Plan_Estudios_Curso.create_plan_estudio_curso(nuevo_plan_estudio_curso)
    print("Relación Plan de Estudio - Curso agregada exitosamente.")

def listar_plan_estudios_curso():
    plan_estudios_cursos = Plan_Estudios_Curso.read_plan_estudios_curso()
    for plan_estudio_cursos in plan_estudios_cursos:
        print(plan_estudio_cursos)

def actualizar_plan_estudios_curso():
    id_plan_estudio_curso = int(input("Ingrese el ID del plan de estudio y curso que desea actualizar:\n"))
    plan_estudio_curso_actualizado ={
        'PlanDeEstudiosID'  : id_plan_estudio_curso,
        'CursoID'           : int(input("Ingrese el ID del curso asociado al plan de estudio:\n"))
    }
    Plan_Estudios_Curso.update_plan_estudios_curso(plan_estudio_curso_actualizado)
    print("Plan de estudio por curso actualizado exitosamente")

def eliminar_plan_estudio_curso():
    id_plan_estudio = int(input("Ingrese el ID del plan de estudios: "))
    id_curso = int(input("Ingrese el ID del curso: "))
    Plan_Estudios_Curso.delete_plan_estudio_curso(id_plan_estudio, id_curso)
    print("Relación Plan de Estudio - Curso eliminada exitosamente.")

# Ejecucion del Codigo 

if __name__ == "__main__":
    ejecutar_menu_principal()

