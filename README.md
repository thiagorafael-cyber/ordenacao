# Trabalho - Algoritmos de Ordenação

Este projeto foi desenvolvido para a disciplina de Projeto e Análise de Algoritmos.

O objetivo da Parte I é implementar e comparar algoritmos clássicos de ordenação, considerando tempo de execução e quantidade de comparações.

## Integrantes

- Bernan Rodrigues do Nascimento
- Danilo Rodrigues Barbosa
- Thiago Rafael Pereira de Carvalho

## Algoritmos implementados

- Bubble Sort
- Insertion Sort
- Merge Sort
- Heap Sort
- Quick Sort

## Tipos de entrada testados

Os algoritmos são testados com três tipos de vetores:

- Vetor em ordem crescente
- Vetor em ordem decrescente
- Vetor aleatório

Na versão atual, utilizada para a entrega parcial, os testes são executados com vetor de tamanho 500.

Cada combinação de algoritmo, tipo de entrada e tamanho é executada 3 vezes. O tempo e a quantidade de comparações apresentados correspondem à média das execuções.

## Estrutura do projeto

```text
ordenacao/
├── algoritmos/
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   ├── quick_sort.py
│   └── aoh.py
│
├── testes/
│   ├── __init__.py
│   ├── benchmark.py
│   ├── gerador_vetores.py
│   ├── teste_bubble.py
│   ├── teste_insertion.py
│   ├── teste_merge.py
│   ├── teste_heap.py
│   ├── teste_quick.py
│   ├── teste_gerador.py
│   └── teste_todos.py
│
├── resultados/
│   └── resultados_parte1.csv
│
├── graficos/
├── main.py
├── README.md
└── .gitignore
```

## Requisitos

É necessário ter o Python instalado.

Versão utilizada no desenvolvimento:

```text
Python 3.14.5
```

## Como verificar se o Python está instalado

### Windows

No PowerShell ou Prompt de Comando:

```powershell
python --version
```

Caso o comando não funcione, instale o Python pelo site oficial e marque a opção:

```text
Add python.exe to PATH
```

durante a instalação.

### Linux e macOS

No terminal:

```bash
python3 --version
```

## Como executar o programa principal

Na raiz do projeto, execute:

### Windows

```powershell
python main.py
```

### Linux/macOS

```bash
python3 main.py
```

Depois escolha a opção:

```text
1 - Executar testes da Parte I
```

## Resultado gerado

Após a execução, será criado ou atualizado o arquivo:

```text
resultados/resultados_parte1.csv
```

Esse arquivo contém:

- nome do algoritmo;
- tipo de entrada;
- tamanho do vetor;
- tempo médio de execução;
- quantidade média de comparações.

## Executar testes individuais

Também é possível executar testes individuais.

### Windows

```powershell
python testes/teste_insertion.py
python testes/teste_bubble.py
python testes/teste_merge.py
python testes/teste_heap.py
python testes/teste_quick.py
python testes/teste_todos.py
```

### Linux/macOS

```bash
python3 testes/teste_insertion.py
python3 testes/teste_bubble.py
python3 testes/teste_merge.py
python3 testes/teste_heap.py
python3 testes/teste_quick.py
python3 testes/teste_todos.py
```

## Executar o benchmark diretamente

Também é possível executar diretamente o arquivo de benchmark.

### Windows

```powershell
python testes/benchmark.py
```

### Linux/macOS

```bash
python3 testes/benchmark.py
```

## Sobre a contagem de comparações

Cada algoritmo retorna a quantidade de comparações realizadas durante o processo de ordenação.

A contagem considera principalmente as comparações entre elementos do vetor, como por exemplo:

```python
if vetor[j] > chave:
```

no Insertion Sort, ou:

```python
if L[i] <= R[j]:
```

no Merge Sort.

## Observação sobre o Quick Sort

A implementação do Quick Sort utiliza o último elemento como pivô, seguindo a versão clássica apresentada no Cormen.

Por isso, em entradas crescentes ou decrescentes, o algoritmo pode apresentar comportamento de pior caso, com quantidade de comparações quadrática.

## Observação sobre arquivos de cache

Arquivos gerados automaticamente pelo Python, como:

```text
__pycache__/
*.pyc
```

não fazem parte da implementação e são ignorados pelo Git por meio do arquivo `.gitignore`.

## Situação atual do projeto

A Parte I está implementada com testes para vetores de tamanho 500, conforme solicitado para a entrega parcial.

As próximas etapas do trabalho serão:

- executar os testes com os tamanhos finais definidos pelo professor;
- gerar gráficos a partir do arquivo CSV;
- propor e implementar o Algoritmo de Ordenação Híbrido;
- comparar o desempenho do algoritmo híbrido com os algoritmos clássicos.