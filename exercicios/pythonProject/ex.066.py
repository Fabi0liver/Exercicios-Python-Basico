# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando  o
#usuário dogitar o valor 999, que é a condição de parada. No final mostre quantos números foram
#digitados e qual a soma entre eles (desconsiderando a flag).
print('')

c = s = 0
while True:
    n = int(input('Digite um número ( se quiser parar digite 999): '))
    print('')
    if n == 999:
        print('finalizando...')
        break
    c += 1
    s += n
print('')
print(f'Você digitou {c} números, e a soma de todos ele é {s}!')


