#crie um programa que vai ler vários números e colocar em lista.
#Depois disso, mostre:
#Quantos números forma digitados
#A lista de valores rdenada de forma decrescente.
#se o valor 5 foi digitado e está ou não na lista.

num = []
while True:
    print('=' * 25)
    num.append(int(input('Digite um número: ')))
    print('=' * 25)
    resp = str(input(' Quer continuar?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        if resp not in 'S' or 'N':
            print('=' * 25)
            print(f'{' ':3}Opção {resp} inválida... \n{' ':4}Tente novamente.')
            print('=' * 25)
            resp = str(input(' Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('=' * 25)
        print(f'{'FINALIZANDO...':^25}')
        break

num1 = num
print('')
print('-' * 30)
print(f'Você digitou {len(num)} números.')
print(f'Os números digitados em ordem decrescente fica:{sorted(num, reverse=True)}')
if 5 in num:
    print(f'O número 5 foi digitado e está na posição {num.index(5)} da lista.')
else:
    print('O número 5 não foi encontrado na lista.')
print('-' * 30)
