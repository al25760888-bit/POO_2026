from Mob import Mob

class Zombie(Mob):
    def hacer_sonido(self):
        return "Bruaaaarrgh..."

    def comportamiento(self):
        return "Hostil: Persigue al jugador y quema bajo el sol."

    def moverse(self):
        return "Camina pesadamente hacia el objetivo."