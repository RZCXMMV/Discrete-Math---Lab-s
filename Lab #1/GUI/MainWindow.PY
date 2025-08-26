import tkinter as tk
import sys, os

# Añadir carpeta GUI al path para que encuentre VariablesChoice
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from VariablesChoice import open_variable_choice

root = tk.Tk()
root.title("Laboratorio #1 - Matemáticas Discretas")
root.configure(background="DARKGRAY")
root.geometry("400x400+500+200")

def On_Click(option):
    open_variable_choice(option)

tk.Label(root, text="Seleccione El Tipo De Tabla", background="DARKGRAY", foreground="WHITE", font=("Arial", 12, "bold")).pack(pady=15)

tk.Button(root, text="Tabla De Conjunción", width=25, foreground="red", command=lambda: On_Click(1)).pack(pady=5)
tk.Button(root, text="Tabla De Disyunción", width=25, foreground="red", command=lambda: On_Click(2)).pack(pady=5)
tk.Button(root, text="Tabla De Disyunción Exclusiva", width=25, foreground="red", command=lambda: On_Click(3)).pack(pady=5)
tk.Button(root, text="Tabla Condicional", width=25, foreground="red", command=lambda: On_Click(4)).pack(pady=5)
tk.Button(root, text="Tabla Bi-Condicional", width=25, foreground="red", command=lambda: On_Click(5)).pack(pady=5)

root.mainloop()
