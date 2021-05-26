#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Algoritmos de busca e de ordenação

Baseado no capítulo 10 de
Introduction to Computation and Programming Using Python,
John Guttag, MIT press, segunda edição, 2016 
"""

__author__ = "John Guttag, Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

# Busca linear numa lista de elementos

def procura(L, e):
    """Procura um elemento numa lista.

    Não assume nada sobre a lista e ptt no pior caso visita a lista completa.
    O(n) onde n = len(L)
    Equivalente à expressão 'e in L'.

    Args:
        L (list[any]): A lista onde procurar
        e (any): O valor a procurar
    Returns:
        bool: True se o elemento foi encontrado; False caso contrário
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

def busca_linear_em_lista_ordenada(L, e):
    """Procura um elemento numa lista.

    No caso médio esta função melhora o tempo de execução da função anterior.
    Mas no pior caso visita a lista completa.
    O(n) onde n = len(L)

    Pre:
        a lista está ordenada.
    Args:
        L (list[any]): A lista onde procurar
        e (any): O valor a procurar
    Returns:
        bool: True se o elemento está na lista; False caso contrário
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def busca_dicotomica(l, e):
    """Procura um elemento numa lista

    Pre:
        A lista está ordenada
    Args:
        l (list): A lista
        e (any): O elemento
    Returns:
        bool: True se o elemento está na lista; False caso contrário
    """
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

# ORDENAÇÃO

def ordenacao_por_insercao(l):
    """Ordena uma dada lista. A lista é modificada

    Args:
        l (list): A lista a ordenar
    """
    for i in range (len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]

def fusao (l1, l2):
    """Funde duas listas numa só

    Pre:
        Ambas as listas estão ordenadas
    Post:
        A lista resultante está ordenada
    Args:
        l1 (list): Uma lista
        l2 (list): A outra lista
    Returns:
        list: A lista com os elementos das duas listas parâmetro
    """
    resultado = []
    i1, i2 = 0, 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            resultado.append(l1[i1])
            i1 += 1
        else:
            resultado.append(l2[i2])
            i2 += 1
    while i1 < len(l1):
        resultado.append(l1[i1])
        i1 += 1
    while i2 < len(l2):
        resultado.append(l2[i2])
        i2 += 1
    return resultado

def ordenacao_por_fusao(l):
    """Ordena uma lista. A lista parâmetro é inalterada

    Args:
        l (list): A lista a ordenar
    Returns:
        list: A lista ordenada com os elementos da lista parâmetro
    """
    if len(l) <= 1:
        return l[:]
    meio = len(l) // 2
    esquerda = ordenacao_por_fusao(l[:meio])
    direita = ordenacao_por_fusao(l[meio:])
    return fusao(esquerda, direita)

nomes = ['Alan Turing', 'Charles Babbage', 'Ada Lovelace', 'Blaise Pascal']

# Funcoes como parametros

def fusao_c(l1, l2, compara):
    """Funde duas listas numa só

    Pre:
        Ambas as listas estão ordenadas
    Post:
        A lista resultante está ordenada
    Args:
        l1 (list): Uma lista
        l2 (list): A outra lista
        compara (binary predicate): A função de comparação
    Returns:
        list: A lista com os elementos das duas listas parâmetro
    """
    resultado = []
    i1, i2 = 0, 0
    while i1 < len(l1) and i2 < len(l2):
        if compara(l1[i1], l2[i2]):
            resultado.append(l1[i1])
            i1 += 1
        else:
            resultado.append(l2[i2])
            i2 += 1
    while i1 < len(l1):
        resultado.append(l1[i1])
        i1 += 1
    while i2 < len(l2):
        resultado.append(l2[i2])
        i2 += 1
    return resultado

def ordenacao_por_fusao_c(l, compara = lambda x,y: x < y):
    """Ordena uma lista. A lista parâmetro é inalterada

    Args:
        l (list): A lista a ordenar
        compara (binary predicate, optional): A função ordenação. Defaults to <
    Returns:
        list: A lista ordenada com os elementos da lista parâmetro
    """
    if len(l) <= 1:
        return l[:]
    meio = len(l) // 2
    esquerda = ordenacao_por_fusao_c(l[:meio], compara)
    direita = ordenacao_por_fusao_c(l[meio:], compara)
    return fusao_c(esquerda, direita, compara)

por_primeiro_nome = ordenacao_por_fusao_c(nomes, lambda x, y: x < y)
por_primeiro_nome_decrescente = ordenacao_por_fusao_c(nomes, lambda x, y: x > y)

def compara_nomes_familia (nome1, nome2):
    """Compara dois nomes pelo nome de família

    Pre:
        nome1 e nome2 têm duas sequencias de carateres separadas por um espaço
    Args:
        nome1 (str): Um nome
        nome2 (str): Outro nome
    Returns:
        bool: True se o nome de família de nome1 é menor do que o do nome2,
        False caso contrário
    """
    l1 = nome1.split(' ')
    l2 = nome2.split(' ')
    if l1[1] == l2[1]:
        return l1[0] < l2[0]
    else:
        return l1[1] < l2[1]

por_nome_familia = ordenacao_por_fusao_c(nomes, compara_nomes_familia)

# Ordenacao em Python, l.sort() e sorted(l)

# Método list.sort aceita uma lista como primeiro elemento e modifica a lista.
# Função sorted aceita um objecto iteravel (lista, dicionario, ...) e devolve uma nova lista

# sorted(iteravel)
d = {'eva': 54322, 'ada': 53281, 'abel': 71321}
# sorted(d)
s = set(d)
# sorted(s)

# list.sort()
# d.sort()
# m.sort()
# Aliasing

# Parâmetros extra para sort e sorted: key e reverse

# sorted(nomes, key = len)

def nome_familia(nome):
    """O nome de família de um nome

    Pre:
        nome tem duas sequencias de carateres separadas por um espaço
    Args:
        nome (str): O nome
    Returns:
        str: O nome de família
    """
    return nome.split(' ')[1]

# sorted(nomes, key = nome_familia)