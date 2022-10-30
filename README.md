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
from distutils.log import info
from pickle import NONE

from sympy import li


class Nodo():
    info, sig=None,None

class Nave():
     def __init__(self,nombre,largo,tripulacion,pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

def agregar_naves():
    naves = []
    naves.append(Nave("Halcón Milenario"))
    naves.append(Nave("Estrella de la Muerte"))
    return naves
def ascendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i].nombre > lista[j].nombre:
                lista[i],lista[j] = lista[j],lista[i]
def descendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i].nombre < lista[j].nombre:
                lista[i],lista[j] = lista[j],lista[i]
def mostrar(lista):
    for nave in lista:
        print(nave.nombre,nave.largo,nave.tripulacion,nave.pasajeros)
def mayorpasajeros(lista):
    mayor = 0
    for i in range(5):
        for nave in lista:
            if nave.pasajeros > mayor.pasajeros:
                mayor = nave
            print(mayor.nombre,mayor.pasajeros)
def mayortripulacion(lista):
    mayor = 0
    for i in range(5):
        for nave in lista:
            if nave.tripulacion > mayor.tripulacion:
                mayor = nave
            print(mayor.nombre,mayor.tripulacion)

def AT(lista):
    for nave in lista:
        if nave.nombre[0] == "A" and nave.nombre[1] == "T":
            print(nave.nombre)

def seispasajerosi(lista):
    for nave in lista:
        if nave.pasajeros >= 6:
            print(nave.nombre,nave.pasajeros)
def navemaspequeña(lista):
    menor = 0
    for nave in lista:
        if nave.largo < menor.largo:
            menor = nave
    print(menor.nombre,menor.largo)
def navemasgrande(lista):
    mayor = 0
    for nave in lista:
        if nave.largo < mayor.largo:
            mayor = nave
    print(mayor.nombre,mayor.largo)
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
def encriptar(mensaje):
    texto = []
    texto_encriptado = " "

    for i in range(len(mensaje)):
        texto_encriptado += hashlib.sha256(i.encode('ASCII')).hexdigest()[:8]
    return ''.join(texto)
def desencriptar(mensaje):
    texto = []
    for i in range(len(mensaje)):
        texto.append(desencriptar[hash_desencriptar(mensaje[i])])

    return ''.join(texto)
```
