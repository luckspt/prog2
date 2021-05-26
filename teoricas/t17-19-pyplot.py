#!/usr/bin/env python

"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Visualização de dados.
Alguns documentos úteis:
https://www.w3schools.com/python/matplotlib_markers.asp
http://www.science.smith.edu/dftwiki/index.php/MatPlotLib_Tutorial_1
https://matplotlib.org/ 
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

import matplotlib.pyplot as plt  # http://matplotlib.org/api/pyplot_api.html
import numpy as np  # http://www.numpy.org/
import math
import csv


# 1 _ Gráfico da função quadrática

def quadratica():
    plt.plot(list(map(lambda x: x ** 2, range(10000))))
    plt.xlabel('x')
    plt.ylabel('f(x) = 2**x')
    plt.title('Gráfico da função quadrática')
    plt.show()


# 2 _ A cadeia de collatz
# https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(n):
    """O próximo número na sequência de Collatz

    Args:
        n (int): Um dado número na sequência

    Returns:
        int: O número seguinte
    """
    return n // 2 if n % 2 == 0 else 3 * n + 1


def cadeia_collatz(x):
    """Uma lista com a cadeia de Collatz desde x até chegar a 1

    Args:
        x (int): O número inicial

    Returns:
        int: A cadeia
    """
    if x == 1:
        return [1]
    else:
        y = collatz(x)
        return [y] + cadeia_collatz(y)

def tracar_collatz(n):
    """Um gráfico com os valores da sequência de Collatz
    começando num dado número.

    Args:
        n (int): O número inicial
    """
    plt.plot(cadeia_collatz(n))
    plt.show()

def tempo_paragem(n):
    """O comprimento da cadeia de Collatz para um dado número

    Args:
        x (int): O número inicial

    Returns:
        int: O comprimento da cadeia
    """
    return len(cadeia_collatz(n))

def tracar_paragem(n):
    """Um histograma com os tempos de paragem das sequências de Collatz
    até um dado número. Por tempo de paragem entende-se o comprimento da
    sequência até atingir o número 1.

    Args:
        n (int): O número inicial limite
    """
    tempos = list(map(tempo_paragem, range(1, n + 1)))
    classes = 100
    plt.hist(tempos, classes)
    plt.title('Tempos totais de paragem para números entre 1 e ' + str(n))
    plt.xlabel('Tempo de paragem')
    plt.ylabel('Frequência')
    plt.show()

# tracar_collatz(1000)
# tracar_collatz(1001)

def tracar_com_max(ordenadas):
    """Traçar um gráfico para uma dada lista de ordenadas.
    Assume-se que a abcissas começam em zero. Apresenta também o ponto
    onde o gráfico atinge o valor máximo.

    Args:
        ordenadas (list[number]): As ordenadas do gráfico
    """
    plt.plot(ordenadas)
    maxy = max(ordenadas)
    maxx = ordenadas.index(maxy)
    plt.annotate('(' + str(maxx) + ', ' + str(maxy) + ')',
                   xy = (maxx, maxy),
                   xytext = (maxx * 1.1, maxy * 1.1),
                   arrowprops = {'shrink': 0.05, 'facecolor': 'black'})
    plt.show()

# tracar_com_max(cadeia_collatz(10001))


# 3 _ Seis gráficos na mesma figura

def constante(n):
    return list(map(lambda _: 10, linear(n)))

def logaritmica(n):
    return list(map(lambda x: math.log(x), linear(n)))

def linear(n):
    return list(range(1, n + 1))

def log_linear(n):
    return list(map(lambda x: x * math.log(x), linear(n)))

def quadratica(n):
    return list(map(lambda x: x * 2, linear(n)))

def exponencial(n):
    return list(map(lambda x: x**2, linear(n)))

def seis_mesma(n):
    """Seis gráficos de seis funções comuns na caracterização da complexidade
    assintótica de funções. Os gráficos aparecem todos na mesma figura.

    Args:
        n (int): O valor limite para cada gráfico.
    """
    plt.plot(constante(n),   color='magenta', linestyle='-')
    plt.plot(logaritmica(n), color='cyan', linestyle=':')
    plt.plot(linear(n),      color='blue',  linestyle='-.')
    plt.plot(log_linear(n),  color='red',   linestyle='--')
    plt.plot(quadratica(n),  color='green', linestyle=':')
    plt.plot(exponencial(n), color='black',  linestyle='-.')
    plt.show()


# 4 _ 6 graficos em 6 figuras

