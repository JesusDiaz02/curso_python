#ejercicio 1
for i in range(0,10):
    print(i+1)

numero1= int(input("ingrese un numero: "))
numero2= int(input("ingrese un numero con valor mayor al anterior: "))
for j in range(numero1,numero2):
    print(j+1)

#ejrcicio 2

numero3 = int(input("ingrese un numero: "))
numero4 = int(input("ingrese un numero con valor mayor al anterior: "))

for h in range(numero3, numero4):
    if h%2!=0:
        print(h)
