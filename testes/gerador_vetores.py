import random


def gerar_vetor_crescente(tamanho):
    vetor = []

    for i in range(1, tamanho + 1):
        vetor.append(i)

    return vetor


def gerar_vetor_decrescente(tamanho):
    vetor = []

    for i in range(tamanho, 0, -1):
        vetor.append(i)

    return vetor


def gerar_vetor_aleatorio(tamanho):
    vetor = []

    for i in range(1, tamanho + 1):
        vetor.append(i)

    random.shuffle(vetor)

    return vetor