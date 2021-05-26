#!/usr/bin/env python3

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Manipulação de ficheiros de valores separados por vírgulas (CSV)
https://docs.python.org/3/library/csv.html
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

import csv

# 1 _ Leitura de ficheiros CSV para lista de listas

# Relembrar a leitura de ficheiros

def ler_e_imprimir_ficheiro(nome_ficheiro):
    """Imprimir o conteúdo de um dado ficheiro no ecrã

    Args:
        nome_ficheiro (str): O nome do ficheiro
    """
    with open(nome_ficheiro, 'r') as leitor:
        for linha in leitor:
            print(linha)

# Um pequeno exercício de aquecimento: ler o conteúdo de um ficheiro
# CSV e escrevê-lo no ecrã.

def ler_imprimir_csv(nome_ficheiro):
    """Ler um ficheiro CSV e escrever o seu conteúdo no ecrã

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV
    """
    with open(nome_ficheiro, 'r') as ficheiro_csv:
        leitor = csv.reader(ficheiro_csv)
        for linha in leitor:
            print(linha)

# Em vez de ler para o ecrã, podemos ler para uma estrutura de
# dados que possamos mais tarde manipular. Desta vez lemos o ficheiro
# para uma lista de listas.

def ler_csv(nome_ficheiro):
    """Ler um ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[list][str]: O conteúdo do ficheiro. 
            Cada elemento da lista contém uma linha do ficheiro CSV.
            Cada string corresponde a um valor no ficheiro CSV.
    """
    with open(nome_ficheiro, 'r') as ficheiro_csv:
        return list(csv.reader(ficheiro_csv)) # list é para forçar a leitura do iterador antes de fechar o ficheiro

def para_lista_listas(it):
    """Converter um iterador de iteradores em lista de listas.
        Útil para visualizar no interpretador o conteúdo de um
        iterador de iteradores.

    Args:
        it (iter[iter]): O iterador de iterador

    Returns:
        list[list]: A lista de listas
    """
    return list(map(list, it))

def max_notas(nome_ficheiro):
    """O valor máximo da terceira coluna de um ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV

    Returns:
        float: O valor máximo da terceira coluna
    """
    linhas = ler_csv(nome_ficheiro)
    notas = map(lambda x: int(x[2]), linhas)
    return max(notas)

def nota_final(nome_ficheiro):
    """Um lista com as notas finais dos constantes num ficheiro CSV.
        O ficheiro CSV tem as notas parciais a partir da 3a coluna.
        O número de notas parciais não é dado. As notas finais são
        arrendondadas às unidades

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[int]: A lista com as notas finais
    """
    linhas = ler_csv(nome_ficheiro)
    notas_str = map(lambda linha: linha[2:], linhas)
    notas = map(lambda linha: map(float, linha), notas_str)
    finais_decimais = map(sum, notas)
    return map(round, finais_decimais)

# nota_final('pauta_prog2.csv')


# 2 _ Escrita em ficheiros CSV

# Primeiro relembrar a escrita em ficheiro convencional

def escrever_em_ficheiro(ficheiro, algo):
    """Escrever algo num ficheiro

    Args:
        ficheiro (str): O nome do ficheiro onde escrever
        algo (any): O que escrever no ficheiro
    """
    with open(ficheiro, 'w') as f:
        f.write(str(algo))

# As notas de alguns alunos do 1o ano da LTI
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

# escrever_em_ficheiro('notas.txt', nome_disciplina_nota)

# Agora escrever num ficheiro em formato CSV.

