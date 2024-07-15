# Escreva um programa que leia um número inteiro qualquel e peça para o usuário escolher
#qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

from random import randint
from time import sleep


print('')
print('-' * 76)
print(' Vamos converter números decimais em números: Binário, Octal, Hexadecimal?')
print('-' * 76)
print('')
sleep(3)
print('Eu vou pensar em um número qualquer, e você vai me falar a base de conversão! OK?!')
print('')
sleep(2)
print('''         Se quiser "BINÁRIO" você digita o: "1" '
         Se quiser o "OCTAL" você digita o: "2"
         se quiser "HEXADECIMAL" vai ser o: "3" ''')
print('')
sleep(4)
print('         Tudo entendido?! ENTÃO VAMOS COMEÇAR!!!')
print('')
n = randint(0, 1000)
sleep(2)
print('PENSANDO...')
sleep(5)
print('')
print(f'         Já pensei!! Que Tal o número {n}!?')
print('')
sleep(2)

usu = int(input('Agora diga em qual sistema de numeração você quer converte-lo: '))
print('')
sleep(3)

if usu == 1:
    print('Você escolher converter o número em "BINÁRIO"? HUMM... Essa é dificil...')
    sleep(2)
    print('Deixa eu pensar...')
    sleep(4)
    print('')
    print(f'O número {n}, convertido em binário é: {bin(n)[2:]}!!')
    print('')
    sleep(2)
    print('Não precisa bater palma! Eu sei que sou o "CARA"!!')

elif usu == 2:
    print('Você escolheu converter o número em "OCTAL"? Jurava que iria escolher o binário.')
    sleep(2)
    print('Mas como ja escolheu esse... não faça barulho... deixa eu pensar aqui ...')
    sleep(4)
    print('')
    print(f'O número {n}, convertido em octal é: {oct(n)[2:]}!!')
    print('')
    sleep(2)
    print('Não fique de boca aberta ai! Mamãe sempre diz que sou bom em matematica!!')

elif usu == 3:
    print('Você escolheu converter o número em "HEXADECIMAL"? Com esse o hexa vem! kkkk')
    sleep(2)
    print('Vamos deixar de brincadeira! Hora de fazer conta ... Deixa pensar...')
    sleep(4)
    print('')
    print(f'O número {n}, convertido em hexadecimal é: {hex(n)[2:]}!!')
    print('')
    print('Ai tá o hexa! Não precisa mais esperar da seleção brasileira!!')

else:
    print(f'Você não entendeu o jogo né?! Olha lá encima as opções é de 1 a 3! O número {usu} não entra !!')
    sleep(2)
    print('É cada doido que me aparece em!!')

sleep(3)
print('')
print('-' * 76)
print('Se quiser, tente as outras opções!!!')
print('_' * 76)













