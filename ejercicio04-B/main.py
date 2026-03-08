from Guerrero import Guerrero
from Mago import Mago 
from Arquero import Arquero


guerrero = Guerrero("Grog", 15, "Hacha Doble")
mago = Mago("Zephyr", 22, "Tormenta de Escarcha")
arquero = Arquero("Lira", 18, 50)


taberna = [guerrero, mago, arquero]

print("--- Registro de la Taberna de los Aventureros ---")
for heroe in taberna:
    heroe.presentarse()
    heroe.usar_habilidad()
    print("-" * 20)