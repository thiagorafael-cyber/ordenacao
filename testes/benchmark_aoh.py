import sys
import os
import time
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algoritmos.aoh import aoh

from testes.gerador_vetores import (
    gerar_vetor_crescente,
    gerar_vetor_decrescente,
    gerar_vetor_aleatorio
)


LIMITES_AOH = [16, 32, 64, 128]

TAMANHOS_FINAIS = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

TIPOS_ENTRADA = [
    ("Crescente", gerar_vetor_crescente),
    ("Decrescente", gerar_vetor_decrescente),
    ("Aleatório", gerar_vetor_aleatorio)
]

REPETICOES_PADRAO = 3

ARQUIVO_SAIDA_PADRAO = "resultados_aoh_limites.csv"


def vetor_esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False

    return True


def escolher_arquivo_saida():
    print("\nArquivo de saída")
    print("Digite apenas o nome do arquivo CSV.")
    print(f"Se deixar em branco, será usado: {ARQUIVO_SAIDA_PADRAO}")

    while True:
        nome_arquivo = input("\nNome do arquivo de saída: ").strip()

        if nome_arquivo == "":
            nome_arquivo = ARQUIVO_SAIDA_PADRAO

        if not nome_arquivo.endswith(".csv"):
            nome_arquivo += ".csv"

        os.makedirs("resultados", exist_ok=True)

        arquivo_saida = os.path.join("resultados", nome_arquivo)

        if os.path.exists(arquivo_saida):
            resposta = input(
                f"O arquivo '{arquivo_saida}' já existe. Deseja sobrescrever? (s/n): "
            ).strip().lower()

            if resposta == "s":
                return arquivo_saida
            else:
                print("Escolha outro nome para o arquivo.")
        else:
            return arquivo_saida


def escolher_repeticoes():
    print("\nNúmero de repetições")
    print("Digite o número de repetições para cada teste.")
    print(f"Se deixar em branco, será usado: {REPETICOES_PADRAO}")

    escolha = input("\nNúmero de repetições: ").strip()

    if escolha == "":
        return REPETICOES_PADRAO

    if escolha.isdigit():
        repeticoes = int(escolha)

        if repeticoes > 0:
            return repeticoes

    print("Valor inválido. Será usado o padrão.")
    return REPETICOES_PADRAO


def salvar_resultados(resultados, arquivo_saida):
    os.makedirs("resultados", exist_ok=True)

    campos = [
        "algoritmo",
        "limite",
        "tipo_entrada",
        "tamanho",
        "repeticoes",
        "tempo_medio",
        "comparacoes_medias",
        "status"
    ]

    with open(arquivo_saida, "w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(resultados)


def executar_teste_aoh(limite, tipo_entrada, vetor_original, repeticoes):
    soma_tempo = 0
    soma_comparacoes = 0

    for execucao in range(1, repeticoes + 1):
        vetor = vetor_original.copy()

        print(f"  Execução {execucao}/{repeticoes}...", end=" ")

        inicio = time.perf_counter()
        vetor_ordenado, comparacoes = aoh(vetor, limite=limite)
        fim = time.perf_counter()

        tempo_execucao = fim - inicio

        if not vetor_esta_ordenado(vetor_ordenado):
            print("ERRO")
            raise ValueError("AOH não ordenou corretamente o vetor.")

        print(f"{tempo_execucao:.6f}s")

        soma_tempo += tempo_execucao
        soma_comparacoes += comparacoes

    media_tempo = soma_tempo / repeticoes
    media_comparacoes = soma_comparacoes / repeticoes

    return {
        "algoritmo": "AOH Merge+Insertion",
        "limite": limite,
        "tipo_entrada": tipo_entrada,
        "tamanho": len(vetor_original),
        "repeticoes": repeticoes,
        "tempo_medio": media_tempo,
        "comparacoes_medias": media_comparacoes,
        "status": "OK"
    }


def executar_benchmark_aoh(arquivo_saida, repeticoes):
    resultados = []

    for tamanho in TAMANHOS_FINAIS:
        print("\n" + "=" * 70)
        print(f"TESTANDO VETORES DE TAMANHO {tamanho}")
        print("=" * 70)

        entradas_geradas = []

        for nome_entrada, funcao_geradora in TIPOS_ENTRADA:
            vetor = funcao_geradora(tamanho)
            entradas_geradas.append((nome_entrada, vetor))

        for tipo_entrada, vetor_original in entradas_geradas:
            print(f"\nEntrada: {tipo_entrada}")

            for limite in LIMITES_AOH:
                print(
                    f"\nExecutando AOH Merge+Insertion | limite {limite} | "
                    f"{tipo_entrada} | tamanho {tamanho}"
                )

                try:
                    resultado = executar_teste_aoh(
                        limite,
                        tipo_entrada,
                        vetor_original,
                        repeticoes
                    )

                except KeyboardInterrupt:
                    print("\nBenchmark interrompido pelo usuário.")
                    salvar_resultados(resultados, arquivo_saida)
                    print(f"Resultados parciais salvos em: {arquivo_saida}")
                    return

                except Exception as erro:
                    print(f"ERRO: {erro}")

                    resultado = {
                        "algoritmo": "AOH Merge+Insertion",
                        "limite": limite,
                        "tipo_entrada": tipo_entrada,
                        "tamanho": tamanho,
                        "repeticoes": repeticoes,
                        "tempo_medio": "",
                        "comparacoes_medias": "",
                        "status": "ERRO"
                    }

                resultados.append(resultado)
                salvar_resultados(resultados, arquivo_saida)

    print("\nBenchmark do AOH finalizado.")
    print(f"Resultados salvos em: {arquivo_saida}")


def main():
    print("\n" + "=" * 70)
    print("BENCHMARK AOH - MERGE SORT + INSERTION SORT")
    print("=" * 70)
    print("Limites testados:", LIMITES_AOH)
    print("Tamanhos testados:", TAMANHOS_FINAIS)

    arquivo_saida = escolher_arquivo_saida()
    repeticoes = escolher_repeticoes()

    executar_benchmark_aoh(arquivo_saida, repeticoes)


if __name__ == "__main__":
    main()