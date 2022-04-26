'''diccionario = {'nombre' : "yisus" , 'apellido' : 12345, 'estatura': 1.91}

print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario["estatura"])


diccionario["peso"] = "105kg"
print(diccionario)
diccionario['nombre'] = "jesus"
print(diccionario)'''



#metodos diccionarios
diccionario = {1 : 2 , 2 : 3 , 3 : 4 }
diccionario2 = {4: 5, 5: 6}

print(diccionario)
diccionario.pop(3)
print(diccionario)

print(diccionario.get(2))
diccionario.clear()

diccionario.setdefault(4 , 5)
print(diccionario)
diccionario.update(diccionario2)
print(diccionario)

diccionario.copy()
print(diccionario)