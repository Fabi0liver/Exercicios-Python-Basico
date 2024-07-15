#crie um programa que leia o ano de sete pessoas. No final mostre quantas pessoas ainda não
#atingiram a maioridade e quantas já são maiores.

import datetime

ano = datetime.date.today().year

'''print('')
print('Vamos saber quem atingiu a maior idade?')
print('')
maior = []
n1 = 0
menor = []
n2 = 0
for i in range(1, 8):
    print('-' * 35)
    nome = str(input(f'Digite o nome {i}º da pessoa: ')).capitalize().strip()
    nasc = int(input('Digite o ano de nascimento: '))
    print('-' * 35)
    idade = ano - nasc
    info = (f'{nome}: Com {idade} anos')
    if idade >= 21:
        maior.append(info)
        n1 += 1
    elif idade < 21:
        menor.append(info)
        n2 += 1

maior = ', '.join(maior)
menor = ', '.join(menor)

print('')
print(f'Destas pessoas {n1} são as que já estão na maioridade são:')
print(maior)
print('')
print(f'E {n2} são as que não atigiram a maioridade são:')
print(menor)
print('')'''


print('\n')
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Qual é o ano de nascimento da {c}º pessoa: '))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('')
print('-' * 40)
print(f'Destas 7 pessoas, {totmaior} estão na Maioridade!')
print(f'\tE {totmenor} está na Menoridade!')
print('-' * 40)
print('')


