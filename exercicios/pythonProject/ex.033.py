#faça um programa que leia três números e mostre qual o maior e qual o menos .

num1 = int(input('Digite o primeiro números : '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor =num3

maior = num2
if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num2 and num3 > num1:
    maior = num3

print(f'O número maior e {maior}.')
print(f'O número menor é {menor}.')


