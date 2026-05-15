import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.quick_sort import quick_sort

vetor = [5, 2, 4, 6, 1, 3]

ordenado, comparacoes = quick_sort(vetor.copy())

print("Vetor original:", vetor)
print("Vetor ordenado:", ordenado)
print("Comparações:", comparacoes)