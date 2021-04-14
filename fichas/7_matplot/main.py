from functools import reduce
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
    
tracar_com_media([constante, logaritmico,linear, loglinear, quadratico, exponencial])

baixo = 0.1
alto = 20.0
constante = graficos(lambda x: 10.0, baixo= baixo, alto=alto)
logaritmico = graficos(lambda x: math.log(x), baixo=baixo, alto=alto)
linear = graficos(lambda x: x, baixo=baixo, alto=alto)
loglinear = graficos(lambda x: x*math.log(x), baixo=baixo, alto=alto)
quadratico = graficos(lambda x: x*x, baixo= baixo, alto=alto)
exponencial = graficos(lambda x: 2**x, baixo= baixo, alto=alto)

tracar_subgraficos_sqrt([constante, logaritmico, linear, loglinear, quadratico, exponencial],2)
