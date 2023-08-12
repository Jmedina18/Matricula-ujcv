import tkinter as tk
from tkinter import ttk
from Logic.Curso import Curso

class Curso_Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Curso")

        # Crear campos de entrada
        entry_width = 35
        entry_font = ('New Times Roman', 11)

        label_id = tk.Label(root, text="ID Curso:")
        label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_id.grid(row=0, column=1)

        label_nombre_curso = tk.Label(root, text="Nombre del Curso:")
        label_nombre_curso.grid(row=1, column=0)
        self.entry_nombre_curso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_nombre_curso.grid(row=1, column=1)

        label_codigo_curso = tk.Label(root, text="Código del Curso:")
        label_codigo_curso.grid(row=2, column=0)
        self.entry_codigo_curso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_codigo_curso.grid(row=2, column=1)

        label_descripcion_curso = tk.Label(root, text="Descripción del Curso:")
        label_descripcion_curso.grid(row=3, column=0)
        self.entry_descripcion_curso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_descripcion_curso.grid(row=3, column=1)

        label_creditos = tk.Label(root, text="Créditos:")
        label_creditos.grid(row=4, column=0)
        self.entry_creditos = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_creditos.grid(row=4, column=1)

        label_horario_curso = tk.Label(root, text="Horario del Curso:")
        label_horario_curso.grid(row=5, column=0)
        self.entry_horario_curso = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_horario_curso.grid(row=5, column=1)

        label_profesor_asignado = tk.Label(root, text="Profesor Asignado:")
        label_profesor_asignado.grid(row=6, column=0)
        self.entry_profesor_asignado = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_profesor_asignado.grid(row=6, column=1)

        # Agregar placeholders a los campos de entrada
        self.fields = [
            self.entry_id, self.entry_nombre_curso, self.entry_codigo_curso,
            self.entry_descripcion_curso, self.entry_creditos, self.entry_horario_curso,
            self.entry_profesor_asignado
        ]

        self.placeholders = [
            "1",
            "Nombre del Curso",
            "Código del Curso",
            "Descripción del Curso",
            "Créditos",
            "Horario del Curso",
            "Profesor Asignado"
        ]       

        for field, placeholder in zip(self.fields, self.placeholders):
            field.insert(0, placeholder)
            field.config(fg='grey')
            field.bind('<FocusIn>', self.clear_placeholder)
            field.bind('<FocusOut>', self.restore_placeholder)
            
        # Botones
        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_curso)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)
        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_cursos)
        self.boton_listar.grid(row=2, column=2, padx=10, pady=5)
        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_curso)
        self.boton_editar.grid(row=4, column=2, padx=10, pady=5)
        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_curso)
        self.boton_eliminar.grid(row=5, column=2, padx=10, pady=5)
        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_curso)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)
        self.boton_limpiar_tabla = tk.Button(root, text="Limpiar Tabla", command=self.limpiar_tabla)
        self.boton_limpiar_tabla.grid(row=2, column=3, padx=10, pady=5)
        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=4, column=3, padx=10, pady=5)

        # Área de salida para mostrar los cursos listados
        self.output_text = ttk.Treeview(root, columns=("ID Curso", "Nombre del Curso", "Código del Curso", "Descripción del Curso", "Créditos", "Horario del Curso", "Profesor Asignado"), show="headings")
        self.output_text.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

       # Configuración del ancho de las columnas
        self.output_text.column("#0", width=0)
        self.output_text.column("ID Curso", width=80)
        self.output_text.column("Nombre del Curso", width=200)
        self.output_text.column("Código del Curso", width=100)
        self.output_text.column("Descripción del Curso", width=200)
        self.output_text.column("Créditos", width=80)
        self.output_text.column("Horario del Curso", width=150)
        self.output_text.column("Profesor Asignado", width=150)

        # Agregar el Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=7, column=3, sticky="ns")

        # Encabezados de las columnas
        self.output_text.heading("ID Curso", text="ID")
        self.output_text.heading("Nombre del Curso", text="Nombre del Curso")
        self.output_text.heading("Código del Curso", text="Código del Curso")
        self.output_text.heading("Descripción del Curso", text="Descripción del Curso")
        self.output_text.heading("Créditos", text="Créditos")
        self.output_text.heading("Horario del Curso", text="Horario del Curso")
        self.output_text.heading("Profesor Asignado", text="Profesor Asignado")

    def guardar_curso(self):
        curso = Curso()
        curso.ID_Curso = int(self.entry_id.get())
        curso.NombreCurso = self.entry_nombre_curso.get()
        curso.CodigoCurso = self.entry_codigo_curso.get()
        curso.DescripcionCurso = self.entry_descripcion_curso.get()
        curso.Creditos = int(self.entry_creditos.get())
        curso.HorarioCurso = self.entry_horario_curso.get()
        curso.ProfesorAsignado = self.entry_profesor_asignado.get()
        curso.create_curso(curso)
        self.limpiar_campos()
        self.listar_cursos()

    def listar_cursos(self):
        curso = Curso()
        cursos = curso.read_curso()
        self.limpiar_tabla()
        for curso in cursos:
            self.output_text.insert("", "end", values=curso)

    def editar_curso(self):
        curso = Curso()
        curso.ID_Curso = int(self.entry_id.get())
        curso.NombreCurso = self.entry_nombre_curso.get()
        curso.CodigoCurso = self.entry_codigo_curso.get()
        curso.DescripcionCurso = self.entry_descripcion_curso.get()
        curso.Creditos = int(self.entry_creditos.get())
        curso.HorarioCurso = self.entry_horario_curso.get()
        curso.ProfesorAsignado = self.entry_profesor_asignado.get()
        curso.update_curso(curso)
        self.limpiar_campos()
        self.listar_cursos()

    def eliminar_curso(self):
        id_curso = int(self.entry_id.get())
        curso = Curso()
        curso.delete_curso(id_curso)
        self.limpiar_campos()
        self.listar_cursos()

    def cargar_datos_curso(self):
        selected_item = self.output_text.focus()
        if selected_item:
            item_data = self.output_text.item(selected_item, "values")
            self.entry_id.delete(0, tk.END)
            self.entry_nombre_curso.delete(0, tk.END)
            self.entry_codigo_curso.delete(0, tk.END)
            self.entry_descripcion_curso.delete(0, tk.END)
            self.entry_creditos.delete(0, tk.END)
            self.entry_horario_curso.delete(0, tk.END)
            self.entry_profesor_asignado.delete(0, tk.END)

            self.entry_id.insert(0, item_data[0])
            self.entry_nombre_curso.insert(0, item_data[1])
            self.entry_codigo_curso.insert(0, item_data[2])
            self.entry_descripcion_curso.insert(0, item_data[3])
            self.entry_creditos.insert(0, item_data[4])
            self.entry_horario_curso.insert(0, item_data[5])
            self.entry_profesor_asignado.insert(0, item_data[6])

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

    def limpiar_tabla(self):
        self.output_text.delete(*self.output_text.get_children())

    def limpiar_campos(self):
        for field, placeholder in zip(self.fields, self.placeholders):
            field.delete(0, tk.END)
            field.insert(0, placeholder)
            field.config(fg='grey')

if __name__ == "__main__":
    root = tk.Tk()
    curso_gui = Curso_Gui(root)
    root.mainloop()
