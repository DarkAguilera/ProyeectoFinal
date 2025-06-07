# 6. Bubble Sort

def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

lista = [1, 2, 3, 5, 4]
print("6. Bubble Sort:", bubble_sort(lista))
# Explicación: Compara elementos adyacentes y los intercambia si están desordenados.