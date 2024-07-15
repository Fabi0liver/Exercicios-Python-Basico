# o Mesmo professor do desafio anterio quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample, shuffle

'''l = []

a1 = input('Digite o nome do aluno que vai apresentar o trabalho: ')
l.append(a1)

a2 = input('Digite o nome do outro aluno que vai apresentar o trabalho: ')
l.append(a2)

a3 = input('Digite o nome de outro aluno que vai apresentar o trabalho: ')
l.append(a3)

a4 = input('Digite o nome de outro aluno  que vai apresentar o trabalho: ')
l.append(a4)

sorteio = sample(l,4)

print('')
print('Os alunos que que vão apresentar o trabalho são {}, {}, {}, {}.'.format(a1, a2, a3, a4))
print('E a ordem de apresentação do trabalho é:')
print('1º: {} \n2º: {} \n3º: {} \n4º: {}'.format((sorteio[0]), (sorteio[3]), (sorteio[1]), (sorteio[2])))'''

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A orde, de apresetação será:')
print(lista)



