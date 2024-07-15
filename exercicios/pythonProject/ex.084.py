#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#No final mostre:
#quantas pessoas foram cadastradas.
#Uma listagem com as pessoas mais pesadas.
#Uma listagem com as pessoas mais leves.

print('')
print('=' * 30)
print(f'{'CADASTRO ACADEMIA':^30}')
print('=' * 30)
print('')
print('\tDigite as informações:')
print('-' * 30)

cadastro = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    print('-' * 30)
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            if dados[1] < menor:
                menor = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    print('-' * 30)
    while resp not in 'SN':
        if resp != 'S' or 'N':
            print(f'\tOpção {resp} inválida...\n\t Tente Novamente.')
            print('-' * 30)
            resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
            print('-' * 30)
    if resp == 'N':
        print(f'{'FINALIZANDO CADASTRO...':^30}')
        print('-' * 30)
        break

print('=' * 65)
print('Dados do Cadastro:')
print(f'um total de {len(cadastro)} pessoas foram cadastradas.')
print(f'As pessoas mais pesadas tem {maior}Kg, e elas são: ', end='')
for c in cadastro:
    if c[1] == maior:
        print(f'{c[0]}', end='')
print('')
print(f'E as pessoas mais leves tem {menor}kg, e elas são: ', end=' ')
for c in cadastro:
    if c[1] == menor:
        print(f'{c[0]}', end=' ')
print('')
print('=' * 65)

