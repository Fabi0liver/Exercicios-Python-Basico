#crie um programa que crie uma matriz de dimentções 3x3 e preencha com valores lidos pelo
#teclado.
#  0[ ] [ ] [ ]
#  1[ ] [ ] [ ]
#  2[ ] [ ] [ ]
#    0   1   2
# No final, mostre a matriz na tela, com a formação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a matriz na posição[{linha}, {coluna}]: '))
print('=' * 50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')







#print('=' * 30)
#print(f'{ma[0][0]}{ma[0][1]}{ma[0][2]}')
#print(f'{ma[1][0]}{ma[1][1]}{ma[1][2]}')
#print(f'{ma[2][0]}{ma[2][1]}{ma[2][2]}')
