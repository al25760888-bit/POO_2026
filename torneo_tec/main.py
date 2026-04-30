
from Jugador import Jugador
from Competidor import Competidor
from Observador import Observador


if __name__ == "__main__":
    player1 = Competidor("Alex", "A101", "Oro", 1500, "Team Liquid")
    player2 = Observador("Sofia", "B202", "Bronce", 100, 45)

    player1.ganar_puntos(50)
    player1.mostrar_perfil()
    
    print("\n" + "="*20 + "\n")
    
    player2.ver_partida()
    player2.mostrar_perfil()