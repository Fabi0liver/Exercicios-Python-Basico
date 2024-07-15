#Faça um programa que leia um número inteiro é diga se ele é ou não um número primo.

print('')
print('Você quer saber se um número é primo?!')
num = int(input('\tDigite aqui o número: '))
tot = 0
print('')
for c in range(1, num+1):
   if num % c == 0:
      print('\33[32m', end=' ')
      tot += 1
   else:
      print('\33[m', end=' ')
   print(c, end=' ')
print('')
print('')
print(f'\33[mO número {num}, foi divisível em {tot} vezes.')
if tot == 2:
   print('Por isso ele é um número primo!')
else:
   print('Por isso ele não é um número Primo.')




print('\n')
n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
   if num % c == 0:
      t = t + 1

if t == 2:
   print('Esse número é Primo.')
else:
   print('Esse número não é Primo.')



