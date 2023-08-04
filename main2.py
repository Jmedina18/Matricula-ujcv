from Gui import Student_Gui

if __name__ == "__main__":
    root = Student_Gui.tk.Tk()  # Crear una instancia de Tkinter
    student_gui = Student_Gui.StudentGUI(root)  # Crear una instancia de la clase StudentGUI
    root.mainloop()


