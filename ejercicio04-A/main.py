from Comida import Comida
from Bebida import Bebida
from Postre import Postre
def ejecutar_menu():
    # Creamos los objetos
    platillo1 = Comida("Enchiladas Verdes", 120.50, "Plato Principal")
    platillo2 = Bebida("Café Americano", 45.00, "Caliente")
    platillo3 = Postre("Pastel de Chocolate", 85.00, False)

    
    menu = [platillo1, platillo2, platillo3]

    print("--- MENÚ DEL RESTAURANTE ---")
    for item in menu:
        item.mostrar_info()
        item.tipo()
        print("-" * 25)

if __name__ == "__main__":
    ejecutar_menu()