def processa_ficheiro(nome_ficheiro):
    num_linhas = 0
    num_palavras = 0
    num_bytes = os.path.getsize(nome_ficheiro) # pode lançar OSError
    with open(nome_ficheiro, 'r') as leitor:
        for linha in leitor:
            num_linhas += 1
            num_palavras += len(linha.split())
    return num_linhas, num_palavras, num_bytes

def imprime_resumo(mostra_linhas, num_linhas, mostra_palavras, num_palavras, mostra_bytes, num_bytes, elemento):
    if mostra_linhas:
        print(num_linhas, end = '\t')
    if mostra_palavras:
        print(num_palavras, end = '\t')
    if mostra_bytes:
        print(num_bytes, end = '\t')
    print(elemento)

def conta_palavras(nomes_ficheiros, mostra_linhas=True, mostra_palavras=True, mostra_bytes=True):
    total_linhas, total_palavras, total_bytes = (0, 0, 0)
    for nome_ficheiro in nomes_ficheiros:
        try:
            num_linhas, num_palavras, num_bytes = processa_ficheiro(nome_ficheiro)
            imprime_resumo(mostra_linhas, num_linhas, mostra_palavras, num_palavras, mostra_bytes, num_bytes, nome_ficheiro)
            total_linhas += num_linhas
            total_palavras += num_palavras
            total_bytes += num_bytes
        except OSError as e:
            print("{0}: {1}: open: {2}".format(sys.argv[0], nome_ficheiro, e.strerror))
    imprime_resumo(mostra_linhas, total_linhas, mostra_palavras, total_palavras, mostra_bytes, total_bytes, "total")

if __name__ == '__main__':
    import argparse, os, sys
    parser = argparse.ArgumentParser(prog='conta_palavras')
    parser.add_argument('-c', action='store_true', help='mostra o número de bytes do ficheiro')
    parser.add_argument('-l', action='store_true', help='mostra o número de linhas do ficheiro')
    parser.add_argument('ficheiro', nargs='+', help='um ou mais nomes de ficheiro')
    argumentos = parser.parse_args()
    mostra_palavras = not (argumentos.l or argumentos.c) # mostra palavras se nenhuma opção foi selecionada
    mostra_linhas = argumentos.l or not argumentos.c # mostra linhas se nenhuma opção ou -l foi selecionado
    mostra_bytes = not argumentos.l or argumentos.c # idem anterior para bytes
    conta_palavras(argumentos.ficheiro, mostra_linhas, mostra_palavras, mostra_bytes)
