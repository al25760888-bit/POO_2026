from Herramienta import Herramienta

class Pala(Herramienta):
    @property
    def nombre(self):
        return "Pala"

    def usar(self, objetivo: str) -> str:
        if self.rota: return f"¡La {self.nombre} está rota!"
        daño = self.calcular_daño()
        self.desgastar()
        return f"⏳ Excavando {objetivo}... (Poder de paleo: {daño})"