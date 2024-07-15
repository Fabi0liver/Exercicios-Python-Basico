#Crie um programa que vai gerar cinco númeors aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
#que estão na tupla.

import numpy as np

n1 = np.random.randint(1, 10, 5)
n = sorted(tuple(n1))
print('Os valores sorteados foram:', n1[0], n1[1], n1[2], n1[3], n1[4])
print(f'O maior valor foi o {n[4]}')
print(f'O menor valor foi o {n[0]}')


