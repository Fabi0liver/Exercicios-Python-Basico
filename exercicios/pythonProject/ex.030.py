#Crie um programa que leia um número inteiro e mostre na pela se ele é Par ou ímpar.

num = int(input('Digite um nùmero inteiro: '))
if num % 2 == 0:
    print(f'Você digitou o número {num}! E ele é um número "Par"!')
else:
    print(f'Você digitou o número {num}! E ele é um número "Ímpar"!')
