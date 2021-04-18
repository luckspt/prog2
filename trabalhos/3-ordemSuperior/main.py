from doctest import testmod
from cidades import cidades

from math import sqrt
from functools import reduce

__author__ = 'Lucas Pinto, 56926'

# 1º Latitude = 111,1949 km
lattToKm = lambda latt: latt * 111.1949
# 1º Longitude = 85,1102km
longToKm = lambda long: long * 85.1102

# Teorema de Pitágoras; h² = c1² + c2² <=> h = sqrt(c1² + c2²)
dist = lambda c1, c2: sqrt(
    (lattToKm(c1[0]) - lattToKm(c2[0])) ** 2
    + (longToKm(c1[1]) - longToKm(c2[1])) ** 2)

def distancia_itinerario(itinerario):
    """Calcula a soma das distâncias entre as cidades do itinerario

    Args:
        itinerario (list<string>): Lista das cidades

    Returns:
        float: Soma das distâncias entre as cidades
    
    Throws:
        KeyError: um elemento do itinerário não pertence ao dicionário cidades

    >>> distancia_itinerario([])
    0
    >>> distancia_itinerario(['Porto'])
    0
    >>> distancia_itinerario(['lâmpada'])
    0
    >>> distancia_itinerario(['Lisboa', 'Lisboa'])
    0.0
    >>> distancia_itinerario(['Lisboa', 'Porto'])
    271.4072149632786
    >>> distancia_itinerario(['meia', 'meia'])
    Traceback (most recent call last):
    ...
    KeyError: 'meia'
    >>> distancia_itinerario(['morango', 'bebé'])
    Traceback (most recent call last):
    ...
    KeyError: 'morango'
    """
    return reduce(
        lambda acc, idx: acc + dist(
            cidades[itinerario[idx]]
            , cidades[itinerario[idx + 1]] )
        , range(len(itinerario)-1)
        , 0)
"""
Características:
    > Comprimento do intinerário (0, 1, >1)
    > Elementos do intinerário pertencem ao dict cidades (T, F)
    > Elementos repetidos (T, F)

        Características                         |           Testes
    Comprimento |   Pertencem?  |   Repetidos?  |   Entrada             |   Saída
            0   |      True     |   True        |                   Inviável
            0   |      True     |   False       |                   Inviável
            0   |      False    |   True        |                   Inviável
            0   |      False    |   False       |       []              |   0

            1   |      True     |   True        |                   Inviável
            1   |      True     |   False       |   ['Porto']           |   0
            1   |      False    |   True        |                   Inviável
            1   |      False    |   False       |   ['lâmpada']         |   KeyError: 'lâmpada'

            2   |      True     |   True        | ['Lisboa', 'Lisboa']  |   0
            2   |      True     |   False       | ['Lisboa', 'Porto']   |   271.4072149632786
            2   |      False    |   True        | ['meia', 'meia']      |   KeyError: 'meia'
            2   |      False    |   False       | ['morango', 'bebé']   |   KeyError: 'morango'
"""

def adicionar_cidade(itinerario, cidade):
    """Adiciona uma cidade ao itinerário

    Args:
        itinerario (list<string>): Itinerário
        cidade (string): Nome da cidade a adicionar ao itinerário

    Requires:
        len(itinerario) >= 2
        cidade in cidades

    >>> adicionar_cidade([], 'Lisboa')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade([], 'abelha')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade(['Aveiro'], 'Porto')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade(['Setúbal'], 'pizza')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade(['ananás'], 'Lisboa')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade(['trotinete'], 'pata')
    Traceback (most recent call last):
    ...
    ValueError: min() arg is an empty sequence
    >>> adicionar_cidade(['Mafra', 'Mafra'], 'Maia')
    ['Mafra', 'Maia', 'Mafra']
    >>> adicionar_cidade(['Leiria', 'Leiria'], 'chocolate')
    Traceback (most recent call last):
    ...
    KeyError: 'chocolate'
    >>> adicionar_cidade(['Oeiras', 'Gondomar'], 'Guimarães')
    ['Oeiras', 'Guimarães', 'Gondomar']
    >>> adicionar_cidade(['Viseu', 'Valongo'], 'açúcar')
    Traceback (most recent call last):
    ...
    KeyError: 'açúcar'
    >>> adicionar_cidade(['queijo', 'queijo'], 'Paredes')
    Traceback (most recent call last):
    ...
    KeyError: 'queijo'
    >>> adicionar_cidade(['pão', 'pão'], 'atum')
    Traceback (most recent call last):
    ...
    KeyError: 'pão'
    >>> adicionar_cidade(['pijama', 'calculadora'], 'Aveiro')
    Traceback (most recent call last):
    ...
    KeyError: 'pijama'
    >>> adicionar_cidade(['eslástico', 'peluche'], 'waffle')
    Traceback (most recent call last):
    ...
    KeyError: 'eslástico'
    """
    itinerarioCpy = list(itinerario)

    ops = list(map(
        lambda idx: 
            distancia_itinerario(itinerarioCpy[:idx] + [cidade] + itinerarioCpy[idx:])
        , range(1, len(itinerario)) ))

    minOp = min(ops)
    idxMinOp = ops.index(minOp)

    itinerarioCpy.insert(idxMinOp+1, cidade)
    return itinerarioCpy
