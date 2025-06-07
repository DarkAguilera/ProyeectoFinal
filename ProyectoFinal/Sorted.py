# 1. sorted() con clave personalizada
personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Marta", "edad": 35}
]
ordenadas = sorted(personas, key=lambda p: p["edad"])
print("1. sorted():", ordenadas)
# Explicación: 'sorted()' retorna una nueva lista ordenada. Aquí ordenamos por la clave 'edad'.
