#!/usr/bin/env python3

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Programação Funcional e Funções de Ordem Superior

Baseado nas referencias
  Functional Programming HOWTO, https://docs.python.org/3/howto/functional.html
  Functional Programming In Python, https://archive.org/details/functional-programming-python/
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

import operator
import itertools
import functools

# 1 _ Iteradores

def ocorrencias(x, s):
    """O número de ocorrencias de um valor num dado objecto iteravel

    Args:
        x (any): O elemento a procurar
        s (any): O objecto iteravel

    Pre:
        s pode ser convertido num iterador

    Returns:
        int: O número de ocorrências
    """
    resultado = 0
    for y in s:
        if x == y:
            resultado += 1
    return resultado

# Uns objectos que podem ser transformados em iteradores
l1 = [1, 2, 3, 4, 6, 2, 0, 1, 5]
d1 = {'a': 1, 'b': 2, 'c': 3}
c1 = {1.62, 2.71, 3.14}

# listas: ocorrencias(True, [True, False, False, True])
# dicionários: ocorrencias('a'', {'a': 1, 'b': 5, 'a':7})
# conjuntos: ocorrencias('a', {'c', 'b', 'd'})

def primeiro(it):
    """O primeiro elemento de um iterador

    Args:
        it (iterator): O iterador

    Pre:
        O iterador tem pelo menos um elemento

    Returns:
        any: O primeiro elemento no iterador
    """
    return next(it)

def dois_primeiros(s):
    """Um par com os dois primeiros elementos de um objecto

    Args:
        s (any): O objecto de onde ler os dois primeiros elementos

    Pre:
        s pode ser convertido num iterador com dois ou mais elementos

    Returns:
        (any, any): Um par com os primeiros dois elementos lidos de s
    """
    it = iter(s)
    return (next(it), next(it))

# listas: dois_primeiros([1, 2, 3, 4])
# dicionarios: dois_primeiros({'a': 1, 'b': 2, 'c': 3})
# conjuntos: dois_primeiros({1.62, 2.71, 3.14})

def ultimo(it):
    """O ultimo elemento de um objecto

    Args:
        it (any): O objecto de onde ler os valores

    Pre:
        s pode ser convertido num iterador *finito*

    Returns:
        any: O ultimo elemento no iterador
    """
    ultimo = next(it)
    for ultimo in it:
        pass
    return ultimo

# Outros operadores sobre objetos que podem ser convertidos em
# iteradores (objectos iteráveis): max, min, in, not in

def max_iter(s):
    """O maior valor num objeto iteravel

    Args:
        s (s): O objecto que pode ser convertido num iterador

    Pre:
        s pode ser convertido num iterador *finito*

    Returns:
        any: O maior valor
    """
    resultado = next(iter(s))
    for x in s:
        if x > resultado:
            resultado = x
    return resultado


# 2 _ A função filter: aceita um predicado e um iterador; devolve um iterador

# Filtrar elementos maiores do que tres

def maior_que_tres(x):
    return x > 3

maiores_que_tres = filter (maior_que_tres, l1)

# Filtar listas nao vazias

def nao_vazia (l):
    return l != []

l2 = [[1, 2], [], [0,7,8], [], [], [6, 1, 7, 9]]

nao_vazias = filter(nao_vazia, l2)

# pares maiores do que tres

def par(x):
    return x % 2 == 0

pares_maiores = filter(maior_que_tres, filter(par, range(1,10)))

# mesma coisa em forma de iterador em compreensao
pares_maiores_it = (x for x in range(1, 10) if par(x) and maior_que_tres(x))

# mesma coisa em forma de lista em compreensao; é uma lista e não um iterador
pares_maiores_lista = [x for x in range(1, 10) if par(x) and maior_que_tres(x)]

# Maior numero inferior a 100.000 que é divisivel por 3829

def p(x): return x % 3829 == 0
numeros = range(99999, 0, -1)
maior = next(filter(p, numeros))

# De um modo geral:
# Estilo programacao funcional classico
#   filter(predicado, iterador)
# Estilo compreensão
#   (x for x in iterador if predicado(x))


# 3 _ A função map: aceita uma funcao de transformacao e um iterador; devolve um iterador

# De um modo geral
# Estilo programacao funcional classico
#   map(transformacao, iterador)
# Estilo compreensão
#   (transformacao(x) for x in iterador)

def mais_tres(x):
    return x + 3

def junta_bang(s):
    return s + "!"

l3 = ["pum", "pum", "bang", "bang"]

it3 = map(junta_bang, l3)

def quatro_copias(x):
    return [x] * 4

it4 = map(quatro_copias, ["pum", "bang"])

def cabeca(l):
    return l[0]

l4 = [[1, 2], [5, 6, 3], [9, 0, 6, 8]]

