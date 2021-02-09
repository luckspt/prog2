def escreverPrimeirasPotencias(nomeFicheiro, n=10):
    """Escreve as primeiras potências num ficheiro até n

    Args:
        nomeFicheiro (string): Nome do ficheiro onde escrever
        n (int, optional): Quantas potências escrever. Defaults to 10.
    """

    f = open(nomeFicheiro, "w")
    i = 1
    for _ in range(n):
        f.write(f"{i}\n")
        i *= 2
    f.close()


def lerEImprimir(nomeFicheiro):
    """Lê um ficheiro e imprime o seu conteúdo

    Args:
        nomeFicheiro (string): Nome do ficheiro
    """
    f = open(nomeFicheiro, "r")

    for linha in f:
        print(linha, end="")
    f.close()


def somar(nomeFicheiro):
    """Lê um ficheiro e retorna a soma do seu conteúdo

    Args:
        nomeFicheiro (string): Nome do ficheiro
    """
    f = open(nomeFicheiro, "r")

    soma = 0
    for linha in f:
        soma += int(linha)
    f.close()
    return soma


def escreverAlgo(algo):
    """Escreve algo no ficheiro algo.txt

    Args:
        algo (string): O que vai ser escrito
    """
    f = open("algo.txt")
    f.write(algo)
    f.close()


def escreverAlgoWith(algo):
    """Escreve algo no ficheiro algo.txt com o with

    Args:
        algo (string): O que vai ser escrito
    """
    with open("algo.txt", "w") as f:
        f.write("algo")


def contaLinhas(nomeFicheiro):
    """Conta as linhas do ficheiro nomeFicheiro

    Args:
        nomeFicheiro (strig): Nome do ficheiro

    Returns:
        int: Quantidade de linhas do ficheiro
    """
    qtd = 0
    with open(nomeFicheiro, "r") as f:
        for _ in f:
            qtd += 1
    return qtd


def copiar(de, para):
    """Copia o ficheiro de para o ficheiro para

    Args:
        de (string): Nome do ficheiro de entrada
        para (string): Nome do ficheiro de saída
    """
    with open(de, "r") as d, open(para, "w") as p:
        p.write(d.read())


# Manipular Conteúdo


def conteudoPorLinhas(nomeFicheiro):
    """Retorna o conteúdo por linhas

    Args:
        nomeFicheiro (string): Nome do ficheiro

    Returns:
        string[]: Linhas do ficheiro
    """
    with open(nomeFicheiro, "r") as f:
        linhas = f.readlines()
    return (linha.rstrip() for linha in linhas)


def conteudoPorLinhas2(nomeFicheiro):
    """Retorna o conteúdo por linhas

    Args:
        nomeFicheiro (string): Nome do ficheiro

    Returns:
        string[]: Linhas do ficheiro
    """
    with open(nomeFicheiro, "r") as f:
        return f.read().splitlines()