#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250,00 , calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%


s = float(input('Digite o seu salário: '))
a1 = (s + (15 / 100) * s)
a2 = (s + (10 / 100) * s)
if s <= 1250.00:
    print(f'O seu salario é R${s:.2f}. Com aumento de 15% ficou R${a1:.2f}.')
else:
    print(f'O seu salario é R${s:.2f}. Com aumento de 10% ficou R${a2:.2f}.')



