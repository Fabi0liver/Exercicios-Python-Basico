#crie um programa que leia o nome de uma pessoa e diga se ela tem " Silva" no nome.

nome = str(input('Digite um nome completo: ')).strip()
print('')
print('seu nome tem Silva? {} '.format('silva' in nome.lower()))


