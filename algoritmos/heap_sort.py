def refaz_heap_max(vetor, tamanho_heap, i):
    comparacoes = 0

    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i

    if esquerda < tamanho_heap:
        comparacoes += 1

        if vetor[esquerda] > vetor[maior]:
            maior = esquerda

    if direita < tamanho_heap:
        comparacoes += 1

        if vetor[direita] > vetor[maior]:
            maior = direita

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        comparacoes += refaz_heap_max(vetor, tamanho_heap, maior)

    return comparacoes


def constroi_heap_max(vetor):
    comparacoes = 0
    tamanho_heap = len(vetor)

    for i in range(tamanho_heap // 2 - 1, -1, -1):
        comparacoes += refaz_heap_max(vetor, tamanho_heap, i)

    return comparacoes


def heap_sort(vetor):
    comparacoes = 0
    tamanho_heap = len(vetor)

    comparacoes += constroi_heap_max(vetor)

    for i in range(len(vetor) - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        tamanho_heap = tamanho_heap - 1
        comparacoes += refaz_heap_max(vetor, tamanho_heap, 0)

    return vetor, comparacoes