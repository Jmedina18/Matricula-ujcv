import tkinter as tk
from tkinter import ttk
from Logic.Student import Student

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Estudiante")

        # Crear campos de entrada
        entry_width = 35  # Ancho de los campos de entrada
        entry_font = ('New Times Roman', 11)  # Fuente de los campos de entrada

        label_id = tk.Label(root, text="ID:")
        label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_id.grid(row=0, column=1)

        label_nombre = tk.Label(root, text="Nombre completo:")
        label_nombre.grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_nombre.grid(row=1, column=1)

        label_fecha_nacimiento = tk.Label(root, text="Fecha de nacimiento:")
        label_fecha_nacimiento.grid(row=2, column=0)
        self.entry_fecha_nacimiento = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_fecha_nacimiento.grid(row=2, column=1)

        label_genero = tk.Label(root, text="Género:")
        label_genero.grid(row=3, column=0)
        self.entry_genero = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_genero.grid(row=3, column=1)

        label_direccion = tk.Label(root, text="Dirección:")
        label_direccion.grid(row=4, column=0)
        self.entry_direccion = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_direccion.grid(row=4, column=1)

        label_correo = tk.Label(root, text="Correo electrónico:")
        label_correo.grid(row=5, column=0)
        self.entry_correo = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_correo.grid(row=5, column=1)

        label_telefono = tk.Label(root, text="Teléfono de contacto:")
        label_telefono.grid(row=6, column=0)
        self.entry_telefono = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_telefono.grid(row=6, column=1)

        label_carrera = tk.Label(root, text="Carrera o programa:")
        label_carrera.grid(row=7, column=0)
        self.entry_carrera = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_carrera.grid(row=7, column=1)

        label_anio_ingreso = tk.Label(root, text="Año de ingreso:")
        label_anio_ingreso.grid(row=8, column=0)
        self.entry_anio_ingreso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_anio_ingreso.grid(row=8, column=1)

        # Botones
        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_estudiante)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)
        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_estudiantes)
        self.boton_listar.grid(row=2, column=2, padx=10, pady=5)
        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_estudiante)
        self.boton_editar.grid(row=5, column=2, padx=10, pady=5)
        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_estudiante)
        self.boton_eliminar.grid(row=8, column=2, padx=10, pady=5)
        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_estudiante)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)

        # Botones adicionales
        self.boton_limpiar_tabla = tk.Button(root, text="Limpiar Tabla", command=self.limpiar_tabla)
        self.boton_limpiar_tabla.grid(row=2, column=3, padx=10, pady=5)

        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=5, column=3, padx=10, pady=5)

        # Área de salida para mostrar los estudiantes listados
        self.output_text = ttk.Treeview(root, columns=("ID", "Nombre", "Fecha de Nacimiento", "Género", "Dirección", "Correo Electrónico", "Teléfono de Contacto", "Carrera/Programa", "Año de Ingreso"), show="headings")
        self.output_text.grid(row=11, column=0, columnspan=4, padx=10, pady=5)

        # Configuración del ancho de las columnas
        self.output_text.column("#0", width=0)  # Ajustar el ancho de la columna de las etiquetas
        self.output_text.column("ID", width=40)  # Ajustar el ancho de la columna del ID
        self.output_text.column("Nombre", width=180)
        self.output_text.column("Fecha de Nacimiento", width=130)
        self.output_text.column("Género", width=100)
        self.output_text.column("Dirección", width=150)
        self.output_text.column("Correo Electrónico", width=180)
        self.output_text.column("Teléfono de Contacto", width=100)
        self.output_text.column("Carrera/Programa", width=180)
        self.output_text.column("Año de Ingreso", width=100)

        # Agregar el Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=11, column=4, sticky="ns")

        # Encabezados de las columnas
        self.output_text.heading("ID", text="ID")
        self.output_text.heading("Nombre", text="Nombre")
        self.output_text.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
        self.output_text.heading("Género", text="Género")
        self.output_text.heading("Dirección", text="Dirección")
        self.output_text.heading("Correo Electrónico", text="Email")
        self.output_text.heading("Teléfono de Contacto", text="Teléfono")
        self.output_text.heading("Carrera/Programa", text="Carrera")
        self.output_text.heading("Año de Ingreso", text="Año de Ingreso")

        # Etiqueta para mostrar el estado del proceso
        self.status_label = tk.Label(root, text="")
        self.status_label.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

    def guardar_estudiante(self):
        estudiante = Student()  # Crear una instancia de la clase Student
        nuevo_estudiante = {
            'ID_Estudiante': int(self.entry_id.get()),
            'NombreCompleto': self.entry_nombre.get(),
            'FechaNacimiento': self.entry_fecha_nacimiento.get(),
            'Genero': self.entry_genero.get(),
            'Direccion': self.entry_direccion.get(),
            'CorreoElectronico': self.entry_correo.get(),
            'TelefonoContacto': self.entry_telefono.get(),
            'CarreraPrograma': self.entry_carrera.get(),
            'AnioIngreso': int(self.entry_anio_ingreso.get())
        }
        estudiante.create_student(nuevo_estudiante)  # Llamar al método de instancia para crear el estudiante
        self.status_label.config(text="Estudiante agregado exitosamente.")
        self.limpiar_campos()

    def listar_estudiantes(self):
        estudiante = Student()  # Crear una instancia de la clase Student
        estudiantes = estudiante.read_student()  # Llamar al método de instancia para obtener la lista de estudiantes
        self.output_text.delete(*self.output_text.get_children())  # Limpiar la tabla antes de mostrar los datos
        for estudiante in estudiantes:
            self.output_text.insert("", "end", values=(estudiante.ID_Estudiante, estudiante.NombreCompleto, estudiante.FechaNacimiento,
                                                      estudiante.Genero, estudiante.Direccion, estudiante.CorreoElectronico,
                                                      estudiante.TelefonoContacto, estudiante.CarreraPrograma,
                                                      estudiante.AnioIngreso))

    def editar_estudiante(self):
        id_estudiante = self.entry_id.get()
        if id_estudiante:
            try:
                id_estudiante = int(id_estudiante)
                estudiante = Student()  # Crear una instancia de la clase Student
                estudiantes = estudiante.read_student()  # Obtener todos los estudiantes

                for datos_estudiante in estudiantes:
                    if datos_estudiante[0] == id_estudiante:  # Verificar el ID del estudiante
                        estudiante_actualizado = {
                            'ID_Estudiante': id_estudiante,
                            'NombreCompleto': self.entry_nombre.get(),
                            'FechaNacimiento': self.entry_fecha_nacimiento.get(),
                            'Genero': self.entry_genero.get(),
                            'Direccion': self.entry_direccion.get(),
                            'CorreoElectronico': self.entry_correo.get(),
                            'TelefonoContacto': self.entry_telefono.get(),
                            'CarreraPrograma': self.entry_carrera.get(),
                            'AnioIngreso': int(self.entry_anio_ingreso.get())
                        }
                        estudiante.update_student(estudiante_actualizado)  # Llamar al método de instancia para actualizar el estudiante
                        self.status_label.config(text="Estudiante actualizado exitosamente.")
                        self.limpiar_campos()
                        break
                else:
                    self.limpiar_campos()
                    self.status_label.config(text="Estudiante no encontrado.")
            except ValueError:
                self.limpiar_campos()
                self.status_label.config(text="Error: ID de estudiante inválido.")
        else:
            self.limpiar_campos()
            self.status_label.config(text="Error: Campo ID vacío.")

    def cargar_datos_estudiante(self):
        id_estudiante = self.entry_id.get()
        if id_estudiante:
            try:
                id_estudiante = int(id_estudiante)
                estudiante = Student()  # Crear una instancia de la clase Student
                estudiantes = estudiante.read_student()  # Obtener todos los estudiantes

                for datos_estudiante in estudiantes:
                    if datos_estudiante[0] == id_estudiante:  # Verificar el ID del estudiante
                        # Cargar los datos del estudiante en los campos de entrada
                        self.entry_nombre.delete(0, tk.END)
                        self.entry_nombre.insert(0, datos_estudiante[1])

                        self.entry_fecha_nacimiento.delete(0, tk.END)
                        self.entry_fecha_nacimiento.insert(0, datos_estudiante[2])

                        self.entry_genero.delete(0, tk.END)
                        self.entry_genero.insert(0, datos_estudiante[3])

                        self.entry_direccion.delete(0, tk.END)
                        self.entry_direccion.insert(0, datos_estudiante[4])

                        self.entry_correo.delete(0, tk.END)
                        self.entry_correo.insert(0, datos_estudiante[5])

                        self.entry_telefono.delete(0, tk.END)
                        self.entry_telefono.insert(0, datos_estudiante[6])

                        self.entry_carrera.delete(0, tk.END)
                        self.entry_carrera.insert(0, datos_estudiante[7])

                        self.entry_anio_ingreso.delete(0, tk.END)
                        self.entry_anio_ingreso.insert(0, datos_estudiante[8])

                        self.status_label.config(text="Datos del estudiante cargados.")
                        break
                else:
                    self.limpiar_campos()
                    self.status_label.config(text="Estudiante no encontrado.")
            except ValueError:
                self.limpiar_campos()
                self.status_label.config(text="Error: ID de estudiante inválido.")
        else:
            self.limpiar_campos()
            self.status_label.config(text="Error: Campo ID vacío.")

    def eliminar_estudiante(self):
        id_estudiante = self.entry_id.get()
        if id_estudiante:
            try:
                id_estudiante = int(id_estudiante)
                estudiante_a_eliminar = Student()  # Crear una instancia de la clase Student
                estudiante_a_eliminar.delete_student(id_estudiante)  # Llamar al método de instancia para eliminar el estudiante
                self.limpiar_campos()
                self.status_label.config(text="Estudiante eliminado exitosamente.")
            except ValueError:
                self.status_label.config(text="Error: ID de estudiante inválido.")
        else:
            self.status_label.config(text="Error: Campo ID vacío.")

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha_nacimiento.delete(0, tk.END)
        self.entry_genero.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)
        self.entry_anio_ingreso.delete(0, tk.END)
    
    def limpiar_tabla(self):
        self.output_text.delete(*self.output_text.get_children())


if __name__ == "__main__":
    root = tk.Tk()
    student_gui = StudentGUI(root)
    root.mainloop()
