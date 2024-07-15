#crie uma programa que tenha uma tupla única com nomes de produtos e seus respsctivos na sequência.
#no final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Computador', 4500, 'Teclado', 120, 'Mouse', 100, 'Monitor', 750, 'Fone', 74,
            'hd', 450, 'Placa de vídeo', 1600, 'Processador', 1358, 'Placa Mãe', 580)

print('')
print('=' * 44)
print(f'{'TABELA DE PREÇOS':^42}')
print('=' * 44)
print('')
print('-' * 44)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<33}', end='')
    else:
        print(f'R$ {produtos[posicao]:>7.2f}')
print('-' * 44)
