it5 = map(cabeca, l4)


# 4 _ Expressões lambda para funções curtas

# listas nao vazias
nao_vazias_bis = filter(lambda l: l != [], l2)

# primeiro elemento de cada lista
it6 = map(lambda l: l[0], l4)

# lambda é uma expressão; podemos guardar o seu valor numa variável
# É um modo de escrever funções simples sem def.
somar = lambda x, y: x + y

sete = somar(3, 4)

# map pode ser chamado com mais do que um iterador.
# neste caso a função tem tantos parametros quantos quantos os iteradores
def produto_vetorial(xs, ys):
    """A produto vetorial de dois vetores em forma de iterador

    Args:
        xs (iter[number]): Um dos vetores
        ys (iter[number]): O outro vetor

    Returns:
        iter[number]: O produto vetorial com comprimento igual os menor
            dos comprimentos de xs e ys
    """
    return map(lambda x, y: x * y, xs, ys)

def produto_escalar(xs, ys):
    """A produto escalar de dois vetores em forma de iterador

    Args:
        xs (iter[number]): Um dos vetores
        ys (iter[number]): O outro vetor

    Returns:
        number: O produto escalar de xs e ys, considerando os prefixos
            de xs e ys correspondentes ao menor comprimento dos vetores
    """
    return sum(produto_vetorial(xs, ys))

# os iteradores nao precisam de ter o mesmo comprimento
prod = produto_vetorial([1, 2, 3, 4, 5], [11, 12])

# exemplo com tres iteradores
saudacoes = ["Olá", "Bom dia", "Oi"]
nomes = ["Ada", "Abel", "Eva"]
perguntas = ["como vais?", "tudo bem?", "tudo em cima?"]
frases = map(lambda s, n, p: s + ", " + n + "! " + p,
    saudacoes, nomes, perguntas)

# Combinando map e filter

# primeiro elemento de cada lista não vazia.
# Não confundir as duas variaveis l, uma em cada lambda
it7 = map(lambda l: l[0], filter(lambda l: l != [], l2))

# Também poderiamos escrever assim:
it8 = map(lambda x: x[0], filter(lambda y: y != [], l2))

# A soma de todos os quadrados impares, para numeros até 100
quadrados_pares = map(lambda x: x * x, filter(lambda x: x % 2 ==0, range(101)))

# Filtros de filtros

# Um filtro depois do outro
pares_maiores_bis = filter(lambda x: x > 3, filter(lambda x : x % 2 == 0, range(1,10)))

# Os 2 filtros de uma vez só
pares_maiores_tris = filter(lambda x: x > 3 and x % 2 == 0, range(1,10))

# maps de maps

# somar 10 a cada elemento de um iterador
def somar_10(xs):
    return map(lambda x: x + 10, xs)

it9 = somar_10([1, 2, 3, 4])

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]]

# Um iterador onde cada elemento é por sua vez um iterador
it10 = map(somar_10, matriz)

# Tudo numa linha
it11 = map(lambda xs: map(lambda x: x + 10, xs), matriz)

def para_lista_listas(it):
    """A lista de listas correspondente a um iterador de iteradores.
    Útil para visualisar o resultado de um map de maps

    Args:
        it (iter[iter]): O iterador de iteradores

    Returns:
        list[list]: A lista de listas
    """
    return list(map(list, it))

listas = para_lista_listas(it11)


# 5 _ O módulo operator, operadores básicos como funções

# https://docs.python.org/3/library/operator.html

def produto_vetorial_bis(xs, ys):
    """A produto vetorial de dois vetores em forma de iterador

    Args:
        xs (iter[number]): Um dos vetores
        ys (iter[number]): O outro vetor

    Returns:
        iter[number]: O produto vetorial com comprimento igual os menor
            dos comprimentos de xs e ys
    """
    return map(operator.mul, xs, ys)

segundo_de_l1 = l1[1]

# operator.itemgetter é uma função que devolve uma função
segundo = operator.itemgetter(1)    # segundo é uma função (sem def)

segundo_de_l1_bis = segundo(l1)

# primeiro elemento de cada lista, revisitado
it12 = map(operator.itemgetter(0), l4)


# 6 _ Mais funções de ordem superior: any, all, zip

# será que todos os elementos da lista l1 sao pares?
b1 = all(map(lambda x: x % 2 == 0, l1))

# existe pelo menos um elemento da lista l1 que é par?
b2 = any(map(lambda x: x % 2 == 0, l1))

# zip: retira um elemento de cada iterador e devolve-os num tuplo.
# Recebe dois iteradores e devolve um iterador de pares com um
# comprimento igual ao menor dos comprimentos dos argumentos.

triplos = zip(saudacoes, nomes, perguntas)

