from testes.benchmark import main as executar_benchmark


def main():
    print("Algoritmos de Ordenação")
    print("---------------------------------------------")
    print("1 - Executar testes da Parte I")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        executar_benchmark()
    elif opcao == "0":
        print("Programa encerrado.")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()