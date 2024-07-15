#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros ,
#Com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    maior = 0
    print('~' * 40)
    print('Analisando os valores passados ...'.center(40))
    print('~' * 40)
    sleep(2)
    print(f'  Foram informados {len(num)} valores.')
    print('     Eles são: ', end='')
    sleep(2)
    for c in num:
        print(c, end=' ')
        sleep(0.3)
        if c > maior:
            maior = c
    print('')
    print(f' O maior valor entre e o valor {maior}.')
    print('')


# programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

