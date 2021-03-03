#1 - Considere a seguinte lista:
# ['a', 'f', 'h', 'e', 'a', 'z', 'b', 'c', 'd']
#
# a) Usando o algoritmo de busca linear, para determinar se cada um dos seguintes elementos está presente na lista, quantas comparações são feitas:
"""
   i.'z'   -> 6
   ii.'a'  -> 1
   iii.'x' -> 9
"""
# b) Considerando uma qualquer lista de tamanho n, qual é a complexidade (em notação O) da busca linear no melhor caso, no pior caso, e no caso médio?
"""
Melhor Caso: O(1)
Pior Caso  : O(n)
Caso Médio : O((n+1)/2) = O(n)
"""
# c) Seria possível usar um algoritmo de busca dicotómica para melhorar a eficiência da busca nesta lista em concreto? Justifique
""" não, pq a lista não está ordenada"""

#2 - Considere a seguinte lista:
# [5, 6, 7, 10, 20, 21, 25, 28, 29, 31, 50]
#
# a) Usando o algoritmo de busca dicotómica, para determinar se cada um dos seguintes elementos está presente na lista, indique quantas comparações são feitas:
"""
   i.   7 -> 2
   ii. 29 -> 2
   iii. 5 -> 3
   iv. 21 -> 1
"""
# b) É possível usar esse mesmo algoritmo de busca dicotómica se a lista estivesse com a ordem invertida? Isto é:
# [50, 31, 29, 28, 25, 21, 20, 10, 7, 6, 5]
# Que modificações teria que fazer no algoritmo para tal ser possível?
"""
Sim. Inverter para em vez de ir para o lado esquerdo ir para o lado direito quando quer um número menor
"""
# c) Considerando uma qualquer lista ordenada de tamanho n, qual é a complexidade (em notação O) da busca dicotómica no melhor caso, no pior caso, e no caso médio.
"""
Melhor caso: O(1)
Pior Caso  : O(log n)
Caso Médio : O(log n)
"""

#3 - Recorde a implementação recursiva da busca dicotómica. Implemente uma versão iterativa desse mesmo algoritmo e analise a sua complexidade.
def busca_dicotomica(l, e):
    def busca(primeiro, ultimo):
        if primeiro > ultimo:
            return False
        meio = (primeiro + ultimo) // 2
        if l[meio] == e:
            return True
        if l[meio] < e:
            return busca(meio + 1, ultimo)
        return busca(primeiro, meio - 1)
    return busca(0, len(l) - 1)

#4- Considere o algoritmo de ordenação por inserção (insert sort).
#
# a) Utilize este algoritmo para ordenar a lista
#   [4, 9, 3, 7]
# por ordem crescente. Apresente os valores intermédios a cada novo estado da lista e indique o número de comparações e de trocas realizadas cumulativamente.
"""
[4, 9, 3, 7] # 1 comp
[4, 9, 3, 7] # 1 comp 1 troca
[3, 9, 4, 7] # 1 comp

[3, 9, 4, 7] # 1 comp 1 troca
[3, 4, 9, 7] # 1 comp

[3, 4, 9, 7] # 1 comp 1 troca

[3, 4, 7, 9] # fim
# 6 comps, 3 trocas
"""
# b)  Repita o exercício para a lista [9, 7, 4, 3].
"""
[9, 7, 4, 3] # 1 comp 1 troca
[7, 9, 4, 3] # 1 comp 1 troca
[4, 9, 7, 3] # 1 comp 1 troca

[3, 9, 7, 4] # 1 comp
[3, 9, 7, 4] # 1 comp
[3, 9, 7, 4] # 1 comp 1 troca

[3, 4, 7, 9] # fim
# 6 comps, 4 trocas
"""
# c)  Apresente a análise da complexidade deste algoritmo (em notação O) para o melhor caso e para o pior, relativamente a comparações e a trocas envolvidas.
"""
Melhor Caso: O(n^2)
Pior Caso  : O(n^2)
"""

