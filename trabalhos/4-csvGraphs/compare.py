import time
from random import randint

from main import sismosSemLer, sakuraSemLer, ler_csv_dicionario

qtasVezes = int(input('Quantas vezes? '))
path = input('Caminho do ficheiro: ')

s = time.time()
dadosRaw = ler_csv_dicionario(path, delimiter=';')

print(f'Leitura Ficheiro: {(time.time() - s) * 1000}ms')

solo = {'sakura': [], 'sismos': []}
zeller = {'sakura': [], 'sismos': []}

for i in range(qtasVezes + 1):
    startSakura = time.time()
    sakuraSemLer(dadosRaw)
    endSakura = time.time()
    sismosSemLer(dadosRaw)
    endSismos = time.time()
    if i != 0:
        solo['sakura'].append(endSakura - startSakura)
        solo['sismos'].append(endSismos - endSakura)

print(
    'Solo Sakura: ' + str(sum(solo['sakura']) * 1000) + 'ms\n'
    'Solo Sismo : ' + str(sum(solo['sismos']) * 1000) + 'ms\n'
)
