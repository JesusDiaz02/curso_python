#class fabricaTelefono():
 #   marca = "samsung"


  #  def elaborarhuawei(self):
   #     self.marca = "huawei"


#telefono = fabricaTelefono()
#telefono.elaborarhuawei()
#print(telefono.marca)

#class fabricatelefono():
 #   def __init__(self, marca, color):
  #      self.marca = marca
   #     self.color = color
#telefono = fabricatelefono('huawei', 'negro')  
#print(telefono.marca)

class fabricaTEl():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print(f'el objeto {self.marca} ha sido creado')
    
        def __str__(self):
            return (f'el objeto es {self.marca}')

        def __del__(self):
            print(f'el objeto {self.marca} ha sido destruido')

telefono = fabricaTEl("nokia", "negro")
print(telefono.marca)
print(telefono)