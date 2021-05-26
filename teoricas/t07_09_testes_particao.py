#!/usr/bin/env python3

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Testes por partição do espaço de entrada

Baseado no livro Paul Ammann and Jeff Offutt, Introduction to Software
Testing, Cambridge University Press, 2008. 
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

# Característica                                Blocos
# A lista está vazia                            v1 = True, v2 = False
# Número de ocorrências na lista                n1 = 0, n2 = 1, n3 > 1
# Elemento ocorre na primeira posição da lista  p1 = True, p2 = False
def membro (lista, elemento):
    """Um dado elemento ocorre numa dada lista?

    Args:
        lista (list): A lista onde procurar
        elemento (any): O elemento a procurar

    Returns:
        bool: True se o elemento está na lista; False caso contrário

    >>> membro([], "c")              # (v1,n1,p2)
    False
    >>> membro(["a","b"], "c")        # (v2,n1,p2)
    False
    >>> membro(["c","a","b"], "c")   # (v2,n2,p1)
    True
    >>> membro(["a","c","b"], "c")    # (v2,n2,p2)
    True
    >>> membro(["c","a","c","b"], "c")  # (v2,n3,p1)
    True
    >>> membro(["a","c","c","b"], "c")  # (v2,n3,p2)
    True
    """
    return elemento in lista

def simetrico (x):
    """O simétrico de um número

    Args:
        x (number): O número

    Returns:
        number: O simétrico

    >>> simetrico(-2.7)
    2.7
    >>> simetrico(0)
    0
    >>> simetrico(7.8)
    -7.8
    """
    return -x

def factorial (n):
    """O factorial de um número

    Args:
        n (number): O número
    Pre:
        n >= 0
    Returns:
        number: O factorial de n

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    return 1 if n ==0 else n * factorial(n - 1)

def hexa(x):
    """A representação hexadecimal de um número

    Args:
        x (integer): O número a convert para hexadecimal
    Pre:
        0 <= x < 15
    Returns:
        str: A representação hexa

    >>> hexa(0)
    '0'
    >>> hexa(7)
    '7'
    >>> hexa(9)
    '9'
    >>> hexa(10)
    'A'
    >>> hexa(13)
    'D'
    >>> hexa(15)
    'F'
    """  
    return chr(x + (48 if x < 10 else 55))

def par(x):
    """Um dado número é par?

    Args:
        x (number): O número

    Returns:
        bool: True se x é par; False caso contrário

    >>> par (0)
    True
    >>> par (33)
    False
    >>> par (126)
    True
    """
    return x % 2 == 0

def fusao (l1, l2):
    """Funde duas listas numa só

    Pre:
        Ambas as listas estão ordenadas
    Post:
        A lista resultado está ordenada
    Args:
        l1 (list): Uma lista
        l2 (list): A outra lista
    Returns:
        list: A lista com os elementos das duas listas parâmetro

    >>> fusao ([], [])
    []
    >>> fusao ([2, 3, 3], [])
    [2, 3, 3]
    >>> fusao ([],[7, 24])
    [7, 24]
    >>> fusao ([3, 7], [9, 17])
    [3, 7, 9, 17]
    >>> fusao ([2, 4], [3, 9])
    [2, 3, 4, 9]
    >>> fusao ([2, 37, 37], [1])
    [1, 2, 37, 37]
    >>> fusao ([3, 9], [2, 4])
    [2, 3, 4, 9]
    >>> fusao ([4], [2, 4, 8])
    [2, 4, 4, 8]
    >>> fusao ([2, 4, 8], [4])
    [2, 4, 4, 8]
    >>> fusao ([1, 4], [1, 4, 8])
    [1, 1, 4, 4, 8]
    >>> fusao ([1, 4, 8], [1, 4])
    [1, 1, 4, 4, 8]
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

# Modelação de uma função fora do seu domínio.
# Característica consideradas
# - a lista é vazia
# - a lista tem um elemento
# - a lista tem todos os elementos iguais
# - a média é um número inteiro
def media (l):
    """A média dos elementos de uma lista

    Args:
        l (list[number]): A lista

    Raises:
        ZeroDivisionError: Quando a lista é vazia

    Returns:
        float: A média dos elementos da lista

    >>> media([])
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    >>> media([2, 4, 7, 9])
    5.5
    >>> round(media([55]), 6)
    55.0
    >>> round(media([3.14]), 6)
    3.14
    >>> round(media([2, 2]), 6)
    2.0
    >>> round(media(([1.1] * 10)), 6)
    1.1
    >>> round(media([2, 4, 6]), 6)
    4.0
    >>> round(media([2, 4, 7, 9]), 6)
    5.5
    """
    return sum(l) / len(l)

def frequencias (l):
    """Um dicionario com o numero de vezes que cada elemento ocorre numa lista

    Args:
        l (list): A lista

    Returns:
        dict: O dicionário com as frequências
    
    >>> frequencias([])
    {}
    >>> frequencias(['a'])
    {'a': 1}
    >>> frequencias(['z', 'b', 'a']) == {'z': 1, 'b': 1, 'a': 1}
    True
    >>> frequencias(['z', 'a', 'b', 'a', 'a']) == {'a': 3, 'b': 1, 'z': 1}
    True
    >>> frequencias(['a', 'a', 'a', 'a', 'a'])
    {'a': 5}
    """
    resultado = {}
    for x in l:
        if x in resultado:
            resultado[x] += 1
        else:
            resultado[x] = 1
    return resultado

def ordenacao_por_insercao(l):
    """Ordena uma dada lista. A lista é modificada

    Args:
        l (list): A lista a ordenar

    >>> l = []; ordenacao_por_insercao(l); l
    []
    >>> l = [5, 5]; ordenacao_por_insercao(l); l
    [5, 5]
    >>> l = [5, 15, 25]; ordenacao_por_insercao(l); l
    [5, 15, 25]
    >>> l = [5, -15, 5, 25, 5]; ordenacao_por_insercao(l); l
    [-15, 5, 5, 5, 25]
    >>> l = [5, -15, 0, 25]; ordenacao_por_insercao(l); l
    [-15, 0, 5, 25]
    """
    for i in range (len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]

def atualiza(base, dic):
    """Atualiza um dado dicionário com os valores de outro dicionário

    Args:
        base (dict): O dicionário base
        dic (dict): O dicionário com os novos valores

    >>> b = {}; atualiza(b, {}); b
    {}
    >>> b = {}; atualiza(b, {'a': 1}); b == {'a': 1}
    True
    >>> b = {'a': 1, 'b': 7}; atualiza(b, {}); b == {'a': 1, 'b': 7}
    True
    >>> b = {'a': 1, 'b': 7}; atualiza(b, {'z': 3}); b == {'a': 1, 'b': 7, 'z': 3}
    True
    >>> b = {'a': 1, 'b': 7}; atualiza(b, {'z': 3, 'b': 11}); b == {'a': 1, 'b': 11, 'z': 3}
    True
    >>> b = {'a': 1, 'b': 7}; atualiza(b, {'a': 3, 'b': 11}); b == {'a': 3, 'b': 11}
    True
    """
    base.update(dic)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
