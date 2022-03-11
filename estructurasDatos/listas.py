'''lista = ['python', 120, 'nombre', 4.14, 6.28]

print(lista)
print(lista[3])
print(len(lista))
lista[0] ="Phyton"
print(lista)

#debanado listas

lista2 =[10, 15, 65, 3.14, "lucha", "tatakae", "turiquitakati", 16]

print(lista2[5])
print(lista2[0:5])
print(lista2[ : 2])
print(lista2[1 : 0])
print(lista2[-1])
print(lista[-5 : -2])

#metodos listas
lista3 = [1, 2, 3, 4, 5]
print(lista)

lista3.append(6) #agregar al final
print(lista3)

lista3.insert(2, 2.5) #insertar en parte selaccionada
print(lista)

lista4 =[1,2,3,4,5,5,5,15,154,4,24,4,5,5,55,]

print(lista4.count(5))
print(lista4.index(4))
lista4.sort()
print(lista4)
lista4.reverse()
print(lista4)


#metodos 3

lista5 = ['python', 24, 'rene', 'alexander', 12]

lista5[3] = "Alexander"
print(lista5)
print(lista5[3])

lista.pop()
print(lista5)

lista5.remove('python')
print(lista5)'''

#lista vacia
nueva_lista = []

edad = int(input("ingrea tu edad: "))
nueva_lista.append(edad)
print(nueva_lista)