"""
Características:
    > Comprimento do intinerário (0, 1, >1)
    > Elementos do intinerário pertencem ao dict cidades (T, F)
    > Elementos repetidos (T, F)
    > Cidade pertence ao dict cidades (T, F)

                        Características                         |                                   Testes
    Comprimento |   Pertencem?  |   Repetidos?  |   Pertence?   |                Entrada               |   Saída
        0       |      True     |   True        |   True        |                                   Inviável
        0       |      True     |   True        |   False       |                                   Inviável
        0       |      True     |   False       |   True        |                                   Inviável
        0       |      True     |   False       |   False       |                                   Inviável
        0       |      False    |   True        |   True        |                                   Inviável
        0       |      False    |   True        |   False       |                                   Inviável
        0       |      False    |   False       |   True        |   [], 'Lisboa'                        |   ValueError: min() arg is an empty sequence
        0       |      False    |   False       |   False       |   [], 'abelha'                        |   ValueError: min() arg is an empty sequence

        1       |      True     |   True        |   True        |                                   Inviável
        1       |      True     |   True        |   False       |                                   Inviável
        1       |      True     |   False       |   True        |   ['Aveiro'], 'Porto'                 |   ValueError: min() arg is an empty sequence
        1       |      True     |   False       |   False       |   ['Setúbal'], 'pizza'                |   ValueError: min() arg is an empty sequence
        1       |      False    |   True        |   True        |                                   Inviável
        1       |      False    |   True        |   False       |                                   Inviável
        1       |      False    |   False       |   True        |   ['ananás'], 'Lisboa'                |   ValueError: min() arg is an empty sequence
        1       |      False    |   False       |   False       |   ['trotinete'], 'pata'               |   ValueError: min() arg is an empty sequence

        2       |      True     |   True        |   True        |   ['Mafra', 'Mafra'], 'Maia'          |   ['Mafra', 'Maia', 'Mafra']
        2       |      True     |   True        |   False       |   ['Leiria', 'Leiria'], 'chocolate'   |   KeyError: 'chocolate'
        2       |      True     |   False       |   True        |   ['Oeiras', 'Gondomar'], 'Guimarães' |   ['Oeiras', 'Guimarães', 'Gondomar']
        2       |      True     |   False       |   False       |   ['Viseu', 'Valongo'], 'açúcar'
        2       |      False    |   True        |   True        |   ['queijo', 'queijo'], 'Paredes'     |   KeyError: 'queijo'
        2       |      False    |   True        |   False       |   ['pão', 'pão'], 'atum'              |   KeyError: 'pão'
        2       |      False    |   False       |   True        |   ['pijama', 'calculadora'], 'Aveiro' |   KeyError: 'pijama'
        2       |      False    |   False       |   False       |   ['eslástico', 'peluche'], 'waffle'  |   KeyError: 'eslástico'
"""

