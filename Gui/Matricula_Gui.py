import tkinter as tk
from tkinter import ttk
from Logic.Matricula import Matricula

class Matricula_Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Matrícula")

        # Crear campos de entrada
        entry_width = 35
        entry_font = ('New Times Roman', 11)

        label_id = tk.Label(root, text="ID Matrícula:")
        label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_id.grid(row=0, column=1)

        label_estudiante_id = tk.Label(root, text="ID Estudiante:")
        label_estudiante_id.grid(row=1, column=0)
        self.entry_estudiante_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_estudiante_id.grid(row=1, column=1)

        label_curso_id = tk.Label(root, text="ID Curso:")
        label_curso_id.grid(row=2, column=0)
        self.entry_curso_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_curso_id.grid(row=2, column=1)

        label_fecha_matricula = tk.Label(root, text="Fecha de Matrícula:")
        label_fecha_matricula.grid(row=3, column=0)
        self.entry_fecha_matricula = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_fecha_matricula.grid(row=3, column=1)

        label_estado_matricula = tk.Label(root, text="Estado de Matrícula:")
        label_estado_matricula.grid(row=4, column=0)
        self.entry_estado_matricula = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_estado_matricula.grid(row=4, column=1)

        label_nota_final = tk.Label(root, text="Nota Final:")
        label_nota_final.grid(row=5, column=0)
        self.entry_nota_final = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_nota_final.grid(row=5, column=1)

        # Agregar placeholders a los campos de entrada
        self.fields = [
            self.entry_id, self.entry_estudiante_id, self.entry_curso_id,
            self.entry_fecha_matricula, self.entry_estado_matricula, self.entry_nota_final
        ]

        self.placeholders = [
            "1",
            "ID Estudiante",
            "ID Curso",
            "YYYY-MM-DD",
            "Estado",
            "Nota Final"
        ]       

        for field, placeholder in zip(self.fields, self.placeholders):
            field.insert(0, placeholder)
            field.config(fg='grey')
            field.bind('<FocusIn>', self.clear_placeholder)
            field.bind('<FocusOut>', self.restore_placeholder)

        # Botones
        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_matricula)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)
        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_matriculas)
        self.boton_listar.grid(row=2, column=2, padx=10, pady=5)
        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_matricula)
        self.boton_editar.grid(row=4, column=2, padx=10, pady=5)
        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_matricula)
        self.boton_eliminar.grid(row=5, column=2, padx=10, pady=5)
        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_matricula)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)
        self.boton_limpiar_tabla = tk.Button(root, text="Limpiar Tabla", command=self.limpiar_tabla)
        self.boton_limpiar_tabla.grid(row=2, column=3, padx=10, pady=5)
        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=4, column=3, padx=10, pady=5)

        # Área de salida para mostrar las matrículas listadas
        self.output_text = ttk.Treeview(root, columns=("ID Matrícula", "ID Estudiante", "ID Curso", "Fecha de Matrícula", "Estado de Matrícula", "Nota Final"), show="headings")
        self.output_text.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

        # Configuración del ancho de las columnas
        self.output_text.column("#0", width=0)
        self.output_text.column("ID Matrícula", width=80)
        self.output_text.column("ID Estudiante", width=100)
        self.output_text.column("ID Curso", width=80)
        self.output_text.column("Fecha de Matrícula", width=120)
        self.output_text.column("Estado de Matrícula", width=100)
        self.output_text.column("Nota Final", width=80)

        # Agregar el Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=7, column=4, sticky="ns")

        # Encabezados de las columnas
        self.output_text.heading("ID Matrícula", text="ID Matrícula")
        self.output_text.heading("ID Estudiante", text="ID Estudiante")
        self.output_text.heading("ID Curso", text="ID Curso")
        self.output_text.heading("Fecha de Matrícula", text="Fecha de Matrícula")
        self.output_text.heading("Estado de Matrícula", text="Estado de Matrícula")
        self.output_text.heading("Nota Final", text="Nota Final")

    
    def guardar_matricula(self):
        matricula = Matricula()
        matricula.ID_Matricula = int(self.entry_id.get())
        matricula.EstudianteID = int(self.entry_estudiante_id.get())
        matricula.CursoID = int(self.entry_curso_id.get())
        matricula.FechaMatricula = self.entry_fecha_matricula.get()
        matricula.EstadoMatricula = self.entry_estado_matricula.get()
        matricula.NotaFinal = float(self.entry_nota_final.get())
        matricula.create_matricula(matricula)
        self.limpiar_campos()
        self.listar_matriculas()

    def listar_matriculas(self):
        matricula = Matricula()
        matriculas = matricula.read_matricula()
        self.limpiar_tabla()
        for matricula in matriculas:
            self.output_text.insert("", "end", values=matricula)

    def editar_matricula(self):
        matricula = Matricula()
        matricula.ID_Matricula = int(self.entry_id.get())
        matricula.EstudianteID = int(self.entry_estudiante_id.get())
        matricula.CursoID = int(self.entry_curso_id.get())
        matricula.FechaMatricula = self.entry_fecha_matricula.get()
        matricula.EstadoMatricula = self.entry_estado_matricula.get()
        matricula.NotaFinal = float(self.entry_nota_final.get())
        matricula.update_matricula(matricula)
        self.limpiar_campos()
        self.listar_matriculas()

    def eliminar_matricula(self):
        id_matricula = int(self.entry_id.get())
        matricula = Matricula()
        matricula.delete_matricula(id_matricula)
        self.limpiar_campos()
        self.listar_matriculas()

    def cargar_datos_matricula(self):
        selected_item = self.output_text.focus()
        if selected_item:
            item_data = self.output_text.item(selected_item, "values")
            self.entry_id.delete(0, tk.END)
            self.entry_estudiante_id.delete(0, tk.END)
            self.entry_curso_id.delete(0, tk.END)
            self.entry_fecha_matricula.delete(0, tk.END)
            self.entry_estado_matricula.delete(0, tk.END)
            self.entry_nota_final.delete(0, tk.END)

            self.entry_id.insert(0, item_data[0])
            self.entry_estudiante_id.insert(0, item_data[1])
            self.entry_curso_id.insert(0, item_data[2])
            self.entry_fecha_matricula.insert(0, item_data[3])
            self.entry_estado_matricula.insert(0, item_data[4])
            self.entry_nota_final.insert(0, item_data[5])

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
    matricula_gui = Matricula_Gui(root)
    root.mainloop()