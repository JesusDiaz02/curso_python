while True:
    try: 
        edad = int(input('ingrese su edad: '))
        print(f'tu edad es:{edad}')
        break
    except:
        print('ingresaste un valor erroneo')
    finally:
        print('la ejecucion a finalizado')


while True:
    try:
        numero1=int(input('ingresa un numero: '))
        resultado = 100 / numero1
        print(resultado)
        break
    except ZeroDivisionError:
        print('no se puede dividir entre cero')


while True:
    try:
        edad=int(input('ingresa tu edad: '))
        print(f'tu edad es: {edad}')
        break
    except KeyboardInterrupt:
        print("\nhas canselado la ejecucion")
        break
