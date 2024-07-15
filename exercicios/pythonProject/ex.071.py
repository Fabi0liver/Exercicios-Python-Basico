#crie um programa que simule o funcionamento de um caixa eletrônica.
#No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e eo programa vai
#vai informar quantas cédulas de cada valor serão entregues.
#obs: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1.

print('')
print('$' * 30)
print(f'{' ':8}BANCO PYTHON')
print('$' * 30)
print('')
valor = int(input('Qual o valor a ser sacado: R$ '))
print('-' * 30)
total = valor
cedulas = 50
totcedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totcedulas += 1
    else:
        if totcedulas > 0:
            print(f'O total é {totcedulas}  cédulas de R${cedulas}.')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 1
        totcedulas = 0
        if total == 0:
            break

print('-' * 30)
print('')
print('\tFIM DA OPERAÇÃO')
print('Obrigada pela prefêrencia')





