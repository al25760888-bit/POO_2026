
from Mob import Mob 
class Creeper(Mob):
    def hacer_sonido(self):
        return "Tssssssss..."

    def comportamiento(self):
        return "Hostil: Explota cerca del jugador."

    def moverse(self):
        return "Acecha silenciosamente."