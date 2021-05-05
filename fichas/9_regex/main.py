import re

# 1 - Para cada um dos casos abaixo indique quais as strings ou substrings que são reconhecidas pela expressão regular indicada.
"""
a) Expressão regular: r'^[a-z]*[0-9]+.$'
    Tem de ter 0 ou mais caracteres de a-z, 1 ou mais caracteres de 0-9 e um caracter qualquer (excepto \n)
    Tem de começar e acabar assim

    x   i. '33'
        ii. '2' // tem de ter pelo menos mais um caracter
        iii. 'carro2' // a seguir ao digito tem de ter pelo menos mais um caracter
    x   iv. 'carro234'
        v. '_25' // o _ estraga tudo

b) Expressão regular: r'^[1-4]\d{3}[^a-z]$'
    Precisa de um caracter de 1-4, três digitos e um caracter não de a-z
    Tem de começar e acabar assim

    x   i. '12345'
        ii. '5392A' // não começa com 1-4
        iii. '1274a' // acaba com a-z
    x   iv. '2461_'
        v. '4a221' // tem um a antes dos 3 digitos
    
c) Expressão regular: r'([a-z0-9]{2}|[A-Z])\d-?'
    Precisa de dois caracteres de a-z ou 0-9 OU um caracter de A-Z, um dígito e 0 ou 1 -

    x   i.'456' // tem os dois dígitos e um dígito
        ii.'ab-' // não tem o dígito
    x   iii.'F44' // ignorar o último '4'. o F está no A-Z e o 4 está no \d
    x   iv.'23A5-' // ignorar o '23'. O A está no A-Z, o 5 está no \d e o - existe logo após o dígito
    x   v.'aZ3x-' // ignorar o 'a' e o 'x-'. O Z está no A-Z e o 3 está no \d
"""

# 2 - Para cada uma das expressões regulares, indique quantas (e quais) ocorrências serão detetadas nas strings indicadas.
"""
a) Expressão regular: r'[a-z0-9]\d'
    Um caracter a-z ou 0-9 e um dígito

    2   i.'a456' // a4, 56
    1   ii.'456' // 45
    1   iii.'456b' // 45
    2   iv.'ab456' // b4, 56
    4   v.'a5b2d456' // a5, b2, d4, 56

b) Expressão regular: r'.[^0-9]*,?[^a-zA-Z]*'
    Um caracter qualquer (excepto \n), 0 ou mais caracteres não 0-9, 0 ou 1 virgula, 0 ou mais caracteres não a-z nem A-Z

    2   i.'234abc'
    1   ii.'abc234'
    2   iii.'234,abc'
    2   iv.',234abc'
    2   v.'xabc,999x'
    2   vi.'xabc999y'
    1   vii.'0'
    1   viii.'00,99'
    0   ix.'\n\n\n'
"""

# 3 - Para cada um dos casos abaixo escreva uma expressão regular Python.
"""
a) Os códigos postais de Portugal.
    Exemplos: 1749-016 Lisboa, 2795-241 Linda a Velha.

    r'^\d{4}-\d{3} [A-Z][a-zA-Z ]*[^ ]$'
    
b) As matrículas de veículos registados em Portugal.
    Exemplos: AA-11-11, 11-AA-11, 11-11-AA, ou AA-11-AA.

    r'^[A-Z]{2}-\d{2}-\d{2}|\d{2}-[A-Z]{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-\d{2}-[A-Z]{2}$'
    
c) Um número em formato vírgula flutuante.
    Exemplos: 2.3 e -1.345.
    Não exemplos: 4 e 0034.0 e -0.0.

    r'^-?[1-9]\d*\.\d+|0\.\d+|-0\.\d*[1-9]\d*$'
    
d) Um número escrito na notação científica.
    Exemplos: 2e4, 2.3e4 e -1.345e-34.
    Não exemplos: 4, -03.0e7, 0.2e2, para além de todos os da alínea anterior.
    
    r'-?[1-9]+(\.[1-9]+)?e[1-9]+' //n funciona para 0.2e2

e) Os endereços de email dos alunos da FCUL.
    Exemplo: fc99999@alunos.fc.ul.pt.

    r'fc\d{5}@alunos\.fc\.ul\.pt'
    
f) Identificadores numa linguagem de programação: uma sequênciade letras, algarismos e traços inferiores (_) que não começam por um algarismo.

    r'^[a-zA-Z_][a-zA-Z0-9_]*'
"""

# 4 - Baseado nas soluções do exercício anterior, escreva funções Python que, dada umastring, devolvam a informação indicada.
# As funções devem devolver None caso a string fornecida não corresponda a um valor bem formado de acordo com a expressão regular.
def testa_exp(er, s):
    print("'" + er + "' reconhece '" + s + "'? ")
    m = re.search(er, s)
    if m:
        print("SIM '" + m.group() + "'")
    else:
        print("NÃO")


# a) Um triplo contendo as três partes de um código postal.
def cod_postal(txt):
    """
    >>> cod_postal('2795-241 Linda a Velha')
    ('2795', '241', 'Linda a Velha')
    """
    pass


# b) Os três constituintes de uma matrícula, juntamente com a informação sobre o tipo de matrícula: letras-primeiro, letras-no-meio, letras-no-fim, números-no-meio.
"""
>>> constituintes_matricula('AA-11-11')
('letras-primeiro', 'AA', '11', '11')
"""
# c) Um número em vírgula flutuante.
"""
>>> numero_vf('2.3')
2.3
"""
