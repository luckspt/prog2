from csv import DictReader
from matplotlib import pyplot as plt
from math import sqrt
from itertools import groupby
    
__author__ = 'Lucas Pinto, 56926'

#Se todas as colunas cols do dicionário dic são vazias
isEmpty = lambda dic, cols: all([dic[k] == '' for k in cols])

def limpa_converte(dados, lista_colunas, pred_filtragem, funcs_converter):
    """Filtra dados inviáveis e converte para novos tipos

    Requires:
        len(lista_colunas) == len(funcs_converter)

    Args:
        dados (list<dict>): Conjunto de dados
        lista_colunas (list<string>): Lista de colunas do cabeçalho
        pred_filtragem (function): Predicado de filtragem.
        funcs_converter (list<function>): Funções de conversão

    Returns:
        list<dict>: Dados viáveis convertidos
    """    
    filtered = filter(lambda linha: pred_filtragem(linha), dados)
    mappedKeys = map(lambda linha: { k: linha[k] for k in lista_colunas }, filtered)
    converted = map(lambda dic: { c: f(dic[c]) for c, f in zip(lista_colunas, funcs_converter) }, mappedKeys)
    return list(converted)

#Cálculo da média
media = lambda l: sum(l) / len(l)
def media_movel(yy, janela):
    """[summary]

    Args:
        yy (list): Lista dos valores das ordenadas de um conjunto de dados
        janela (int): Dimensão da janela

    Returns:
        iter<list<float>>: Médias
    """
    return ( media(yy[ max(i-janela, 0) : i ]) for i in range(1, len(yy)+1) )

def desvio_padrao(yy, janela):
    """Calcula o desvio padrão dados uma lista de valores e a janela.

    Args:
        yy (list<float|int>): Lista dos valores das ordenadas de um conjunto de dados.
        janela (int): Dimensão da janela.

    Returns:
        iter<list<float>>: Desvio padrão.
    """
    mMovel = list(media_movel(yy, janela))
    return map(
        lambda i: (sum(
                ( (i2 - mMovel[i-1])**2 for i2 in yy[max(i-janela, 0):i])
            ) / i) ** 0.5
        , range(1, len(yy)+1))

def tracar(abcissas, ordenadas, parametros, janela=30):
    mediaMovel = list(media_movel(ordenadas, janela))
    desvioPadrao = list(desvio_padrao(ordenadas, janela))

    plt.title(parametros['title'])
    plt.xlabel(parametros['xlabel'])
    plt.ylabel(parametros['ylabel'])

    plt.fill_between(abcissas, list(map(lambda u, o: u+2*o, mediaMovel, desvioPadrao)), list(map(lambda u, o: u-2*o, mediaMovel, desvioPadrao)), color='0.9')
    plt.plot(abcissas, ordenadas, 'g.', markersize=2)
    plt.plot(abcissas, mediaMovel, 'r')

    # plt.show()

def ler_csv_dicionario (nome_ficheiro, delimiter=','):
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
        leitor = DictReader(ficheiro_csv, delimiter=delimiter)
        return list(leitor)

def sakura(ficheiro_csv):
    dadosRaw = ler_csv_dicionario(ficheiro_csv)
    dados = limpa_converte(dadosRaw
        , ['AD', 'Full-flowering date (DOY)']
        , lambda d: d['Full-flowering date (DOY)'] != ''
        , [int, int])
    tracar([dic['AD'] for dic in dados]
        , [dic['Full-flowering date (DOY)'] for dic in dados]
        , { 'title': 'Registo Histórico da Data de Florescimento das Cerejeiras em Quioto'
            , 'xlabel': 'Ano DC'
            , 'ylabel': 'Dias a partir do início do ano' })

def minsPassed(date):
    """Calcula a diferença em minutos desde o inicio do mês

    Args:
        date (str): Data em formato ISO Date (Date-Time)

    Returns:
        int: Diferença, em minutos, desde o inicio do mês
    """
    dias = int(date[8:10]) - 1 #o primeiro dia não conta
    horas = int(date[11:13])
    minutos = int(date[14:16])
    return minutos + horas*60 + dias*24*60

def mediasAvg(dados):
    """Calcula a média das magnitudes

    Args:
        dados (list<dict>): Lista de dicionários dos dados

    Returns:
        float: [description]
    """
    mags = list(map(lambda d: d['mag'], dados))
    return media(mags)

def sismos(ficheiro_csv):
    dadosRaw = ler_csv_dicionario(ficheiro_csv)
    dados = limpa_converte(dadosRaw
        , ['time', 'mag']
        , lambda d: d['mag'] != ''
        , [str, float])

    for d in dados:
        d['mins'] = minsPassed(d['time'])

    dadosSorted = sorted(dados, key=lambda d: d['mins'])
    dadosGroupped = [(k, mediasAvg(g)) for k, g in groupby(dadosSorted, key=lambda d: d['mins'])]

    tracar([d[0] for d in dadosGroupped]
        , [d[1] for d in dadosGroupped]
        , { 'title': 'Sismos de março de 2021'
            , 'xlabel': 'Minutos desde o inicio do mês'
            , 'ylabel': 'Média das magnitudes nesse minuto' })

def sakuraSemLer(dadosRaw):
    dados = limpa_converte(dadosRaw
        , ['AD', 'Full-flowering date (DOY)']
        , lambda d: d['Full-flowering date (DOY)'] != ''
        , [int, int])
    tracar([dic['AD'] for dic in dados]
        , [dic['Full-flowering date (DOY)'] for dic in dados]
        , { 'title': 'Registo Histórico da Data de Florescimento das Cerejeiras em Quioto'
            , 'xlabel': 'Ano DC'
            , 'ylabel': 'Dias a partir do início do ano' })

def sismosSemLer(dadosRaw):
    dados = limpa_converte(dadosRaw
        , ['time', 'mag']
        , lambda d: d['mag'] != ''
        , [str, float])

    for d in dados:
        d['mins'] = minsPassed(d['time'])

    dadosSorted = sorted(dados, key=lambda d: d['mins'])
    dadosGroupped = [(k, mediasAvg(g)) for k, g in groupby(dadosSorted, key=lambda d: d['mins'])]

    tracar([d[0] for d in dadosGroupped]
        , [d[1] for d in dadosGroupped]
        , { 'title': 'Sismos de março de 2021'
            , 'xlabel': 'Minutos desde o inicio do mês'
            , 'ylabel': 'Média das magnitudes nesse minuto' })
