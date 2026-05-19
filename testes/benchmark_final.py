import sys
import os
import time
import csv

sys.setrecursionlimit(1000000) # Aumenta o limite de recursão do Python.

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


TODOS_ALGORITMOS = {
    "1": ("Insertion Sort", insertion_sort),
    "2": ("Bubble Sort", bubble_sort),
    "3": ("Merge Sort", merge_sort),
    "4": ("Heap Sort", heap_sort),
    "5": ("Quick Sort", quick_sort),
}


TODAS_ENTRADAS = {
    "1": ("Crescente", gerar_vetor_crescente),
    "2": ("Decrescente", gerar_vetor_decrescente),
    "3": ("Aleatório", gerar_vetor_aleatorio),
}


TAMANHOS_FINAIS = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

REPETICOES = 3

ARQUIVO_SAIDA = "resultados/resultados_benchmark_final.csv"


def vetor_esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False

    return True


def salvar_resultados(resultados):
    os.makedirs("resultados", exist_ok=True)

    campos = [
        "algoritmo",
        "tipo_entrada",
        "tamanho",
        "tempo_medio",
        "comparacoes_medias",
        "status"
    ]

    with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(resultados)


def executar_teste(nome_algoritmo, funcao_algoritmo, tipo_entrada, vetor_original, repeticoes):
    soma_tempo = 0
    soma_comparacoes = 0

    for execucao in range(1, repeticoes + 1):
        vetor = vetor_original.copy()

        print(f"  Execução {execucao}/{repeticoes}...", end=" ")

        inicio = time.perf_counter()
        vetor_ordenado, comparacoes = funcao_algoritmo(vetor)
        fim = time.perf_counter()

        tempo_execucao = fim - inicio

        if not vetor_esta_ordenado(vetor_ordenado):
            print("ERRO")
            raise ValueError(f"{nome_algoritmo} não ordenou corretamente o vetor.")

        print(f"{tempo_execucao:.6f}s")

        soma_tempo += tempo_execucao
        soma_comparacoes += comparacoes

    media_tempo = soma_tempo / repeticoes
    media_comparacoes = soma_comparacoes / repeticoes

    return {
        "algoritmo": nome_algoritmo,
        "tipo_entrada": tipo_entrada,
        "tamanho": len(vetor_original),
        "tempo_medio": media_tempo,
        "comparacoes_medias": media_comparacoes,
        "status": "OK"
    }


def executar_benchmark(algoritmos_escolhidos, entradas_escolhidas, tamanhos_escolhidos):
    resultados = []

    for tamanho in tamanhos_escolhidos:
        print("\n" + "=" * 70)
        print(f"TESTANDO VETORES DE TAMANHO {tamanho}")
        print("=" * 70)

        entradas_geradas = []

        for nome_entrada, funcao_geradora in entradas_escolhidas:
            vetor = funcao_geradora(tamanho)
            entradas_geradas.append((nome_entrada, vetor))

        for tipo_entrada, vetor_original in entradas_geradas:
            print(f"\nEntrada: {tipo_entrada}")

            for nome_algoritmo, funcao_algoritmo in algoritmos_escolhidos:
                print(f"\nExecutando {nome_algoritmo} | {tipo_entrada} | tamanho {tamanho}")

                try:
                    resultado = executar_teste(
                        nome_algoritmo,
                        funcao_algoritmo,
                        tipo_entrada,
                        vetor_original,
                        REPETICOES
                    )

                except RecursionError:
                    print("ERRO: limite de recursão atingido.")

                    resultado = {
                        "algoritmo": nome_algoritmo,
                        "tipo_entrada": tipo_entrada,
                        "tamanho": tamanho,
                        "tempo_medio": "",
                        "comparacoes_medias": "",
                        "status": "ERRO_RECURSAO"
                    }

                except KeyboardInterrupt:
                    print("\nBenchmark interrompido pelo usuário.")
                    salvar_resultados(resultados)
                    print(f"Resultados parciais salvos em: {ARQUIVO_SAIDA}")
                    return

                except Exception as erro:
                    print(f"ERRO: {erro}")

                    resultado = {
                        "algoritmo": nome_algoritmo,
                        "tipo_entrada": tipo_entrada,
                        "tamanho": tamanho,
                        "tempo_medio": "",
                        "comparacoes_medias": "",
                        "status": "ERRO"
                    }

                resultados.append(resultado)
                salvar_resultados(resultados)

    print("\nBenchmark finalizado.")
    print(f"Resultados salvos em: {ARQUIVO_SAIDA}")


