import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.insertion_sort import insertion_sort

vetor = [5, 2, 4, 6, 1, 3]

ordenado, comparacoes = insertion_sort(vetor)

print("Vetor ordenado:", ordenado)
print("Comparações:", comparacoes)