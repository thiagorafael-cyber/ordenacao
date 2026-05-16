from algoritmos.bubble_sort import bubble_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort

import random
import time
import csv


vetor_ordenado = list(range(500))
vetor_decrescente = list(range(499, -1, -1))
vetor_aleatorio = [random.randint(0, 1000) for _ in range(500)]


while True:

    print("\n===== MENU DE ALGORITMOS =====")
    print("1 - Bubble Sort")
    print("2 - Heap Sort")
    print("3 - Insertion Sort")
    print("4 - Merge Sort")
    print("5 - Quick Sort")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    if opcao == "1":
        nome_algoritmo = "Bubble Sort"
        algoritmo = bubble_sort

    elif opcao == "2":
        nome_algoritmo = "Heap Sort"
        algoritmo = heap_sort

    elif opcao == "3":
        nome_algoritmo = "Insertion Sort"
        algoritmo = insertion_sort

    elif opcao == "4":
        nome_algoritmo = "Merge Sort"
        algoritmo = merge_sort

    elif opcao == "5":
        nome_algoritmo = "Quick Sort"
        algoritmo = quick_sort

    else:
        print("Opção inválida!")
        continue

    qtd_execucao = int(input("Quantas vezes deseja executar o algoritmo: "))

    tipo_vetor = 1


    arquivo_csv = open("resultados_"+nome_algoritmo+".csv", mode="w", newline="")
    escritor = csv.writer(arquivo_csv)

    escritor.writerow([
    "Algoritmo",
    "Vetor",
    "Execucao",
    "Tempo",
    "Comparacoes"
    ])


    while tipo_vetor <= 3:

        if tipo_vetor == 1:
            nome_vetor = "Ordenado"
            vetor = vetor_ordenado

        elif tipo_vetor == 2:
            nome_vetor = "Decrescente"
            vetor = vetor_decrescente

        else:
            nome_vetor = "Aleatorio"
            vetor = vetor_aleatorio

        for i in range(qtd_execucao):

            inicio = time.time()

            ordenado, comparacoes = algoritmo(vetor.copy())

            fim = time.time()

            tempo = fim - inicio

            escritor.writerow([
                nome_algoritmo,
                nome_vetor,
                i + 1,
                tempo,
                comparacoes
            ])

        escritor.writerow([])
        
        tipo_vetor += 1
    
    arquivo_csv.close()
