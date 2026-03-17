
from Arco import Arco
from  Espada import Espada
from Pala import Pala
from Pico import Pico




if __name__ == "__main__":
    # 1. Prueba básica
    mis_herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Arco("madera", 10,2),
        Pala("Tierra",3)
    ]

    print("--- 🔨 PRUEBA DE HERRAMIENTAS ---")
    for h in mis_herramientas:
        objetivo = "Zombie" if isinstance(h, (Espada, Arco)) else "Piedra"
        print(h.usar(objetivo))
        h.estado()
        print("-" * 30)

    # 2. Prueba de durabilidad extrema (Tarea 2)
    print("\n--- 🧨 PROBANDO DURABILIDAD HASTA ROMPER ---")
    pala_vieja = Pala("madera", 3)
    
    while not pala_vieja.rota:
        print(pala_vieja.usar("Tierra"))
        pala_vieja.estado()
    
    # Intento de uso final
    print(pala_vieja.usar("Tierra"))
    
"""if __name__ == "__main__":
        herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
    ]
    objetivos = ["mena de diamante", "Creeper", "arena"]

for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()"""