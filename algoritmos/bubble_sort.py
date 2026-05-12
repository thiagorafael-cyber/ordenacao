def bubble_sort(vetor):
    comparacoes = 0
    n = len(vetor)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

    return vetor, comparacoes