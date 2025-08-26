import tkinter as tk
import sys, os

# Añadir carpeta raíz al path para que encuentre Exercises
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Exercises import Conjuncion

def open_variable_choice(table_type):
    def On_Click():
        try:
            n = int(text.get())
            if table_type == 1:  # Conjunción
                Conjuncion.generate_conjunction(n)
            else:
                print("Otras tablas aún no implementadas")
        except:
            print("Ingrese un número válido")

    win = tk.Toplevel()
    win.title("Seleccione Número de Variables")
    win.configure(background="DARKGRAY")
    win.geometry("300x200")

    tk.Label(win, text="Ingrese número de variables (2-4)", background="DARKGRAY", foreground="WHITE").pack(pady=10)
    text = tk.Entry(win, width=20)
    text.pack()

    tk.Button(win, text="Accept", foreground="red", command=On_Click).pack(pady=10)
