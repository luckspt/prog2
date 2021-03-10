# 1. Considere a função conta_positivos indicada abaixo.
def conta_positivos(v):
    """número de elementos positivos numa lista
    
    Args:
        v (list): lista de números

    Returns:
        int: número de valores positivos em v
    """
    conta = 0
    for x in v:
        if x >= 0:
            conta = conta + 1
    return conta


# a) Encontre a falha (o defeito) na implementação.
"""
Qdo o 0 está na lista
"""


# c) Repare a falha.
def prob1c(v):
    """número de elementos positivos numa lista

    Args:
        v (list): lista de números

    Returns:
        int: número de valores positivos em v

    >>> prob1c([0, 0, 0, 0, 0])
    0
    >>> prob1c([1, 2, 3, 4, 5])
    5
    """
    conta = 0
    for x in v:
        if x > 0:
            conta = conta + 1
    return conta


# 2 - Repita os passos do exercício 1 para a função encontra_ultimo indicada abaixo.
def encontra_ultimo(lista, x):
    """índice do último elemento numa lista que é igual a um dado elemento.
    
    Args:
        lista (list): lista
        x (any): valor a procurar numa lista
        
    Returns:
        índice da última ocorrência de x em lista,
        ou None se x não ocorrer na lista
    """
    for i in range(len(lista) - 1, 0, -1):
        if lista[i] == x:
            return i
    return None


# a) Encontre a falha (o defeito) na implementação.
"""
Qdo o elemento que se procura está no índice 0
"""


# c) Repare a falha.
def prob2c(lista, x):
    """índice do último elemento numa lista que é igual a um dado elemento.

    Args:
        lista (list): lista
        x (any): valor a procurar numa lista

    Returns:
        índice da última ocorrência de x em lista,
        ou None se x não ocorrer na lista

    >>> prob2c(['a', 'b'], 'a')
    0
    >>> prob2c(['a', 'b'], 'b')
    1
    """
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == x:
            return i
    return None


# 3 - Escreva três testes para a função fibonacci indicada abaixo.
def fibonacci(n, a=1, b=1):
    """termo n da sequência de Fibonacci
    
    Args:
        n (int): índice do termo a calcular
        a (int, optional): guarda o termo atual da sequência. Defaults to 1.
        b (int, optional): guarda o termo seguinte da sequência. Defaults to 1.

    Returns:
        int: termo de índice n

    >>> fibonacci(0)
    1
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    2
    """
    return a if n == 0 else fibonacci(n - 1, b, a + b)

#4 - Escreva quatro testes para o predicado e_bissexto indicado abaixo.
def e_bissexto(ano):
    """Verifica se um dado ano é bissexto
    
    Args:
        ano (int): ano a verificar
        
    Returns:
        bool: True se ano for bissexto, False c.c.

    >>> e_bissexto(0)
    True
    >>> e_bissexto(2004)
    True
    >>> e_bissexto(2020)
    True
    >>> e_bissexto(2021)
    False
    """
    return ano % 400 == 0 if ano % 100 == 0 else ano% 4 == 0


#5 - Considere a função media indicada abaixo.
def media(lista):
    """média dos valores de uma lista

    Args:
        lista (list): lista de números

    Returns:
        média dos valores na lista se esta for não vazia,
        ou None caso contrário.

    >>> media([])
    >>> media([1])
    1.0
    >>> media([-1])
    -1.0
    >>> media([1, 2])
    1.5
    >>> media([-1, -2])
    -1.5
    """
    return sum(lista)/len(lista) if len(lista) > 0 else None

# Considere as seguintes características:
#   > Número de elementos na lista.
#   > A lista contém números negativos?
# a)  Para cada característica identifique blocos adequados.
# b)  Combine todos os blocos, eliminando os casos inviáveis. Apresente os resultados numa tabela desta forma

