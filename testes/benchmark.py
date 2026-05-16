import sys
import os
import time
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.insertion_sort import insertion_sort
from algoritmos.bubble_sort import bubble_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quick_sort

from testes.gerador_vetores import (
    gerar_vetor_crescente,
    gerar_vetor_decrescente,
    gerar_vetor_aleatorio
)


def executar_teste(nome_algoritmo, funcao_algoritmo, tipo_entrada, vetor_original, repeticoes):
    soma_tempo = 0
    soma_comparacoes = 0

    for execucao in range(repeticoes):
        vetor = vetor_original.copy()

        inicio = time.perf_counter()
        vetor_ordenado, comparacoes = funcao_algoritmo(vetor)
        fim = time.perf_counter()

        tempo_execucao = fim - inicio

        soma_tempo += tempo_execucao
        soma_comparacoes += comparacoes

    media_tempo = soma_tempo / repeticoes
    media_comparacoes = soma_comparacoes / repeticoes

    return {
        "algoritmo": nome_algoritmo,
        "tipo_entrada": tipo_entrada,
        "tamanho": len(vetor_original),
        "tempo_medio": media_tempo,
        "comparacoes_medias": media_comparacoes
    }


def main():
    algoritmos = [
        ("Insertion Sort", insertion_sort),
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Heap Sort", heap_sort),
        ("Quick Sort", quick_sort),
    ]

    tamanhos = [500]
    repeticoes = 3

    resultados = []

    for tamanho in tamanhos:
        entradas = [
            ("Crescente", gerar_vetor_crescente(tamanho)),
            ("Decrescente", gerar_vetor_decrescente(tamanho)),
            ("Aleatório", gerar_vetor_aleatorio(tamanho)),
        ]

        for tipo_entrada, vetor_original in entradas:
            for nome_algoritmo, funcao_algoritmo in algoritmos:
                print(f"Executando {nome_algoritmo} | {tipo_entrada} | tamanho {tamanho}")

                resultado = executar_teste(
                    nome_algoritmo,
                    funcao_algoritmo,
                    tipo_entrada,
                    vetor_original,
                    repeticoes
                )

                resultados.append(resultado)

    os.makedirs("resultados", exist_ok=True)

    with open("resultados/resultados_parte1.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        campos = ["algoritmo", "tipo_entrada", "tamanho", "tempo_medio", "comparacoes_medias"]
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(resultados)

    print("\nBenchmark finalizado.")
    print("Resultados salvos em: resultados/resultados_parte1.csv")


if __name__ == "__main__":
    main()