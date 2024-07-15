#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio e somarpat().
#A primeira funções vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores pares sorteados pela função anterios.

from random import randint
from time import sleep


def sorteia():
    print('Os 5 números sorteados foram: ', end='')
    for c in range(5):
        n = randint(1, 10)
        numeros.append(n)
        sleep(0.3)
        print(n, end=' ')
    sleep(0.9)
    print('PRONTO!')


def somapar(list):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'''Somando os valores pares entre {numeros}, 
              Temos o valor {soma}''')


# programa principal
numeros = []

print('')
print('~' * 50)
sorteia()
print('-' * 50)
somapar(numeros)
print('~' * 50)

