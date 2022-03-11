from ctypes.wintypes import PINT
from time import process_time_ns


vocal = input("ingrese voval en minuscula: ")
letra = input("ingrese letra en mayuscula: ")

print(vocal.upper())
print(letra.lower())
print(vocal + letra)
print(vocal.upper()+letra.lower())

#ejercicio2

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
genero = input("digite su genero: ")

print("te llamas : {}  \ntu edad es: {} \neres: {}".format(nombre,edad,genero))