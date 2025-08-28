import os
import tkinter as tk
from PIL import Image, ImageTk  # ✅ Importar PIL

def PathImagen(filename):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "..", "Resources", filename)

def MostrarImagen(filename):
    img_path = PathImagen(filename)

    # Crear nueva ventana
    img_win = tk.Toplevel()
    img_win.title("Tabla de Conjunción")
    img_win.configure(background="DARKGRAY")

    # Cargar y redimensionar imagen
    original = Image.open(img_path)
    resized = original.resize((int(original.width * 0.8), int(original.height * 0.8)))  #Tamaño de la imagen 80%
    img = ImageTk.PhotoImage(resized)

    # Ajustar tamaño de ventana a la imagen redimensionada
    img_win.geometry(f"{img.width()}x{img.height()}")

    # Mostrar imagen
    label = tk.Label(img_win, image=img, background="DARKGRAY")
    label.image = img  # Mantener referencia
    label.pack()

def generate_disyunctionexclusiva(n):
    if n == 2:
        MostrarImagen("../resources/conjuncionexclusiva_2.png")
    elif n == 3:
        MostrarImagen("../resources/conjuncionexclusiva_3.png")
    elif n == 4:
        MostrarImagen("../resources/conjuncionexclusiva_4.png")
    else:
        error_win = tk.Toplevel()
        error_win.title("Error")
        tk.Label(error_win, text="Número de variables no válido", background="DARKGRAY", foreground="red").pack(padx=20, pady=20)