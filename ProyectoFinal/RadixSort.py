# 11. Radix Sort

def counting_sort_digito(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    return output

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_digito(arr, exp)
        exp *= 10
    return arr

lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("11. Radix Sort:", radix_sort(lista))
# Explicación: Ordena por cada dígito, de menor a mayor.