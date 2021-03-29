__author__ = 'Lucas Pinto, 56926'

def leLinhas(caminho):
    """Retorna as palavras das linhas de um ficheiro

    Args:
        caminho (string): Caminho do ficheiro

    Returns:
        list<list<string>>: lista de linhas com lista de palavras desse ficheiro
    """
    with open(caminho) as f:
        return [linha.split() for linha in f]

def ler_palavras(caminho):
    """Lê as palavras de um ficheiro

    Args:
        caminho (string): Caminho do ficheiro

    Returns:
        list<string>: Lista das palavras
    """
    return set([palavra for subLista in leLinhas(caminho) for palavra in subLista])

def initDict(lst):
    """Inicializa o dicionário com a quantidade de vezes que o elemento aparece na lista

    Args:
        lst (list): Lista com os elementos para transformar em dicionário

    Returns:
        dict: Dicionário com os elementos (key) da lista e (value) vezes que aparecem
    """
    dic = dict()
    for el in lst:
        try:
            dic[el] += 1
        except:
            dic[el] = 1

    return dic

def encontrar_palavras(caminhoTexto, caminhoPalavras):
    """Encontra as ocorrências das palavras no caminhoPalavras no texto em caminhoTexto

    Args:
        caminhoTexto (string): Caminho do ficheiro de texto
        caminhoPalavras (string): Caminho do ficheiro das palavras

    Returns:
        dict<string, (int, set<int>)>: Ocorrêcia das palavras
    """
    palavras = ler_palavras(caminhoPalavras)
    linhas = leLinhas(caminhoTexto)
    
    dic = { palavra: [0, set()] for palavra in palavras}

    for i, linha in enumerate(linhas):
        if not len(linha):
            continue
        
        linhaDict = initDict(linha)

        for palavra in palavras:
            try:
                dic[palavra][0] += linhaDict[palavra]
                dic[palavra][1].add(i+1)
            except:
                continue
                
    return { k: tuple(dic[k]) for k in dic }