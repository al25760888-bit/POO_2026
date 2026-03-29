from Herramienta import Herramienta

class Espada(Herramienta):
    @property
    def nombre(self):
        return "Espada"

    def usar(self, objetivo: str) -> str:
        if self.rota: return f"¡La {self.nombre} está rota!"
        daño = self.calcular_daño()
        self.desgastar()
        return f"⚔️ Atacando a {objetivo}... ¡Daño crítico de {daño}!"