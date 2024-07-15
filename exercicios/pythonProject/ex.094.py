#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
#pessoa em uma dicionário e todos os dicionários em uma lista. no final, mostre:
#Quantas pessoas foram cadastradas.
#A média de idade do grupo.
#Uma lista com todas as mulheres.
#uma lista com todas as pessoas com idade acima da média.

pessoa = dict()
pessoas = list()
total = 0

print('')
print('=' * 40)
print(f'{'CADASTRO DE PESSOAS':^40}')
print('=' * 40)
print('')

while True:
    print('-' * 40)
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['Sexo'] = str(input('Sexo[M/F]: ')).strip().capitalize()[0]
    while pessoa['Sexo'] not in 'MF':
        if pessoa['Sexo'] not in 'M' or 'F':
            print('-' * 40)
            print(f'Opção {pessoa['Sexo']} inválida...Digite apenas M ou F')
            print('-' * 40)
            pessoa['Sexo'] = str(input('Sexo[M/F]: ')).strip().capitalize()[0]
        elif pessoa['Sexo'] == 'M' or 'F':
            break
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa['idade']
    pessoas.append(pessoa.copy())
    print('-' * 40)

    print('=' * 40)
    R = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    print('=' * 40)
    while R not in 'SN':
        if R not in 'S' or 'N':
            print('Opção inválida... Tente Novamente.')
            print('=' * 40)
            R = str(input('Quer continuar?[S/N]')).strip().upper()[0]
            print('=' * 40)
    if R == 'N':
        break

print('-' * 55)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade das pessoas cadastrada é: {total/len(pessoas):.2f} anos.')
print('As mulheres cadastradas forma: ', end='')
for pessoa in pessoas:
    for v in pessoa.values():
        if v == 'F':
            print(pessoa['nome'], end=' ')
print('')
print('A pessoas que estão acima da média de idade:')
for pessoa in pessoas:
    for k, v in pessoa.items():
        if pessoa['idade'] > (total / len(pessoas)):
            print(f'{k} = {v}', end=', ')
    print('')
print('')
print('-' * 55)