def escrever_csv(nome_ficheiro, iterador_de_iteradores, separador = ','):
    """Escrever um iterador de iteradores num ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro
        iterador_de_iteradores (iter[iter]): O iterador
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = csv.writer(ficheiro_csv, delimiter = separador)
        for linha in iterador_de_iteradores:
            escritor.writerow(linha)

# Uma pequena aplicação: ler csv para iterador, manipular iterador
# (calcular media de cada linha), escrever novo csv.

def media(it):
    """A média de uma lista não vazia

    Args:
        it (list[number]): A lista

    Returns:
        float: A média dos valores constantes na lista
    """
    l = list(it)
    return sum(l) / len(l)

def transpor(it):
    """A transposta de uma lista, isto é uma lista "na vertical".
        Por exemplo, a lista [1, 2, 3] é transformada em [[1], [2], [3]].

    Args:
        it (iter): O iterador a transpor

    Returns:
        iter: O iterador transposto
    """
    return map(lambda x: [x], it)

def escrever_medias(ficheiro_entrada, ficheiro_saida):
    """Ler inteiros de um ficheiro CSV e escrever a média de cada linha
        num outro ficheiro CSV.

    Args:
        ficheiro_entrada (str): O nome do ficheiro com os números
        ficheiro_saida (str): O nome do ficheiro onde escrever as médias
    """
    it = ler_csv(ficheiro_entrada)
    numeros = map(lambda linha: map(int, linha), it)
    medias = map(media, numeros)
    escrever_csv(ficheiro_saida, transpor(medias))

# Outra aplicação: ler as notas parciais dos alunos, calcular a nota final,
# escrever num outro ficheiro mais uma coluna com a nota final

def escrever_nota_final_bis(ficheiro_entrada, ficheiro_saida):
    linhas = ler_csv(ficheiro_entrada)
    novas_linhas = []
    for linha in linhas:
        final = round(sum(map(float, linha[2:])))
        novas_linhas += [linha + [final]]
    escrever_csv(ficheiro_saida, novas_linhas, separador=';')


# 3 _ Ler CSV para lista de dicionários

# Começamos por ler um ficheiro CSV para uma lista de dicionários (em
# vez de lista de listas, como fizemos na secção anterior). Para
# determinar o nome das chaves da dicionário utilizamos a primeira linha
# do ficheiro de entrada. A esta primeira linha chamamos o cabeçalho do
# ficheiro.

def imprimir_csv_dicionario (nome_ficheiro):
    """Imprimir no ecrã o conteudo de um ficheiro CSV.
    Cada linha do ficheiro aparece em forma de dicionário.
    As chaves do dicionário são lidas da 1a linha do ficheiro

    Args:
        nome_ficheiro (str): O nome do ficheiro
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = csv.DictReader (ficheiro_csv)
        for linha in leitor:
            print(linha)

# Se o ficheiro já contiver cabeçalho:
# imprimir_csv_dicionario('pauta_prog2_cabecalho.csv')

# Em vez de escrever o conteúdo do ficheiro no ecrã, podemos devolver
# uma lista de dicionários.

def ler_csv_dicionario_cabecalho (nome_ficheiro):
    """Ler um ficheiro CSV com cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[dict]: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv)
        return list(leitor)

# Nem todos os ficheiros têm cabeçalho. Se pretendermos ler um ficheiro
# sem cabeçalho para um dicionário, temos de escolher as chaves. Neste
# caso passamos para a função de leitura uma lista de Strings contendo as
# chaves que escolhemos.

def ler_csv_dicionario (nome_ficheiro, cabecalho = None):
    """Ler um ficheiro CSV. O ficheiro pode ou não ter cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro
        fieldnames (list[str], optional):  A lista com o nomes das colunas.
            Utilizar quando o ficheiro não tiver cabeçalho. Defaults to None.

    Returns:
        list[dict]: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro
            ou tiradas da lista cabeçalho.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = csv.DictReader(ficheiro_csv, fieldnames = cabecalho)
        return list(leitor)

# Se o ficheiro não tiver cabeçalho:
# ler_csv_dicionario('pauta_prog2.csv', ['Name', 'Id', 'A1', 'A2', 'A3', 'A4', 'A5'])


# 4 _ Escrever iterador de dicionários para CSV

