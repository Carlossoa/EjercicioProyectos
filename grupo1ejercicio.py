
def merge_sort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # 1. Dividir la lista en dos sublistas
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # 2. Ordenar recursivamente ambas mitades
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # 3. Combinar las sublistas ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izq, der):
    resultado = []
    i = j = 0

    # Mientras haya elementos en ambas listas
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Agregar elementos restantes si hay
    resultado += izq[i:]
    resultado += der[j:]
    return resultado

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]
ordenados = merge_sort(numeros)
print("Lista ordenada:", ordenados)
