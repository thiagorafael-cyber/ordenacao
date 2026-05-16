import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.insertion_sort import insertion_sort
from algoritmos.bubble_sort import bubble_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quick_sort


vetor = [5, 2, 4, 6, 1, 3]

algoritmos = [
    ("Insertion Sort", insertion_sort),
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Heap Sort", heap_sort),
    ("Quick Sort", quick_sort),
]

for nome, algoritmo in algoritmos:
    ordenado, comparacoes = algoritmo(vetor.copy())

    print(f"Algoritmo: {nome}")
    print("Vetor original:", vetor)
    print("Vetor ordenado:", ordenado)
    print("Comparações:", comparacoes)
    print("-" * 40)