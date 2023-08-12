from Gui import Student_Gui,Profesor_Gui

if __name__ == "__main__":
    root = Student_Gui.tk.Tk()  # Crear una instancia de Tkinter
    student_gui = Student_Gui.StudentGUI(root)  # Crear una instancia de la clase StudentGUI
    root2 = Profesor_Gui.tk.Tk()  # Crear otra instancia de Tkinter para el GUI de profesores
    profesor_gui = Profesor_Gui.ProfesorGUI(root2)  # Crear una instancia de la clase ProfesorGUI
    
    root.mainloop()
    root2.mainloop()

