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
from re import search as reSearch, match as reMatch
from matplotlib import pyplot as plt

__author__ = 'Lucas Pinto, 56926; Mário Zeller, 49570'

#? Ver se o xadrez.csv.cached existe. Se sim, fazer ast.literal_eval
#? Poupa a leitura do csv e processamento para lista de dicts visto que o xadrez.csv.cached seria o ficheiro csv já em lista de dicts

def ler_csv_dicionario(nome_ficheiro, delimiter=','):
    """Ler um ficheiro CSV. O ficheiro pode ou não ter cabeçalho.

    Args:
        nome_ficheiro (str): O nome do ficheiro.
        fieldnames (list<str>, opcional):  A lista com o nomes das colunas.
            Utilizar quando o ficheiro não tiver cabeçalho. None por defeito.

    Returns:
        list<dict>: Uma lista de dicionarios com o conteúdo do ficheiro;
            as chaves do dicionário são lidas da primeira linha do ficheiro
            ou tiradas da lista cabeçalho.
    """
    with open(nome_ficheiro) as ficheiro_csv:
        leitor = DictReader(ficheiro_csv, delimiter=delimiter)
        return list(leitor)


def escrever_csv_dicionario(nome_ficheiro, iterador_de_dicionarios, cabecalho, separador=','):
    """Escrever num ficheiro CSV um dicionário de iteradores.

    Args:
        nome_ficheiro (str): O nome do ficheiro CSV.
        iterador_de_dicionarios (iter<dict>): O iterador.
        cabecalho (list): A sequência de chaves do dicionário que indica a *ordem* das
            colunas a escrever no CSV.
        separador (str, opcional): O separador a utilizar. , por defeito.
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = DictWriter(ficheiro_csv, cabecalho, delimiter=separador)
        escritor.writeheader()
        for linha in iterador_de_dicionarios:
            escritor.writerow(linha)

# ? A definição explicita do tipo deve-se ao map ser opcional
#! Só é necessário para os verificadores de tipos (como o Pyright) não se chatearem


def sortGroup(dados, key, keyGroup=None, mapFunc=None) -> Iterator:
    """Ordena e agrupa dados, opcionalmente mapeando os dados agrupados.

    Args:
        dados (iter<any>): Iterador a processar.
        key (func): Função de chave.
        keyGroup (func, opcional): Função de chave para agrupar. Usa a key por defeito.
        mapFunc (func, opcional): Função de mapear. None por defeito.

    Yields:
        list<any, iter<any>>|iter<any>: Lista de dados agrupados ou iterador quando mapeado.
    """
    sortedDados = sorted(dados, key=key)
    grouppedDados = groupby(sortedDados, key=keyGroup or key)

    if mapFunc:
        return map(mapFunc, grouppedDados)
    else:
        return grouppedDados


def anosDraw(abcissas, ordenadasJogos, ordenadasJogadoras):
    """Desenha o plot dos anos.

    Requires:
        len(abcissas) == len(ordenadasJogos) and len(ordenadasJogos) == len(ordenadasJogadoras).

    Args:
        abcissas (list<int>): Lista de anos das abcissas.
        ordenadasJogos (list<int>): Lista da quantidade de jogos.
        ordenadasJogadoras (list<int>): Lista da quantidade de jogadoras diferentes.
    """
    fig, jogos = plt.subplots()
    plt.title('Jogos e jogadoras por ano')
    color = 'g'
    jogos.bar(abcissas, ordenadasJogos, color=color,
              label='#jogos')  # clip_on=False
    jogos.set_xlabel('Ano')
    jogos.set_ylabel('Jogos', color=color)
    jogos.tick_params(axis='x', labelrotation=90)
    jogos.legend(loc=6)

    color = 'b'
    jogadoras = jogos.twinx()
    jogadoras.plot(abcissas, ordenadasJogadoras, color=color,
                   label='#jogadoras Diferentes')  # clip_on=False

    jogadoras.set_ylabel('#Jogadoras diferentes', color=color)
    jogadoras.set_ylim(ymin=min(ordenadasJogadoras),
                       ymax=max(ordenadasJogadoras))
    jogadoras.legend()

    fig.tight_layout()
    plt.show()


def anos(dados):
    """Processa e gera um gráfico dos jogos e jogadoras por ano.

    Requires:
        Cada dicionário no iterador dados deve ter as chaves end_time, white_username e black_username.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
    """
    processed = list(sortGroup(
        dados, lambda dic: dic['end_time'], lambda dic: dic['end_time'][:4], lambda x: (x[0], list(x[1]))))

    abcissas, ordenadasJogos, ordenadasJogadoras = [], [], []
    for ano, jogosAno in processed:
        abcissas.append(ano)
        ordenadasJogos.append(len(jogosAno))

        jogadoras = set()
        jogadoras.update(
            *[(jogo['white_username'], jogo['black_username']) for jogo in jogosAno])
        ordenadasJogadoras.append(len(jogadoras))

    anosDraw(abcissas, ordenadasJogos, ordenadasJogadoras)


def classesPopularFormat(dados, count):
    """Obtém os count formatos mais populares do dados.

    Requires:
        Cada dicionário no iterador dados deve ter a chave time_control.

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


