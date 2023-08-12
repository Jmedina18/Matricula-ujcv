import tkinter as tk
from tkinter import ttk
from Logic.Profesor import Profesor  # Asegúrate de importar la clase Profesor correctamente

class ProfesorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Profesor")

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

        label_AreaEspecializacion = tk.Label(root, text="Area de Especializacion:")
        label_AreaEspecializacion.grid(row=7, column=0)
        self.entry_area_especializacion = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_area_especializacion.grid(row=7, column=1)

        label_FechaIngreso = tk.Label(root, text="Fecha de Ingreso:")
        label_FechaIngreso.grid(row=8, column=0)
        self.entry_fecha_ingreso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_fecha_ingreso.grid(row=8, column=1)

        # Agregar placeholders a todos los campos de entrada
        self.fields = [
         self.entry_id, self.entry_nombre, self.entry_fecha_nacimiento,
         self.entry_genero, self.entry_direccion, self.entry_correo,
         self.entry_telefono, self.entry_area_especializacion, self.entry_fecha_ingreso
        ]

        self.placeholders = [
         "1",
         "Nombre Completo",
         "YYYY-MM-DD",
         "Masculino",
         "Av.Poseidon",
         "nombre.completo@ujcv.edu.hn",
         "+504 12345678",
         "Infotecnologia",
         "YYYY-MM-DD"
        ]       

        for field, placeholder in zip(self.fields, self.placeholders):
            field.insert(0, placeholder)
            field.config(fg='grey')
            field.bind('<FocusIn>', self.clear_placeholder)
            field.bind('<FocusOut>', self.restore_placeholder)

        # Botones
        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_profesor)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)
        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_profesores)
        self.boton_listar.grid(row=2, column=2, padx=10, pady=5)
        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_profesor)
        self.boton_editar.grid(row=5, column=2, padx=10, pady=5)
        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_profesor)
        self.boton_eliminar.grid(row=8, column=2, padx=10, pady=5)
        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_profesor)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)
        self.boton_limpiar_tabla = tk.Button(root, text="Limpiar Tabla", command=self.limpiar_tabla)
        self.boton_limpiar_tabla.grid(row=2, column=3, padx=10, pady=5)
        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=5, column=3, padx=10, pady=5)

        # Área de salida para mostrar los profesores listados
        self.output_text = ttk.Treeview(root, columns=("ID", "Nombre", "Fecha de Nacimiento", "Género", "Dirección", "Correo Electrónico", "Teléfono de Contacto", "Área de Especialización", "Fecha de Ingreso"), show="headings")
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
        self.output_text.column("Área de Especialización", width=180)
        self.output_text.column("Fecha de Ingreso", width=100)

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
        self.output_text.heading("Área de Especialización", text="Área de Especialización")
        self.output_text.heading("Fecha de Ingreso", text="Fecha de Ingreso")

        # Etiqueta para mostrar el estado del proceso
        self.status_label = tk.Label(root, text="")
        self.status_label.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

    #(Métodos para las operaciones como guardar, listar, editar, eliminar y limpiar)
    def guardar_profesor(self):
        profesor = Profesor()  # Crear una instancia de la clase Profesor
        nuevo_profesor = {
            'ID_Profesor': int(self.entry_id.get()),
            'NombreCompleto': self.entry_nombre.get(),
            'FechaNacimiento': self.entry_fecha_nacimiento.get(),
            'Genero': self.entry_genero.get(),
            'Direccion': self.entry_direccion.get(),
            'CorreoElectronico': self.entry_correo.get(),
            'TelefonoContacto': self.entry_telefono.get(),
            'AreaEspecializacion': self.entry_area_especializacion.get(),
            'FechaIngreso': self.entry_fecha_ingreso.get()
        }
        profesor.create_profesor(nuevo_profesor)  # Llamar al método de instancia para crear el Profesor
        self.status_label.config(text="Profesor agregado exitosamente.")
        self.limpiar_campos()

    def listar_profesores(self):
        profesor = Profesor()  # Crear una instancia de la clase Profesor
        profesores = profesor.read_profesor()  # Llamar al método de instancia para obtener la lista de profesores
        self.output_text.delete(*self.output_text.get_children())  # Limpiar la tabla antes de mostrar los datos
        for prof in profesores:
            self.output_text.insert("", "end", values=(prof.ID_Profesor, prof.NombreCompleto, prof.FechaNacimiento,
                                                      prof.Genero, prof.Direccion, prof.CorreoElectronico,
                                                      prof.TelefonoContacto, prof.AreaEspecializacion,
                                                      prof.FechaIngreso))

    def editar_profesor(self):
        id_profesor = self.entry_id.get()
        if id_profesor:
            try:
                id_profesor = int(id_profesor)
                profesor = Profesor()  # Crear una instancia de la clase Profesor
                profesores = profesor.read_profesor()  # Obtener todos los profesores

                for datos_profesor in profesores:
                    if datos_profesor[0] == id_profesor:  # Verificar el ID del profesor
                        profesor_actualizado = {
                            'ID_Profesor': id_profesor,
                            'NombreCompleto': self.entry_nombre.get(),
                            'FechaNacimiento': self.entry_fecha_nacimiento.get(),
                            'Genero': self.entry_genero.get(),
                            'Direccion': self.entry_direccion.get(),
                            'CorreoElectronico': self.entry_correo.get(),
                            'TelefonoContacto': self.entry_telefono.get(),
                            'AreaEspecializacion': self.entry_area_especializacion.get(),
                            'FechaIngreso': self.entry_fecha_ingreso.get()
                        }
                        profesor.update_profesor(profesor_actualizado)  # Llamar al método de instancia para actualizar el profesor
                        self.status_label.config(text="Profesor actualizado exitosamente.")
                        self.limpiar_campos()
                        break
                else:
                    self.limpiar_campos()
                    self.status_label.config(text="Profesor no encontrado.")
            except ValueError:
                self.limpiar_campos()
                self.status_label.config(text="Error: ID de profesor inválido.")
        else:
            self.limpiar_campos()
            self.status_label.config(text="Error: Campo ID vacío.")

    def eliminar_profesor(self):
        id_profesor = self.entry_id.get()
        if id_profesor:
            try:
                id_profesor = int(id_profesor)
                profesor_a_eliminar = Profesor()  # Crear una instancia de la clase profesor
                profesor_a_eliminar.delete_profesor(id_profesor)  # Llamar al método de instancia para eliminar el profesor
                self.limpiar_campos()
                self.status_label.config(text="Profesor eliminado exitosamente.")
            except ValueError:
                self.status_label.config(text="Error: ID de profesor inválido.")
        else:
            self.status_label.config(text="Error: Campo ID vacío.")

    def cargar_datos_profesor(self):
        id_profesor = self.entry_id.get()
        if id_profesor:
            try:
                id_profesor = int(id_profesor)
                profesor = Profesor()  # Crear una instancia de la clase Profesor
                profesores = profesor.read_profesor()  # Obtener todos los profesores

                for datos_profesor in profesores:
                    if datos_profesor[0] == id_profesor:  # Verificar el ID del profesor
                        # Cargar los datos del profesor en los campos de entrada
                        self.entry_nombre.delete(0, tk.END)
                        self.entry_nombre.insert(0, datos_profesor[1])

                        self.entry_fecha_nacimiento.delete(0, tk.END)
                        self.entry_fecha_nacimiento.insert(0, datos_profesor[2])

                        self.entry_genero.delete(0, tk.END)
                        self.entry_genero.insert(0, datos_profesor[3])

                        self.entry_direccion.delete(0, tk.END)
                        self.entry_direccion.insert(0, datos_profesor[4])

                        self.entry_correo.delete(0, tk.END)
                        self.entry_correo.insert(0, datos_profesor[5])

                        self.entry_telefono.delete(0, tk.END)
                        self.entry_telefono.insert(0, datos_profesor[6])

                        self.entry_area_especializacion.delete(0, tk.END)
                        self.entry_area_especializacion.insert(0, datos_profesor[7])

                        self.entry_fecha_ingreso.delete(0, tk.END)
                        self.entry_fecha_ingreso.insert(0, datos_profesor[8])

                        self.status_label.config(text="Datos del profesor cargados.")
                        break
                else:
                    self.limpiar_campos()
                    self.status_label.config(text="Profesor no encontrado.")
            except ValueError:
                self.limpiar_campos()
                self.status_label.config(text="Error: ID de profesor inválido.")
        else:
            self.limpiar_campos()
            self.status_label.config(text="Error: Campo ID vacío.")

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha_nacimiento.delete(0, tk.END)
        self.entry_genero.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_area_especializacion.delete(0, tk.END)
        self.entry_fecha_ingreso.delete(0, tk.END)
    
    def limpiar_tabla(self):
        self.output_text.delete(*self.output_text.get_children())

    def clear_placeholder(self, event):
        widget = event.widget
        if widget.get() == self.placeholders[self.fields.index(widget)]:
            widget.delete(0, tk.END)
            widget.config(fg='black')

    def restore_placeholder(self, event):
        widget = event.widget
        if widget.get() == "":
            placeholder = self.placeholders[self.fields.index(widget)]
            widget.insert(0, placeholder)
            widget.config(fg='grey')

if __name__ == "__main__":
    root = tk.Tk()
    profesor_gui = ProfesorGUI(root)
    root.mainloop()