#5- Considere a seguinte descrição de um algoritmo de ordenação (bubblesort):
# enquanto a lista não estiver ordenada:
#   para cada par de elementos adjacentes:
#       se o par está fora de ordem:
#           ordená-lo
# a) Implemente este algoritmo de ordenação em Python.
def bubbleSort(lst):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(lst)-1):
            print(f'{lst} | lst[{i}] vs lst[{i+1}]', end='')
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                isSorted = False
                print('| S')
            else:
                print('| N')

# b) Utilize o algoritmo para ordenar a lista
#   [4, 9, 3, 7]
# por ordem crescente, apresentando os valores intermédios a cada novo estado da lista e indicando o número de comparações e de trocas realizadas cumulativamente.
# print('b\n')
# bubbleSort([4, 9, 3, 7])
"""
    lista    |    comparação   | troca
[4, 9, 3, 7] | lst[0] vs lst[1]| N
[4, 9, 3, 7] | lst[1] vs lst[2]| S
[4, 3, 9, 7] | lst[2] vs lst[3]| S
[4, 3, 7, 9] | lst[0] vs lst[1]| S
[3, 4, 7, 9] | lst[1] vs lst[2]| N
[3, 4, 7, 9] | lst[2] vs lst[3]| N
[3, 4, 7, 9] | lst[0] vs lst[1]| N
[3, 4, 7, 9] | lst[1] vs lst[2]| N
[3, 4, 7, 9] | lst[2] vs lst[3]| N
9 comps, 3 trocas
"""

# c) Repita para a lista [9, 7, 4, 3].
# print('c\n')
# bubbleSort([9, 7, 4, 3])
"""
    lista    |    comparação   | troca
[9, 7, 4, 3] | lst[0] vs lst[1]| S
[7, 9, 4, 3] | lst[1] vs lst[2]| S
[7, 4, 9, 3] | lst[2] vs lst[3]| S
[7, 4, 3, 9] | lst[0] vs lst[1]| S
[4, 7, 3, 9] | lst[1] vs lst[2]| S
[4, 3, 7, 9] | lst[2] vs lst[3]| N
[4, 3, 7, 9] | lst[0] vs lst[1]| S
[3, 4, 7, 9] | lst[1] vs lst[2]| N
[3, 4, 7, 9] | lst[2] vs lst[3]| N
[3, 4, 7, 9] | lst[0] vs lst[1]| N
[3, 4, 7, 9] | lst[1] vs lst[2]| N
[3, 4, 7, 9] | lst[2] vs lst[3]| N
12 comps, 6 trocas
"""
# d) Apresente a análise da complexidade deste algoritmo (em notação O) para o melhor caso e para o pior, relativamente a comparações e a trocas envolvidas.
"""
Pior Caso  : O(n^2) comps e trocas
Melhor Caso: O(n) comps, O(1) trocas (já está ordenado)
"""

#7 - Considere a seguinte lista cujos elementos são tuplos que representam estudantes:
#   alunos = [ ('pedro', 'A', 15), ('ana', 'B', 15),
#       ('david', 'B', 16), ('mariana', 'C', 12),
#       ('pedro', 'C', 12), ('david', 'A', 10) ]
# com o primeiro, o segundo e o terceiro argumento do tuplo arepresentar, respetivamente, o nome, a turma e a idade

# a) Qual seria o resultado de executar a instrução
#   alunos.sort(key =lambdax : x[0])
# seguida de
#   print(alunos)
# ?
"""
b) [ ('ana', 'B', 15), ('david', 'B', 16),
    ('david', 'A', 10), ('mariana', 'C', 12),
    ('pedro', 'A', 15), ('pedro', 'C', 12) ] 
"""

