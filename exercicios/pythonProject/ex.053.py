#Crie um programa que lea uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.

'''print('')
print('Vamos descobrir se uma frase é Palíndromo?')
print('')
print('Você vai falar uma frase, e eu digo se é ou não um Palíndromo!')
print('')
frase = str(input('Digite uma frase:')).strip().lower()
frase = frase.replace(' ', '')
n = len(frase)
l = n - 1
for i in range(n):
    if frase[i] != frase[l]:
        break
    l = l - 1

print('')
if l == -1:
    print('Verdade!! A frase é um Palíndromo!')
else:
    print('Falso!! A frase não é um Palíndromo!')'''

print('')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
#for letra in range(len(junto) - 1, -1, -1):
#    inverso = inverso + junto[letra]
print('')
print(f'O contrario de {junto}, é {inverso}!')
if inverso == junto:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo!')



