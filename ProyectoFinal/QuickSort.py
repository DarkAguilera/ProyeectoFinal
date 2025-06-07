# 3. Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)

lista = [3, -1, 4, -1, 5, 9, -2, 6, 5, 3]
print("3. Quick Sort:", quick_sort(lista))
# Explicación: Divide usando un pivote, y ordena recursivamente cada mitad.