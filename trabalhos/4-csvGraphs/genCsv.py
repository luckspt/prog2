import sys
import csv
from random import randint, seed

seed(56926)
header = [
            chr(c) 
            for c
            in range(ord(' '), ord('~'))
         ] + ['AD', 'Full-flowering date (DOY)', 'mag', 'time']

add0 = lambda num: str(num) if num >= 10 else f'0{num}'

genDate = lambda: f'2021-12-{add0(randint(1, 31))}T{add0(randint(0,24))}:{add0(randint(0,60))}:{add0(randint(0, 60))}.123Z'

def genData(qtd):
    nice = ['AD', 'Full-flowering date (DOY)', 'mag', 'time']
    return [{k: genDate() if k in nice and nice.index(k) == 3 else randint(0, 10000) for k in header} for _ in range(qtd)]

qtd = int(input('Bora lá chefe quantas linhas queres pa? '))
nome = input('E o nome do fchero hm? ')
with open(f'{nome}.csv', 'w') as f:
    writer = csv.DictWriter(f
        , header
        , delimiter=';')

    writer.writeheader()
    dados = genData(qtd)

    writer.writerows(dados)