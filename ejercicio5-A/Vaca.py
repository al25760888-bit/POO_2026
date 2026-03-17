from Mob import Mob

class Vaca(Mob):
    def hacer_sonido(self):
        return "Mooo!"

    def comportamiento(self):
        return "Pasivo: Huye si es atacada."

    def moverse(self):
        return "Camina lentamente buscando pasto."