def escrever_csv_dicionario(nome_ficheiro, iterador_de_dicionarios, cabecalho, separador = ','):
    """Escrever num ficheiro CSV um dicionário de iteradores

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV
        iterador_de_dicionarios (iter[dict]): O iterador
        cabecalho (list): A sequência de chaves do dicionário que indica a *ordem* das
        colunas a escrever no CSV.
        separador (str, optional): O separador a utilizar. Defaults to ','.
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = csv.DictWriter(ficheiro_csv, cabecalho, delimiter = separador)
        escritor.writeheader()
        for linha in iterador_de_dicionarios:
            escritor.writerow(linha)

pauta = [   # N.B.: chaves dos diferentes dicionários por ordens variadas
{'Nome': 'Ana',
  'T1': '2.0',
  'T3': '2.8',
  'T4': '3.4',
  'T2': '1.4',
  'Número': '53622',
  'T5': '7.3'},
 {'Nome': 'Eva',
  'T2': '2.5',
  'T1': '1.4',
  'T3': '2.3',
  'T4': '0.0',
  'Número': '55444',
  'T5': '6.8'},
 {'Nome': 'Abel',
  'T4': '3.3',
  'T1': '1.8',
  'T2': '2.5',
  'Número': '57523',
  'T3': '2.7',
  'T5': '5.8'}]

# escrever_csv_dicionario('pauta.csv', pauta, ['Nome', 'Número', 'T1', 'T2', 'T3', 'T4', 'T5'])

# Eis uma pequena aplicação: Calcular a magnitude maxima dos sismos
# constantes num ficheiro CSV. Calcular também o local onde ocorreu este
# tremor de terra. Calcular todos os tremores de terra num dado local.
# Os ficheiros CSV podem ser obtidos aqui
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

def magnitude_maxima(nome_ficheiro):
    """A magnitude máxima de todos os sismos num dado ficheiro.
    O ficheiro de ser CSV e ter uma coluna com o nome 'mag'.
    As células na coluna 'mag' podem estar vazias.

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV

    Returns:
        float: A magnitude máxima
    """
    tabela = ler_csv_dicionario(nome_ficheiro)
    return max(map(lambda linha: 0 if linha['mag'] == '' else float(linha['mag']), tabela))

def local_magnitude_maxima(nome_ficheiro):
    """O local onde ocorreu a magnitude máxima de um sismo num dado ficheiro.
    O ficheiro de ser CSV e ter colunas com os nomes 'mag' e 'place'.
    As células na coluna 'mag' podem estar vazias.

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV

    Returns:
        str: O local onde ocorreu o sismo com a maior magnitude 
    """
    tabela = ler_csv_dicionario(nome_ficheiro)
    linha_max = max(tabela, key = lambda linha: 0 if linha['mag'] == '' else float(linha['mag']))
    return linha_max['place']

def sismos_num_local(nome_ficheiro, local):
    """Todos os sismos que ocorreram num dado local.
    O ficheiro de ser CSV e ter colunas com os nomes 'mag' e 'place'.
    As células na coluna 'mag' podem estar vazias.
    

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV
        local (str): O local onde procurar sismos

    Returns:
        iter[str]: O iterador com todos os sismos cujo campo 'place'
        contenha a string local.
    """
    tabela = ler_csv_dicionario(nome_ficheiro)
    return filter(lambda linha: local in linha['place'], tabela)

# Outra pequena aplicação: ler um ficheiro CSV para uma lista de
# dicionários; juntar um campo a cada dicionário; escrever o novo
# dicionário. O novo campo é a idade em anos. Para isso subtraímos do ano
# corrente a idade constante no ficheiro. Para obtermos o ano atual usamos
# o pacote datetime.

import datetime
# http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/

def juntar_idade (ficheiro_entrada, ficheiro_saida):
    """Escrever no ficheiro de saida o conteudo do ficheiro de entrada com
    mais uma coluna: a da idade

    Pre: O ficheiro de entrada descreve um ficheiro CSV com cabeçalho
    (1a linha). As colunas são ['Nome proprio', 'Apelido', 'Ano nascimento'],
    não necessariamente por esta orde.

    Args:
        ficheiro_entrada (str): O nome do ficheiro CSV de leitura
        ficheiro_saida (str): O nome do ficheiro CSV de escrita
    """
    tabela = ler_csv_dicionario(ficheiro_entrada)
    for d in tabela:
        d['Idade'] = datetime.datetime.now().year - int(d['Ano nascimento'])
    escrever_csv_dicionario(ficheiro_saida, tabela, cabecalho = ['Nome proprio', 'Apelido', 'Ano nascimento', 'Idade'])

# juntar_idade('pessoas.csv', 'idades.csv')
