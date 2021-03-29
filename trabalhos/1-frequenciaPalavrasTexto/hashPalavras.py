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
    
    dic = { palavra: [0, set()] for palavra in palavras }

    for i, linha in enumerate(linhas):
        if not len(linha):
            continue
        
        for palavra in linha:
            try:
                dic[palavra][0] += 1
                dic[palavra][1].add(i+1)
            except:
                continue

    return { k: tuple(dic[k]) for k in dic }
