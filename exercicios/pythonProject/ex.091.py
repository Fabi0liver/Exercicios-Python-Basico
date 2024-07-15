#crie Um programa onde Jogadores joguem um dado e tenha resultado aleatórios.
#Guarde esses resultados em um dicionário. No final, coloque esses dicionário em ordem, sabendo que o
#vendedor tirou a maior número no dado.

from random import randint
from time import sleep

jogo = dict()
jogo_ordem = dict()

print('')
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
for v in sorted(jogo, key=jogo.get, reverse=True):
    jogo_ordem[v] = jogo[v]

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('')

c = 1
print('  ==Ranking dos Jogadores:==')
sleep(2)
print('')
for k, v in jogo_ordem.items():
    print(f'  {c}º lugar: {k} com {v}')
    sleep(1)
    c += 1


