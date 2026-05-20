def insertion_sort_intervalo(vetor, primeiro, ultimo):
    comparacoes = 0

    for i in range(primeiro + 1, ultimo + 1):
        chave = vetor[i]
        j = i - 1

        while j >= primeiro:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                j = j - 1
            else:
                break

        vetor[j + 1] = chave

    return comparacoes


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


def aoh_recursivo(vetor, primeiro, ultimo, limite):
    comparacoes = 0

    tamanho = ultimo - primeiro + 1

    if primeiro < ultimo:
        if tamanho <= limite:
            comparacoes += insertion_sort_intervalo(vetor, primeiro, ultimo)

        else:
            meio = (primeiro + ultimo) // 2

            comparacoes += aoh_recursivo(vetor, primeiro, meio, limite)
            comparacoes += aoh_recursivo(vetor, meio + 1, ultimo, limite)
            comparacoes += merge(vetor, primeiro, meio, ultimo)

    return comparacoes


def aoh(vetor, limite=16):
    comparacoes = aoh_recursivo(vetor, 0, len(vetor) - 1, limite)
    return vetor, comparacoes