# (0 elementos, negativos) é inviável
# Características | Teste
# elementos | negativos | lista    | resultado
# ----------+-----------+----------+----------
# 0         | F         | []       | None
# 1         | F         | [1]      | 1
# 1         | T         | [-1]     | -1
# >1        | F         | [1,2]    | 1.5
# >1        | T         | [-1,-2]  | -1.5
#
# c) Apresente os testes em formato doctest

#6 - Considere a função substituir indicada abaixo.
def substituir(lista, antigo, novo):
    """cria uma cópia da lista dada onde ocorrências de um dado valor são substituídas por outro valor

    Args:
        lista (list): lista de valores
        antigo (any): valor a substituir
        novo (any): novo valor

    Returns:
        list: lista após a substituição
    """
    return [novo if x==antigo else x for x in lista]
# Escreva uma bateria de testes para esta função, seguindo os passos do exercício 5. Considere as seguintes características:
#   > Número de elementos na lista
#   > Número de vezes que antigo ocorre em lista
# Características | Teste
# elementos | nº antigos | lista        | antigo | novo | resultado
# ----------+------------+--------------+--------+------+----------
# 0         | 0          | []           | 1      | 5    | []
# 1         | 0          | [1]          | 2      | 5    | [1]
# 1         | 1          | [-1]         | -1     | 5    | [5]
# >1        | 0          | [1,2]        | 3      | 5    | [1,2]
# >1        | 1          | [-1,-2]      | -1     | 5    | [5, -2]
# >1        | >1         | [-1,-2, -1]  | -1     | 5    | [5, -2, 5]

#8 - Considere a função intersecao indicada abaixo:
def intersecao (lista1, lista2):
    """lista interseção de duas listas.

    Pre:
        ambas as listas são sem duplicados

    Post:
        a lista resultante é sem duplicados

    Args:
        lista1 (list): uma lista
        lista2 (list): outra lista

    Returns:
        list: a lista com os elementos que ocorrem em ambas as listas"""
    pass
# Escreva uma bateria de testes para esta função, seguindo os passos do exercício 5. Considere as seguintes características
#   > A lista1 está vazia?
#   > A lista2 está vazia?
#   > Relação entre lista1 e lista2: as listas têm os mesmos elementos, lista1 é subconjunto de lista2, lista2 é subconjunto de lista1, as listas não têm elementos em comum, nenhuma das anteriores.
# Características | Testes
# l1 vazia  | l2 vazia  | rel l1 l2 | input             | resultado
# ----------+-----------+-----------+-------------------+----------
# T         | T         | iguais    | ([],[])           | []
# T         | F         | l1 C      | ([],[1,2])        | []
# F         | T         | l2 C      | ([1,2,3],[])      | []
# F         | F         | iguais    | ([1,2],[1,2])     | [1,2]
# F         | F         | l1 C      | ([1],[1,2,3])     | [1]
# F         | F         | l2 C      | ([4,5,6],[5,6])   | [5,6]
# F         | F         | nenhum    | ([1,2,3],[4,5,6]) | []
# F         | F         | outros    | ([1,2,3],[2,6,7]) | [2]

# 12 - Escreva uma bateria de testes para a função conta_positivos (exercício 1) utilizando a técnica da partição de espaço de entrada.
def prob12(v):
    """número de elementos positivos numa lista

    Args:
        v (list): lista de números

    Returns:
        int: número de valores positivos em v
    >>> prob12([])
    0
    >>> prob12([1])
    1
    >>> prob12([-1])
    0
    >>> prob12([0])
    0
    >>> prob12([1,2])
    2
    >>> prob12([-1,-2])
    0
    >>> prob12([1,-2])
    1
    """
    conta = 0
    for x in v:
        if x > 0:
            conta = conta + 1
    return conta


