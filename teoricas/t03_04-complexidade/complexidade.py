"""
O(1)        significa tempo de execução constante
O(log n)    significa tempo de execução logarítmico
O(n)        significa tempo de execução linear
O(n log n)  significa tempo de execução log-linear
O(n^c)      significa tempo de execução polinomial (c é uma constante)
O(c^n)      significa tempo de execução exponencial (c é uma constante)
"""

# Quanto tempo leva esta função a executar?
def f(i):
    """
    Args:
        i (int)

    Assumes:
        i >= 0
    """
    resultado = 1
    while(i>=1):
        resultado *= 1
        i-=1
    return resultado

def buscaLinear(L, x):
    """Procura um elemento na lista
    Devolve True se o elemento estiver na lista
    Devolve False caso contrário

    Args:
        L (list): A lista onde procurar
        x (any): O elemento a procurar

    Returns:
        bool: O elemento está na lista?
    """
    for e in L:
        if e == x:
            return True
    return False

def factorial(n):
    """O factorial de um dado número

    Args:
        n (int): O número

    Returns:
        int: o factorial de n
    """
    i = 1 #1op
    resultado = 1 #1op
    while i <= n: #1op
        resultado *= i #2op
        i += 1 # 2op
    return resultado #1 op
# 2 + n*5 + 1 = 5n + 3
# considerar n mto grande, complexidade assintotica
# n = 1'000'000, 5n + 3 ~= 5n + 27 ~= 5n
# n 1'000'000'000'000, 5n ~= n

def constant(): # 2 + 3*1000 -> constante
    resultado = 0 #1op
    for _ in range(1000): #1op; for executado 1000 vezes
        resultado += 1 #1op
    return resultado # 1op

def linear(n): # 2 + n*3 ~= 3n ~= n -> linear
    resultado = 0 #1op
    for _ in range(n): #1op; for executado n vezes
        resultado += 1 #2op
    return resultado #1op

def quadratico(n): # 2 + 2*n (1 + n*3) + 1 ~= 2n^2
    resultado = 0 #1op
    for _ in range(n): #1op; corpo do for executado n vezes
        for _ in range(n): #1op; executado n vezes
            resultado += 1 #2op
    return resultado #1op

def comparar(n): # k + n + n^2 -> manter o termo que cresce mais rápido -> n^2
    print(f'{constant()} constant') #k (1000) ops
    print(f'{linear(n)} linear') #n ops
    print(f'{quadratico(n)} quadratico') #n^2 ops

##### Complexidade constante ######
def modulo(n):
    return n if n >= 0 else -n

##### Complexidade logaritmica #####
def intParaString(n): # k + k'*log_10 n -> logaritmico O(log n)
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
    while n > 0: #qtas vezes executa? em função de n -> log_10 n -> log n
        resultado = digitos[n%10] + resultado
        n = n//10
    return resultado

def somaDigitos(n): # 1 + log n + 2 * log n + 1 -> 3 * log n -> log n
    resultado = 0 # 1op
    s = intParaString(n) #log n ops
    for c in s: #log n ops
        resultado += int(c) # 2ops
    return resultado # 1op

def fact_rec(n):
    """O fatorial de dado número

    Args:
        n (int): O número

    Returns:
        int: O factorial de n
    """
    return 1 if n < 2 else n * fact_rec(n-1)
##### Complexidade

##### Complexidade log-linear - Ordenação
##### Complexidade log-linear

##### Complexidade polinomial
def intersectam(l1, l2):
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                return True
    return False
##### Complexidade polinomial