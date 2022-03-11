'''lista =[]
num = 0

def pedir():
    i = 0
   while i <=5:
        num = float(input("ingresa un numero: "))
        lista.append(num)
        i += 1 


def ordenar():
    lista.sort()
    pares = []
    impares =[]
    for i in lista :
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

pedir()
ordenar() '''


#ejercicio2

def factorial():
    numero = int(input("ingrese numero entero y positivo: "))
    if numero >0:
        factorial = 1
        for i in range(1 , numero +1):
            factorial = factorial*i
        print(factorial)
    else:
        print("el numero es negativo y no se puede proceder")

factorial()

def factorial():
    from math import factorial
    numero = int(input("ingrese numero entero y positivo: "))
    if numero >0:
        print(factorial(numero))
    else:
        print("el numero es negativo y no se puede proceder")

factorial()


