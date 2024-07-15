#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O progama deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

n = randint(0, 5)

print('')
print('-=-' * 20)
print('VAMOS JOGAR?! Estou pensando em um número entre 0 e 5! TENTE ADIVINHAR!!!')
print('-=-' * 20)
print('')
sleep(1)
usu = int(input('Em que  número que estou pensando: '))
print('')
print('PROCESSANDO...')
print('')
sleep(2)
if usu == n:
    print(f'''O número que pensei foi o {n}!
  Você acertou!! Parabéns!!''')
else:
    print(f'''O número que pensei foi o {n}!
   Você errou!! Que pena!!''')
sleep(1)
print('')
print('-=-' * 20)
print('Foi legal jogar com você!;) \nTente denovo se desejar!!')
print('-=-' *20)


