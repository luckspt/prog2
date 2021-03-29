import time
from random import randint

from brute import busca_lista_dupla as busca_lista_dupla_brute
from binariaSublista import busca_lista_dupla as busca_lista_dupla_binariaSublista
from binariaListaBinariaSublista import busca_lista_dupla as busca_lista_dupla_binariaListaBinariaSublista

qtdListas = int(input('Quantas sublistas gerar? '))
qtdNums = int(input('Quantos numeros por sublista gerar? '))

inp = [[x for x in range(qtdNums*lst, qtdNums+(lst*qtdNums))] for lst in range(qtdListas)]

qtasVezes = int(input('Quantas vezes? '))

brute = []
binariaSublista = []
binariaListaBinariaSublista = []
flat = []

for i in range(qtasVezes + 1):
    num = randint(0, ((qtdListas*qtdNums) or 1) - 1)

    current = time.time()
    busca_lista_dupla_brute(inp, num)
    end = time.time()
    if i != 0:
        brute.append(end - current)

    current = time.time()
    busca_lista_dupla_binariaSublista(inp, num)
    end = time.time()
    if i != 0:
        binariaSublista.append(end - current)

    current = time.time()
    busca_lista_dupla_binariaListaBinariaSublista(inp, num)
    end = time.time()
    if i != 0:
        binariaListaBinariaSublista.append(end - current)

print(
    f'Brute                             : {sum(brute) * 1000}ms\n'
    f'Binaria Sublista                  : {sum(binariaSublista) * 1000}ms\n'
    f'Binaria Lista Binaria Sublista    : {sum(binariaListaBinariaSublista) * 1000}ms\n'
)