def mostrar_algoritmos():
    print("\nAlgoritmos disponíveis:")

    for chave, dados in TODOS_ALGORITMOS.items():
        nome_algoritmo, _ = dados
        print(f"{chave} - {nome_algoritmo}")


def mostrar_entradas():
    print("\nTipos de entrada disponíveis:")

    for chave, dados in TODAS_ENTRADAS.items():
        nome_entrada, _ = dados
        print(f"{chave} - {nome_entrada}")


def escolher_algoritmos():
    mostrar_algoritmos()

    escolha = input("\nDigite os números dos algoritmos separados por vírgula ou 'todos': ")

    if escolha.lower() == "todos":
        return list(TODOS_ALGORITMOS.values())

    algoritmos_escolhidos = []

    for item in escolha.split(","):
        item = item.strip()

        if item in TODOS_ALGORITMOS:
            algoritmos_escolhidos.append(TODOS_ALGORITMOS[item])

    return algoritmos_escolhidos


def escolher_entradas():
    mostrar_entradas()

    escolha = input("\nDigite os números dos tipos de entrada separados por vírgula ou 'todos': ")

    if escolha.lower() == "todos":
        return list(TODAS_ENTRADAS.values())

    entradas_escolhidas = []

    for item in escolha.split(","):
        item = item.strip()

        if item in TODAS_ENTRADAS:
            entradas_escolhidas.append(TODAS_ENTRADAS[item])

    return entradas_escolhidas


def escolher_tamanhos():
    print("\nTamanhos finais do trabalho:")
    print(TAMANHOS_FINAIS)

    escolha = input("\nDigite os tamanhos separados por vírgula ou 'todos': ")

    if escolha.lower() == "todos":
        return TAMANHOS_FINAIS

    tamanhos_escolhidos = []

    for item in escolha.split(","):
        item = item.strip()

        if item.isdigit():
            tamanhos_escolhidos.append(int(item))

    return tamanhos_escolhidos


def confirmar_benchmark_completo():
    print("\nATENÇÃO:")
    print("O benchmark completo pode demorar muito, principalmente para Bubble Sort,")
    print("Insertion Sort e Quick Sort em entradas crescentes ou decrescentes.")
    print("Esses casos podem ter comportamento quadrático.")

    resposta = input("\nDeseja continuar mesmo assim? (s/n): ")

    return resposta.lower() == "s"


def menu():
    while True:
        print("\n" + "=" * 70)
        print("BENCHMARK FINAL - ALGORITMOS DE ORDENAÇÃO")
        print("=" * 70)
        print("1 - Rodar benchmark completo exigido no trabalho")
        print("2 - Rodar teste rápido")
        print("3 - Escolher algoritmos, entradas e tamanhos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            if confirmar_benchmark_completo():
                executar_benchmark(
                    list(TODOS_ALGORITMOS.values()),
                    list(TODAS_ENTRADAS.values()),
                    TAMANHOS_FINAIS
                )

        elif opcao == "2":
            executar_benchmark(
                list(TODOS_ALGORITMOS.values()),
                list(TODAS_ENTRADAS.values()),
                [100, 1000, 5000]
            )

        elif opcao == "3":
            algoritmos_escolhidos = escolher_algoritmos()
            entradas_escolhidas = escolher_entradas()
            tamanhos_escolhidos = escolher_tamanhos()

            if not algoritmos_escolhidos:
                print("Nenhum algoritmo válido foi escolhido.")
                continue

            if not entradas_escolhidas:
                print("Nenhum tipo de entrada válido foi escolhido.")
                continue

            if not tamanhos_escolhidos:
                print("Nenhum tamanho válido foi escolhido.")
                continue

            executar_benchmark(
                algoritmos_escolhidos,
                entradas_escolhidas,
                tamanhos_escolhidos
            )

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()