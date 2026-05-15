def particiona(vetor, primeiro, ultimo):
    comparacoes = 0

    pivo = vetor[ultimo]
    i = primeiro - 1

    for j in range(primeiro, ultimo):
        comparacoes += 1

        if vetor[j] <= pivo:
            i = i + 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[ultimo] = vetor[ultimo], vetor[i + 1]

    return i + 1, comparacoes


def quick_sort_recursivo(vetor, primeiro, ultimo):
    comparacoes = 0

    if primeiro < ultimo:
        posicao_pivo, comp_particao = particiona(vetor, primeiro, ultimo)
        comparacoes += comp_particao

        comparacoes += quick_sort_recursivo(vetor, primeiro, posicao_pivo - 1)
        comparacoes += quick_sort_recursivo(vetor, posicao_pivo + 1, ultimo)

    return comparacoes


def quick_sort(vetor):
    comparacoes = quick_sort_recursivo(vetor, 0, len(vetor) - 1)
    return vetor, comparacoes