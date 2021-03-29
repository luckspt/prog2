import functools
import itertools

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


#13

#15 - Escreva a função filter recorrendo apenas à função reduce.
def prob15(f, lst):
    return functools.reduce(lambda acc, el: acc+[el] if f(el) else acc, lst, [])

#16 - Escreva a função map recorrendo apenas à função reduce.


#17 - Defina as seguintes funções:
# a) a função total, de modo a que total(f, n) seja f(0)+ f(1)+ ... + f(n).
"""
Por exemplo:
>>> total(lambda x: x**2, 4)
30
"""
def prob17a(f, n):
    return functools.reduce(lambda acc, el: acc + f(el), range(n+1), 0)

# b) a função total_superior, de modo a que total_superior(f) é a função que, no ponto n, retorna f(0)+ f(1)+ ... + f(n).
"""
Exemplo:
>>> total_superior(lambda x: x**2)(4)
30
"""
def prob17b(f):
    return lambda n: prob17a(f, n)

#18 - A função take retorna os primeiros n elementos de uma lista. Escreva esta função recorrendo à função islice
def prob18(lst, n):
    return list(itertools.islice(lst, n))

#19 - A função drop retorna os últimos n elementos de uma lista. Escreva esta função recorrendo à função islice.
def prob19(lst, n):
    comp = len(lst)
    return list(itertools.islice(lst, comp-n, comp))

#20 - Escreva a função enumerate recorrendo à função zip.
def prob20(lst):
    return zip(lst, range(len(lst)))

#21 - Na pasta Documentos do Moodle pode encontrar um ficheiro olimpicos.py que possui informação sobre os atletas que participaram nos Jogos Olímpicos de 2016 no Rio de Janeiro, sob a formade uma lista de listas atletas. Descarregue este ficheiro para o seu computador. Pode obter a lista de listas através da instrução
# >>> from olimpicos import atletas
from olimpicos import atletas

# ID, nome, sexo, idade, altura, peso, país de origem, código do país de origem, desporto, evento, e medalha ('NA', 'Bronze', 'Silver' ou 'Gold')
# Utilizando a função group by do módulo itertools, responda às seguintes questões:
# a) Quantas medalhas foram alcançadas pelos diferentes países?
def prob21a():
    atletasSortedPais = sorted(atletas, key=lambda el: el[7])
    atletasComMedalhas = filter(lambda el: el[-1] != 'NA', atletasSortedPais)
    paisesAgrupados = itertools.groupby(atletasComMedalhas, key=lambda el: el[7])
    paisesMapped = map(lambda el: [el[0], len(list(el[1]))], paisesAgrupados)

    paisesSort = sorted(paisesMapped, key=lambda el: el[1], reverse=True)
    print(paisesSort)

# b) Qual foi a atleta (mulher) mais medalhada?
def prob21b():
    ordenadosNome = sorted(atletas, key=lambda el: el[1])
    medalhas = filter(lambda x: x[-1] != "NA" and x[2] != "M", ordenadosNome)
    agruparMulheres = itertools.groupby(medalhas, key=lambda el: el[1])
    contarMedalhas = map(lambda x: (x[0], len(list(x[1]))), agruparMulheres)
    print(sorted(contarMedalhas, key=lambda el: el[1], reverse=True)[:5]) 

# c) Quantas medalhas de Ouro, Prata, e Bronze, foram alcançadas pela Espanha?
def prob21c():
    espanhois = filter(lambda el: el[7] == 'ESP' and el[-1] != 'NA', atletas)
    espanhoisSort = sorted(espanhois, key=lambda el: el[-1])
    medalhas = itertools.groupby(espanhoisSort, key=lambda el: el[-1])
    medalhasMapped = map(lambda el: (el[0], len(list(el[1]))), medalhas)
    print(list(medalhasMapped))

# d) Quantos atletas portugueses medem 160cm de altura ou menos? Nota: conte cada atleta apenas uma vez.
def prob21d():
    portugueses160cm = filter(lambda el: el[7] == 'POR' and el[4] <= 160, atletas)
    portuguesesSorted = sorted(portugueses160cm, key=lambda el: el[0])
    portuguesesGroupped = itertools.groupby(portuguesesSorted, key=lambda el: el[0])
    print(len(list(portuguesesGroupped)))

# e) Que país competiu com a equipa Olímpica mais leve (em média)? Nota: Descarte atletas para os quais a informação sobre o peso não existe, 'NA'.
def mapPaises(pais):
    codigo, atletas = pais
    atletasPeso = list(map(lambda el: el[5], atletas))

    return (codigo, sum(atletasPeso) / len(atletasPeso))

def prob21e():
    atletasComPeso = filter(lambda el: el[5] != 'NA', atletas)
    atletasSortedPais = sorted(atletasComPeso, key=lambda el: el[7])
    paisesAgrupados = itertools.groupby(atletasSortedPais, key=lambda el: el[7])
    paisesMapped = map(mapPaises, paisesAgrupados)
    paisesSorted = sorted(paisesMapped, key=lambda el: el[1])
    print(list(paisesSorted)[0])

#22 - Na pasta Documentos do Moodle pode encontrar um ficheiro movimentos.py que possui informação sobre várias transações de um agregado familiar entre junho de 2019 e junho de 2020. Esta informação encontra-se sob a forma de uma lista de listas movimentos. Descarregue este ficheiro para o seu computador. Pode obter a lista de listas através da instrução
# >>> from movimentos import movimentos
from movimentos import movimentos
# Verifique que a tabela tem 2000 linhas e que a primeira linha da tabela é
# >>> print(movimentos[0])
# ['Francisco', -13.06, '2019-06-20', 'curso']
# Os vários campos de cada linha significam, por ordem:
# nome, valor da transação, data de execução, e categoria.
# Utilizando a função groupby do módulo itertools, responda às seguintes questões:
 
# a)  Quanto dinheiro foi gasto (despesa) em cada categoria?
def mapDinheiro(obj):
    nome, registos = obj

    mapRegistos = map(lambda el: el[1], registos)
    return (nome, sum(mapRegistos))

def prob22a():
    categoriasSorted = sorted(movimentos, key=lambda el: el[-1])
    categoriasGroupped = itertools.groupby(categoriasSorted, key=lambda el: el[-1])
    dinheiroMapped = map(mapDinheiro, categoriasGroupped)
    print(list(dinheiroMapped))

# b)  Quanto dinheiro foi obtido (receita) por cada pessoa?
def prob22b():
    receitas = filter(lambda el: el[1] > 0, movimentos)
    receitasSorted = sorted(receitas, key=lambda el: el[0])
    receitasGroupped = itertools.groupby(receitasSorted, key=lambda el: el[0])
    dinheiroMapped = map(mapDinheiro, receitasGroupped)
    print(list(dinheiroMapped))

# c)  Qual o saldo (receita menos despesa) do Francisco durante cada mês de 2019?
def prob22c():
    francisco2019 = filter(lambda el: el[0] == 'Francisco' and el[2][:4] == '2019', movimentos)
    francisco2019Meses = map(lambda el: (el[0], el[1], el[2][:7]), francisco2019)
    mesesSorted = sorted(francisco2019Meses, key=lambda el: el[2])
    mesesGrouped = itertools.groupby(mesesSorted, lambda el: el[2])
    dinheiroMapped = map(mapDinheiro, mesesGrouped)

# Testes
if __name__ == '__main__':
    import doctest

    doctest.testmod()
