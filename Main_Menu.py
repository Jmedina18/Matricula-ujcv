import tkinter as tk
from tkinter import ttk
from Gui.Student_Gui import StudentGUI
from Gui.Profesor_Gui import ProfesorGUI
from Gui.Plan_Estudios_Curso_Gui import Plan_Estudios_Curso_Gui
from Gui.Plan_de_Estudio_Gui import Plan_de_Estudio_Gui
from Gui.Matricula_Gui import Matricula_Gui
from Gui.Curso_Gui import Curso_Gui

class MenuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("400x400")

        # Crear botones para cada GUI
        student_button = tk.Button(root, text="Estudiantes", command=self.open_student_gui)
        student_button.pack(pady=10)

        profesor_button = tk.Button(root, text="Profesores", command=self.open_profesor_gui)
        profesor_button.pack(pady=10)

        plan_estudios_curso_button = tk.Button(root, text="Plan de Estudios por Curso", command=self.open_plan_estudios_curso_gui)
        plan_estudios_curso_button.pack(pady=10)

        plan_estudio_button = tk.Button(root, text="Plan de Estudio", command=self.open_plan_estudio_gui)
        plan_estudio_button.pack(pady=10)

        matricula_button = tk.Button(root, text="Matrícula", command=self.open_matricula_gui)
        matricula_button.pack(pady=10)

        curso_button = tk.Button(root, text="Cursos", command=self.open_curso_gui)
        curso_button.pack(pady=10)

    def open_student_gui(self):
        student_window = tk.Toplevel(self.root)
        student_gui = StudentGUI(student_window)

    def open_profesor_gui(self):
        profesor_window = tk.Toplevel(self.root)
        profesor_gui = ProfesorGUI(profesor_window)

    def open_plan_estudios_curso_gui(self):
        plan_estudios_curso_window = tk.Toplevel(self.root)
        plan_estudios_curso_gui = Plan_Estudios_Curso_Gui(plan_estudios_curso_window)

    def open_plan_estudio_gui(self):
        plan_estudio_window = tk.Toplevel(self.root)
        plan_estudio_gui = Plan_de_Estudio_Gui(plan_estudio_window)

    def open_matricula_gui(self):
        matricula_window = tk.Toplevel(self.root)
        matricula_gui = Matricula_Gui(matricula_window)

    def open_curso_gui(self):
        curso_window = tk.Toplevel(self.root)
        curso_gui = Curso_Gui(curso_window)

if __name__ == "__main__":
    root = tk.Tk()
    menu_gui = MenuGUI(root)
    root.mainloop()
