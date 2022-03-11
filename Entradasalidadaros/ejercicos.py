#ejercicio1
from math import sqrt

A = int(input("ingresa el valor de A: "  ))
B = int(input("ingresa el valor de B: ")) 
C = int(input("ingresa el valor de C: "))
x1 = 0
x2 = 0

if(B**2)-(4*A*C) < 0:
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)

    print("la solucion es \nx1=",x1, "\nx2=",x2)
#ejercico2

examen_parcial = float(input('inserte nota del examen parcial: '))
examen_final = float(input('inserte nota del examen : '))
practica_1 = float(input('nota practica 1: '))
practica_2 = float(input('nota practica 2: '))
practica_3 = float(input('nota practica 3: '))

promedio_practicas = ((practica_1+practica_2+practica_3)/3)
print("el promedio de las practicas es: ",promedio_practicas )

promedio_total = ((promedio_practicas+(2*examen_parcial)+(3*examen_final))/6)
print("El promedio total del estudiantes es: ",promedio_total)