def classesDraw(classes):
    """Desenha o plot das classes.

    Args:
        classes (list): Lista das classes.
    """
    for ind, classe in enumerate(classes, start=1):
        plt.subplot(2, 3, ind)
        plt.bar(list(map(lambda modo: modo[1], classe[1])), list(
            map(lambda jogos: jogos[0], classe[1])))
        plt.title(classe[0])
        repetido()

    #! As listas estão revertidas para igualar o gráfico do enunciado
    x = list(map(lambda x: x[0], classes))[::-1]
    y = list(map(lambda classe: sum(
        list(map(lambda jogos: jogos[0], classe[1]))), classes))[::-1]
    plt.subplot(2, 3, 5)
    plt.bar(x, y)
    plt.title('Distribuição de jogos por formato de jogo')
    repetido()
    plt.tight_layout()
    plt.show()

# TODO: Melhor nome xd


def repetido():
    plt.xlabel('Formato de jogo')
    plt.ylabel('#jogos')
    plt.tick_params(axis='x', labelrotation=90)


def classes(dados, count=None):
    """Processa e gera um gráfico dos jogos e classes por cada formato.

    Requires:
        Cada dicionário no iterador dados deve ter as chaves time_class e time_control.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        count (int, opcional): Quantidade de classes a mostrar. 5 por defeito.
    """
    count = count or 5

    # reverse para ficar igual ao enunciado
    sortedTimeclass = sorted(
        dados, key=lambda dic: dic['time_class'], reverse=True)
    grouppedTimeclass = groupby(
        sortedTimeclass, key=lambda dic: dic['time_class'])
    grouppedTimeclassDict = {t[0]: list(t[1]) for t in grouppedTimeclass}

    # [(time_class, [(nºjogos, time_control), ... ]), ... ]
    classesDraw(list(map(lambda key: (key, classesPopularFormat(
        grouppedTimeclassDict[key], count)), grouppedTimeclassDict.keys())))


def vitoriasDraw(abcissas, ordenadasBrancas, ordenadasPretas):
    """Desenha o plot das vitórias.

    Args:
        abcissas (list): Lista das abcissas.
        ordenadasBrancas (list): Lista das ordenadas para as barras brancas.
        ordenadasPretas (list): Lista das ordenadas para as barras pretas.
    """
    w = 0.4

    print(abcissas, ordenadasBrancas, ordenadasPretas, sep='\n\n')

    barBrancas = list(range(len(abcissas)))
    barPretas = [i+w for i in barBrancas]

    plt.bar(barBrancas, ordenadasBrancas, w,
            label='peças brancas', color='lightgray')
    plt.bar(barPretas, ordenadasPretas, w, label='peças pretas', color='black')

    plt.tick_params(labelrotation=90)
    plt.xlabel('Jogadoras')
    plt.ylabel('Percentagem')

    plt.xticks([x+(w/2) for x in barBrancas], abcissas)
    plt.legend()
    plt.tight_layout()
    plt.show()


