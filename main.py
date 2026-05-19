from testes.benchmark_final import menu as executar_benchmark_final
from graficos.gerar_graficos import main as gerar_graficos


def main():
    while True:
        print("\nTrabalho Prático 2 - Algoritmos de Ordenação")
        print("---------------------------------------------")
        print("1 - Executar benchmark final")
        print("2 - Gerar gráficos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            executar_benchmark_final()

        elif opcao == "2":
            gerar_graficos()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()