#  Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

s = 0
cont= 0
for i in range(3, 501, 6):
    cont += 1
    s += i
print('')
print(f'A soma de todos os {cont} números ímpares e que são múltiplos de três é: {s}!')


