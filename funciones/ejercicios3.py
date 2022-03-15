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

def medida(*tupla):
    return len(tupla)
    for i in  tupla:
        print(i)
    return len(tupla)

print(medida(2, 3 ,4 ,5,5 ,2,3 ,4,8))
