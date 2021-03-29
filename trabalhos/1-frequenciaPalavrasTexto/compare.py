
import time

from normal import encontrar_palavras
from sort import encontrar_palavras as encontrar_palavras_sort
from hashSem import encontrar_palavras as encontra_ocorrencias_hashSem
from hashCom import encontrar_palavras as encontra_ocorrencias_hashCom
from hashPalavras import encontrar_palavras as encontra_ocorrencias_hashPal


def ler_palavras(nome_ficheiro):
    with open(nome_ficheiro, 'r') as f:
        return set(palavra for linha in f for palavra in linha.split())


def encontrar_palavras_extra(texto, palavras):
    pass


inp = 'textoIpsum.txt'
out = 'palavras.txt'
print(f'A usar {inp} como texto e {out} como palavras.')

qtasVezes = int(input('Quantas vezes? '))
brute = []
sortd = []
hashSem = []
hashCom = []
hashPal = []
extra = []

for i in range(qtasVezes + 1):
    current = time.time()
    encontrar_palavras(inp, out)
    end = time.time()
    if i != 0:
        brute.append(end - current)

    current = time.time()
    encontrar_palavras_sort(inp, out)
    end = time.time()
    if i != 0:
        sortd.append(end - current)

    current = time.time()
    encontra_ocorrencias_hashSem(inp, out)
    end = time.time()
    if i != 0:
        hashSem.append(end - current)

    current = time.time()
    encontra_ocorrencias_hashCom(inp, out)
    end = time.time()
    if i != 0:
        hashCom.append(end - current)

    current = time.time()
    encontra_ocorrencias_hashPal(inp, out)
    end = time.time()
    if i != 0:
        hashPal.append(end - current)

    current = time.time()
    encontrar_palavras_extra(inp, out)
    end = time.time()
    if i != 0:
        extra.append(end - current)

print(
    f'Brute    : {sum(brute) * 1000}ms\nSort     : {sum(sortd) * 1000}ms\nHash Sem : {sum(hashSem) * 1000}ms\nHash Com : {sum(hashCom) * 1000}ms\nHash Pal : {sum(hashPal) * 1000}ms\nExtra    : {sum(extra) * 1000}ms')