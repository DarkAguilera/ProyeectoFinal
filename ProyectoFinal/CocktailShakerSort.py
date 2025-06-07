# 15. Cocktail Shaker Sort

def cocktail_shaker_sort(arr):
    arr = arr[:]
    n = len(arr)
    inicio = 0
    fin = n - 1
    while inicio < fin:
        for i in range(inicio, fin):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        fin -= 1
        for i in range(fin, inicio, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        inicio += 1
    return arr

lista = [3, 2, 5, 4, 6, 7, 1]
print("15. Cocktail Shaker Sort:", cocktail_shaker_sort(lista))
# Explicación: Ordena hacia adelante y hacia atrás en cada pasada.
