def Hanoi(discos,primeraguja=1,segundaguja=2,terceraguja=3):

    if discos > 0:
        Hanoi(discos-1,primeraguja,terceraguja,segundaguja)
        print("Se mueve de",primeraguja, "a ",terceraguja)
        Hanoi(discos-1,segundaguja,primeraguja,terceraguja)

if __name__ == '__main__':
    discos = 74
    Hanoi(discos)