from functools import reduce
from matplotlib import pyplot as plt
from math import ceil
# 6
# a) 
def tracar_subgrafico(graf, numero_linhas, numero_col, numero_graf):
    plt.subplot(numero_linhas,numero_col, numero_graf)
    plt.plot(graf[0],graf[1])

# b)

def tracar_subgraficos(lista_grafs, numero_linhas):
    n=0
    numero_colunas = math.ceil(len(lista_grafs)/numero_linhas)
    for graf in lista_grafs:
        tracar_subgrafico(graf, numero_linhas, numero_colunas, n+1)
        n+=1
    plt.show()

# c)
def tracar_subgraficos_sqrt(lis):
   tracar_subgraficos(lis,round(math.sqrt(len(lis))))
   
### 7
def tracar_graficos_personalizados(lista_graf, lista_form):
   list(map(lambda graf, form : plt.plot(graf[0],graf[1],form), lista_graf, lista_form))
   plt.show()
   
def mediaLista(lst):
    return sum(lst) / len(lst)

def transposta(lista_de_listas):
    """
    A solução preferida.
    
    >>> transposta([[0.0, 0.0], [1.0, 2.0], [2.0, 4.0], [3.0, 6.0], [4.0, 8.0], [5.0, 10.0]])
    [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0], [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]]
    >>> transposta([['0', '0'], ['1', '2'], ['2', '4'], ['3', '6'], ['4', '8'], ['5', '10']])
    [['0', '1', '2', '3', '4', '5'], ['0', '2', '4', '6', '8', '10']]
    """
    linhas = len(lista_de_listas)
    colunas = len(lista_de_listas[0])
    # linha varia mais rapidamente que coluna
    return [ [lista_de_listas[linha][coluna] for linha in range(linhas)]
                for coluna in range(colunas) ]

# 9
# a
def grafico_media(lst):
    abcissas = lst[0][0]
    ordenadas = list(map(lambda el: el[1], lst))
    #return (abcissas, list(map(lambda i: mediaLista([ordenadas[j][i] for j in range(len(ordenadas))]), range(len(ordenadas[0])))))
    return (abcissas, list(map(mediaLista, transposta(ordenadas))))

def tracar_com_media(lista_graficos):
    grafico_medias = grafico_media(lista_graficos)
    formatar = ['go--']*len(lista_graficos) +['ro-']
    tracar_graficos_personalizados(lista_graficos + [grafico_medias], formatar)

# tracar_com_media([constante, logaritmico,linear, loglinear, quadratico, exponencial])

# baixo = 0.1
# alto = 20.0
# constante = graficos(lambda x: 10.0, baixo= baixo, alto=alto)
# logaritmico = graficos(lambda x: math.log(x), baixo=baixo, alto=alto)
# linear = graficos(lambda x: x, baixo=baixo, alto=alto)
# loglinear = graficos(lambda x: x*math.log(x), baixo=baixo, alto=alto)
# quadratico = graficos(lambda x: x*x, baixo= baixo, alto=alto)
# exponencial = graficos(lambda x: 2**x, baixo= baixo, alto=alto)

# tracar_subgraficos_sqrt([constante, logaritmico, linear, loglinear, quadratico, exponencial],2)

#12 - Defina uma função grafico_barras que, dada um dicionário, apresente um gráfico de barras no qual os nomes das barras correspondem às chaves do dicionário e as alturas das barras correspondem aos respetivos valores. Defina a função de modo a que, para o dicionário abaixo seja apresentado um gráfico do tipo também abaixo:
precipitacao = {'jan': 118, 'fev': 98, 'mar': 61, 'abr': 80, 'mai': 70, 'jun': 18, 'jul': 17, 'ago':17, 'set': 42, 'out': 97, 'nov': 110, 'dez':143}
# Sugestões. Comece por programar a função unzip que, dada um dicionário, devolve um par de listas com as chaves e os valores respetivamente. Por exemplo
"""
>>> unzip ({'jan': 118, 'fev': 98, 'mar': 61})
(['jan', 'fev', 'mar'], [118, 98, 61])
"""
# Utilize a função pyplot.xticks(posição_das_etiquetas, etiquetas). Os parâmetros são duas listas que devem ter o mesmo comprimento. O primeiro parâmetro dá as posições em torno das quais o texto da etiqueta é centrado.
unzipdic = lambda dic: (dic.keys(), dic.values())
def prob12(dic):
    unzipped = unzipdic(dic)
    plt.bar(unzipped[0], unzipped[1])
    plt.show()
    """
    etiquetas, ordenadas = unzip(dic)
    abcissas = list(range(0,len(ordenadas)))
    plt.bar(abcissas, ordenadas)
    plt.xticks(abcissas, etiquetas)
    plt.show() 
    """
# prob12(precipitacao)

#13 - A função pyplot.hist(valores, num_classes) permite representar um conjunto de valores sob a forma de um histograma como número de classes dado. Por exemplo, o código Python abaixo deve imprimir o gráfico na figura também abaixo
"""
>>> dados = [1, 1, 1, 3, 2, 5, 1, 5, 6, 6, 7, 8, 8]
>>> pyplot.hist(dados, 3)
"""
# Defina uma função histogramas_classes que permita mostrar várias representações em histograma de um mesmo conjunto de valores, considerando um número variável de classes. A função recebe dois argumentos: a lista de valores para construir o histograma e uma lista de inteiros. Cada inteiro na segunda lista representa um número de classes. A função apresenta tantos histogramas quantos os elementos desta segunda lista. Defina a função de modo a que:
# a) Cada histograma seja apresentado numa figura independente.
def prob13a(vals, ints):
    for elems in ints:
        plt.hist(vals, elems)
    plt.show()
# b) Os histogramas apareçam todos numa mesma figura, havendo, no máximo, 2 por coluna. Utilize a função pyplot.subplot e as ideias do exercício 6. Por exemplo, o código seguinte deverá mostrar a figura apresentada
def prob13b(vals, ints):
    lins = ceil(len(ints)/2)
    for idx, elems in enumerate(ints):
        plt.subplot(lins, 2, idx+1)
        plt.hist(vals, elems)
    plt.show()

dados = [1, 1, 1, 3, 2, 5, 1, 5, 6, 6, 7, 8, 8]
prob13b(dados, [2, 3, 4, 5])

#14 - Escreva uma função traca_frequencias(nome_ficheiro) que lê um ficheiro de texto e apresenta um gráfico de barras com as frequências de cada letra no texto. Para simplificar, considere apenas letras minúsculas abc...xyz e ignore pontuação e acentuação.
# Sugestões. Utilize um dicionário em que as chaves correspondem às vinte e seis letras do alfabeto, e os valores correspondem às respetivas frequências. Defina uma função dicionario_frequencias que leia o ficheiro de texto e devolva o respetivo dicionário de frequências. Utilize afunção grafico_barras do exercício 12.
def prob14freqs(path):
    dic = { c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
    # for c in "abcdefghijklmnopqrstuvwxyz":
    #   dic[c] = 0
    # for ascii in range(ord('a'), ord('z')+1):
    #     dic[chr(ascii)] = 0 

    with open(path) as f:
        txt = f.read()
        for c in txt:
            if c in dic:
                dic[c] += 1

    return dic

def prob14(path):
    freqs = prob14freqs(path)
    prob12(freqs)
# prob14('repo/fichas/7_matplot/lusiadas.txt')