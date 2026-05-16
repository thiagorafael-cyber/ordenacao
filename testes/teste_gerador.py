import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testes.gerador_vetores import (
    gerar_vetor_crescente,
    gerar_vetor_decrescente,
    gerar_vetor_aleatorio
)


tamanho = 10

vetor_crescente = gerar_vetor_crescente(tamanho)
vetor_decrescente = gerar_vetor_decrescente(tamanho)
vetor_aleatorio = gerar_vetor_aleatorio(tamanho)

print("Vetor crescente:")
print(vetor_crescente)

print("\nVetor decrescente:")
print(vetor_decrescente)

print("\nVetor aleatório:")
print(vetor_aleatorio)