__author__ = "Lucas Pinto, 56926"
"""
A. Complexidade assintótica
Para a primeira parte deste trabalho deverá fazer a análise da complexidade assintótica das funções abaixo.

A.1. A função f1 recebe um inteiro positivo n e uma lista v. Pode assumir que v tem tamanho superior a n.
"""
def f1(n, v):
    b = n * n       # O(1)
    s = 0           # O(1)
    while b > 1:    # Guarda: O(1) - Ciclo: O((n^2)/2) => O(n^2)
        s += v[n]   # O(1)
        s += b      # O(1)
        b -= 2      # O(1)
    return s        # O(1)
"""
Podemos ignorar as intruções anteriores e posteriores ao ciclo while, pois são O(1) e o ciclo tem uma ordem superior. Também podemos ignorar as operações do corpo do ciclo pos são igualmente O(1), ficando assim com uma complexidade de O(1) no corpo do ciclo.
O ciclo itera (n^2)/2 vezes (onde n é a variável parâmetro n) pois b = n*n <=> b = n^2 e b é decrementado por 2 a cada iteração. Como o divisor é constante podemos removê-lo na nossa análise assintótica, ficando o ciclo com uma complexidade de O(n^2)
Assim, f1 é quadrática => O(n^2)
"""

"""
A.2. A função f2 recebe um dicionário de uma lista l
"""
def f2(d, l):
    r = []              # O(1)
    for x in l:         # O(n)
        if x not in d:  # O(1) (x in d => O(1), not => O(1))
            r.append(x) # O(1)
    return r            # O(1)
"""
Podemos ignorar as operações anteriores e posteriores ao ciclo for pois são O(1) e o ciclo tem uma ordem superior.
Este ciclo itera n vezes (onde n é o comprimento de l) e, a cada iteração, vê se a chave x está no dicionário d, que é uma operação de custo O(1). Como o append também é constante podemos afirmar que o corpo do ciclo é constante, logo apenas interessa a quantidade de iterações feita pelo mesmo.
No fim, ficamos com uma complexidade O(n), sendo f2 linear  
"""



"""
As respostas deverão ser dadas em notação O-grande, O, e funções de uma ou mais variáveis n, m.
    > Indique claramente o significado das variáveis escolhidas.
    > Para cada uma das duas funções apresente os cálculos que conduzem ao resultado (pode utilizar os números de linha das funções para o efeito)
"""

"""
B. Busca em listas duplas 
Para a segunda parte deste trabalho pretende-se a implementação de uma função de procura em listas duplas ordenadas. Uma lista dupla é uma lista de listas, como por exemplo
lista_dupla = [[2, 4, 4, 6], [7, 11, 12, 13],
[13, 13, 13, 13], [15, 19, 42, 100]]
Uma lista dupla está ordenada se todas as suas sublistas estão ordenadas (de forma crescente) e o último elemento de cada sublista é menor ou igual ao primeiro elemento da sublista seguinte. O exemplo lista_dupla dado acima constitui uma lista dupla ordenada. Mas o seguinte exemplo não constitui uma lista dupla ordenada.
lista_nao_ordenada = [[3, 5, 5, 10], [17, 19, 23, 30],
[11, 12, 13, 14], [32, 42, 42, 42]]
Para este trabalho deverá escrever o predicado busca_lista_dupla(lista, x) que recebe uma lista dupla ordenada lista e um elemento x e verifica se x ocorre em lista, isto é, se é um elemento de alguma sublista de lista.
Exemplos de execução:
>>>print(busca_lista_dupla(lista_dupla,4))
True
>>>print(busca_lista_dupla(lista_dupla,5))
False
>>>print(busca_lista_dupla(lista_dupla,14))
False
>>>print(busca_lista_dupla(lista_dupla,42))
True
Pode fazer as seguintes assunções, indicando-as na descrição docstring da função:
    > os elementos que ocorrem nas sublistas são valores inteiros;
    > nenhuma sublista de lista é vazia (no entanto, a própria lista poderá ser vazia).
"""

def pesquisaBinaria(lst, comp):
    """
    Pesquisa binária numa lista com comparação por função
    Args:
        lst: lista onde fazer a pesquisa binária
        comp: função de comparação. Deve devolver -1 se o elemento está à esquerda, 0 se é o elemento e 1 se o elemento está à direita

    Returns: índice do elemento na lista ou -1 se não estiver na lista
    """
    def recur(min, max):
        if min >= max:
            return -1

        meio = min + (max - min) // 2
        res = comp(lst[meio])
        if res == 0:
            return meio
        elif res == -1:
            return recur(min, meio - 1)
        else:
            return recur(meio + 1, max)

    return recur(0, len(lst))


def busca_lista_dupla(matriz, num):
    """
    Procura se um inteiro está numa matriz de inteiros
    Args:
        matriz: Matriz de inteiros onde procurar
        num: Inteiro a procurar

    Returns: True se o elemento estiver presente na matriz, False caso contrário

    """
    if len(matriz) == 0:
        return False

    for lst in matriz:
        if pesquisaBinaria(lst, num) != -1:
            return True

    return False
