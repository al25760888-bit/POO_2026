from Jugador import Jugador

class Competidor(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, equipo):
        # Llamada al constructor de la clase base
        super().__init__(nombre, num_control, nivel, puntos)
        self.__equipo = equipo

    def mostrar_perfil(self):
        # Sobreescritura del método (Override)
        super().mostrar_perfil()
        print(f"Equipo: {self.__equipo}")
        print("Tipo: Competidor")