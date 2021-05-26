#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências

Programação II (LTI) 2020/2021

Projeto — Script analizador de jogos de xadrez
"""

__author__ = "Lucas Pinto, 56926; Mário Zeller, 49570"
__email__ = "fc56926@alunos.fc.ul.pt; fc49570@alunos.fc.ul.pt"


###################################################################################################
### Imports #######################################################################################
###################################################################################################


from csv import DictReader, DictWriter
from itertools import groupby
from operator import itemgetter
from re import match as reMatch, search as reSearch

from matplotlib import pyplot as plt


###################################################################################################
### Funções de gestão de ficheiros csv ############################################################
###################################################################################################


def ler_csv_dicionario(nome_ficheiro):
    """Ler um ficheiro CSV. O ficheiro pode ou não ter cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro.

    Returns:
        list<dict>: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro
            ou tiradas da lista cabeçalho.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = DictReader(ficheiro_csv)
        return list(leitor)


###################################################################################################


def escrever_csv_dicionario(nome_ficheiro, iterador_de_dicionarios, cabecalho):
    """Escrever num ficheiro CSV um dicionário de iteradores.

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV.
        iterador_de_dicionarios (iter<dict>): O iterador.
        cabecalho (list): A sequência de chaves do dicionário que indica a *ordem* das
            colunas a escrever no CSV.
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = DictWriter(ficheiro_csv, cabecalho)
        escritor.writeheader()
        for linha in iterador_de_dicionarios:
            escritor.writerow(linha)


###################################################################################################
#### Operação anos ################################################################################
###################################################################################################


def anosDraw(abcissas, ordenadasJogos, ordenadasJogadoras):
    """Desenha o gráfico da função anos.

    Requires:
        len(abcissas) == len(ordenadasJogos) and len(ordenadasJogos) == len(ordenadasJogadoras).

    Args:
        abcissas (list<int>): Lista de anos das abcissas.
        ordenadasJogos (list<int>): Lista da quantidade de jogos.
        ordenadasJogadoras (list<int>): Lista da quantidade de jogadoras diferentes.
    """
    fig, jogos = plt.subplots()
    plt.title('Jogos e jogadoras por ano')

    jogos.bar(abcissas, ordenadasJogos, color='g', label='#jogos')
    jogos.set_xlabel('Ano')
    jogos.set_ylabel('Jogos', color='g')
    jogos.tick_params(axis='x', labelrotation=90)
    jogos.legend(loc=6)

    jogadoras = jogos.twinx()
    jogadoras.plot(abcissas, ordenadasJogadoras, color='b',
                   label='#jogadoras Diferentes')
    jogadoras.set_ylabel('#Jogadoras diferentes', color='b')
    jogadoras.set_ylim(ymin=min(ordenadasJogadoras),
                       ymax=max(ordenadasJogadoras))
    jogadoras.legend()

    fig.tight_layout()
    plt.show()


###################################################################################################


def anos(dados):
    """Processa e gera o gráfico dos jogos e jogadoras por ano.

    Requires:
        Os dicionários do iterador dados devem conter as chaves end_time, white_username e black_username.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
    """
    anosSorted = sorted(dados, key=lambda dic: dic['end_time'])
    anosGroupped = groupby(anosSorted, key=lambda dic: dic['end_time'][:4])
    anosMapped = map(lambda x: (x[0], list(x[1])), anosGroupped)

    abcissas, ordenadasJogos, ordenadasJogadoras = [], [], []
    for ano, jogosAno in anosMapped:
        abcissas.append(ano)
        ordenadasJogos.append(len(jogosAno))

        jogadoras = set()
        jogadoras.update(
            *[(jogo['white_username'], jogo['black_username']) for jogo in jogosAno])
        ordenadasJogadoras.append(len(jogadoras))

    anosDraw(abcissas, ordenadasJogos, ordenadasJogadoras)


###################################################################################################
#### Operação classes #############################################################################
###################################################################################################


def classesPopularFormat(dados, count):
    """Obtém os count formatos mais populares em dados.

    Requires:
        Os dicionários do iterador dados devem conter a chave time_control.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        count (int): Quantidade de formatos a obter.

    Returns:
        list: Lista dos jogos jogados em cada formato.
    """
    sortedTimeControl = sorted(dados, key=lambda dic: dic['time_control'])
    grouppedTimeControl = groupby(
        sortedTimeControl, key=lambda dic: dic['time_control'])
    grouppedTimeControlLst = [(len(list(y[1])), y[0])
                              for y in grouppedTimeControl]
    return sorted(grouppedTimeControlLst, reverse=True)[:count]


###################################################################################################


def classesDraw(classes):
    """Desenha os gráficos da função classes.

    Args:
        classes (list): Lista das classes.
    """
    timeClass = [('time_class', (list(map(lambda classe: sum(classe[1][0]), classes))[::-1], list(map(lambda x: x[0], classes))[::-1]))]
    for ind, classe in enumerate(classes + timeClass, start=1):
        plt.subplot(2, 3, ind)
        plt.bar(classe[1][1], classe[1][0])
        plt.title(classe[0])
        plt.xlabel('Formato de jogo')
        plt.ylabel('#jogos')
        plt.tick_params(axis='x', labelrotation=90)

    plt.tight_layout()
    plt.show()


###################################################################################################


def classes(dados, count=None):
    """Processa e gera o gráfico de jogos e classes por cada formato.

    Requires:
        Os dicionários do iterador dados devem conter as chaves time_control e time_class.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        count (int, opcional): Quantidade de classes a mostrar. 5 por defeito.
    """
    count = count or 5

    sortedTimeclass = sorted(
        dados, key=lambda dic: dic['time_class'], reverse=True)
    grouppedTimeclass = groupby(
        sortedTimeclass, key=lambda dic: dic['time_class'])
    grouppedTimeclassDict = {t[0]: list(t[1]) for t in grouppedTimeclass}

    # [(time_class, [(nºjogos, time_control), ... ]), ... ]
    classesDraw(list(map(lambda key: (key, list(zip(*classesPopularFormat(
        grouppedTimeclassDict[key], count)))), grouppedTimeclassDict.keys())))


###################################################################################################
### Operação vitorias #############################################################################
###################################################################################################


def vitoriasDraw(abcissas, ordenadasBrancas, ordenadasPretas):
    """Desenha o gráfico da função vitorias.

    Args:
        abcissas (list<str>): Lista dos nomes das jogadoras.
        ordenadasBrancas (list<float>): Lista da percentagem de vitorias com as peças brancas.
        ordenadasPretas (list<float>): Lista da percentagem de vitorias com as peças pretas.
    """
    plt.title('Percentagem de vitórias jogando com\npeças brancas / pretas')

    plt.bar(abcissas, ordenadasBrancas, width=-0.4,
            label='peças brancas', color='lightgray', align='edge')
    plt.bar(abcissas, ordenadasPretas, width=0.4,
            label='peças pretas', color='black', align='edge')
    plt.tick_params(labelrotation=90)
    plt.xlabel('Jogadoras')
    plt.ylabel('Percentagem')
    plt.legend(loc=1)
    plt.tight_layout()
    plt.show()


###################################################################################################


def vitoriasProcess(dados, jogadoras=None):
    """Calcula os jogos jogados no total e com as peças brancas e as vitorias com as peças brancas e pretas.

    Requires:
        Os dicionários do iterador dados devem conter as chaves black_username, white_username, white_result, e black_result.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        jogadoras (list<str>, opcional): Lista de jogadoras a mostrar. 

    Returns:
        list: Dados processados.
    """
    # {nome: [jogosTotais, jogosBrancas, vitoriasBrancas, vitoriasPretas]}
    jog = {}
    for dic in dados:
        w, b = dic['white_username'], dic['black_username']
        if w not in jog:
            jog[w] = [0, 0, 0, 0]

        if b not in jog:
            jog[b] = [0, 0, 0, 0]

        # one-liner
        # jog[w][0], jog[w][1], jog[w][2], jog[b][0], jog[b][3] = jog[w][0] + 1, jog[w][1] + 1, jog[w][2] + int(dic['white_result'] == 'win'), jog[b][0] + 1, jog[b][3] + int(dic['black_result'] == 'win')
        jog[w][0] += 1
        jog[w][1] += 1
        jog[w][2] += int(dic['white_result'] == 'win')
        jog[b][0] += 1
        jog[b][3] += int(dic['black_result'] == 'win')

    # Correr o filtro duas vezes (aqui e na função vitorias) compensa vs correr o filtro só no fim.
    # É muito pouco provável (e prático) que se escreva usernames suficientes para que não compense.
    return sorted(filter(lambda user: user[0] in jogadoras, jog.items()) if jogadoras else jog.items(), key=itemgetter(1), reverse=True)


###################################################################################################


def vitorias(dados, top=None, jogadoras=None):
    """Processa e gera o gráfico da percentagem de vitórias das jogadoras.

    Requires:
        Os dicionários do iterador dados devem conter as chaves black_username, white_username, white_result, e black_result.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        top (int, opcional): Quantidade de jogadoras a mostrar. 5 por defeito.
        jogadoras (list<str>, opcional): Lista de jogadoras a mostrar.

    Raises:
        UserWarning: Levantado quando os parâmetros top e jogadoras são ambos especificados ou quando não existem vitorias a mostrar.
    """
    if top and jogadoras:
        raise UserWarning(
            'Os argumentos -c e -u não podem ser usados em conjunto.')
    elif jogadoras:
        dados = filter(lambda dic: dic['white_username'].lower(
        ) in jogadoras or dic['black_username'].lower() in jogadoras, dados)
        top = len(jogadoras)
    elif not top:
        top = 5

    # (nome,  [jogosTotais, jogosBrancas, vitoriasBrancas, vitoriasPretas])
    processed = vitoriasProcess(dados, jogadoras)[:top]
    if not processed:
        raise UserWarning('Sem vitorias a mostrar.')
    # (nome, %vitBrancas, %vitPretas)
    # o nome.lower() é mais inteligente aqui do que no process
    jogadasMapped = map(lambda x: (
        x[0].lower(), x[1][2]/x[1][1], x[1][3]/(x[1][0]-x[1][1])), processed)
    vitoriasDraw(*list(zip(*jogadasMapped)))


###################################################################################################
### Operação seguinte #############################################################################
###################################################################################################


def seguinteDraw(abcissas, ordenadas, jogada):
    """Desenha o plot das jogadas seguintes.

    Args:
        abcissas (list): Lista das abcissas.
        ordenadasBrancas (list): Lista das ordenadas.
        jogada (str): Jogada anterior.
    """
    plt.bar(abcissas, ordenadas)
    plt.title(f'Jogadas mais prováveis depois de {jogada}')
    plt.xlabel('Jogadas')
    plt.ylabel('Probabilidades')
    plt.tight_layout()
    plt.show()


###################################################################################################


def seguinteProcess(dados, jogada):
    """Obtém as próximas jogadas (e o seu total) à jogada.

    Requires:
        Os dicionários do iterador dados devem conter a chave pgn.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        jogada (str): Jogada inicial.

    Returns:
        tuple<dict, int>: Tuplo do dicionario de jogadas e quantidade de jogadas.
    """
    regex = f'1. {jogada} ' + r'{\[%clk [\d:\.]+\]} 1\.{3} (N?[a-h][1-8])'

    jogadas, total = {}, 0
    for jogoDic in dados:
        matches = reMatch(regex, jogoDic['pgn'])
        if matches:
            j = matches.group(1)
            jogadas[j] = 1 if j not in jogadas else jogadas[j]+1
            total += 1

    return (jogadas, total)


###################################################################################################


def seguinte(dados, jogada=None, count=None):
    """Processa e gera um gráfico da percentagem das jogadas seguintes a uma abertura.

    Requires:
        Os dicionários do iterador dados devem conter a chave pgn.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        jogada (str, opcional): Jogada de abertura para procurar jogadas seguintes. e4 por defeito.
        count (int, opcional): Quantidade de jogadas a mostrar. 5 por defeito.

    Raises:
        UserWarning: Levantado quando não existem jogadas seguintes.
    """
    jogada = jogada or 'e4'
    count = count or 5

    jogadas, total = seguinteProcess(dados, jogada)

    if not jogadas:
        raise UserWarning('Sem jogadas seguintes.')

    jogadasSorted = sorted(
        jogadas.items(), key=itemgetter(1), reverse=True)[:count]
    jogadasMapped = map(lambda x: (x[0], x[1]/total), jogadasSorted)
    seguinteDraw(*list(zip(*jogadasMapped)), jogada)


###################################################################################################
### Operação mate #################################################################################
###################################################################################################


def mateDraw(abcissas, ordenadasGanhos, ordenadasXeques, ordenadasPercentagem):
    """Desenha o plot das jogadas seguintes.

    Args:
        abcissas (list<any>): Lista das abcissas.
        ordenadasGanhos (list<float>): Lista das ordenadas para as barras de jogos ganhos.
        ordenadasXeques (list<float>): Lista das ordenadas para as barras de jogos ganhos por xeque-mate.
        ordenadasPercentagem (list<float>): Lista das ordenadas para as percentagens.
    """
    fig, xeques = plt.subplots()
    plt.title(
        'Percentagem de xeque-mate,\njogos ganhos, e jogos ganhos por xeque-mate')

    xeques.bar(abcissas, ordenadasXeques, -0.4,
               label='jogos ganhos por xeque-mate', color='lightgray', align='edge')
    xeques.bar(abcissas, ordenadasGanhos, 0.4,
               label='jogos ganhos', color='blue', align='edge')
    xeques.tick_params(axis='x', labelrotation=90)
    xeques.set_ylabel('#Jogos')
    xeques.legend()

    ratio = xeques.twinx()
    ratio.plot(abcissas, ordenadasPercentagem, color='red',
               label='percentagem\nde xeque-mate')
    ratio.set_ylabel('Percentagem de xeque-mate', color='red')
    ratio.legend(loc=6)

    fig.tight_layout()
    plt.show()


###################################################################################################


def mateProcess(dados):
    """Processa os dados de forma a retornar um iterador de tuplos com os dados de cada jogador.

    Requires:
        Os dicionários do iterador dados devem conter as chaves  white_result, black_result, white_username, e black_username.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.

    Yields:
        tuple<str, int, int, float>: Tuplo com o nome, qtd de jogos ganhos, qtd de jogos ganhos por xeque-mate e percentagem de xeque mate.
    """
    # {nome: [ganhos, xeques]}
    dicJogos = {}

    for dic in dados:
        if dic['white_result'] == 'win':
            nome = dic['white_username']
            inc = int(dic['black_result'] == 'checkmated')
        elif dic['black_result'] == 'win':  # ñ pode ser else pq dos empates
            nome = dic['black_username']
            inc = int(dic['white_result'] == 'checkmated')
        else:
            continue

        if nome not in dicJogos:
            dicJogos[nome] = [1, inc]
        else:
            dicJogos[nome][0] += 1
            dicJogos[nome][1] += inc

    # [(nome, ganhos, xeques, %xeques)]
    return map(lambda lst: (lst[0].lower(), *lst[1], lst[1][1]/lst[1][0]), dicJogos.items())


###################################################################################################


def mate(dados, top=None):
    """Processa e gera um gráfico da percentagem de xeque-mate, a quantidade de jogos ganhos e jogos ganhos por xeque-mate.

    Requires:
        Os dicionários do iterador dados devem conter as chaves  white_result, black_result, white_username, e black_username.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        top (int, opcional): Quantidade de jogadoras a mostrar. 5 por defeito.
    """
    if not top:
        top = 5

    sortedDados = sorted(mateProcess(
        dados), key=itemgetter(1), reverse=True)[:top]
    mateDraw(*list(zip(*sortedDados)))


###################################################################################################
### Operação extrair ##############################################################################
###################################################################################################


def extrair(dados, regex=None, coluna=None, ficheiroSaida=None):
    """Processa e guarda os dados filtrados num ficheiro csv.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        regex (str, opcional): Expressão regular para filtrar as linhas interessantes. .* por defeito.
        coluna (str, opcional): Coluna na qual a expressão regular é testada. wgm_username por defeito.
        ficheiroSaida (str, opcional): Caminho do ficheiro onde guardar os dados processador. out.csv por defeito.

    Raises:
        UserWarning: Levantado quando a chhave coluna não existe no iterador dados.
    """
    if coluna not in dados[0]:
        raise UserWarning(f'"{coluna}" não é uma coluna válida.')
    filtered = filter(lambda dic: reSearch(regex, dic[coluna]), dados)
    escrever_csv_dicionario(ficheiroSaida, filtered, dados[0].keys())


###################################################################################################
### Iniciador e dispatcher do script ##############################################################
###################################################################################################


def dispatch(args):
    """Trata dos argumentos e chama a função relacionada com cada caso.

    Args:
        args (dict<comando: str, ficheiro: str, count: int, nomes: list<str>, jogada: str, regex: str, output: str): Dicionário dos argumentos.
    """
    dados = ler_csv_dicionario(args['ficheiro'])

    cmdSwitch = {
        'anos': (anos, ()),
        'classes': (classes, ('count',)),
        'vitorias': (vitorias, ('count', 'nomes')),
        'seguinte': (seguinte, ('jogada', 'count')),
        'mate': (mate, ('count',)),
        'extrair': (extrair, ('regex', 'coluna', 'output'))
    }

    cmd = cmdSwitch[args['comando']]
    cmd[0](dados, *[args[x] for x in cmd[1]])


###################################################################################################


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Analisador de jogos de xadrez.')
    parser.add_argument('ficheiro', help='Caminho do ficheiro de dados CSV.')
    parser.add_argument('comando', choices=[
                        'anos', 'classes', 'vitorias', 'seguinte', 'mate', 'extrair'], help='Comando a executar.')
    parser.add_argument(
        '-c', '--count', type=int, help='Quantidade de valores a considerar.')
    parser.add_argument(
        '-u', '--nomes', nargs='+', help='Nomes das jogadoras a comparar. Duplicados serão descartados.')
    parser.add_argument('-j', '--jogada', help='Jogada.')
    parser.add_argument(
        '-r', '--regex', help='Expressão regular que identifica as linhas de interesse.', default='.*')
    parser.add_argument(
        '-d', '--coluna', help='Coluna na qual testar a expressão regular.', default='wgm_username')
    parser.add_argument(
        '-o', '--output', help='Nome do ficheiro de saída.', default='out.csv')

    args = parser.parse_args()

    try:
        dispatch(args.__dict__)
    except UserWarning as w:
        print(w)


###################################################################################################
