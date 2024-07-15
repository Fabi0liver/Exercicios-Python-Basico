#crie um programa onde o usuário possa digitar vários valores numéricos e cadastre em uma lista.
#caso o número ja exista lá dentro, ele não será adiconado. No final, serão exibidos todos os valores
#digitas, e, ordem crescente.

num = list()
while True:
    print('>' * 35)
    n = int(input(f'{"Digite um número:":>24} '))
    print('>' * 35)
    if n not in num:
        num.append(n)
        print('-' * 35)
        print(f'Número {n} adicionado com sucesso...')
        print('-' * 35)
    else:
        print('-' * 35)
        print(f''' Número {n} já existe no castrado...
  não pode ser mas cadastrado...''')
        print('-' * 35)

    resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    print('-' * 35)
    while resp not in 'SN':
        if resp not in 'S' or 'N':
            print(f'\tResposta {resp} inválida... \n{' ':6}tente novamente.')
            print('-' * 35)
            resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
            print('-' * 35)
    if resp == 'N':
        print('<' * 35)
        print(f'{'FINALIZANDO...':^35}')
        print('<' * 35)
        break
print('')
print(f'Você digitou os números: {sorted(num)}')


