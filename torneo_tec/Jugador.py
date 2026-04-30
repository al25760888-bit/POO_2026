
class Jugador:

    def __init__(self, nombre: str, num_control: str, nivel: str, puntos:int):
      self.nombre=nombre
      self.num_control=num_control
      self.nivel=nivel
      self.puntos=puntos
    
    def ganar_puntos(self, cantidad):
        
        self.puntos+=cantidad
        print(f"{self.nombre} gano {cantidad} puntos Total: {self.puntos}")
    
    def perder_puntos(self, cantidad):
        if cantidad>0 :
            self.puntos-=cantidad
            print(f"{self.nombre} perdio {cantidad} puntos Total: {self.puntos}" )
    
    def mostrar_perfil(self):
        print("Perfil del jugador")
        print(f"nombre:{self.nombre}")
        print(f"numero de control: {self.num_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos Totales: {self.puntos}")
        
@property
def nombre(self):
        return self.__nombre