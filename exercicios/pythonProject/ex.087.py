#Aprimore o desafio anterior, mostrando no final:
#A soma de todos os valores pares digitados.
#A soma dos valores da terceira coluna.
#O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma_ter = 0

print('')
print('=' * 55)
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite uma valor para a matriz na posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        if matriz[linha][2] >= 0:
            soma_ter += matriz[linha][2]
print('=' * 55)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')
print('=' * 55)
print('')
print('-' * 55)
print(f'A soma de todos os valores  pares digitados é: {par}')
print(f'A soma dos valores digitados da terceira coluna é: {soma_ter}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print('-' * 55)
