#refaça o desafio 051, lendo a primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
#da progressão usando a estrutura While.

print('')
print('\t\tVamos fazer um Progressão Aritmérica?')
print('')
print('   Você Vai falar o primeiro termo e a razão da P.A.')
print('E eu vou lher mostras os 10 primeiros termos dessa P.A!')
print('')
p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
print('')
print('OS 10 PRIMEIROS TERMOS DESTA P.A SÃO: ')
print('-' * 50)
print('')
termo = p
c = 1
while c <= 10:
    print(termo, end='->')
    termo += r
    c += 1
print('Acabou!')
print()
print('-' * 50)
print('')
print('Gostou? A pode matematica é bem legal!')
print('')