# a) Modele o domínio da função, identificando uma ou mais características.
# b) Para cada característica identifique blocos adequados.
"""
        A                           B
Tamanho da lista            |   0, 1, >1
Todos elementos positivos   |   True, False
Todos elementos negativos   |   True, False
"""
# c) Combine todos os blocos, eliminando os pares inviáveis. Apresente os resultados na forma de uma tabela.
"""
                CARACTERISTICAS                             |           TESTES
Tamanho Lista   |   Todos Positivos |   Todos Negativos     |   Entrada     |   Saída
----------------+-------------------+-----------------------+---------------+------------- 
    0           |       True        |       True            |       []      |       0
    0           |       True        |       False           |           Inviável
    0           |       False       |       True            |           Inviável
    0           |       False       |       False           |           Inviável
    ---------------------------------------------------------------------------------
    1           |       True        |       True            |           Inviável
    1           |       True        |       False           |      [1]      |       1
    1           |       False       |       True            |     [-1]      |       0
    1           |       False       |       False           |      [0]      |       0
    ---------------------------------------------------------------------------------
    >1          |       True        |       True            |           Inviável
    >1          |       True        |       False           |     [1, 2]    |       2
    >1          |       False       |       True            |    [-1,-2]    |       0
    >1          |       False       |       False           |     [1,-2]    |       1 
"""
# d)  Apresente os testes em formato doctest.

# 13 - Escreva uma bateria de testes para a função encontra_ultimo (exercício 2) utilizando a técnica da partição de espaço de entrada. Siga os passos do exercício 12.
def prob13(lista, x):
    """índice do último elemento numa lista que é igual a um dado elemento.

    Args:
        lista (list): lista
        x (any): valor a procurar numa lista

    Returns:
        índice da última ocorrência de x em lista,
        ou None se x não ocorrer na lista

    >>> prob13([], 7)
    >>> prob13([1], 7)
    >>> prob13([7], 7)
    0
    >>> prob13([1, 2], 7)
    >>> prob13([1, 7], 7)
    1
    >>> prob13([7, 7, 7], 7)
    2
    """
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == x:
            return i
    return None
# a) Modele o domínio da função, identificando uma ou mais características.
# b) Para cada característica identifique blocos adequados.
"""
        A                           B
Tamanho da lista            |   0, 1, >1
Qtd ocorrências             |   0, 1, >1
"""
# c) Combine todos os blocos, eliminando os pares inviáveis. Apresente os resultados na forma de uma tabela.
"""
                CARACTERISTICAS     |           TESTES
Tamanho Lista   |   Qtd ocorrências |   Entrada         |   Saída
----------------+-------------------+-------------------+-------------- 
    0           |       0           |      ([], 7)      |       None
    0           |       1           |               Inviável
    0           |       >1          |               Inviável    
    -------------------------------------------------------------------
    1           |       0           |    ([1], 7)       |   None
    1           |       1           |    ([7], 7)       |   0
    1           |       >1          |               Inviável
    -------------------------------------------------------------------
    >1          |       0           |    ([1, 2], 7)    |   None
    >1          |       1           |    ([1, 7], 7)    |   1
    >1          |       >1          |    ([7, 7, 7], 7) |   2
"""
# d)  Apresente os testes em formato doctest.


# 14 - Considere a função diferenca indicada abaixo.
# Escreva uma bateria de testes para esta função utilizando a técnica da partição de espaço de entrada. Siga os passos do exercício 12.
def diferenca(l1, l2):
    """lista que contém os elementos de l1 que não estão em l2

    Args:
        l1 (list): lista
        l2 (list): lista

    Returns:
        list: lista l1 \ l2

    >>> diferenca([],[])
    []
    >>> diferenca([],[1,2])
    []
    >>> diferenca([1,2],[])
    [1, 2]
    >>> diferenca([1,2,3],[1,2,3])
    []
    >>> diferenca([1,2,3],[1,4,5])
    [2, 3]
    >>> diferenca([1,2,3],[7,4,5])
    [1, 2, 3]
    """
    resultado = []
    for x in l1:
        if x not in l2:
            resultado.append(x)
    return resultado
