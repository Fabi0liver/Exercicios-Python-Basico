# Desenvolva um progama que leia seis números e soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

s = 0
print('-' * 38)
for i in range(40, 46):
    print('\t', i, end='')
    n = int(i % 2)
    if n == 0:
        s = s + i
print('')
print('-' * 38)
print(f'A soma somentos dos números pares acima é "{s}"')
print('')

soma = 0
cont = 0

print('\n')
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('')
print(f'A soma dos {cont} números pares acima é "{soma}".')


