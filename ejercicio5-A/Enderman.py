
from Mob import Mob 

class Enderman(Mob):
    def hacer_sonido(self):
        return "Vwoop! (Sonido distorsionado)"

    def comportamiento(self):
        return "Neutral: Ataca si lo miras a los ojos."

    def moverse(self):
        return "Se teletransporta aleatoriamente."