# a) Modele o domínio da função, identificando uma ou mais características.
# b) Para cada característica identifique blocos adequados.
"""
        A                           B
len(l1)                 |   0, >0
len(l2)                 |   0, >0
l1 tem elementos de l2  | alguns, nenhuns, todos

"""
# c) Combine todos os blocos, eliminando os pares inviáveis. Apresente os resultados na forma de uma tabela.
"""
                CARACTERISTICAS     |           TESTES
Comp. l1    |   Comp. l2    |   l1 contem l2    |   Entrada             |   Saída
------------+---------------+-------------------+-----------------------+-------------- 
     0      |    0          |   todos           |   ([], [])            |   []
     0      |   >0          |   nenhum          |   ([], [1,2])         |   []
    --------------------------------------------------------------------+----------
    >0      |    0          |    todos          |   ([1,2], [])         |   [1,2]
    >0      |   >0          |    todos          |   ([1,2,3], [1,2,3])  |   []
    --------------------------------------------------------------------+----------
    >0      |    0          |    alguns         |   ([1,2,3], [1,4,5])  |   [2,3]
    >0      |   >0          |    nenhum         |   ([1,2,3], [7,4,5])  |   [1,2,3]
"""
# d)  Apresente os testes em formato doctest.


#15 - Considere a função soma_produtos indicada abaixo. No caso de a função ser chamada com listas de tamanho diferente, levanta a exceção ValueError. Observe que a documentação inclui um teste para o caso em que a primeira lista tem dimensão inferior à segunda lista.
def soma_produtos(xs, ys):
    """soma dos produtos dos elementos de duas listas dadas, elemento a elemento
    
    Args:
        xs (list[float]): lista de floats
        ys (list[float]): lista de floats
        
    Raises:
        ValueError: caso as listas tenham comprimentos diferentes
    
    Returns:
        float: produto interno entre xs e ys
        
    >>> soma_produtos([1.0], [1.0, 2.0])# (x1,y2)
    Traceback (most recent call last):
    ...
    ValueError
    """
    if len(xs) != len(ys):
        raise ValueError
    resultado = 0.0
    for i in range(len(xs)):
        resultado += xs[i] * ys[i]
    return resultado
# a) Modele o domínio da função, identificando uma ou mais características.
# b) Para cada característica identifique blocos adequados.
"""
        A                           B
len(l1)                 |   0, 1, >1
len(l2)                 |   0, 1, >1
"""
# c) Combine todos os blocos, eliminando os pares inviáveis. Apresente os resultados na forma de uma tabela.
# Características | Teste
# tamanho l1 | tamanho l2 | Entrada | resultado
# -----------+-------------+-----------+--------------
# 0 0 ([],[]) 0.0 # 0 1 ([],[1]) ValueError
# 0 >1 ([],[1.0,2.0]) ValueError
# 1 0 ([1],[]) ValueError
# 1 1 ([1.0],[1.0]) 1.0
# 1 >1 ([1.0], [1.0, 2.0]) ValueError
# >1 0 ([1.0,2.0],[]) ValueError
# >1 1 ([1.0,2.0],[1.0]) ValueError
# >1 >1 ([1.0,2.0],[1.0,2.0]) 5.0

# Inclua testes adicionais para esta função, utilizando a técnica da partição de espaço de entrada. Siga os passos do exercício 12.
# 16 - Considere a função maximo_lista que devolve o máximo de uma lista de números inteiros. No caso de a função ser chamada com uma lista vazia, levanta a exceção IndexError.
# Nota: a lista vazia faz parte do espaço de entrada da função maximo_lista, mesmo que não faça parte do seu domínio. Como temos informação sobre o comportamento excecional (fora do domínio) podemos testar a função para este caso. Escreva uma bateria de testes para esta função utilizando a técnica da partição de espaço de entrada. Siga os passos do exercício 12

"""
len(lst)
0 na lista
tem nums negativos
"""







# Correr testes
if __name__ == "__main__":
    import doctest

    doctest.testmod()