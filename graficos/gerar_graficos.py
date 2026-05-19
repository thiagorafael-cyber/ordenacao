import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


ARQUIVOS_CSV = [
    "resultados/resultados_bubble_completo.csv",
    "resultados/resultados_insertion_completo.csv",
    "resultados/resultados_merge_completo.csv",
    "resultados/resultados_heap_completo.csv",
    "resultados/resultados_quick_completo.csv",
]


PASTA_SAIDA = "graficos/imagens"


def carregar_dados():
    dados = []

    for arquivo in ARQUIVOS_CSV:
        if os.path.exists(arquivo):
            df = pd.read_csv(arquivo)
            dados.append(df)
        else:
            print(f"Aviso: arquivo não encontrado: {arquivo}")

    if not dados:
        raise FileNotFoundError("Nenhum arquivo CSV foi encontrado.")

    df_final = pd.concat(dados, ignore_index=True)

    df_final["tamanho"] = pd.to_numeric(df_final["tamanho"])
    df_final["tempo_medio"] = pd.to_numeric(df_final["tempo_medio"])
    df_final["comparacoes_medias"] = pd.to_numeric(df_final["comparacoes_medias"])

    return df_final


def formatar_nome_arquivo(texto):
    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ç", "c")
    texto = texto.replace(" ", "_")

    return texto


def gerar_grafico(df, tipo_entrada, coluna_y, nome_y, nome_arquivo):
    dados_entrada = df[df["tipo_entrada"] == tipo_entrada]

    plt.figure(figsize=(10, 6))

    for algoritmo in sorted(dados_entrada["algoritmo"].unique()):
        dados_algoritmo = dados_entrada[dados_entrada["algoritmo"] == algoritmo]
        dados_algoritmo = dados_algoritmo.sort_values("tamanho")

        plt.plot(
            dados_algoritmo["tamanho"],
            dados_algoritmo[coluna_y],
            marker="o",
            label=algoritmo
        )

    plt.title(f"{nome_y} - Entrada {tipo_entrada}")
    plt.xlabel("Tamanho da entrada")
    plt.ylabel(nome_y)
    plt.yscale("log")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    os.makedirs(PASTA_SAIDA, exist_ok=True)

    caminho_saida = os.path.join(PASTA_SAIDA, nome_arquivo)
    plt.savefig(caminho_saida, dpi=300)
    plt.close()

    print(f"Gráfico salvo em: {caminho_saida}")


def gerar_todos_os_graficos():
    df = carregar_dados()

    tipos_entrada = ["Crescente", "Decrescente", "Aleatório"]

    for tipo_entrada in tipos_entrada:
        nome_tipo = formatar_nome_arquivo(tipo_entrada)

        gerar_grafico(
            df,
            tipo_entrada,
            "tempo_medio",
            "Tempo médio (s)",
            f"tempo_todos_{nome_tipo}.png"
        )

        gerar_grafico(
            df,
            tipo_entrada,
            "comparacoes_medias",
            "Comparações médias",
            f"comparacoes_todos_{nome_tipo}.png"
        )


def main():
    print("Gerando gráficos comparativos com todos os algoritmos...")
    gerar_todos_os_graficos()
    print("\nGráficos gerados com sucesso.")


if __name__ == "__main__":
    main()