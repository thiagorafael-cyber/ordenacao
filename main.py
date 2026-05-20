from testes.benchmark_final import menu as executar_benchmark_classicos
from testes.benchmark_aoh import main as executar_benchmark_aoh
from graficos.gerar_graficos import main as gerar_graficos


def main():
    while True:
        print("\nTrabalho Prático 2 - Algoritmos de Ordenação")
        print("---------------------------------------------")
        print("1 - Executar benchmark dos algoritmos clássicos")
        print("2 - Executar benchmark do AOH")
        print("3 - Gerar gráficos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            executar_benchmark_classicos()

        elif opcao == "2":
            executar_benchmark_aoh()

        elif opcao == "3":
            gerar_graficos()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()