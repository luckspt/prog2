# Função auxiliar
def imprime_se_python (caminho):
    if caminho.endswith('.py'):
        print(os.path.abspath(caminho))

# a)

def todos_python_iter(raiz):
    """
    Imprime o caminho completo de todos os ficheiros Python que se encontram
    numa diretoria, incluindo subdiretorias. (iterativo)

    Args:
        raiz (str): caminho para a diretoria
    """
    for (diretorio, _, ficheiros) in os.walk(raiz):
        for ficheiro in ficheiros:
            caminho = os.path.join(diretorio, ficheiro)
            imprime_se_python(caminho)

def todos_python_rec(raiz):
    """
    Imprime o caminho completo de todos os ficheiros Python que se encontram
    numa diretoria, incluindo subdiretorias. (recursivo)

    Args:
        raiz (str): caminho para a diretoria
    """
    for ficheiro in os.listdir(raiz):
        caminho = os.path.join(raiz, ficheiro)
        if os.path.isdir(caminho):
            todos_python_rec(caminho)
        else:
            imprime_se_python(caminho)

if __name__ == '__main__':
    import sys, os
    # a)
    # todos_python_iter(sys.argv[1])
    # b)
    todos_python_rec(sys.argv[1])
