#Escreva  um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro número é o maior
# O segundo número é o maior
# Não existe valor maior, os dois são iguais.
from random import randint

n1 = randint(0, 1000)
n2 = randint(0, 1000)
print(f'O primeiro valor é {n1}!')
print(f'O segundo valor é {n2}!')
if n1 > n2:
    print('O primeiro valor é o maior!')
elif n1 < n2:
    print('O segundo valor é o maior!')
else:
    print('Não existe valor maior, os dois são iguais!')



