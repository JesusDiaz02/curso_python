#ejercicio1
import math


def area_cuadrado():
    base= float(input('ingrese la medidad de la base: '))
    altura= float(input('ingrese la medida de la altura: '))
    area = base * altura
    print(f'el area del cuadrado es de: {area}(2)')

area_cuadrado()

def area_circulo():
    radio = float(input('ingrese el radio del circulo: '))
    area2= math.pi * radio**2
    print(f'el area del circulo es de: {area2}')

area_circulo()

#ejercicio2
def lista_numeros():
    lista = []
    i = 0
    while i <=10000:
        num = float(input("ingresa un numero: "))
        lista.append(num)
        i += 1 
        print(len(lista))

lista_numeros()
