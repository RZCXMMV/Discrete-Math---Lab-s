import tkinter as tk
from Lab1.Excercises.Conjuncion import generate_conjunction
from Lab1.Excercises.Disyuncion import generate_disyuncion
from Lab1.Excercises.Disyuncion_Exclusiva import generate_disyunctionexclusiva
from Lab1.Excercises.Condicional import generate_condicional
from Lab1.Excercises.Bi_Condicional import generate_bicondicional



def open_variable_choice(root, table_type):
    win = tk.Toplevel(root)
    win.overrideredirect(True)

    win.title("Seleccione Número de Variables")
    win.configure(background="DARKGRAY")
    win.geometry("400x400+500+100")

    tk.Label(
        win,
        text="Seleccione número de variables (2-4)",
        background="DARKGRAY",
        foreground="WHITE",
        font=("Arial", 15, "bold")
    ).pack(pady=10)

    var = tk.IntVar(value=2)

    for i in range(2, 5):
        tk.Radiobutton(
            win,
            text=f"{i} variables",
            variable=var,
            value=i,
            background="DARKGRAY",
            foreground="WHITE",
            selectcolor="gray",
            font=("Arial", 12)
        ).pack(anchor="w", padx=40)

    def On_Click():
        n = var.get()
        if table_type == 1:  # Conjunción
            generate_conjunction(n)  # ✅ Ya no se necesita output_frame
        elif table_type == 2: # Disyuncion
            generate_disyuncion(n)
        elif table_type == 3: # DisyuncionExclusiva
            generate_disyunctionexclusiva(n)
        elif table_type == 4: # Condicional
            generate_condicional(n)
        elif table_type == 5: # Bi-Condicional
            generate_bicondicional(n)
        else:
            print("Otras tablas aún no implementadas")

    def volver_al_root():
        win.withdraw()
        root.deiconify()
        root.focus_force()

    tk.Button(win, text="Aceptar", foreground="red", command=On_Click).pack(pady=10)
    tk.Button(win, text="Volver", command=volver_al_root).pack(pady=10)
