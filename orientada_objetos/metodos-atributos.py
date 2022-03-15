class FabricaCelular():
    marca = "huawei"
    color = "negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print('estas escuchando musica')

telefono = FabricaCelular()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar('hola cole, que todo bien?'))
telefono.escucharMusica()