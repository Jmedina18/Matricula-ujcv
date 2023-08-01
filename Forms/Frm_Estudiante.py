import tkinter as tk
from Logic.Student import Student

def guardar_estudiante():
    nuevo_estudiante = {
        'ID_Estudiante': int(entry_id.get()),
        'NombreCompleto': entry_nombre.get(),
        'FechaNacimiento': entry_fecha_nacimiento.get(),
        'Genero': entry_genero.get(),
        'Direccion': entry_direccion.get(),
        'CorreoElectronico': entry_correo.get(),
        'TelefonoContacto': entry_telefono.get(),
        'CarreraPrograma': entry_carrera.get(),
        'AnioIngreso': int(entry_anio_ingreso.get())
    }
    Student.create_student(nuevo_estudiante)
    status_label.config(text="Estudiante agregado exitosamente.")

def listar_estudiantes():
    estudiantes = Student.read_student()
    output_text.delete(1.0, tk.END)
    for estudiante in estudiantes:
        output_text.insert(tk.END, f"{estudiante}\n")

def editar_estudiante():
    id_estudiante = int(entry_id.get())
    estudiante_actualizado = {
        'ID_Estudiante': id_estudiante,
        'NombreCompleto': entry_nombre.get(),
        'FechaNacimiento': entry_fecha_nacimiento.get(),
        'Genero': entry_genero.get(),
        'Direccion': entry_direccion.get(),
        'CorreoElectronico': entry_correo.get(),
        'TelefonoContacto': entry_telefono.get(),
        'CarreraPrograma': entry_carrera.get(),
        'AnioIngreso': int(entry_anio_ingreso.get())
    }
    Student.update_student(estudiante_actualizado)
    status_label.config(text="Estudiante actualizado exitosamente.")

def eliminar_estudiante():
    id_estudiante = int(entry_id.get())
    Student.delete_student(id_estudiante)
    status_label.config(text="Estudiante eliminado exitosamente.")

# Crear ventana principal
root = tk.Tk()
root.title("Formulario Estudiante")

# Crear campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

# Crear más campos de entrada para los demás atributos del estudiante...

# Botones
boton_guardar = tk.Button(root, text="Guardar", command=guardar_estudiante)
boton_guardar.grid(row=10, column=0, padx=10, pady=5)
boton_listar = tk.Button(root, text="Listar", command=listar_estudiantes)
boton_listar.grid(row=10, column=1, padx=10, pady=5)
boton_editar = tk.Button(root, text="Editar", command=editar_estudiante)
boton_editar.grid(row=10, column=2, padx=10, pady=5)
boton_eliminar = tk.Button(root, text="Eliminar", command=eliminar_estudiante)
boton_eliminar.grid(row=10, column=3, padx=10, pady=5)

# Área de salida para mostrar los estudiantes listados
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=11, column=0, columnspan=4, padx=10, pady=5)

# Etiqueta para mostrar el estado del proceso
status_label = tk.Label(root, text="")
status_label.grid(row=12, column=0, columnspan=4)

root.mainloop()
