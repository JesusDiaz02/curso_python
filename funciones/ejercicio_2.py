import math
from queue import Empty
#ejercico1

lista = []

def numero():
    i = 0
    while i < 2:
        numero = float(input("ingresa un numero: "))
        lista.append(numero)
        i += 1
    lista.sort
    for i in lista:
        if lista[0] > lista[1]:
            return 1
        elif lista[0] < lista[1]:
            return -1
        else:
            return 0

        

print(numero())

#ejercicio2

def descuento():
    precio = float(input("ingrese el total de la factura: "))
    iva = int(input("ingrese el IVA a aplicar: "))
    total = (precio) * iva/100
    if iva == 0:
        print("el valor de la factura es: ", precio + ((precio) * 0.21))
    else:
        print("el total de la factura es : ", precio + total) 

descuento()