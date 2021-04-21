#!/usr/bin/env python
import argparse

def more(nome_ficheiro, qtdLinhas = 10, linhaInicio=1):
    with open(nome_ficheiro, 'r') as leitor:
        for _ in range(linhaInicio):
            leitor.readline()
        tecla = ''
        linha = leitor.readline()
        while linha and not(tecla):
            for _ in range(qtdLinhas):
                print(linha, end = '')
                linha = leitor.readline()
            if linha: # termina imediatamente se não houver mais linhas
                tecla = input()
            
if __name__ == '__main__':
    import sys

    """
    if len(sys.argv) == 4:
        #b
        _, flg, v, nome_ficheiro = sys.argv
        if flg == '-c':
            more(nome_ficheiro, qtdLinhas=int(v))
        else:
            print('Flag inválida')
    elif len(sys.argv) == 2:
        #a)
        nome_ficheiro = sys.argv[1]
        more(nome_ficheiro)
    """

    #c
    parser = argparse.ArgumentParser(description='Imprime um ficheiro por páginas.')
    parser.add_argument('path', help='Caminho do ficheiro')
    parser.add_argument('-c', '--comprimento', type=int, default=10, help='Comprimento da página em número de linhas (valor por omissão: 10 linhas)')
    parser.add_argument('-l', '--linha', type=int, default=1, help='Numero da primeira linha a mostrar (valor por omissão: linha 1)')

    args = parser.parse_args()
    more(args.path, qtdLinhas=args.c, linhaInicio=args.l)
