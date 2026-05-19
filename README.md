# Trabalho - Algoritmos de Ordenação

Este projeto foi desenvolvido para a disciplina de Projeto e Análise de Algoritmos.

O objetivo do trabalho é implementar e comparar algoritmos clássicos de ordenação, considerando tempo de execução e quantidade de comparações. Além disso, o projeto servirá de base para a proposta de um Algoritmo de Ordenação Híbrido (AOH).

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

Os tamanhos utilizados nos testes finais são:

```text
100
1.000
5.000
30.000
50.000
100.000
150.000
200.000
```

Cada combinação de algoritmo, tipo de entrada e tamanho pode ser executada várias vezes. Por padrão, recomenda-se utilizar 3 repetições, conforme solicitado no enunciado do trabalho. O tempo e a quantidade de comparações apresentados correspondem à média das execuções.

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
│   ├── benchmark_final.py
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
│   ├── resultados_bubble_completo.csv
│   ├── resultados_insertion_completo.csv
│   ├── resultados_merge_completo.csv
│   ├── resultados_heap_completo.csv
│   └── resultados_quick_completo.csv
│
├── graficos/
│   ├── gerar_graficos.py
│   └── imagens/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requisitos

É necessário ter o Python instalado.

Versão utilizada no desenvolvimento:

```text
Python 3.14.5
```

Para gerar gráficos, também é necessário instalar as dependências listadas no arquivo `requirements.txt`.

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

## Instalação das dependências

Na raiz do projeto, execute:

### Windows

```powershell
python -m pip install -r requirements.txt
```

### Linux/macOS

```bash
python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém:

```text
pandas
matplotlib
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

O menu principal apresenta as opções:

```text
1 - Executar benchmark final
2 - Gerar gráficos
0 - Sair
```

## Benchmark final

A opção de benchmark final permite escolher:

- algoritmos;
- tipos de entrada;
- tamanhos;
- nome do arquivo CSV de saída;
- número de repetições.

O benchmark final pode ser executado pelo menu principal ou diretamente pelo arquivo:

### Windows

```powershell
python testes/benchmark_final.py
```

### Linux/macOS

```bash
python3 testes/benchmark_final.py
```

Os resultados são salvos na pasta:

```text
resultados/
```

Cada arquivo CSV contém:

- nome do algoritmo;
- tipo de entrada;
- tamanho do vetor;
- número de repetições;
- tempo médio de execução;
- quantidade média de comparações;
- status da execução.

## Gerar gráficos

Após executar os benchmarks e gerar os arquivos CSV na pasta `resultados/`, é possível gerar os gráficos pelo menu principal:

```text
2 - Gerar gráficos
```

Também é possível executar diretamente:

### Windows

```powershell
python graficos/gerar_graficos.py
```

### Linux/macOS

```bash
python3 graficos/gerar_graficos.py
```

Os gráficos serão salvos automaticamente em:

```text
graficos/imagens/
```

Atualmente, são gerados gráficos comparativos para:

- tempo médio de execução;
- quantidade média de comparações;
- entrada crescente;
- entrada decrescente;
- entrada aleatória.

Os arquivos gerados seguem este padrão:

```text
tempo_todos_crescente.png
tempo_todos_decrescente.png
tempo_todos_aleatorio.png

comparacoes_todos_crescente.png
comparacoes_todos_decrescente.png
comparacoes_todos_aleatorio.png
```

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

A implementação dos algoritmos clássicos está concluída, assim como o benchmark final e a geração de gráficos comparativos.

As próximas etapas do trabalho são:

- analisar os resultados obtidos;
- propor e implementar o Algoritmo de Ordenação Híbrido;
- comparar o desempenho do algoritmo híbrido com os algoritmos clássicos;
- utilizar os resultados no relatório final e na apresentação.