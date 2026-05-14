from algoritmos.merge_sort import merge_sort

vetor = [5, 2, 4, 6, 1, 3]

ordenado, comparacoes = merge_sort(vetor)

print("Vetor original:", [5, 2, 4, 6, 1, 3])
print("Vetor ordenado:", ordenado)
print("Comparações:", comparacoes)