def vitoriasMap(dados):
    """Mapeia os dados para as vitorias.

    Requires:
        Cada dicionário no iterador no dados deve ter as chaves white_username, white_result e black_result.

    Args:
        dados (tuple<str, iter<dict>>): Tuplo com o nome da jogadora e os seus jogos.

    Returns:
        dict: A versão atualizada do dicionário jog.
    """
    if dic['white_username'] not in jog:
        jog[dic['white_username']] = [1, 1, 0, 0, 0]
    else:
        jog[dic['white_username']][0] += 1
        jog[dic['white_username']][1] += 1

    if dic['black_username'] not in jog:
        jog[dic['black_username']] = [1, 0, 1, 0, 0]
    else:
        jog[dic['black_username']][0] += 1
        jog[dic['black_username']][2] += 1

    return jog

###################################################################################################


def vitoriasAux(dados, top, jogadoras=None):
    """Função auxiliar da função vitorias. Processa os dados.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        jogadoras (list<str>, opcional): Lista de jogadoras a mostrar.    
    """
    jogadora, jogos = dados

    jogadoraLower = jogadora.lower()
    bJogs, bVits, pJogs, pVits = 0, 0, 0, 0
    for jogo in jogos:
        if jogo['white_username'].lower() == jogadoraLower:
            bJogs += 1
            if jogo['white_result'] == 'win':
                bVits += 1
        else:
            pJogs += 1
            if jogo['black_result'] == 'win':
                pVits += 1

    brancas = bVits / bJogs if bJogs != 0 else 0
    pretas = pVits / pJogs if pJogs != 0 else 0
    total = pJogs + pJogs
    # nome, %vitorias brancas, %vitorias pretas, qtd jogos
    return (jogadora, brancas, pretas, total)


def vitorias(dados, top=None, jogadoras=None):
    """Processa e gera um gráfico da percentagem de vitórias das jogadoras.

    Requires:
        Cada dicionário no iterador dados deve ter a chave wgm_username.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        top (int, opcional): Quantidade de jogadoras a mostrar. 5 por defeito.
        jogadoras (list<str>, opcional): Lista de jogadoras a mostrar.

    Raises:
        UserWarning: Levantado quando os parâmetros top e o jogadoras são ambos especificados.
    """
    # não podem ser usados ao mesmo tempo
    if top and jogadoras:
        raise UserWarning(
            'Os argumentos -c e -u não podem ser usados em conjunto.')
    elif jogadoras:
        dados = filter(lambda dic: dic['wgm_username'] in jogadoras, dados)
    elif not top:
        top = 5

    sortedDados = sorted(sortGroup(
        dados, lambda dic: dic['wgm_username'], mapFunc=vitoriasMap), key=lambda lst: lst[3], reverse=True)
    if top:
        sortedDados = sortedDados[:top]

    vitoriasDraw(*list(zip(*sortedDados))[:-1])


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


def seguinte(dados, jogada=None, count=None):
    """Processa e gera um gráfico da percentagem das jogadas seguintes a uma abertura.

    Requires:
        Cada dicionário no iterador dados deve ter a chave pgn.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        jogada (str, opcional): Jogada de abertura para procurar jogadas seguintes. e4 por defeito.
        count (int, opcional): Quantidade de jogadas a mostrar. 5 por defeito.
    """
    jogada = jogada or 'e4'
    count = count or 5

    regex = f'1. {jogada} ' + r'{\[%clk [\d:\.]+\]} 1\.{3} (N?[a-h][1-8])'

    jogadas, total = {}, 0
    for jogoDic in dados:
        matches = reMatch(regex, jogoDic['pgn'])
        if matches:
            j = matches.group(1)
            jogadas[j] = 1 if j not in jogadas else jogadas[j]+1
            total += 1

    if not jogadas:
        raise UserWarning('Sem jogadas seguintes.')
    jogadasSorted = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
    jogadasMapped = map(lambda x: (x[0], x[1]/total), jogadasSorted[:count])
    #! os verificadores de tipos (como o Pyright) podem dar falso positivo
    seguinteDraw(*list(zip(*jogadasMapped)), jogada)


