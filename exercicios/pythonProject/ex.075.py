#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre:
#Quantos vezes apareceu o valor 9.
#em que posição foi digitado o  primeiro valor 3.
#Quantos números pares.


print('')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
print('')
n = (n1, n2, n3, n4)

print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 <= 0:
        print(num, end=' ')
print('\n')



