def insertion_sort(vetor):
    comparacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                j = j - 1
            else:
                break

        vetor[j + 1] = chave

    return vetor, comparacoes