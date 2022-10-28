from curses import raw


print("Ingresa los valores")
print("|a00 a01 a02|")
print("|a10 a11 a12|")
print("|a20 a21 a22")

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