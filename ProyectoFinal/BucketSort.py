# 12. Bucket Sort

def bucket_sort(arr):
    if not arr:
        return []
    buckets = [[] for _ in range(10)]
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    for i in range(len(buckets)):
        buckets[i] = bubble_sort(buckets[i])

    return [num for bucket in buckets for num in bucket]

lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("12. Bucket Sort:", bucket_sort(lista))
# Explicación: Distribuye en cubetas y luego ordena cada cubeta usando Bubble Sort.