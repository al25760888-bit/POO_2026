import os

ruta="test.txt"
#nos va a regresar el tamano en bits
size=os.path.getsize(ruta)
kb=size/1024
mb=size/(1024**2)

print(f"Tamaño del archivo {kb:.2f} KB")
print(f"Tamaño del archivo {mb:.4f} MB")