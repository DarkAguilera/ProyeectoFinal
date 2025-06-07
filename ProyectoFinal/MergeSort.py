# 4. Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])
    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado += izq[i:]
    resultado += der[j:]
    return resultado

lista = [8, -3, 7, -1, 2, -6, 4, 0]
print("4. Merge Sort:", merge_sort(lista))
# Explicación: Divide y conquista. Mezcla listas ordenadas.
