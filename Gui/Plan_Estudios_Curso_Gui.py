import tkinter as tk
from tkinter import ttk
from Data.Conexion import Conexion
from Logic.Plan_Estudios_Curso import Plan_Estudios_Curso

class Plan_Estudios_Curso_Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Plan de Estudios - Curso")
        #self.root.geometry("800x600")  # Nuevo tamaño de ventana

        # Crear campos de entrada
        entry_width = 35
        entry_font = ('New Times Roman', 11)

        label_plan_id = tk.Label(root, text="Plan de Estudios ID:")
        label_plan_id.grid(row=0, column=0)
        self.entry_plan_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_plan_id.grid(row=0, column=1)

        label_curso_id = tk.Label(root, text="Curso ID:")
        label_curso_id.grid(row=1, column=0)
        self.entry_curso_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_curso_id.grid(row=1, column=1)

        # Agregar placeholders a los campos de entrada
        self.fields = [self.entry_plan_id, self.entry_curso_id]

        self.placeholders = ["Plan de Estudios ID", "Curso ID"]

        for field, placeholder in zip(self.fields, self.placeholders):
            field.insert(0, placeholder)
            field.config(fg='grey')
            field.bind('<FocusIn>', self.clear_placeholder)
            field.bind('<FocusOut>', self.restore_placeholder)

        # Botones
        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_plan_estudios_curso)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)

        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_planes_estudios_cursos)
        self.boton_listar.grid(row=1, column=2, padx=10, pady=5)

        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_plan_estudios_curso)
        self.boton_editar.grid(row=2, column=2, padx=10, pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_plan_estudios_curso)
        self.boton_eliminar.grid(row=3, column=2, padx=10, pady=5)

        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_plan_estudios_curso)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)

        self.boton_limpiar_tabla = tk.Button(root, text="Limpiar Tabla", command=self.limpiar_tabla)
        self.boton_limpiar_tabla.grid(row=1, column=3, padx=10, pady=5)

        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=2, column=3, padx=10, pady=5)

        # Área de salida para mostrar los planes de estudios - cursos listados
        self.output_text = ttk.Treeview(root, columns=("Plan de Estudios ID", "Curso ID"), show="headings")
        self.output_text.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

        self.output_text.column("#0", width=0)
        self.output_text.column("Plan de Estudios ID", width=150)
        self.output_text.column("Curso ID", width=150)

        self.output_text.heading("Plan de Estudios ID", text="Plan de Estudios ID")
        self.output_text.heading("Curso ID", text="Curso ID")

        self.conexion = Conexion()

    # Métodos para las operaciones
    def guardar_plan_estudios_curso(self):
        plan_estudios_curso = Plan_Estudios_Curso()
        nuevo_plan_estudios_curso = {
            'PlanDeEstudiosID': int(self.entry_plan_id.get()),
            'CursoID': int(self.entry_curso_id.get())
        }
        plan_estudios_curso.create_plan_estudios_curso(nuevo_plan_estudios_curso)
        self.limpiar_campos()

    def listar_planes_estudios_cursos(self):
        plan_estudios_curso = Plan_Estudios_Curso()
        planes_estudios_cursos = plan_estudios_curso.read_plan_estudios_curso()
        self.output_text.delete(*self.output_text.get_children())
        for plan_curso in planes_estudios_cursos:
            self.output_text.insert("", "end", values=(plan_curso.PlanDeEstudiosID, plan_curso.CursoID))

    def editar_plan_estudios_curso(self):
        plan_id = self.entry_plan_id.get()
        curso_id = self.entry_curso_id.get()
        if plan_id and curso_id:
            try:
                plan_id = int(plan_id)
                curso_id = int(curso_id)
                plan_estudios_curso = Plan_Estudios_Curso()
                planes_estudios_cursos = plan_estudios_curso.read_plan_estudios_curso()

                for plan_curso in planes_estudios_cursos:
                    if plan_curso.PlanDeEstudiosID == plan_id and plan_curso.CursoID == curso_id:
                        plan_actualizado = {
                            'PlanDeEstudiosID': plan_id,
                            'CursoID': curso_id
                        }
                        plan_estudios_curso.update_plan_estudios_curso(plan_actualizado)
                        self.limpiar_campos()
                        break
                else:
                    self.limpiar_campos()
            except ValueError:
                self.limpiar_campos()
        else:
            self.limpiar_campos()

    def eliminar_plan_estudios_curso(self):
        plan_id = self.entry_plan_id.get()
        curso_id = self.entry_curso_id.get()
        if plan_id and curso_id:
            try:
                plan_id = int(plan_id)
                curso_id = int(curso_id)
                plan_estudios_curso = Plan_Estudios_Curso()
                plan_estudios_curso.delete_plan_estudios_curso(plan_id, curso_id)
                self.limpiar_campos()
            except ValueError:
                pass

    def cargar_datos_plan_estudios_curso(self):
        plan_id = self.entry_plan_id.get()
        curso_id = self.entry_curso_id.get()
        if plan_id and curso_id:
            try:
                plan_id = int(plan_id)
                curso_id = int(curso_id)
                plan_estudios_curso = Plan_Estudios_Curso()
                planes_estudios_cursos = plan_estudios_curso.read_plan_estudios_curso()

                for plan_curso in planes_estudios_cursos:
                    if plan_curso.PlanDeEstudiosID == plan_id and plan_curso.CursoID == curso_id:
                        self.entry_plan_id.delete(0, tk.END)
                        self.entry_plan_id.insert(0, str(plan_curso.PlanDeEstudiosID))

                        self.entry_curso_id.delete(0, tk.END)
                        self.entry_curso_id.insert(0, str(plan_curso.CursoID))

                        break
                else:
                    self.limpiar_campos()
            except ValueError:
                self.limpiar_campos()
        else:
            self.limpiar_campos()

    def limpiar_campos(self):
        for field, placeholder in zip(self.fields, self.placeholders):
            field.delete(0, tk.END)
            field.insert(0, placeholder)
            field.config(fg='grey')

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
    plan_estudios_curso_gui = Plan_Estudios_Curso_Gui(root)
    root.mainloop()
