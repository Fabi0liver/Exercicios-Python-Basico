#Crie um programa que leia dois valores e mostre um menu na tela :
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
m = 0
while m != 5:
    print('')
    print('''\tOPÇÕES DE OPERAÇÃO:
     [1] SOMAR
     [2] MULTIPLICAR
     [3] MAIOR
     [4] NOVOS NÚMEROS
     [5] SAIR DA OPERAÇÃO''')
    print('')
    m = str(input('Digite a opção: ')).strip()
    if m == '1':
        print('')
        print(f'A soma {n1} e {n2} é: {n1 + n2}')
    elif m == '2':
        print('')
        print(f'A multiplicação de {n1} e {n2} é: {n1 * n2}')
    elif m == '3':
        if n1 > n2:
            print('')
            print(f'O valor {n1} é maior que o valor {n2}.')
        else:
            print('')
            print(f'O valor "{n2}" é maior que o valor "{n1}".')
    elif m == '4':
        print('')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif m == '5':
        print('')
        print('Finalizando operação ...')
        sleep(2)
        break
    else:
        print('')
        print('OPÇÃO DE OPERAÇÃO INVALIDA!')

print('')
print('FIM DA OPERAÇÃO!')
print('-' * 40)
print('')





