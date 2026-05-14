def merge(vetor, primeiro, meio, ultimo):
    comparacoes = 0

    n1 = meio - primeiro + 1
    n2 = ultimo - meio

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = vetor[primeiro + i]

    for j in range(n2):
        R[j] = vetor[meio + 1 + j]

    i = 0
    j = 0

    for k in range(primeiro, ultimo + 1):
        if i >= n1 and j < n2:
            vetor[k] = R[j]
            j = j + 1

        elif j >= n2 and i < n1:
            vetor[k] = L[i]
            i = i + 1

        else:
            comparacoes += 1

            if L[i] <= R[j]:
                vetor[k] = L[i]
                i = i + 1
            else:
                vetor[k] = R[j]
                j = j + 1

    return comparacoes


def merge_sort_recursivo(vetor, primeiro, ultimo):
    comparacoes = 0

    if primeiro < ultimo:
        meio = (primeiro + ultimo) // 2

        comparacoes += merge_sort_recursivo(vetor, primeiro, meio)
        comparacoes += merge_sort_recursivo(vetor, meio + 1, ultimo)
        comparacoes += merge(vetor, primeiro, meio, ultimo)

    return comparacoes


def merge_sort(vetor):
    comparacoes = merge_sort_recursivo(vetor, 0, len(vetor) - 1)
    return vetor, comparacoes