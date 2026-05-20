import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.aoh import aoh


vetor = [5, 2, 4, 6, 1, 3]

ordenado, comparacoes = aoh(vetor.copy(), limite=32)

print("Vetor original:", vetor)
print("Vetor ordenado:", ordenado)
print("Comparações:", comparacoes)