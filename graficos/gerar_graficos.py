import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


ARQUIVOS_CLASSICOS = [
    "resultados/resultados_bubble_completo.csv",
    "resultados/resultados_insertion_completo.csv",
    "resultados/resultados_merge_completo.csv",
    "resultados/resultados_heap_completo.csv",
    "resultados/resultados_quick_completo.csv",
]


ARQUIVO_AOH = "resultados/resultados_aoh_limites.csv"

LIMITE_AOH_ESCOLHIDO = 16

PASTA_SAIDA = "graficos/imagens"


def carregar_dados_classicos():
    dados = []

    for arquivo in ARQUIVOS_CLASSICOS:
        if os.path.exists(arquivo):
            df = pd.read_csv(arquivo)
            dados.append(df)
        else:
            print(f"Aviso: arquivo não encontrado: {arquivo}")

    if not dados:
        raise FileNotFoundError("Nenhum arquivo CSV dos algoritmos clássicos foi encontrado.")

    df_final = pd.concat(dados, ignore_index=True)

    df_final["tamanho"] = pd.to_numeric(df_final["tamanho"])
    df_final["tempo_medio"] = pd.to_numeric(df_final["tempo_medio"])
    df_final["comparacoes_medias"] = pd.to_numeric(df_final["comparacoes_medias"])

    return df_final


def carregar_dados_aoh():
    if not os.path.exists(ARQUIVO_AOH):
        print(f"Aviso: arquivo do AOH não encontrado: {ARQUIVO_AOH}")
        return None

    df = pd.read_csv(ARQUIVO_AOH)

    df["tamanho"] = pd.to_numeric(df["tamanho"])
    df["tempo_medio"] = pd.to_numeric(df["tempo_medio"])
    df["comparacoes_medias"] = pd.to_numeric(df["comparacoes_medias"])
    df["limite"] = pd.to_numeric(df["limite"])

    df = df[df["limite"] == LIMITE_AOH_ESCOLHIDO].copy()
    df["algoritmo"] = "AOH Merge+Insertion"

    return df


def carregar_dados_com_aoh():
    df_classicos = carregar_dados_classicos()
    df_aoh = carregar_dados_aoh()

    if df_aoh is None:
        return df_classicos

    return pd.concat([df_classicos, df_aoh], ignore_index=True)


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

    estilos = {
        "Bubble Sort": "--",
        "Insertion Sort": "-.",
        "Merge Sort": "-",
        "Heap Sort": ":",
        "Quick Sort": "-",
        "AOH Merge+Insertion": "--"
    }
    marcadores = {
        "Bubble Sort": "o",
        "Insertion Sort": "s",
        "Merge Sort": "^",
        "Heap Sort": "D",
        "Quick Sort": "x",
        "AOH Merge+Insertion": "*"
    }

    for algoritmo in sorted(dados_entrada["algoritmo"].unique()):
        dados_algoritmo = dados_entrada[dados_entrada["algoritmo"] == algoritmo]
        dados_algoritmo = dados_algoritmo.sort_values("tamanho")

        plt.plot(
            dados_algoritmo["tamanho"],
            dados_algoritmo[coluna_y],
            marker=marcadores.get(algoritmo, "o"),
            linestyle=estilos.get(algoritmo, "-"),
            label=algoritmo,
            alpha=0.85
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


def gerar_graficos_comparativos():
    df = carregar_dados_com_aoh()

    tipos_entrada = ["Crescente", "Decrescente", "Aleatório"]

    for tipo_entrada in tipos_entrada:
        nome_tipo = formatar_nome_arquivo(tipo_entrada)

        gerar_grafico(
            df,
            tipo_entrada,
            "tempo_medio",
            "Tempo médio (s)",
            f"tempo_todos_com_aoh_{nome_tipo}.png"
        )

        gerar_grafico(
            df,
            tipo_entrada,
            "comparacoes_medias",
            "Comparações médias",
            f"comparacoes_todos_com_aoh_{nome_tipo}.png"
        )


def gerar_graficos_limites_aoh():
    if not os.path.exists(ARQUIVO_AOH):
        print(f"Aviso: arquivo do AOH não encontrado: {ARQUIVO_AOH}")
        return

    df = pd.read_csv(ARQUIVO_AOH)

    df["tamanho"] = pd.to_numeric(df["tamanho"])
    df["tempo_medio"] = pd.to_numeric(df["tempo_medio"])
    df["comparacoes_medias"] = pd.to_numeric(df["comparacoes_medias"])
    df["limite"] = pd.to_numeric(df["limite"])

    tipos_entrada = ["Crescente", "Decrescente", "Aleatório"]

    for tipo_entrada in tipos_entrada:
        dados_entrada = df[df["tipo_entrada"] == tipo_entrada]
        nome_tipo = formatar_nome_arquivo(tipo_entrada)

        plt.figure(figsize=(10, 6))

        estilos_limites = {
            16: "--",
            32: ":",
            64: "-.",
            128: "-"
        }
        marcadores_limites = {
            16: "o",
            32: "s",
            64: "D",
            128: "^"
        }

        for limite in sorted(dados_entrada["limite"].unique()):
            dados_limite = dados_entrada[dados_entrada["limite"] == limite]
            dados_limite = dados_limite.sort_values("tamanho")

            plt.plot(
                dados_limite["tamanho"],
                dados_limite["tempo_medio"],
                marker=marcadores_limites.get(limite, "o"),
                linestyle=estilos_limites.get(limite, "-"),
                label=f"Limite {limite}",
                alpha=0.85
            )

        plt.title(f"AOH - Tempo médio por limite - Entrada {tipo_entrada}")
        plt.xlabel("Tamanho da entrada")
        plt.ylabel("Tempo médio (s)")
        plt.yscale("log")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        os.makedirs(PASTA_SAIDA, exist_ok=True)

        caminho_saida = os.path.join(PASTA_SAIDA, f"aoh_limites_tempo_{nome_tipo}.png")
        plt.savefig(caminho_saida, dpi=300)
        plt.close()

        print(f"Gráfico salvo em: {caminho_saida}")


def gerar_graficos_por_entrada(df, prefixo_tempo, prefixo_comparacoes):
    tipos_entrada = ["Crescente", "Decrescente", "Aleatório"]

    for tipo_entrada in tipos_entrada:
        nome_tipo = formatar_nome_arquivo(tipo_entrada)

        gerar_grafico(
            df,
            tipo_entrada,
            "tempo_medio",
            "Tempo médio (s)",
            f"{prefixo_tempo}_{nome_tipo}.png"
        )

        gerar_grafico(
            df,
            tipo_entrada,
            "comparacoes_medias",
            "Comparações médias",
            f"{prefixo_comparacoes}_{nome_tipo}.png"
        )

def main():
    print("Gerando gráficos somente dos algoritmos clássicos...")
    df_classicos = carregar_dados_classicos()

    gerar_graficos_por_entrada(
        df_classicos,
        "tempo_classicos",
        "comparacoes_classicos"
    )

    print("\nGerando gráficos com algoritmos clássicos e AOH...")
    df_com_aoh = carregar_dados_com_aoh()

    gerar_graficos_por_entrada(
        df_com_aoh,
        "tempo_todos_com_aoh",
        "comparacoes_todos_com_aoh"
    )

    print("\nGerando gráficos dos limites do AOH...")
    gerar_graficos_limites_aoh()

    print("\nGráficos gerados com sucesso.")


if __name__ == "__main__":
    main()