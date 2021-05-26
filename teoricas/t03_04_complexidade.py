#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Complexidade Assintótica

Baseado no capítulo 9 de
Introduction to Computation and Programming Using Python,
John Guttag, MIT press, segunda edição, 2016 
"""

__author__ = "John Guttag, Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

# Quanto tempo leva esta função a executar?
def f(i):
    """
    Args:
        i (int):
    Assumes:
        i >= 0
    """
    resultado = 1
    while i >= 1:
        resultado *= i
        i -= 1
    return resultado


def buscaLinear(l, x):
    """Procura um elemento numa lista.
    Devolve True se o elemento estiver na lista;
    devolve False caso contrário.

    Args:
        L (list): A lista onde procurar
        x (any): O elemento a procurar

    Returns:
        bool: O elemento está na lista?
    """
    for e in l:
        if e == x:
            return True
    return False

def factorial (n):
    """O factorial de um dado número

    Args:
        n (int): O número

    Returns:
        int: O factorial de n
    """
    i = 1
    resultado = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

def constant(n): # 2 + 1000 * 2 = 2002
    resultado = 0
    for _ in range(1000):
        resultado += 1
    return resultado

def linear (n): # 2 + 2n
    resultado = 0
    for _ in range(n):
        resultado = resultado + 1
    return resultado

def quadratico (n): # 2 + 2n^2
    resultado = 0
    for _ in range(n):
        for _ in range(n):
            resultado += 1
    return resultado

# Tentar com n = 1, 10, 1000, 
# Não tentar com n = 100000
def comparar (n): # 2002 + 2 + 2n + 2 + 2n^2 -> 2n^2 -> n^2 (quadratico ou O(n^2))
    print(constant(n))
    print(linear(n))
    print(quadratico(n))

"""
Algumas classes de complexidade:

O(1)       significa tempo de execução constante
O(log n)   significa tempo de execução logarítmico
O(n)       significa tempo de execução linear
O(n log n) significa tempo de execução log-linear
O(n^c)     significa tempo de execução polinomial (c é uma constante)
O(c^n)     significa tempo de execução exponencial (c é uma constante
           elevada a uma potência baseada no tamanho do input)
"""

"""
Regras para calcular a complexidade assintótica de uma função:

1 _ Se o tempo de execução é a soma de vários termos, fique com aquele
que apresenta a maior taxa de crescimento e descarte os restantes termos.

