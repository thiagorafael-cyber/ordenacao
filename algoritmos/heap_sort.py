tamHeap=0

def refazHeapMax(A, i):
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    maior = i

    if esquerda < tamHeap and A[esquerda] > A[maior]:
        maior = esquerda

    if direita < tamHeap and A[direita] > A[maior]:
        maior = direita

    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        refazHeapMax(A, maior)


def constroiHeapMax(A):
    global tamHeap 
    
    tamHeap= len(A)
    for i in range(tamHeap // 2 - 1, -1, -1):
        refazHeapMax(A, i)


def heapSort(A):

    global tamHeap
    constroiHeapMax(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        tamHeap -= 1
        refazHeapMax(A, 0)
