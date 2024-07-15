#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte,
#seu programa deverá ler um número pelo teclado(entre e 20) e msotrá-lo por extenso.

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
  'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('')
while True:
    print('=' * 41)
    n = int(input('\tDigite um número(entre 0 e 20): '))
    print('=' * 41)
    while n < 0 or n > 20:
        print(f'  Número {n} inválido...Tente novamente.')
        print('=' * 41)
        n = int(input('\tDigite um número(entre 0 e 20): '))
        print('=' * 41)
    print('-' * 41)
    print(f'{' ' * 5}Você digitou o número {num[n]}.')
    print('-' * 40)
    print('=' * 41)
    cont = str(input('Você quer continuar:[S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        print('=' * 41)
        print(f'Opção {cont} inválida...Tente novamente.')
        print('=' * 41)
        cont = str(input('Você quer continuar:[S/N] ')).strip().upper()[0]
    if cont == 'N':
        print('=' * 41)
        break
print('')
print(f'{'':^8}FIM DA OPERAÇÃO')
print('')




