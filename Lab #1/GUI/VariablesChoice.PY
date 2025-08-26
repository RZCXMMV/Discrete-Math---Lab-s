import tkinter as tk

root = tk.Tk()

root.title("Laboratorio #1 - Matemáticas Discretas")
root.configure(background = "DARKGRAY")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("400x400+500+200")

tk.Label(root, text = "Seleccione El Número De Variables", background = "DARKGRAY", foreground = "WHITE").pack()
text = tk.Entry(root, width = 20)
text.pack()

def On_Click():
    TextInput(text)

Button = tk.Button(root, text = "Accept", foreground = "red", command = On_Click)
Button.pack()

def TextInput(text):
    Option = int(text.get())
    
    if Option == 2:
        print("2")
    elif Option == 3:
        print("3")
    elif Option == 4:
        print("4")
    else:
        print("Opción no válida")


root.mainloop()