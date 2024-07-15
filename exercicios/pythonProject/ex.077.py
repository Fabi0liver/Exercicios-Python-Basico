#Crie um programa que tenha uma tupla com várias palavras(Não usar acentos). Depois disso
#você deve mostrar, para cada palavra, quais são as vogais.

palavras = ('lugar', 'apendice', 'sismo', 'multiply', 'locker',
        'realidade', 'galope', 'apartamento', 'dente', 'garantir')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print('')





