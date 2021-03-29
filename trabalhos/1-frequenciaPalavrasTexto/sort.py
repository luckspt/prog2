__author__ = 'Lucas Pinto, 56926'

def getLinha(caminho):
    """Iterador que obtém uma linha do ficheiro especificado pelo caminho

    Args:
        caminho (string): Caminho do ficheiro

    Yields:
        list<string>: lista de palavras da linha desse ficheiro
    """
    with open(caminho) as f:
        for linha in f:
            yield linha.split()

def ler_palavras(caminho):
    """Lê as palavras de um ficheiro

    Args:
        caminho (string): Caminho do ficheiro

    Returns:
        list<string>: Lista das palavras
    """
    iterLinhas = getLinha(caminho)
    return set([palavra for subLista in iterLinhas for palavra in subLista])

def encontrar_palavras(caminhoTexto, caminhoPalavras):
    """Encontra as ocorrências das palavras no caminhoPalavras no texto em caminhoTexto

    Args:
        caminhoTexto (string): Caminho do ficheiro de texto
        caminhoPalavras (string): Caminho do ficheiro das palavras

    Returns:
        dict<string, (int, set<int>)>: Ocorrêcia das palavras
    """
    palavras = ler_palavras(caminhoPalavras)
    iterLinhas = getLinha(caminhoTexto)

    dic = {palavra: [0, set()] for palavra in palavras}
    for i, linha in enumerate(iterLinhas):
        nlinha = sorted(linha)

        for palavra in palavras:
            try:
                first = nlinha.index(palavra)
                cnt = 1
                while nlinha[first + cnt] == palavra:
                    cnt += 1
                dic[palavra][0] += cnt
                dic[palavra][1].add(i+1)
            except:
                continue

    return { k: tuple(dic[k]) for k in dic }