frases_bis = map(lambda t: t[0] + ", " + t[1] + "! " + t[2],
    zip(saudacoes, nomes, perguntas))

# Tal como no map, os iteradores não precisam ter todos o mesmo comprimento

pares = zip(range(100), ['p', 'r', 'o', 'g', '2'])


# 7 _ O módulo itertools (não esquecer o import)

# https://docs.python.org/3/library/itertools.html#module-itertools

# itertools.takewhile, devolve elementos enquanto o predicado é verdadeiro

it13 = itertools.takewhile(lambda x: x > 0, [1, 2, 3, 4, 5, -4, 6, 7, 8, 9])

# A soma de todos os quadrados impares menores do que 10.000
adivinha = sum(
    itertools.takewhile(lambda x: x < 10000, 
        filter(lambda x: x % 2 == 1,
            map(lambda x: x * x,
                itertools.count(1)))))


# 8 _ A funcao reduce (modulo functools)

str = ["ola, ", "como ", "vais?"]
# Transformar numa frase:
#   ["ola, ", "como ", "vais?"] -->
#   "ola, " + "como + "vais?" -->
#   "ola, como vais?"

str1 = functools.reduce(lambda x, y: x + y, str, "")
str2 = functools.reduce(operator.concat, str, "")

soma = functools.reduce(operator.add, [1, 4, 2], 0)

def factorial (n): # 1 * 2 * 3 * 4 * ... * n
    return functools.reduce(operator.mul, range(1, n + 1), 1)

def inverter (it):
    """O iterador inverso de um iterador finito

    Args:
        it (iter): Um iterador

    Returns:
        iter: O iterador inverso
    """
    return functools.reduce(lambda acc, x: [x] + acc, it, [])


# 9 _ A função groupby (módulo itertools)

l5 = [1, 1, 1, 5, 5, 7, 7, 7, 8, 9, 9, 9, 9] # Ordenada!

# Uma iterador com 5 pares: um para os elementos 1, outro para os 5, ...
# e outro para os 9. O segundo elemento de cada par é um iterador com
# os tres 1, dois 5, ... quatro 9.
l6 = itertools.groupby(l5)

# Para visualisar estes iteradores de pares nos quais o segundo elemento
# é um iterador precisamos de uma função simples. Eis algumas alternativas:

def para_dict(it): # Dicionarios em compreensao
    return {chave:list(valor) for (chave, valor) in it}

def para_lista_map(it): # Usando map
    return list(map(lambda x: (x[0], list(x[1])), it))

def para_lista_comp(it): # Usando lista em compreensao
    return [(x[0], list(x[1])) for x in it]

def para_lista(it): # usando lista em compreensao e pattern matching
    return [(x, list(y)) for x, y in it]

distrito_cidades = [
    ('Beja', 'Beja'),
    ('Beja', 'Moura'),
    ('Beja', 'Serpa'),
    ('Évora', 'Borba'),
    ('Évora', 'Estremoz'),
    ('Évora', 'Évora'),
    ('Évora', 'Montemor-o-Novo'),
    ('Évora', 'Reguengos de Monsaraz'),
    ('Évora', 'Vendas Novas'),
    ('Évora', 'Abrantes'),
    ('Santarém', 'Almeirim'),
    ('Santarém', 'Cartaxo'),
    ('Santarém', 'Entroncamento'),
    ('Santarém', 'Fátima (Ourém)'),
    ('Santarém', 'Ourém'),
    ('Santarém', 'Rio Maior'),
    ('Santarém', 'Samora Correia (Benavente)'),
    ('Santarém', 'Santarém'),
    ('Santarém', 'Tomar'),
    ('Santarém', 'Torres Novas')
]

agrupado_por_distrito = itertools.groupby(distrito_cidades, operator.itemgetter(0))

cidades_por_distrito = dict(map(lambda x: (x[0], len(list(x[1]))), agrupado_por_distrito))

distrito_com_mais_cidades = max(cidades_por_distrito, key = cidades_por_distrito.get)

distrito_maior_alfabeticamente = max(cidades_por_distrito)

nome_disciplina_nota = [
    ('Ana', 'Prog2', 20),
    ('Ana', 'ITW', 16),
    ('Ana', 'IPE', 18),
    ('Eva', 'Prog2', 19),
    ('Eva', 'ITW', 19),
    ('Eva', 'IPE', 16),
    ('Abel', 'Prog2', 19),
    ('Abel', 'ITW', 16),
    ('Abel', 'IPE', 20)
]

# Média de todos os alunos a todas as disciplinas
def media(it):
    notas = list(map(operator.itemgetter(2), it))
    return sum(notas) / len(notas)

agrupados = itertools.groupby(nome_disciplina_nota, operator.itemgetter(0))

media_por_aluno = map(lambda x: (x[0], media(x[1])), agrupados)