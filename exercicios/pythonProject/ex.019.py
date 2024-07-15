#Um professor quer sortear um dos alunos para apagar o quadro.
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

'''lista = []

a1 = input('Digite o nome do primeiro aluno que está no sorteio para apagar o quadro: ')
lista.append(a1)

a2 = input('Digite o nome do segundo aluno  que está no sorteio para apagar o quadro ')
lista.append(a2)

a3 = input('Digite o nome do terceiro aluno que está no sorteio para apagar o quadro: ')
lista.append(a3)

a4 = input('Digite o nome do quarto aluno que está no sorteio para apagar o quadro: ')
lista.append(a4)

sorteio = choice(lista)

print('')
print('Entre os alunos {}, {}, {}, {}. O escolhido para apagar o quadro é "{}"'.format(a1, a2, a3, a4, sorteio))'''


a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno escolhido foi {}.'.format(sorteio))


