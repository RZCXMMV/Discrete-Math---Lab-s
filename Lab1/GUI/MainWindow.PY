import tkinter as tk
import sys, os
from .VariablesChoice import open_variable_choice


def TablasDeVerdad():


    root = tk.Tk()
    root.overrideredirect(True)
    root.title("Laboratorio #1 - Matemáticas Discretas")
    root.configure(background="DARKGRAY")
    root.geometry("400x400+500+100")

    def On_Click(option):
        open_variable_choice(root, option)

    tk.Label(root, text="Seleccione El Tipo De Tabla de Verdad ", background="DARKGRAY", foreground="WHITE", font=("Arial", 15, "bold")).pack(pady=15)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Button(frame, text="Tabla De Conjunción", width=25, foreground="red", command=lambda: On_Click(1)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame, text="Tabla De Disyunción", width=25, foreground="red", command=lambda: On_Click(2)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Tabla De Disyunción Exclusiva", width=25, foreground="red", command=lambda: On_Click(3)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame, text="Tabla Condicional", width=25, foreground="red", command=lambda: On_Click(4)).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(frame, text="Tabla Bi-Condicional", width=25, foreground="red", command=lambda: On_Click(5)).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    btn_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    btn_cerrar.pack(pady=10)

    root.mainloop()
