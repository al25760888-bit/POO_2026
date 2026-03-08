#clase padre

class Animal:
    #creamos el contructor
    def __init__(self,nombre,edad):
        self.nombre=nombre 
        self.edad =edad
    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años") 
        
    def hablar(self):
        print("...")
        
#-------------------------------
#clase derivada o clase hija



#class Perro(Animal):
 #   def hablar(self):
 #       print(f"{self.nombre} : GUAU!!!")
#class Gato(Animal):
    #def hablar(self):
       # print(f"{self.nombre}: Miau!!!")
#uso
#se crearon las instancias
#pakito=Perro("Pakito",5)
#Salem=Gato('salem',7)

#usar las instancias

#Salem.hablar()
#pakito.hablar()
#Salem.describir()
