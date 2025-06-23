def merge_sort_productos(productos):
    if len(productos) <= 1:
        return productos

    mitad = len(productos) // 2
    izquierda = merge_sort_productos(productos[:mitad])
    derecha = merge_sort_productos(productos[mitad:])

    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i]["precio"] <= der[j]["precio"]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Lista de productos
productos = [
    {"nombre": "Audífonos", "precio": 25.99},
    {"nombre": "Laptop", "precio": 799.99},
    {"nombre": "Mouse", "precio": 15.49},
    {"nombre": "Teclado", "precio": 45.00},
    {"nombre": "Monitor", "precio": 189.99}
]

# Ordenar productos por precio
ordenados = merge_sort_productos(productos)

# Mostrar productos ordenados
print("Productos ordenados por precio:")
for p in ordenados:
    print(f"{p['nombre']} - ${p['precio']}")
