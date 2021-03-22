# 1- Escreva expressões lambda para as seguintes funções:
# a) Dobro de x
prob1a = lambda x: x * 2

# b) Primeiro elemento de um tuplo
prob1b = lambda tupl: tupl[0]

# c) Triplo da soma de x e y
prob1c = lambda x, y: 3 * (x + y)

# d) Produto de três números
prob1d = lambda x, y, z: x * y * z

# e) Concatenação de duas listas
prob1e = lambda lst1, lst2: lst1 + lst2

# f) A primeira metade de uma lista
prob1f = lambda lst: lst[:len(lst) // 2]

# 2 - Escreva uma expressão lambda para uma função que devolve True apenas quando aplicada a caracteres não brancos, isto é, quando aplicada a caracteres que não pertencem à lista ['', '\t', '\n'].
prob2 = lambda chrs: chrs not in ['', '\t', '\n']

# 3 - Qual o valor de cada expressão?
# a) map(lambda x: x + 1, range(1, 4))
"""
[2, 3, 4]
"""

# b) map(lambda x: x > 0, [3, -5, -2, 0])
"""
[True, False, False, True]
"""

# c) filter(lambda x: x > 5, range(1, 7))
"""
[6]
"""

# d) filter(lambda x: x % 2 == 0, range(1, 11))
"""
[2, 4, 6, 8, 10]
"""

# e) filter(lambda x: x > 0,map(lambda y: y**2,range(-3, 4)))
"""
[1, 4, 9]
"""

# f) map(lambda x: x**2,filter(lambda x: x > 0,range(-3, 4)))
"""
[1, 4, 9]
"""

# g) map(lambda x: x + 's', ['As', 'armas', 'e', 'os', 'barões'])
"""
['Ass', 'armass', 'es', 'oss', 'barõess']
"""

# h) map(lambda x: 's'+ x, ['As', 'armas', 'e', 'os', 'barões'])
"""
['sAs', 'sarmas', 'se', 'sos', 'sbarões']
"""

# i) map(lambda x: map(lambda y: y*y, x), [[1, 2],[3, 4, 5]])
"""
[ [1, 4], [9, 16, 25] ]
"""

# 4 - Defina uma função mapa_seletivo que recebe uma função, um predicado e um iterador, e devolve um iterador. O iterador resultado contém os resultados de aplicar a função aos elementos do iterador que satisfaçam o predicado. Os elementos que não satisfazem o predicado são descartados.
"""
Exemplo:
    >>> list(mapa_seletivo(lambda x: x*3, lambda y: y>0, range(-4, 5)))
    [3, 6, 9, 12]
"""


# a) Utilize listas por compreensão.
def prob4a(mapa, filtro, iter):
    return [mapa(x) for x in iter if filtro(x)]


# b) Utilize a função map.
def prob4b(mapa, filtro, iter):
    return map(mapa, filter(filtro, iter))


# 5 - Escreva a função aplica_todas que chama várias funções com o mesmo argumento e coleciona os resultados num iterador.
"""
Por exemplo:
    >>> list(aplica_todas([e_menor_100, e_maior_10, e_primo], 71))
    [True, True, True]
"""


# a) Utilize listas por compreensão.
def prob5a(funcs, el):
    return (func(el) for func in funcs)


# b) Utilize a função map.
def prob5b(funcs, el):
    return map(lambda func: func(el), funcs)


# 6 - Escreva uma função maior_zero que transforme um iterador de iteradores de inteiros num iterador de iteradores de valores lógicos.
# Cada entrada no iterador resultante indica se o valor na respetiva posição do iterador original é ou não maior do que zero.
"""
Por exemplo:
    >>> [ list(it) for it in maior_zero([ [-1, -2, 3], [2,-1, 3, 7] ]) ]
    [[False, False, True], [True, False, True, True]]
"""


# a) Utilize listas por compreensão.
def prob6a(iters):
    return ((el > 0 for el in it) for it in iters)


# b) Utilize a função map e expressões lambda.
def prob6b(iters):
    return map(lambda it: map(lambda el: el > 0, it), iters)


# 7 - Defina uma função produto_escalar que calcule o produto escalar ∑ni=1xi·yi de dois vetores x e y.
# Os vetores são dados por iteradores de números com o mesmo comprimento. Utilize as funções sum, map e zip.
def prob7(vetx, vety):
    return sum(map(lambda el: el[0] * el[1], zip(vetx, vety)))


# 8 - Dado um par de iteradores, a função zip devolve um iterador de pares. O i-ésimo par é composto pelo i-ésimo elemento do primeiro iterador e pelo i-ésimo do segundo iterador. O iterador resultante contém tantos elementos quantos os do mais curto dos dois iteradores parâmetro. Neste exercício estamos interessados numa função zip_with, variante da função zip, que recebe uma função que combina os dois elementos
def zip_with(f, lista1, lista2):
    """
    >>> list(zip_with(lambda x, y: x, [], [1, 2]))
    []
    >>> list(zip_with(lambda x,y : x, ['a'], []))
    []
    >>> list(zip_with(lambda x, y: (x, y),['a', 'b'], [2, 3, 4]))
    [('a', 2), ('b', 3)]
    >>> list(zip_with(max, [5, 2, 0, 9], [2, 3, 4]))
    [5, 3, 4]
    """
    return prob8d(f, lista1, lista2)


# a) Escreva uma variante da função, utilizando iteração sobre os objetos dadas.
def prob8a(f, lst1, lst2):
    nlista = []
    for idx in range(min(len(lst1), len(lst2))):
        nlista.append(f(lst1[idx], lst2[idx]))
    return nlista


# b) Escreva uma variante da função, utilizando listas por compreensão.
def prob8b(f, lst1, lst2):
    return [f(lst1[idx], lst2[idx]) for idx in range(min(len(lst1), len(lst2)))]


# c) Escreva uma variante recorrendo às funções zip e map.
def prob8c(f, lst1, lst2):
    return map(lambda x: f(x[0], x[1]), zip(lst1, lst2))


# d) Proponha uma solução recorrendo apenas à função map(a função map pode ser utilizada com mais do que um iterador).
def prob8d(f, lst1, lst2):
    return map(lambda x, y: f(x, y), lst1, lst2)


# 9 - Escreva a função zip recorrendo à função zip_with do exercício acima
def prob9(*iters):
    return zip_with(lambda x, y: x + y, iters)

#10 - Determine o valor de cada uma das expressões seguintes.
# a) reduce(operator.mul, range(-3, 0, 1), 1)
"""

"""
# b) reduce(operator.mul, range(-3, 0, -1), 1)
# c) reduce(operator.sub, [1, 2, 3])
# d) reduce(operator.sub, [1, 2, 3], 10)
# e) reduce(lambda acc, z: acc*3 + z, range(1, 5))
# f) reduce(lambda acc, y: acc + y if acc > 0 else y, [4, -3, -2, -1])
# g) reduce(lambda acc, y: acc**2 + y, range(5))
# Não se esqueça de fazer import operator para as primeiras quatro alíneas.

# Testes
if __name__ == '__main__':
    import doctest

    doctest.testmod()
