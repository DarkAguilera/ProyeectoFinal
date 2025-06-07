# 5. Heap Sort
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

lista = [4, 1, 3, 2, 1, 4, 6, 5]
print("5. Heap Sort:", heap_sort(lista[:]))
# Explicación: Convierte en heap y extrae en orden.