# TODO fazer o grafico de linhas
def mateDraw(abcissas, ordenadasXeques, ordenadasGanhos, ordenadasPercentagem):
    """Desenha o plot das jogadas seguintes.

    Args:
        abcissas (list<any>): Lista das abcissas.
        ordenadasXeques (list<float>): Lista das ordenadas para as barras de jogos ganhos por xeque-mate.
        ordenadasGanhos (list<float>): Lista das ordenadas para as barras de jogos ganhos.
        ordenadasPercentagem (list<float>): Lista das ordenadas para as percentagens.
    """
    w = 0.4
    fig, xeques = plt.subplots()
    plt.title(
        'Percentagem de xeque-mate,\njogos ganhos, e jogos ganhos por xeque-mate')

    xeques.bar(abcissas, ordenadasXeques, -w,
               label='jogos ganhos por xeque-mate', color='lightgray', align='edge')
    xeques.bar(abcissas, ordenadasGanhos, w,
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


def mateMap(dados):
    """Mapeia os dados para as vitórias.

    Requires:
        Cada dicionário no iterador no dados deve ter as chaves white_username, white_result e black_result.

    Args:
        dados (tuple<str, iter<dict>>): Tuplo com o nome da jogadora e os seus jogos.
    """
    # {nome: [ganhos, xeques]}
    dicJogos = {}

    for dic in dados:
        if dic['white_result'] == 'win':
            nome = dic['white_username'].lower()
            inc = int(dic['black_result'] == 'checkmated')
        elif dic['black_result'] == 'win': # ñ pode ser else pq dos empates
            nome = dic['black_username'].lower()
            inc = int(dic['white_result'] == 'checkmated')
        else:
            continue

    return (jogadora, xeques, ganhos, xeques/ganhos if ganhos != 0 else 0, total)


def mate(dados, top=None):
    """Processa e gera um gráfico da percentagem de xeque-mate, a quantidade de jogos ganhos e jogos ganhos por xeque-mate.

    Requires:
        Cada dicionário no iterador dados deve ter a chave wgm_username.

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

    Requires:
         Cada dicionário no iterador dados deve ter a chave do argumento coluna.

    Args:
        dados (iter<dict>): Iterador de dicionários dos dados.
        regex (str, opcional): Expressão regular para filtrar as linhas interessantes. .* por defeito.
        coluna (str, opcional): Coluna na qual a expressão regular é testada. wgm_username por defeito.
        ficheiroSaida (str, opcional): Caminho do ficheiro onde guardar os dados processador. out.csv por defeito.
    """
    if coluna not in dados[0]:
        print(f'"{coluna}" não é uma coluna válida.')
    filtered = filter(lambda dic: reSearch(regex, dic[coluna]), dados)
    escrever_csv_dicionario(ficheiroSaida, filtered, dados[0].keys())


def dispatch(args):
    """Trata dos argumentos e chama a função relacionada com cada caso.

    Args:
        args (dict<comando: str, ficheiro: str, count: int, nomes: list<str>, jogada: str, regex: str, output: str): Dicionário dos argumentos.
    """
    s = time.time()
    dados = ler_csv_dicionario(args['ficheiro'])
    e = time.time()
    print(f'read {(e - s) * 1000}ms')

    cmdSwitch = {
        'anos': (anos, ()),
        'classes': (classes, ('count',)),
        'vitorias': (vitorias, ('count', 'nomes')),
        'seguinte': (seguinte, ('jogada', 'count')),
        'mate': (mate, ('count',)),
        'extrair': (extrair, ('regex', 'coluna', 'output'))
    }

    cmd = cmdSwitch[args['comando']]
    s = time.time()
    cmd[0](dados, *[args[x] for x in cmd[1]])
    e = time.time()
    print(f'process {(e - s) * 1000}ms')


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
    parser.add_argument('-j', '--jogada', help='Jogada ')
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
