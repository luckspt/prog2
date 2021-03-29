def busca_lista_dupla(matriz, num):
    """
    Procura se um inteiro está numa matriz de inteiros
    Args:
        matriz: Matriz de inteiros onde procurar
        num: Inteiro a procurar

    Returns: True se o elemento estiver presente na matriz, False caso contrário

    """
    if len(matriz) == 0:
        return False

    for subLista in matriz:
        if num in subLista:
            return True
    return False
