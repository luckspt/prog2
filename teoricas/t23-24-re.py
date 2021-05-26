#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Expressões regulares.
Documentos útil:
https://docs.python.org/3/howto/regex.html
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

import re
import itertools

frase = 'O meu numero é 937462851, o teu é 945983285 e 229732239 é o de casa'

def numeros_moveis(texto):
    """Procura números de telemóveis numa frase.
    Um número de telemóvel começa por 9 e tem nove algarismos no total.

    Args:
        texto (str): O texto onde procurar
    """
    padrao = r'9\d{8}'  # o r é de "raw", quer dizer que não há carateres de fuga
    # padrao = '9\\d{8}' # alternativa sem r, a 1a barra é carater de fuga
    p = re.compile(padrao) # programa
    # m = p.match(frase)   # match: inicio da string
    m = p.search(frase)    # search : qualquer posicao da string
    if m != None:
        print('encontrou o número', m.group(),
        'entre o carater', m.start(),
        '(inclusivé) e o carater', m.end(),
        '(exclusivé)')
    else:
        print('azar')

# numeros_moveis(frase)

def procura_todos(padrao, texto):
    """Procura todas as ocorrências de um padrão numa frase.

    Args:
        padrao (str): O padrão a procurar
        texto (str): A frase onde procurar

    Returns:
        list[str]: A lista das ocorrências
    """
    p = re.compile(padrao)     # p, program
    return p.findall(texto)    # m, match

# procura_todos(frase, r'9\d{8}')

def tem_algarismos_pares(texto):
    """Verifica se um texto contém pelo menos um algarismo par

    Args:
        texto (str): O texto onde procurar

    Returns:
        bool: True se contém, False caso contrário
    """
    # p = re.compile('[02468]')
    # m = p.search(texto)
    # return m != None
    # return re.search('[02468]', texto) != None # Alternativa mais compacta

def so_tem_algarismos_pares(texto):
    """Verifica de um texto tem apenas algarismos pares

    Args:
        texto (str): O texto onde procurar

    Returns:
        bool: True, se contém apenas pares, False caso contrário
    """
    return re.search('^[02468]*$', texto) != None

palavras_importantes = r'mar|guerra|rei|arma|Portugal|Lusitano'
artigos_definidos = r'\b(a|A|as|As|o|O|os|Os)\b'
lus3 = """
1
As armas e os barões assinalados,
Que da ocidental praia Lusitana,
Por mares nunca de antes navegados,
Passaram ainda além da Taprobana,
Em perigos e guerras esforçados,
Mais do que prometia a força humana,
E entre gente remota edificaram
Novo Reino, que tanto sublimaram;

2
E também as memórias gloriosas
Daqueles Reis, que foram dilatando
A Fé, o Império, e as terras viciosas
De África e de Ásia andaram devastando;
E aqueles, que por obras valerosas
Se vão da lei da morte libertando;
Cantando espalharei por toda parte,
Se a tanto me ajudar o engenho e arte.

3
Cessem do sábio Grego e do Troiano
As navegações grandes que fizeram;
Cale-se de Alexandro e de Trajano
A fama das vitórias que tiveram;
Que eu canto o peito ilustre Lusitano,
A quem Neptuno e Marte obedeceram:
Cesse tudo o que a Musa antígua canta,
Que outro valor mais alto se alevanta.
"""

def imprime_ocorrencias(padrao, texto):
    """Imprime as ocorrencias de um padrão num texto.
    Para cada ocorrência imprime o número do carater inicial (inclusivé),
    o número do carater final (exclusivé) e o string encontrada.

    Args:
        padrao (str): O padrão a procurar
        texto (str): O texto onde procurar
    """
    for m in re.finditer(padrao, texto):
        print('%02d-%02d: %s' % (m.start(), m.end(), m.group()))

# imprime_ocorrencias(palavras_importantes, lus3)
# imprime_ocorrencias(artigos_definidos, lus3)

def imprime_ocorrencias_textos(padrao, textos):
    """Imprime todas as ocorrencias de um padrão numa lista de textos.
    Para cada ocorrência imprime o número do carater inicial (inclusivé),
    o número do carater final (exclusivé) e o string encontrada.

    Args:
        padrao (str): O padrão a procurar
        textos (list[str]): A lista de textos onde procurar
    """
    # Neste caso compensa compilar e procurar separadamente.
    # Gera uma solução mais eficiente porque compila uma vez
    # e usa o programa compilado para procurar múltiplas vezes
    p = re.compile(padrao)
    for texto in textos:
        for m in p.finditer(texto):
            print('%02d-%02d: %s' % (m.start(), m.end(), m.group()))

# imprime_ocorrencias_textos(artigos_definidos, [frase, lus3])

def frequencias(padrao, texto):
    """Um dicionário com as frequências com que as ocorrências de um padrão
    ocorrem num dado texto. As chaves são as ocorrências do padrão, os valores
    o número de ocorrências.

    Args:
        padrao (str): O padrão a procurar
        texto (str): O texto onde procurar

    Returns:
        dict: O dicionário com as ocorrências
    """
    palavras = sorted(re.findall(padrao, texto))
    grouped = itertools.groupby(palavras)
    return dict(map(lambda x: (x[0], len(list(x[1]))), grouped))

# frequencias(palavras_importantes, lus3)
# frequencias(artigos_definidos, lus3)

def frequencias_nos_lusiadas(padrao):
    with open('lusiadas.txt') as lusiadas:
        return frequencias(padrao, lusiadas.read())

# frequencias_nos_lusiadas(palavras_importantes)
# frequencias_nos_lusiadas(artigos_definidos)

acidente = """AF 70 DR colidiu com AA 98 PQ que embateu em AC 98 EF.
    O acidente ocorreu defronte do número 70 da rua DR Silva"""

# Uma lista com todas as matriculas no texto acidente
m1 = re.findall(r'[A-Z]{2} \d{2} [A-Z]{2}', acidente)

# Mesma coisa, mas com as matriculas agrupadas por grupos de letras e números
m2 = re.findall(r'([A-Z]{2}) (\d{2}) ([A-Z]{2})', acidente)

def decompoe_matricula (texto):
    """Escreve as letras, os números e novamente as letras de uma matrícula

    Args:
        texto (src): O texto onde procurar
    """
    match = re.search(r'([A-Z]{2}) (\d{2}) ([A-Z]{2})', texto)
    if match == None:
        print('Padrão não encontrado')
    else:
        print('letras:', match.group(1), ', números:', match.group(2), ', letras:', match.group(3))

# decompoe_matricula(acidente)