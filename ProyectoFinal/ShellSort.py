# 9. Shell Sort

def shell_sort(arr):
    arr = arr[:]
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

import random
lista = random.sample(range(100), 20)
print("9. Shell Sort:", shell_sort(lista))
# Explicación: Ordena usando espacios (gaps) para mejorar la eficiencia del insertion sort.