#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disse que quer mostrar 0 termos.

print('')
print('=' * 50)
print('\tVamos fazer uma progressão aritmética?')
print('=' * 50)
print('')
print('Você vai me falar o primeiro termo e razão da P.A.')
print('\tE eu vou lhe dizer os termos delas. OK?!')
print('')
p = int(input('Diga o primeiro termo: '))
r = int(input('Agora me diga a razão da P.A: '))
print('')
termo = p
c = 1
t = 0
ac = 10
while ac != 0:
    t = t + ac
    while c <= t:
        print(termo, end='-> ')
        termo += r
        c += 1
    print('Pausa')
    print('')
    ac = int(input('Quantos termos você quer acrescentar: '))

print('')
print(f'Mostrei o total de {t} termos de P.A!')







