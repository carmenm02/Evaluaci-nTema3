<h1 align="center">	Evaluacion Tema 3</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/Evaluaci-nTema3.git)

```
## Ejercicio1 :

def Hanoi(discos,primeraguja=1,segundaguja=2,terceraguja=3):

    if discos > 0:
        Hanoi(discos-1,primeraguja,terceraguja,segundaguja)
        print("Se mueve de",primeraguja, "a ",terceraguja)
        Hanoi(discos-1,segundaguja,primeraguja,terceraguja)

if __name__ == '__main__':
    discos = 74
    Hanoi(discos)
alumna.calificación()
```
```
## Ejercicio2:

print("Ingresa los valores")
print("|a00 a01 a02|")
print("|a10 a11 a12|")
print("|a20 a21 a22|")

a00 = float(input("Ingresa el valor de a00: "))
a01 = float(input("Ingresa el valor de a01: "))
a02 = float(input("Ingresa el valor de a02: "))
a10 = float(input("Ingresa el valor de a10: "))
a11 = float(input("Ingresa el valor de a11: "))
a12 = float(input("Ingresa el valor de a12: "))
a20 = float(input("Ingresa el valor de a20: "))
a21 = float(input("Ingresa el valor de a21: "))
a22 = float(input("Ingresa el valor de a22: "))

total = ((a00*a11*a22) + (a10*a21*a02) + (a20 * a01 * a12)) - ((a20*a11*a02)+(a00*a21*a22)+(a10*a01*a22))

if total != 0:
    print(a00," ",a01," ",a02)
    print(a10," ",a11," ",a12)
    print(a20," ",a21," ",a22)
    print("Determinante: ",total)
else:
    print("Determinante igual a 0")
```
```
## Ejercicio3:

```
```
## Ejercicio4:

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
    elemento = input("Introduce un elemento: ")
    if elemento in polinomio:
        print("El elemento introducido está en el polinomio.")
    else:
        print("El elemento introducido no está en el polinomio")
```
```
## Ejercicio5:

```
