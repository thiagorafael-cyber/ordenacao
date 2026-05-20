# Trabalho - Algoritmos de Ordenação

Este projeto foi desenvolvido para a disciplina de Projeto e Análise de Algoritmos.

O objetivo do trabalho é implementar, testar e comparar algoritmos clássicos de ordenação, considerando tempo médio de execução e quantidade média de comparações. Além disso, foi proposta e implementada uma versão de Algoritmo de Ordenação Híbrido (AOH).

## Integrantes

- Bernan Rodrigues do Nascimento
- Danilo Rodrigues Barbosa
- Thiago Rafael Pereira de Carvalho

## Algoritmos implementados

### Algoritmos clássicos

- Bubble Sort
- Insertion Sort
- Merge Sort
- Heap Sort
- Quick Sort

### Algoritmo de Ordenação Híbrido

O AOH implementado utiliza:

```text
Algoritmo principal: Merge Sort
Algoritmo secundário: Insertion Sort
Limite de troca: 16 elementos
```

A ideia do AOH é utilizar a divisão do Merge Sort normalmente, mas quando o tamanho do subvetor for menor ou igual a 16, o algoritmo deixa de continuar a divisão recursiva e passa a ordenar aquele trecho com Insertion Sort.

Essa escolha foi feita com base nos testes experimentais, nos quais o Merge Sort apresentou comportamento estável em todos os cenários e o Insertion Sort apresentou bom desempenho em vetores pequenos ou já ordenados.

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
│   ├── benchmark_final.py
│   ├── benchmark_aoh.py
│   ├── gerador_vetores.py
│   ├── teste_bubble.py
│   ├── teste_insertion.py
│   ├── teste_merge.py
│   ├── teste_heap.py
│   ├── teste_quick.py
│   ├── teste_aoh.py
│   ├── teste_gerador.py
│   └── teste_todos.py
│
├── resultados/
│   ├── resultados_bubble_completo.csv
│   ├── resultados_insertion_completo.csv
│   ├── resultados_merge_completo.csv
│   ├── resultados_heap_completo.csv
│   ├── resultados_quick_completo.csv
│   └── resultados_aoh_limites.csv
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
1 - Executar benchmark dos algoritmos clássicos
2 - Executar benchmark do AOH
3 - Gerar gráficos
0 - Sair
```

## Benchmark dos algoritmos clássicos

A opção de benchmark dos algoritmos clássicos permite escolher:

- algoritmos;
- tipos de entrada;
- tamanhos;
- nome do arquivo CSV de saída;
- número de repetições.

Também é possível executar diretamente:

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

## Benchmark do AOH

O benchmark do AOH testa a versão híbrida baseada em Merge Sort e Insertion Sort.

Foram avaliados os seguintes limites de troca:

```text
16
32
64
128
```

O limite representa o tamanho máximo do subvetor a partir do qual o AOH deixa de continuar a divisão recursiva do Merge Sort e passa a utilizar Insertion Sort.

Também é possível executar o benchmark do AOH diretamente:

### Windows

```powershell
python testes/benchmark_aoh.py
```

### Linux/macOS

```bash
python3 testes/benchmark_aoh.py
```

O arquivo principal gerado pelo benchmark do AOH é:

```text
resultados/resultados_aoh_limites.csv
```

Com base nos testes realizados, o limite escolhido para a versão final do AOH foi:

```text
16
```

Esse limite apresentou o melhor equilíbrio geral entre entradas crescentes, decrescentes e aleatórias.

## Gerar gráficos

Após executar os benchmarks e gerar os arquivos CSV na pasta `resultados/`, é possível gerar os gráficos pelo menu principal:

```text
3 - Gerar gráficos
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

Os gráficos são salvos automaticamente em:

```text
graficos/imagens/
```

Atualmente, são gerados três grupos de gráficos:

### 1. Gráficos dos algoritmos clássicos

```text
tempo_classicos_crescente.png
tempo_classicos_decrescente.png
tempo_classicos_aleatorio.png

comparacoes_classicos_crescente.png
comparacoes_classicos_decrescente.png
comparacoes_classicos_aleatorio.png
```

### 2. Gráficos dos algoritmos clássicos com o AOH

```text
tempo_todos_com_aoh_crescente.png
tempo_todos_com_aoh_decrescente.png
tempo_todos_com_aoh_aleatorio.png

comparacoes_todos_com_aoh_crescente.png
comparacoes_todos_com_aoh_decrescente.png
comparacoes_todos_com_aoh_aleatorio.png
```

### 3. Gráficos dos limites do AOH

```text
aoh_limites_tempo_crescente.png
aoh_limites_tempo_decrescente.png
aoh_limites_tempo_aleatorio.png
```

Os gráficos utilizam escala logarítmica no eixo Y para facilitar a visualização, pois os tempos e quantidades de comparações variam muito entre os algoritmos.

## Executar testes individuais

Também é possível executar testes individuais.

### Windows

```powershell
python testes/teste_insertion.py
python testes/teste_bubble.py
python testes/teste_merge.py
python testes/teste_heap.py
python testes/teste_quick.py
python testes/teste_aoh.py
python testes/teste_todos.py
```

### Linux/macOS

```bash
python3 testes/teste_insertion.py
python3 testes/teste_bubble.py
python3 testes/teste_merge.py
python3 testes/teste_heap.py
python3 testes/teste_quick.py
python3 testes/teste_aoh.py
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

No AOH, as comparações são acumuladas tanto na etapa de Insertion Sort aplicada aos subvetores pequenos quanto nas etapas de intercalação do Merge Sort.

## Observação sobre o Quick Sort

A implementação do Quick Sort utiliza o último elemento como pivô, seguindo a versão clássica apresentada no Cormen.

Por isso, em entradas crescentes ou decrescentes, o algoritmo pode apresentar comportamento de pior caso, com quantidade de comparações quadrática.

## Observação sobre o AOH

O AOH implementado combina Merge Sort e Insertion Sort.

O Merge Sort foi escolhido como algoritmo principal por apresentar comportamento estável nos testes realizados. O Insertion Sort foi escolhido como algoritmo secundário por apresentar bom desempenho em vetores pequenos ou já ordenados.

Durante os testes, foram avaliados os limites 16, 32, 64 e 128. O limite 16 foi escolhido por apresentar melhor equilíbrio geral, principalmente por evitar que o Insertion Sort seja aplicado em subvetores grandes nos casos decrescente e aleatório.

## Observação sobre arquivos de cache

Arquivos gerados automaticamente pelo Python, como:

```text
__pycache__/
*.pyc
```

não fazem parte da implementação e são ignorados pelo Git por meio do arquivo `.gitignore`.