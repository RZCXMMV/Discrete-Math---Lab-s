def Conjuncion_2():
    print("A | B | Conjunción")
    print("-------------------")
    print("V | V | V")
    print("V | F | F")
    print("F | V | F")
    print("F | F | F")

def Conjuncion_3():
    print("A | B | C | Conjunción")
    print("-----------------------")
    print("V | V | V | V")
    print("V | V | F | F")
    print("V | F | V | F")
    print("V | F | F | F")
    print("F | V | V | F")
    print("F | V | F | F")
    print("F | F | V | F")
    print("F | F | F | F")

def Conjuncion_4():
    print("A | B | C | D | Conjunción")
    print("---------------------------")
    print("V | V | V | V | V")
    print("V | V | V | F | F")
    print("V | V | F | V | F")
    print("V | V | F | F | F")
    print("V | F | V | V | F")
    print("V | F | V | F | F")
    print("V | F | F | V | F")
    print("V | F | F | F | F")
    print("F | V | V | V | F")
    print("F | V | V | F | F")
    print("F | V | F | V | F")
    print("F | V | F | F | F")
    print("F | F | V | V | F")
    print("F | F | V | F | F")
    print("F | F | F | V | F")
    print("F | F | F | F | F")

def generate_conjunction(n):
    if n == 2:
        Conjuncion_2()
    elif n == 3:
        Conjuncion_3()
    elif n == 4:
        Conjuncion_4()
    else:
        print("Número de variables no válido")
