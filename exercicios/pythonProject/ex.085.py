#crie um programa onde o usuário possa digitar sete valores numéricos e cadstre-os em uma lista única
#que mantenha separados os valores pares e impares.No final, mostre os valores pares e impares em ordem
#crescente.

num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('=' * 50)
print(f'Os valores digitados são: {num}')
print(f'Os valores Pares digitados foram:{sorted(num[0])}')
print(f'Os números Ímpares digitados foram:{sorted(num[1])}')





