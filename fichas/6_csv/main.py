import csv
def ler_csv(nome_ficheiro, delimiter=','):
    """Ler um ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[list][str]: O conteúdo do ficheiro. 
            Cada elemento da lista contém uma linha do ficheiro CSV.
            Cada string corresponde a um valor no ficheiro CSV.
    """
    with open(nome_ficheiro, 'r') as ficheiro_csv:
        return list(csv.reader(ficheiro_csv, delimiter=delimiter)) # list é para forçar a leitura do iterador antes de fechar o ficheiro

def escrever_csv(nome_ficheiro, iterador_de_iteradores, separador=','):
    """Escrever um iterador de iteradores num ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro
        iterador_de_iteradores (iter[iter]): O iterador
    """
    with open(nome_ficheiro, 'w') as ficheiro_csv:
        escritor = csv.writer(ficheiro_csv, delimiter = separador)
        for linha in iterador_de_iteradores:
            escritor.writerow(linha)

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

#1 - Escreva uma função ler_primeiras_csv(nome_de_ficheiro, n) que lê até n linhas de um ficheiro CSV, linha a linha e para uma lista de listas de strings. Caso o ficheiro tenha menos de n linhas, a função deverá ler o ficheiro todo.
def prob1(path, n):
    with open(path) as f:
        reader = csv.reader(f)
        return list(map(lambda el: el[0], zip(reader, range(n))))

#2 - A função ler_csv(nome_ficheiro) discutida nas aulas teóricas devolve uma lista de listas de strings. Muitas vezes precisamos de converter estas strings para valores de outros tipos, tais como inteiros ou números em vírgula flutuante. Escreva uma função converter_todos que, dado um iterável de iteráveis de valores e uma função de conversão, devolve um novo iterável de iteráveis onde todos os elementos do iterável original foram convertidos pela função parâmetro.
def prob2(its, conv):
    """
    >>> [list(it) for it in converter_todos([['0', '1', '2', '3', '4', '5'], ['0', '2', '4', '6', '8', '10']], int)]
    [[0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10]]
    """
    return ((conv(el) for el in it) for it in its)

#3 - Muitas vezes, precisamos de aplicar uma função de conversão aos valores em cada coluna, que difere de coluna para coluna.
# a) Escreva uma função converter.
def prob3a(iteravel, iteravel_de_funcoes):
    """iterável cujos elementos são obtidos por aplicação de cada função a cada elemento
    
    Args:
        iteravel (iter): iterável de valores
        iteravel_de_funcoes (iter): iterável de funções
    
    Returns:
        iter: novo iterável de valores

    >>> list(converter(['0', '3', '4', '5', '-1', '1'], [float]*2 + [lambda x: x]*2 + [lambda x: -int(x) if int(x) < 0 else int(x)]*2))
    [0.0, 3.0, '4', '5', 1, 1]
    """
    return (func(el) for el, func in zip(iteravel, iteravel_de_funcoes))

# b) Utilizando a função da alínea anterior, escreva agora a função converter_iteraveis.
def prob3b(iter_de_iteraveis, iteravel_de_funcoes):
    """converte cada 'coluna' do iter_de_iteraveis pela função respetiva no iteravel_de_funcoes
    
    Args:
        iter_de_iteraveis (iter): iterável de iteráveis (de valores)
        iteravel_de_funcoes (iter): iterável de funções
        
    Returns:
        iter: iterável de iteráveis de valores

    >>> [list(it) for it in prob3b([['Joao', '2001', '17.35'], ['Ana', '1999', '14.50'], ['Adao', '2000', '18.71']], [lambda x: x, int,float])]
    [['Joao', 2001, 17.35], ['Ana', 1999, 14.5], ['Adao', 2000, 18.71]]
    """
    funcoes = list(iteravel_de_funcoes)
    return (prob3a(it, funcoes) for it in iter_de_iteraveis)

def prob3bmap(iter_de_iteraveis, iteravel_de_funcoes):
    funcoes = list(iteravel_de_funcoes)
    return map(lambda x: prob3a(x, funcoes), iter_de_iteraveis)

# c) Finalmente, utilizando a função ler_csv(nome_ficheiro) e a função da alínea anterior, escreva uma função ler_csv_com_conversao(nome_ficheiro,iteravel_de_funcoes) que lê um ficheiro e devolve um iterável de iteráveis onde as ‘colunas’ se apresentam convertidas de acordo com as funções no iteravel_de_funcoes.
def prob3c(path, iterFuncs):
    linhas = ler_csv(path, delimiter=';')
    return prob3b(linhas, iterFuncs)

#4 - Escreva uma função escrever_primeiros_csv(nome_ficheiro,iter_de_iteraveis, n) que escreva num ficheiro em formato CSV os primeiros n elementos do iter_de_iteraveis. Se o iterável tiver menos de n elementos a função deverá escrever o iterável completo
def prob4(path, iterIters, n):
    toWrite = map(lambda el: el[0], zip(iterIters, range(n)))
    escrever_csv(path, toWrite)
