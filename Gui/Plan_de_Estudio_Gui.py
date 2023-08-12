import tkinter as tk
from tkinter import ttk
from Data.Conexion import Conexion
from Logic.Plan_de_Estudio import Plan_de_Estudio

class Plan_de_Estudio_Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Plan de Estudio")
        #self.root.geometry("800x600")

        entry_width = 35
        entry_font = ('New Times Roman', 11)

        label_plan_id = tk.Label(root, text="ID Plan de Estudio:")
        label_plan_id.grid(row=0, column=0)
        self.entry_plan_id = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_plan_id.grid(row=0, column=1)

        label_nombre_plan = tk.Label(root, text="Nombre del Plan de Estudio:")
        label_nombre_plan.grid(row=1, column=0)
        self.entry_nombre_plan = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_nombre_plan.grid(row=1, column=1)

        label_fecha_aprobacion = tk.Label(root, text="Fecha de Aprobación:")
        label_fecha_aprobacion.grid(row=2, column=0)
        self.entry_fecha_aprobacion = tk.Entry(root, width=entry_width, font=entry_font)
        self.entry_fecha_aprobacion.grid(row=2, column=1)

        self.fields = [self.entry_plan_id, self.entry_nombre_plan, self.entry_fecha_aprobacion]

        self.placeholders = ["ID Plan de Estudio", "Nombre del Plan de Estudio", "YYYY-MM-DD"]

        for field, placeholder in zip(self.fields, self.placeholders):
            field.insert(0, placeholder)
            field.config(fg='grey')
            field.bind('<FocusIn>', self.clear_placeholder)
            field.bind('<FocusOut>', self.restore_placeholder)

        self.boton_guardar = tk.Button(root, text="Guardar", command=self.guardar_plan_estudio)
        self.boton_guardar.grid(row=0, column=2, padx=10, pady=5)

        self.boton_listar = tk.Button(root, text="Listar", command=self.listar_planes_estudio)
        self.boton_listar.grid(row=1, column=2, padx=10, pady=5)

        self.boton_editar = tk.Button(root, text="Editar", command=self.editar_plan_estudio)
        self.boton_editar.grid(row=2, column=2, padx=10, pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_plan_estudio)
        self.boton_eliminar.grid(row=3, column=2, padx=10, pady=5)

        self.boton_cargar_datos = tk.Button(root, text="Cargar Datos", command=self.cargar_datos_plan_estudio)
        self.boton_cargar_datos.grid(row=0, column=3, padx=10, pady=5)

        self.boton_limpiar_campos = tk.Button(root, text="Limpiar Campos", command=self.limpiar_campos)
        self.boton_limpiar_campos.grid(row=1, column=3, padx=10, pady=5)

        self.output_text = ttk.Treeview(root, columns=("ID Plan de Estudio", "Nombre del Plan de Estudio", "Fecha de Aprobación"), show="headings")
        self.output_text.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

        self.output_text.column("#0", width=0)
        self.output_text.column("ID Plan de Estudio", width=150)
        self.output_text.column("Nombre del Plan de Estudio", width=300)
        self.output_text.column("Fecha de Aprobación", width=150)

        self.output_text.heading("ID Plan de Estudio", text="ID Plan de Estudio")
        self.output_text.heading("Nombre del Plan de Estudio", text="Nombre del Plan de Estudio")
        self.output_text.heading("Fecha de Aprobación", text="Fecha de Aprobación")

        self.conexion = Conexion()

    def guardar_plan_estudio(self):
        plan_estudio = Plan_de_Estudio()
        nuevo_plan_estudio = {
            'ID_PlanEstudio': int(self.entry_plan_id.get()),
            'NombrePlanEstudio': self.entry_nombre_plan.get(),
            'FechaAprobacion': self.entry_fecha_aprobacion.get()
        }
        plan_estudio.create_plan_estudio(nuevo_plan_estudio)
        self.limpiar_campos()

    def listar_planes_estudio(self):
        plan_estudio = Plan_de_Estudio()
        planes_estudio = plan_estudio.read_plan_estudio()
        self.output_text.delete(*self.output_text.get_children())
        for plan in planes_estudio:
            self.output_text.insert("", "end", values=(plan.ID_PlanEstudio, plan.NombrePlanEstudio, plan.FechaAprobacion))

    def editar_plan_estudio(self):
        plan_id = self.entry_plan_id.get()
        if plan_id:
            try:
                plan_id = int(plan_id)
                plan_estudio = Plan_de_Estudio()
                planes_estudio = plan_estudio.read_plan_estudio()

                for plan in planes_estudio:
                    if plan.ID_PlanEstudio == plan_id:
                        plan_actualizado = {
                            'ID_PlanEstudio': plan_id,
                            'NombrePlanEstudio': self.entry_nombre_plan.get(),
                            'FechaAprobacion': self.entry_fecha_aprobacion.get()
                        }
                        plan_estudio.update_plan_estudio(plan_actualizado)
                        self.limpiar_campos()
                        break
                else:
                    self.limpiar_campos()
            except ValueError:
                self.limpiar_campos()
        else:
            self.limpiar_campos()

    def eliminar_plan_estudio(self):
        plan_id = self.entry_plan_id.get()
        if plan_id:
            try:
                plan_id = int(plan_id)
                plan_estudio = Plan_de_Estudio()
                plan_estudio.delete_plan_estudio(plan_id)
                self.limpiar_campos()
            except ValueError:
                pass

    def cargar_datos_plan_estudio(self):
        plan_id = self.entry_plan_id.get()
        if plan_id:
            try:
                plan_id = int(plan_id)
                plan_estudio = Plan_de_Estudio()
                planes_estudio = plan_estudio.read_plan_estudio()

                for plan in planes_estudio:
                    if plan.ID_PlanEstudio == plan_id:
                        self.entry_nombre_plan.delete(0, tk.END)
                        self.entry_nombre_plan.insert(0, plan.NombrePlanEstudio)

                        self.entry_fecha_aprobacion.delete(0, tk.END)
                        self.entry_fecha_aprobacion.insert(0, plan.FechaAprobacion)

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
    plan_estudio_gui = Plan_de_Estudio_Gui(root)
    root.mainloop()
