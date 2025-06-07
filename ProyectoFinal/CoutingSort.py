# 10. Counting Sort

def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    min_val = min(arr)
    rango = max_val - min_val + 1
    conteo = [0] * rango
    for num in arr:
        conteo[num - min_val] += 1
    resultado = []
    for i in range(rango):
        resultado.extend([i + min_val] * conteo[i])
    return resultado

lista = [5, 3, 6, 5, 3, 2, 4, 1, 0]
print("10. Counting Sort:", counting_sort(lista))
# Explicación: Cuenta ocurrencias y reconstruye lista ordenada. No compara.