# b) Use a função list.sort para ordenar a lista alunos original por ordem crescente da idade dos estudantes
def prob7b():
    alunos = [('pedro', 'A', 15), ('ana', 'B', 15),
           ('david', 'B', 16), ('mariana', 'C', 12),
           ('pedro', 'C', 12), ('david', 'A', 10) ]
    alunos.sort(key=lambda x: x[2])
    print(alunos)

# c) Use a função sorted para obter a partir da lista alunos original uma outra lista em que os elementos se encontram pela ordem crescente da idade dos estudantes e, em caso de empate, pela ordem lexicográfica crescente dos nomes.
def prob7c():
    alunos = [('pedro', 'A', 15), ('ana', 'B', 15),
              ('david', 'B', 16), ('mariana', 'C', 12),
              ('pedro', 'C', 12), ('david', 'A', 10)]
    nAlunos = sorted(alunos, key=lambda x: [x[2], x[0]] )
    print(nAlunos)

#8- Considere a seguinte string "ahbdfre".
# a) Use a função sorted para obter a partir desta string, uma lista com os seus caracteres por ordem lexicográfica crescente.
def prob8a():
    string = "ahbdfre"
    nLista = [char for char in sorted(string)]
    print(nLista)

# b) Escreva uma função ordena_string que dada uma string, devolve uma string que é uma versão por ordem lexicográfica crescente da string dada.
def ordena_string(string):
    return sorted(string)
#9 - Escreva uma função ordena_conjunto que recebe um conjunto e devolve a lista com os elementos do conjunto por ordem crescente (pode assumir que os elementos do conjunto são strings). Utilize a função list.sort.
def ordena_conjunto(conj):
    lst = list(conj)
    lst.sort()
    return lst

#10 - Escreva uma função ordena_dicionario que recebe um dicionário e devolve uma lista com os pares (chave, valor) do dicionário, por ordem crescente das chaves (pode assumir que as chaves do dicionário são strings). Utilize a função sorted.
def ordena_dicionario(dic):
    return sorted(dic.items())

#11 - QuickSort, desenvolvido por Sir Tony Hoare, 1960, apoia-se numa estratégia de dividir para conquistar em que uma sequência inicial S é dividida em várias sub-sequências às quais o algoritmo é aplicado recursivamente. O resultado é posteriormente concatenado obtendo-se uma sequência ordenada. Tipicamente o QuickSort pode ser dividido em três passos:
# Dividir       Se S tem zero ou um elementos, a sequência está ordenada. Caso contrário, selecionar o último elemento de S, que passa a ser o pivot. Retirar todos os elementos de S construindo as seguintes duas sequências:
#                   B(baixo) contendo todos os elementos inferiores ou iguais ao pivot;
#                   A(alto) contendo todos os elementos superiores ao pivot;
# Conquistar    Aplicar recursivamente o algoritmo às sequências B e A.
# Combinar      Concatenar B, pivot, A, por esta ordem para obter o resultado.

# a) Implemente o algoritmo na linguagem Python.
def quickSort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    baixo = [el for el in lst[:-1] if el <= pivot]
    alto = [el for el in lst[:-1] if el > pivot]
    baixo = quickSort(baixo)
    alto = quickSort(alto)

    return baixo + [pivot] + alto
print(quickSort(['a', 'g', 'c', 'b']))
# b) Qual a complexidade do algoritmo quando a lista já se encontra ordenada?
"""
ex: [1, 2, 3, 4, 5, 6, 7, 8, 9]
baixos = [1, 2, 3, 4, 5, 6, 7, 8], altos = []
quickSort(baixos):
    baixos = [1, 2, 3, 4, 5, 6, 7], altos = []
    quickSort(baixos):
        baixos = [1, 2, 3, 4, 5, 6], altos = []
        ....

O(n-1 + n-2 + n-3 + n-4) -> O(n^2)
"""
# c) Discuta a complexidade computational do algoritmo no melhor e no pior caso.
"""
Melhor Caso: O(n log n)
Pior Caso  : O(n^2) qdo está ordenada

Caso Médio :
"""