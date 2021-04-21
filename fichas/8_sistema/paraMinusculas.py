#!/usr/bin/env python

def para_minusculas(nome_ficheiro):
    with open(nome_ficheiro) as f:
        txt = f.read()
        print(txt.casefold(), end='') # txt.lower()

if __name__ == '__main__':
    import sys
    
    nome_ficheiro = sys.argv[1]
    para_minusculas(nome_ficheiro)