2 _ Se o termo assim obtido for um produto, descarte as constantes
"""

# Complexidade constante

def modulo (n):
    return n if n >= 0 else -n

# Complexidade logaritmica

def intParaStr(n):
    """A representação textual de um inteiro

    Args:
        n (int): O inteiro
    Assumes:
        n >= 0
    Returns:
        str: A representação textual
    """
    digitos = '0123456789'
    if n == 0:
        return '0'
    resultado = ''
    while n > 0:
        resultado = digitos[n%10] + resultado
        n = n//10 # divisao inteira
    return resultado

def somaDigitos(n):
    """A soma dos algarismos de um número

    Args:
        n (int): O número
    Assumes:
        n >= 0
    Returns:
        str: A soma dos algarismos
    """
    resultado = 0   # 1
    s = intParaStr(n)   # log n
    for c in s: # log n
        resultado += int(c) # 3
    return resultado # 1
    # 1 + log n + 3 * log n + 1  -> 3 * log n -> log n

# Complexidade linear

def fact (n):   # O(n)
    """O factorial de um dado número

    Args:
        n (int): O número

    Returns:
        int: O factorial de n
    """
    i = 1
    resultado = 1
    while i <= n:   # n vezes
        resultado *= i  # O(1)
        i += 1
    return resultado

def fact_rec (n):
    """O factorial de um dado número

    Args:
        n (int): O número

    Returns:
        int: O factorial de n
    """
    return 1 if n < 2 else n * fact_rec(n - 1)
    # fact_rec(n), fact_rec(n-1), fact_rec(n-2), ... fact_rec(1) -> n chamadas recursivas, cada uma com O(1) -> O(n)

# Complexidade log-linear. Esperem até estudarmos ordenação.

# Complexidade polinomial

def intersectam (l1, l2): # quadrática, O(n^2), onde n é o comprimento da maior das 2 listas
    """Uma dada lista tem pelo menos um elemento em comum com uma outra lista?

    Args:
        l1 (list): Uma lista
        l2 (list): A outra lista

    Returns:
        bool: True se as listas têm um elemento em comum, falso caso contrário
    """
    for e1 in l1:   # n
        for e2 in l2:   # n
            if e1 == e2:    # O(1)
                return True
    return False

def sem_repetidos (l): # n = len(l), O(n^2)
    """Devolve uma lista com os elementos de uma dada lista
    eliminando os repetidos

    Args:
        l (list): A lista

    Returns:
        list: A lista sem repetidos
    """
    resultado = []
    for e in l: # n vezes
        if not e in resultado:  # 1 + O(n)
            resultado.append(e) # O(1)
    return resultado

def produto_matrizes (A, B):     # n = linhas_A = colunas_A = colunas_B, O(n^3)
    linhas_A = len(A)
    colunas_A = len(A[0])
    colunas_B = len(B[0])
    # criar a matrix resultado: colunas_A x colunas_B
    C = [[0 for linha in range(colunas_B)] for coluna in range(linhas_A)] # n^2
    for i in range(linhas_A):   # n vezes
        for j in range(colunas_B):  # n vezes
            for k in range(colunas_A):  # n vezes
                C[i][j] += A[i][k] * B[k][j] # O(1)
    return C

# matriz 3x3
X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]
# matriz 3x4
Y = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
C = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
# produto_matrizes(X, Y)

# Complexidade exponencial

def representacaoBinaria (n, numBits):  # O(numBits)
    """A representacao binária de um dado número natural
    com um dado número de bits 

    Args:
        n (int): O número a converter
        numBits (int): O número de bits
    Assumes: n e numBits são não negativos
    Returns:
        str: A representação binária de n com zeros à esquerda
             até preencher numBits
    """
    resultado = ''
    i = n
    while i > 0:
        resultado = str(i % 2) + resultado
        i = i // 2
    # colocar zeros à esquerda
    for _ in range(numBits - len(resultado)):
        resultado = '0' + resultado
    return resultado

def conjuntoPotencia (L):   # O(2^n)
    """O conjunto potência de um dado conjunto em forma de lista

    Args:
        L (list(any)): O conjunto em forma de lista

    Returns:
        list[list(list(any))]: O conjunto potência em forma de lista de listas
    """
    resultado = []
    for i in range(2**len(L)):
        binario = representacaoBinaria(i, len(L))
        subconjunto = []
        for j in range(len(L)):
            if binario[j] == '1':
                subconjunto.append(L[j])
        resultado.append(subconjunto)
    return resultado

toppings = ['Ricota', 'Azeitonas', 'Cogumelos', 'Oregaos', 'Cebola', 'Abacate']

# conjuntoPotencia(toppings)
# Warning: não tentar com mais de 23 toppings

"""
A complexidade das operações Python mais comuns

* Listas l, onde n = len(l)

- Comprimento, len(l): O(1)
- Acesso indexado, l[4]: O(1)
- Alteração indexada, l[7] = 4: O(1)
- Concatenação, l.append(4): O(1)
- Fatiamento, l[:k]: O(k)
- Membro?, 4 in l: O(n)
- Cópia, list(x): O(len(x))
- Apagar, del l[4], O(n)
- min, max: O(n)
- Inserção, l.insert(4, 234): O(n)
- Ordenação, sorted(l), O(n * log n)
- Produto, l * k, O(n * k)

* Conjuntos s, t, onde n = len(s) e m = len(t)

- Comprimento, len(l): O(1)
- Membro?, 4 in l: O(1)
- Uniao, s | t: O( n + m)
- Interseção, s & t: O( n * m)
- Diferença, s - t: O(n)
- Cópia, set(x): O(len(x))

* Dicionários d onde n = len(d)
- Membro?, 4 in d: O(1)
- Acesso, chave in d, O(1)
- Alteração, d[chave] = 4: O(1)
- Apagar, del d[chave], O(1)
- Cópia, dict(d): O(n)
"""

"""
"""