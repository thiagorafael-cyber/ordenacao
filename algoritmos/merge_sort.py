def merge(vetor, esquerda, meio, direita):
    comparacoes = 0

    n1 = meio - esquerda + 1
    n2 = direita - meio

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = vetor[esquerda + i]

    for j in range(n2):
        R[j] = vetor[meio + 1 + j]

    i = 0
    j = 0
    k = esquerda

    while i < n1 and j < n2:
        comparacoes += 1

        if L[i] <= R[j]:
            vetor[k] = L[i]
            i = i + 1
        else:
            vetor[k] = R[j]
            j = j + 1

        k = k + 1

    while i < n1:
        vetor[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n2:
        vetor[k] = R[j]
        j = j + 1
        k = k + 1

    return comparacoes


def merge_sort_recursivo(vetor, esquerda, direita):
    comparacoes = 0

    if esquerda < direita:
        meio = (esquerda + direita) // 2

        comparacoes += merge_sort_recursivo(vetor, esquerda, meio)
        comparacoes += merge_sort_recursivo(vetor, meio + 1, direita)
        comparacoes += merge(vetor, esquerda, meio, direita)

    return comparacoes


def merge_sort(vetor):
    comparacoes = merge_sort_recursivo(vetor, 0, len(vetor) - 1)
    return vetor, comparacoes