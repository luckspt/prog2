import math
#1 - Ordene as seguintes funções por taxa de crescimento assintótico: 4 n log n, 2^{10}, 2^{log_{10}n}, 3n + 100log n, 4^n, n^2 + 10n
"""
    2^{10}              O(1)
    2^{log_{10}n}       O(n^c) => 2^{log_10 n} = 2^{log_2 n / log_2 10} = n^{1 / log_2 10} = n^0,30..
    3n + 100 log n      O(n)
    4 n log n           O(n log n)
    n^2 + 10n           O(n^c)
    4^n                 O(c^n)
"""

#2 - Num dado computador, uma operação demora um milisegundo a ser executada. Considere um programa que realiza um número de operações dado pela função f(n) = n^5, para um qualquer parâmetro n. Qual o maior valor de n para o qual o programa é capaz de terminar os seus cálculos se o tempo disponível for (a) um ano; (b) uma década; (c) 15 mil milhões de anos (a idade do universo)? Nota: um ano tem aproximadamente 3.15*(10^7) segundos.
def prob2():
    anoMS = 3.15 * (10 ** 7) * 1000
    decadaMS = 10 * anoMS
    universo = 15000000000 * anoMS
    
    print(f'1 ano: {round(anoMS ** (1/5))}')
    print(f'10 anos: {round(decadaMS ** (1/5))}')
    print(f'universo: {round(universo ** (1/5))}')

#3 - Repita o exercício anterior para as seguintes funções: f(n) = 10n, f(n) = 1000n, f(n) =n^2 e f(n) = 2^n
def prob3():
    anoMS = 3.15 * (10 ** 10)
    decadaMS = 10 * anoMS
    universoMS = 15 * (10**9) * anoMS
    lst = [
        anoMS,
        decadaMS,
        universoMS
    ]

    print('f(n) = 10n')
    for n in lst:
        print(round(n / 10))

    print('f(n) = 1000n')
    for n in lst:
        print(round(n / 1000))
    
    print('f(n) = n^2')
    for n in lst:
        print(round((n**(1/2) / 10)))
    
    print('f(n) = 2^n')
    for n in lst:
        print(round(math.log(n, 2)))
    
#4 - Supponha que o tempo de execução de um algoritmo em inputs de tamanho 1000, 2000, 3000 e 4000 é de 5 segundos, 20 segundos, 45 segundos, e 80 segundos, respetivamente. Estime quanto tempo levará para resolver um problema de tamanho 5000. A taxa de crescimento assintótico do algoritmo é linear, log-linear, quadrática,cúbica ou exponencial?

#5 - Apresente uma caracterização O do tempo de execução de cada uma das funções abaixo, em termos do input n.
#O(n^2)
def prog5_a(n):
    m = 0
    for i in range(1, 10 * n):
        for j in range(1, n):
            m += 1
    return m

# O(1)
def prog5_b(n):
    x = 0
    for a in range(0, 2021):
        x += a * n
    return x

#o(n^2)
def prog5_c(n):
    b = n * n
    while b > n:
        if b % 2 == 0:
            b -= 1
        else:
            b -= 2
    return b

# O(n)
def prog5_d(n, v):
    soma = 0
    for i in range(0, n):
        for j in range(1, 4):
            soma += v[i]
    return soma

# O(log n)
def prog5_e(n):
    x = n * n * n
    while x > 1:
        x /= 2
    return x

# O(1)
def prog5_f(n):
    soma = n * n
    while soma % 2 == 0:
        soma -= 1
    return soma

# O(n^2)
def prog5_g(n):
    c = 0
    for i in range(0, n):
        for j in range(i, n):
            c += 1
    return c

# pior caso O(n*m), melhor caso O(n)
def prog5_h(l1, l2):
    soma = 0
    for x in l1:            #O(n)
        if x % 2 == 0:
            soma += 1
        else:
            for y in l2:    #O(m)
                soma += y
    return soma

#6 - Analise a complexidade assintótica da função diferenca.
# O(len(l1) * len(l2)) 
def diferenca(l1, l2):
    """Devolve uma lista que contém os elementos de l1 que não estão em l2
    
    Args:
        l1 (list): lista
        l2 (list): lista
        
    Returns:
        list: lista l1 \ l2
    """
    resultado = []
    for x in l1:
        if x not in l2:
            resultado.append(x)
    return resultado

#7 - Analise a complexidade assintótica da função unicos.
def unicos(lista):
    """Recebe uma lista ordenada e devolve uma outra lista contendo exatamente uma ocorrência de cada elemento da lista original
    
    Args:
        lista (list): lista original de valores
    
    Returns:
        list: lista resultado
    
    Requires: a lista original está ordenada
    Ensures: a lista resultado está ordenada
    """
    return [] if not lista else(
        [lista[i] for i in range(len(lista)-1)
            if lista[i] != lista[i+1]]
        + [lista[-1]])