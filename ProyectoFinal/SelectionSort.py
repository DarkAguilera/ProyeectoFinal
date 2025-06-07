# 8. Selection Sort

def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

lista = [7, 4, 6, 2, 3, 9, 1]
print("8. Selection Sort:", selection_sort(lista))
# Explicación: Busca el mínimo en cada iteración y lo coloca en su lugar.