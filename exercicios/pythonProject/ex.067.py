# Faça um programa que mostre a tabuada de vários números , um de cada valor digitado pelo usuário.
#o programa será interrompido quando a número solicido for negativo.

print('')
print('=' * 40)
print(f'{' ':8}Vamos fazer tabuada?!')
print('=' * 40)
print('')
print('\t Você vai me dizer um número. \n\tE vou ti passar a tabuada dele.')
print('')
print(' ENTENDEU?!... OK!... Então vamos lá!')

while True:
    print('')
    n = int(input('Digite o número que quer saber a tabuada\n  (ou um número negativo para parar): '))
    if n < 1:
        print('')
        print(f'{' ' * 10}Finalizando...')
        break
    print('')
    print(f'{'':8}A tabuada de {n} é:')
    print('')
    print('', '-' * 30)
    for c in range(0, 11):
        print(f'{'':10} {n} X {c:2} = {n * c}')
    print(' ', '-' * 30)



print('')
print('Assim é fácil saber tabuada né?!! kkkk')
print('\tTente outras vezes, quando quiser.')
