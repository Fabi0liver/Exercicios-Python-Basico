#Faça um programa que ajude um jogador da Mega Sena a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear  6 números entre 1 e 60
#para cada jogo, cadastrando tudo em uma lista composta.

import numpy as np
from random import randint
from time import sleep

sorteios = []
num = []

print('')
print('$' * 42)
print(f'{'NÚMEROS DA MEGA CENA':^40}')
print('$' * 42)
print('')
sort = int(input('Digite quantos jogos devem ser gerados: '))
print('')
print(f'{f' SORTEANDO {sort} JOGOS ':-^42}')
print('')
for c in range(1, sort + 1):
    n = np.random.randint(1, 60, 6)
    n.sort()
    num.append(n)
    print(f'  JOGO{c:2}: {f'{n}':.>30}')
    sorteios.append(num)
    num.clear()
    sleep(1)
print('')
print(f'{' BOA SORTE! ':$^42}')