def seis_subplot(n):
    """Seis gráficos de seis funções comuns na caracterização da complexidade
    assintótica de funções. Os gráficos aparecem em figuras diferentes.

    Args:
        n (int): O abcissa limite para cada um dos gráficos
    """
    graficos = [constante(n), logaritmica(n), linear(
        n), log_linear(n), quadratica(n), exponencial(n)]
    titulos = ['constante', 'log', 'linear', 'log-lin', 'quad', 'exp']
    for n in range(len(graficos)):
        plt.subplot(2, 3, n + 1)  # linhas, colunas, número do gráfico
        plt.plot(graficos[n])
        plt.title(titulos[n])
    plt.show()


# 5 _ Grafico barras com notas 1o ano LTI

def barras_notas():
    """Um gráfico de barras para as notas das disciplinas do primeiro
    ano de um aluno.
    """
    ordenadas = [12, 14, 15, 19, 14, 17, 10, 20, 14]
    abcissas = range(len(ordenadas))
    etiquetas = ['AC', 'EM1', 'PDT', 'P1', 'EM2', 'IPE', 'ITW', 'P2', 'RC']
    plt.title('Notas primeiro ano')
    largura = 0.8
    plt.bar(abcissas, ordenadas, largura, color = 'green')
    plt.xticks(abcissas, etiquetas) # As etiquetas ficam alinhadas com o inicio da barra
#    pylab.xticks(map(lambda x: x + largura / 2.0, abcissas), etiquetas) # As etiquetas ficam alinhadas com o centro da barra
    plt.show()


# 6 _ Visualização de informação contida em ficheiros CSV

def ler_csv_dicionario(nome_ficheiro, cabecalho=None):
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
        leitor = csv.DictReader(ficheiro_csv, fieldnames=cabecalho)
        return list(leitor)

def coluna_para_floats(tabela, coluna):
    """Uma lista dos floats correspondentes às strings de uma coluna numa tabela.

    Args:
        tabela (iter[dict]): A tabela
        coluna (str): O nome da coluna

    Returns:
        list[float]: A lista de float
    """
    return list(map(lambda linha: float(linha[coluna]), tabela))

def sismos_no_mapa():
    """Um mapa com os sismos apresentados por pontos sobre um planisfério.
    A cor indica a magnitude do sismo.
    Grava o mapa num fichiro com o nome 'sismos.png'.
    """
    tabela = ler_csv_dicionario('all_month.csv')
    tabela_limpa = list(filter(
        lambda linha: linha['latitude'] != '' and linha['longitude'] != '' and linha['mag'] != '', tabela))
    longitudes = coluna_para_floats(tabela_limpa, 'longitude')
    latitudes = coluna_para_floats(tabela_limpa, 'latitude')
    magnitudes = coluna_para_floats(tabela_limpa, 'mag')
    plt.scatter(longitudes, latitudes, c = magnitudes, cmap='viridis')
    plt.colorbar()
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Distribuição geográfica dos sismos ocorridos no mês de março de 2021')
    mapa = plt.imread("planisferio.png")
    implot = plt.imshow(mapa, extent=[-180, 180, -90, 90])
    plt.savefig('sismos.png', format = 'png')
    plt.show()


# 7 _ Histogramas com valores lidos dum ficheiro CSV

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

def hist_notas_finais(nome_ficheiro):
    """Um histograma com as notas finais de uma disciplina. Os valores são
    lidos de um ficheiro CSV. O ficheiro não deve ter cabeçalho. Os
    valores são lidos da primeira coluna.

    Args:
        nome_ficheiro (str): O nome do ficheiro
    """
    linhas = ler_csv(nome_ficheiro)
    notas = list(filter(lambda x : x > 0, map(lambda linha: int(linha[0]), linhas)))
    classes = max(notas) - min(notas)
    plt.hist(notas, classes, facecolor = 'orange')
    plt.show()


# 8 _ Histogramas de uma distribuição normal, absoluta e cumulativa

def distribuicao_normal(nclasses, dimensao_amostra):
    """Dois gráficos com a distribuição normal: absoluta e cumulativa.

    Args:
        nclasses (int): O número de classes a considerar no histograma
        dimensao_amostra (int): A dimensão da amostra para gerar os dados
    """
    dados = np.random.normal(size = dimensao_amostra)
    plt.subplot(1, 2, 1)
    plt.hist(dados, nclasses, facecolor = 'orange')
    plt.ylabel('Densidade de probabilidade absoluta')
    plt.subplot(1, 2, 2)
    plt.hist(dados, nclasses, facecolor = 'orange', cumulative = True)
    plt.ylabel('Densidade absoluta cumulativa')
    plt.show()