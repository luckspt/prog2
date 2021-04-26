from csv import DictReader
from matplotlib import pyplot as plt
from math import sqrt
from itertools import groupby
from functools import reduce

__author__ = 'Lucas Pinto, 56926'

def limpa_converte(dados, lista_colunas, pred_filtragem, funcs_converter):
    """Filtra dados inviáveis e converte para novos tipos.

    Requires:
        len(lista_colunas) == len(funcs_converter).

    Args:
        dados (iter<dict>): Conjunto de dados.
        lista_colunas (list<string>): Lista de colunas do cabeçalho.
        pred_filtragem (function): Predicado de filtragem.
        funcs_converter (list<function>): Funções de conversão.

    Returns:
        iter<dict>: Dados viáveis convertidos.
    """    
    return map(lambda linha: { k: f(linha[k]) for k, f in zip(lista_colunas, funcs_converter) }
        , filter(pred_filtragem, dados))

#Cálculo da média
media = lambda l: sum(l) / len(l)
def media_movel(yy, janela):
    """Calcula a média móvel dados uma lista de valores e a janela.

    Args:
        yy (list<float|int>): Lista dos valores das ordenadas de um conjunto de dados.
        janela (int): Dimensão da janela.

    Returns:
        iter<list<float>>: Média móvel.
    """
    return map(lambda i: media(yy[ max(i-janela, 0) : i ]), range(1, len(yy)+1) )

def desvio_padrao(yy, janela):
    """Calcula o desvio padrão dados uma lista de valores e a janela.

    Args:
        yy (list<float|int>): Lista dos valores das ordenadas de um conjunto de dados.
        janela (int): Dimensão da janela.

    Returns:
        iter<list<float>>: Desvio padrão.
    """
    for i in range(1, len(yy)+1):
        dados = yy[ max(i-janela, 0) : i ]
        avg = media(dados)
        mapped = list(map(lambda d: (d-avg)**2, dados))
        yield media(mapped)**.5

def tracar(abcissas, ordenadas, parametros, janela=30):
    """Traca um grafico

    Args:
        abcissas (list<float|int>): Lista das abcissas.
        ordenadas (list<float|int>): Lista das ordenadas.
        parametros (dict<title: string, xlabel: string, ylabel: string>): Dicionário de parâmetros.
        janela (int, optional): Janela para o cálculo da média móvel e desvio padrão. Defaults to 30.
    """
    mediaMovel = list(media_movel(ordenadas, janela))
    desvioPadrao = list(desvio_padrao(ordenadas, janela))

    plt.title(parametros['title'])
    plt.xlabel(parametros['xlabel'])
    plt.ylabel(parametros['ylabel'])

    fBetween = ((u-2*o, u+2*o) for u, o in zip(mediaMovel, desvioPadrao))
    low, upper = zip(*fBetween)
    plt.fill_between(abcissas
        , low
        , upper
        , color='0.9')
    plt.plot(abcissas, ordenadas, 'g.', markersize=2)
    plt.plot(abcissas, mediaMovel, 'r')

    plt.show()

def ler_csv_dicionario (nome_ficheiro, delimiter=','):
    """Ler um ficheiro CSV. O ficheiro pode ou não ter cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro.
        delimiter (string, optional): O caracter separador das colunas. Defaults to ','.

    Returns:
        list[dict]: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro
            ou tiradas da lista cabeçalho.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        return list(DictReader(ficheiro_csv, delimiter=delimiter))

def sakura(ficheiro_csv):
    """Lê dados de um ficheiro CSV, limpa e converte os dados e traça um gráfico.

    Args:
        ficheiro_csv (string): caminho para o ficheiro CSV
    """
    dadosRaw = ler_csv_dicionario(ficheiro_csv, delimiter=';')
    dados = limpa_converte(dadosRaw
        , ['AD', 'Full-flowering date (DOY)']
        , lambda d: d['Full-flowering date (DOY)'] != '' and d['AD'] != ''
        , [int, int])

    dados = ((d['AD'], d['Full-flowering date (DOY)']) for d in dados)
    abcissas, ordenadas = zip(*dados)
    tracar(abcissas, ordenadas
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
        float: Média das magnitudes
    """
    mags = list(map(lambda d: d['mag'], dados))
    return media(mags)

def sismos(ficheiro_csv):
    """Lê dados de um ficheiro CSV, limpa e converte os dados e traça um gráfico.

    Args:
        ficheiro_csv (string): caminho para o ficheiro CSV
    """
    dadosRaw = ler_csv_dicionario(ficheiro_csv)
    dados = limpa_converte(dadosRaw
        , ['time', 'mag']
        , lambda d: d['mag'] != '' and d['time'] != ''
        , [minsPassed, float])

    dadosSorted = sorted(dados, key=lambda d: d['time'])
    dadosGroupped = [(k, mediasAvg(g)) for k, g in groupby(dadosSorted, key=lambda d: d['time'])]

    abcissas, ordenadas = zip(*dadosGroupped)
    tracar(abcissas, ordenadas
        , { 'title': 'Sismos de março de 2021'
            , 'xlabel': 'Minutos desde o inicio do mês'
            , 'ylabel': 'Média das magnitudes nesse minuto' })

def sakuraSemLer(dadosRaw):
    """Faz o mesmo que a anterior mas sem ler o ficheiro por motivos de desempenho em testes em massa

    Args:
        dadosRaw (list<dict>): Lista de dicionários com os valores lidos do CSV
    """
    dados = limpa_converte(dadosRaw
        , ['AD', 'Full-flowering date (DOY)']
        , lambda d: d['Full-flowering date (DOY)'] != '' and d['AD'] != ''
        , [int, int])

    dados = ((d['AD'], d['Full-flowering date (DOY)']) for d in dados)
    abcissas, ordenadas = zip(*dados)
    tracar(abcissas, ordenadas
        , { 'title': 'Registo Histórico da Data de Florescimento das Cerejeiras em Quioto'
            , 'xlabel': 'Ano DC'
            , 'ylabel': 'Dias a partir do início do ano' })

def sismosSemLer(dadosRaw):
    """Faz o mesmo que a anterior mas sem ler o ficheiro por motivos de desempenho em testes em massa

    Args:
        dadosRaw (list<dict>): Lista de dicionários com os valores lidos do CSV
    """
    dados = limpa_converte(dadosRaw
        , ['time', 'mag']
        , lambda d: d['mag'] != '' and d['time'] != ''
        , [minsPassed, float])

    dadosSorted = sorted(dados, key=lambda d: d['time'])
    dadosGroupped = [(k, mediasAvg(g)) for k, g in groupby(dadosSorted, key=lambda d: d['time'])]

    abcissas, ordenadas = zip(*dadosGroupped)
    tracar(abcissas, ordenadas
        , { 'title': 'Sismos de março de 2021'
            , 'xlabel': 'Minutos desde o inicio do mês'
            , 'ylabel': 'Média das magnitudes nesse minuto' })

# sakura('trabalhos/4-csvGraphs/kyoto.csv')
# sismos('trabalhos/4-csvGraphs/all_month.csv')