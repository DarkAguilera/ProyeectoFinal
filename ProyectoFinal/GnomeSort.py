# 14. Gnome Sort

def gnome_sort(arr):
    arr = arr[:]
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

lista = [34, 2, 10, -9, 2, 10, 0, 3]
print("14. Gnome Sort:", gnome_sort(lista))
# Explicación: Avanza si está bien, retrocede si encuentra desorden (como un gnomo testarudo).