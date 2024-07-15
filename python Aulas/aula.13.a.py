for i in range(0, 6):
    print('OI')
print('Fim')

print('-' *40)

for i in range(0, 6):
    print('OI')
    print('Fim')
# Tudo que estiver na dentação do "for" vai repetir o número de vezes pedidadas.

print('-' * 40)

for i in range(0, 6):
    print(i)
print('Fim')
# Usado para númeração

print('-' * 40)

for i in range(6, 0):
    print(i)
print('Fim')
# forma errada de pedir númeração de trás pra frente.

print('-' * 40)

for i in range(6, 0, -1):
    print(i)
print('Fim')
# forma certa de pedir númeração de trás pra frente.

print('-' * 40)

for i in range(0, 7, 2):
    print(i)
print('Fim')
# mostras os números depidos, pulado em 2 em 2 números.

print('-' * 40)

n = int(input('Digite um número: '))
for i in range(0, n+1):
    print(i)
print('Fim')

print('-' * 40)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

print('-' * 40)

for i in range(0,3):
    n = int(input('Digite Um número: '))
print('Fim')

print('-' * 40)

s = 0
for i in range(0 ,4):
    n = int(input('Digite um número: '))
    s = s + n
print(f'A soma de todos os valores foi {s}.')
print('Fim')















