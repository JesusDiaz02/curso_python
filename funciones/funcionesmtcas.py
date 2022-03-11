import math 
import random

'''print(math.pow(10 , 2))
print(math.sqrt(64))
print(math.isqrt(64))
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))
print(math.factorial(5))

print(random.randint(10 , 1000))'''

def entero():
    print('este es un dato entero: ')
    return 10

def decimal():
    print('este es un decimal: ')
    return 10.10


def frase():
    return "ahhhhhhhhhhhhhhh "

def asignacion():
    return 1 , 2 , 3 , 4 , 5
 


a , b , c , d , e = asignacion()  
print(entero())
print(decimal())
print(frase())
print(e)