#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$ 1000.
# Qual é o produto mais barato.

print('')
print('=' * 40)
print(f'{' ':10}LOJÃO DO BOM PREÇO')
print('=' * 40)
menorp = ''
total = mil = c = menor = 0
while True:
    print('-' * 40)
    produ = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o Preço do produto: R$ '))
    print('-' * 40)
    total += preco
    c += 1
    if preco > 1000:
        mil += 1
    if c == 1 or menor > preco:
        menor = preco
        menorp = produ
    para = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while para not in 'SN':
        print(f'Opção {para} inválida.')
        print('Tente novamente')
        print('-' * 40)
        para = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        print('-' * 40)
    if para == 'N':
        print(f'{' ':8}FIM DA COMPRA')
        print('')
        break
print(f'O total gasta na compra foi R${total:.2f}.')
print(f'Na compra {mil} custaram mais de R$ 1000.00')
print(f'E o produto mais barato foi o {menorp}, custando R${menor:.2f}.')
