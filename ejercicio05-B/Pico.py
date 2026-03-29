from Herramienta import Herramienta

class Pico(Herramienta):
    @property
    def nombre(self):
        return "Pico"

    def usar(self, objetivo: str) -> str:
        if self.rota: return f"¡El {self.nombre} está roto!"
        daño = self.calcular_daño()
        self.desgastar()
        return f"⛏️ Minando {objetivo}... ¡Bloque extraído! (Impacto: {daño})"