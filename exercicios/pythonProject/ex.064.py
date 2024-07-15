#crie um programa que leia vários números inteiros pelo teclado inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#no final, mstre quantos números form digitados e qual foi a soma entre eles.
# (desconsiderando o flag(999))

print('')
print('=#=' * 17)
print('\tVamos fazer somar números que você passar?!')
print('=#=' * 17)
print('')
n = 0
c = 1
while True:
    if c == 1:
        n = int(input('\t\t\tDigite  um número: '))
        print('-' * 50)
        c += 1
    elif c != 0:
        print('')
        n1 = int(input(f'\tDigite o número que quer acrescentar.\n(se não quiser mais acrescentar digite 999): '))
        print('-' * 50)
        if n1 != 999:
            n = n + n1
            c += 1
            continue
        elif n1 == 999:
            break

print('')
print('=#=' * 17)
print(f'\t\tVocê digitou \33[32m{c-1}\33[m números!')
print(f'\t\t E a soma deles é: \33[33m{n}\33[m!')
print('=#=' * 17)
print('')

