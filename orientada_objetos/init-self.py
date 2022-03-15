#class fabricaTelefono():
 #   marca = "samsung"


  #  def elaborarhuawei(self):
   #     self.marca = "huawei"


#telefono = fabricaTelefono()
#telefono.elaborarhuawei()
#print(telefono.marca)

class fabricatelefono():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
telefono = fabricatelefono('huawei', 'negro')  
print(telefono.marca)