import time
from random import randint

from lstComp import sismosSemLer, sakuraSemLer
from zip import sismosSemLer as sismosSemLer_nvo, sakuraSemLer as sakuraSemLer_nvo, ler_csv_dicionario
from zeller import sismos, sakura

qtasVezes = int(input('Quantas vezes? '))
path = input('Caminho do ficheiro: ')

s = time.time()
dadosRaw = ler_csv_dicionario(path, delimiter=';')

print(f'Leitura Ficheiro: {(time.time() - s) * 1000}ms')

zeller = {'sakura': [], 'sismos': []}
nvo = {'sakura': [], 'sismos': []}
old = {'sakura': [], 'sismos': []}

for i in range(qtasVezes + 1):
    startSakura = time.time()
    sakura(dadosRaw)
    endSakura = time.time()
    sismos(dadosRaw)
    endSismos = time.time()
    if i != 0:
        zeller['sakura'].append(endSakura - startSakura)
        zeller['sismos'].append(endSismos - endSakura)

    startSakura = time.time()
    sakuraSemLer_nvo(dadosRaw)
    endSakura = time.time()
    sismosSemLer_nvo(dadosRaw)
    endSismos = time.time()
    if i != 0:
        nvo['sakura'].append(endSakura - startSakura)
        nvo['sismos'].append(endSismos - endSakura)

    startSakura = time.time()
    sakuraSemLer(dadosRaw)
    endSakura = time.time()
    sismosSemLer(dadosRaw)
    endSismos = time.time()
    if i != 0:
        old['sakura'].append(endSakura - startSakura)
        old['sismos'].append(endSismos - endSakura)

print(
    'Zeller Sakura: ' + str(sum(zeller['sakura']) * 1000) + 'ms\n'
    'Novo Sakura  : ' + str(sum(nvo['sakura']) * 1000) + 'ms\n'
    'Old Sakura   : ' + str(sum(old['sakura']) * 1000) + 'ms\n'
    'Zeller Sismo : ' + str(sum(zeller['sismos']) * 1000) + 'ms\n'
    'Novo Sismo   : ' + str(sum(nvo['sismos']) * 1000) + 'ms\n'
    'Old Sismo    : ' + str(sum(old['sismos']) * 1000) + 'ms\n'
)
