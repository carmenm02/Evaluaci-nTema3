import sympy
P1 = input("Primer polinomio: ")
P2 = input("Segundo polinomio: ")

def restar(p1,p2):
    return p1 - p2
def dividir(p1,p2):
    return p1 / p2

def eliminar(polinomio):
    polinomio = input("Introduce un polinomio: ")
    terminos = terminos(polinomio)
    terminos.pop()
    for i in terminos:
        print(i)

def comprobar(polinomio):
    
       