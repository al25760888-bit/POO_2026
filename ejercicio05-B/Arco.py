from Herramienta import Herramienta


class Arco(Herramienta):
    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self.flechas = flechas

    @property
    def nombre(self):
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.rota: return "¡El arco se ha partido!"
        if self.flechas <= 0: return "🏹 ¡Click! Sin flechas en el inventario."
        
        self.flechas -= 1
        self.desgastar()
        return f"🏹 ¡Zas! Flecha disparada a {objetivo}. (Quedan {self.flechas} flechas)"