from Jugador import Jugador

class Observador(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, partidas_vistas):
        # Llamada al constructor de la clase base
        super().__init__(nombre, num_control, nivel, puntos)
        self.__partidas_vistas = partidas_vistas

    def ver_partida(self):
        self.__partidas_vistas += 1
        print(f"{self.nombre} esta viendo una partida. Total vistas: {self.__partidas_vistas}")

    def mostrar_perfil(self):
        # Sobreescritura del método (Override)
        super().mostrar_perfil()
        print(f"Partidas Vistas: {self.__partidas_vistas}")
        print("Tipo: Observador")