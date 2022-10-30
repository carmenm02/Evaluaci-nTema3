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

