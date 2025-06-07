# 7. Insertion Sort

def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

lista = [1, 2, 4, 3, 5]
print("7. Insertion Sort:", insertion_sort(lista))
# Explicación: Inserta cada elemento en su posición correcta dentro de la lista ordenada.