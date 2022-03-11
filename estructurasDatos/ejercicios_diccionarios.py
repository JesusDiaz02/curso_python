diccionario ={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("ingrese un pais para la busqueda: ")


if pais.title() in diccionario:
    print("la capital del pais es : ", diccionario[pais.title()])
else:
    print("el pais no se encuentra registrado")


#ejercicio 2

diccionario2 = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

numero = int(input("Pregunte por el numero del jugador: "))

if numero in diccionario2.keys():
    print("El jugador correspondiente a ese numero es: ", diccionario2[numero])
else:
    print("El numero no esta asociado a ningun jugador") 