def construir_itinerario(origem, destino, listaCidades):
    """Constrói um itinerário a partir de uma lista de cidades de uma origem a um destino

    Args:
        origem (string): Nome da cidade de origem
        destino (string): Nome da cidade de destino
        listaCidades (list<string>): Lista de cidades do itinerário

    Returns:
        list<string>: Itenerário

    >>> construir_itinerario('ovo', 'Aveiro', [])
    ['ovo', 'Aveiro']
    >>> construir_itinerario('Braga', 'Maia', [])
    ['Braga', 'Maia']
    >>> construir_itinerario('panqueca', 'sim', ['Aveiro'])
    Traceback (most recent call last):
    ...
    KeyError: 'panqueca'
    >>> construir_itinerario('Loulé', 'Barreiro', ['Mafra'])
    ['Loulé', 'Mafra', 'Barreiro']
    >>> construir_itinerario('py', 'Leiria', ['cidade'])
    Traceback (most recent call last):
    ...
    KeyError: 'py'
    >>> construir_itinerario('Penafiel', 'Paredes', ['fcul'])
    Traceback (most recent call last):
    ...
    KeyError: 'fcul'
    >>> construir_itinerario('mosca', 'Queluz', ['Mafra', 'Mafra'])
    Traceback (most recent call last):
    ...
    KeyError: 'mosca'
    >>> construir_itinerario('Valongo', 'Setúbal', ['Leiria', 'Leiria'])
    ['Valongo', 'Leiria', 'Leiria', 'Setúbal']
    >>> construir_itinerario('Maia', 'pescoço', ['Oeiras', 'Gondomar']) 
    Traceback (most recent call last):
    ...
    KeyError: 'pescoço'
    >>> construir_itinerario('Paredes', 'Almada', ['Viseu', 'Valongo'])  
    ['Paredes', 'Valongo', 'Viseu', 'Almada']
    >>> construir_itinerario('eu', 'tu', ['queijo', 'queijo'])
    Traceback (most recent call last):
    ...
    KeyError: 'eu'
    >>> construir_itinerario('Barreiro', 'Matosinhos', ['pão', 'pão'])
    Traceback (most recent call last):
    ...
    KeyError: 'pão'
    >>> construir_itinerario('nós', 'vós', ['pijama', 'calculadora'])   
    Traceback (most recent call last):
    ...
    KeyError: 'nós'
    >>> construir_itinerario('Amadora', 'Porto', ['eslástico', 'peluche'])
    Traceback (most recent call last):
    ...
    KeyError: 'eslástico'
    """
    return reduce(lambda acc, cidade: adicionar_cidade(acc, cidade), listaCidades, [origem, destino])

"""
Características:
    > Comprimento do intinerário (0, 1, >1)
    > Elementos do intinerário pertencem ao dict cidades (T, F)
    > Elementos repetidos (T, F)
    > Origem ou destino não pertence ao dict cidades (T, F)

                        Características                         |                                   Testes
    Comprimento |   Pertencem?  |   Repetidos?  | ñ Pertence?   |                Entrada                            |   Saída
        0       |      True     |   True        |   True        |                                               Inviável
        0       |      True     |   True        |   False       |                                               Inviável
        0       |      True     |   False       |   True        |                                               Inviável
        0       |      True     |   False       |   False       |                                               Inviável
        0       |      False    |   True        |   True        |                                               Inviável
        0       |      False    |   True        |   False       |                                               Inviável
        0       |      False    |   False       |   True        |   'ovo', 'Aveiro', []                             |   ['ovo', 'Aveiro']
        0       |      False    |   False       |   False       |   'Braga', 'Maia', []                             |   ['Braga', 'Maia']

        1       |      True     |   True        |   True        |                                               Inviável
        1       |      True     |   True        |   False       |                                               Inviável
        1       |      True     |   False       |   True        |   'panqueca', 'sim', ['Aveiro']                   |   KeyError: 'panqueca'
        1       |      True     |   False       |   False       |   'Loulé', 'Barreiro', ['Mafra']                  |   ['Loulé', 'Mafra', 'Barreiro']
        1       |      False    |   True        |   True        |                                               Inviável
        1       |      False    |   True        |   False       |                                               Inviável
        1       |      False    |   False       |   True        |   'py', 'Leiria', ['cidade']                      |   KeyError: 'py'
        1       |      False    |   False       |   False       |   'Penafiel', 'Paredes', ['fcul']                 |   KeyError: 'fcul'

        2       |      True     |   True        |   True        |   'mosca', 'Queluz', ['Mafra', 'Mafra']           |   KeyError: 'mosca'
        2       |      True     |   True        |   False       |   'Valongo', 'Setúbal', ['Leiria', 'Leiria']      |   ['Valongo', 'Leiria', 'Leiria', 'Setúbal']
        2       |      True     |   False       |   True        |   'Maia', 'pescoço', ['Oeiras', 'Gondomar']       |   KeyError: 'pescoço'
        2       |      True     |   False       |   False       |   'Paredes', 'Almada', ['Viseu', 'Valongo']       |   ['Paredes', 'Valongo', 'Viseu', 'Almada']
        2       |      False    |   True        |   True        |   'eu', 'tu', ['queijo', 'queijo']                |   KeyError: 'eu'
        2       |      False    |   True        |   False       |   'Barreiro', 'Matosinhos', ['pão', 'pão']        |   KeyError: 'pão'
        2       |      False    |   False       |   True        |   'nós', 'vós', ['pijama', 'calculadora']         |   KeyError: 'nós'
        2       |      False    |   False       |   False       |   'Amadora', 'Porto', ['eslástico', 'peluche']    |   KeyError: 'eslástico'
"""

testmod()
