#ejercico 1
vocal = input("ingrese una vocal: ")

'''if vocal.lower() == "a":
    print("Es vocal")
elif vocal.lower() == "e":
    print("es vocal")
elif vocal.lower() == "i":
    print("es vocal")
elif vocal.lower() == "o":
    print("es vocal")
elif vocal.lower() == "u":
    print("es vocal")
else:
    print("esto no es una vocal")'''
if vocal.lower() in "aeiou":
    print("es una vocal")
else:
    print("no es una vocal")


    #ejercico 2
numero = int(input("inserte un numero: "))

if numero >= 0:
    print("el valor absoluto del numero es: ",numero)
else: 
    print("el valor absoluto del numero es: ",numero * -1)

    
#ejercicio 3
palabra1 = input("inserte la primer palabra: ")
palabra2 = input("inserte la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No rima porque tiene menos de tres caracteres")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print("las palabras riman")
elif palabra1[-2 : ] == palabra2[-2:]:
    print("las palabras riman un poco")
else:
    print("las palabras no riman")

#ejercicio 4

candidato = input("ingrese la opcion de su candidato: " )

if candidato.upper() == "a":
    print("usted a votado por el partido rojo" )
elif candidato.upper() == "b":
    print("Usted a votado por el partido verde")
elif candidato.upper() == "c":
    print("usted a votado por el partido azul")
else:
    print("opcion incorrecta") 
    