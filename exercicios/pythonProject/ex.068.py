#Faça um programa que jogue par ou ímpar com o computador. O jogador só será interrompido, quando o jogador Perder,
#mostrando o total de vítorias consecutivas que ele conquistou no final do jogo.

from random import randint

print('')
print('=' * 38)
print('\tVAMOS JOGAR PAR OU ÍMPAR?!')
print('=' * 38)
print('')
print(f'{' ':10}PREPARADO?! \n{' ':8}Então vamos lá!')
print('')
c = 0
while True:
    pc = randint(1, 10)
    jog = int(input(f'{' ':3}Diga um número de 1 a 10: '))
    p_i = str(input(' Você quer PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    while p_i not in 'PI':
        print('')
        print(f'  Não dá pra entender o seu "{p_i}". \n{' ':5}Ele é PAR ou ÌMPAR?!')
        print(f'{' ':6}Tente Novamente...')
        print('')
        p_i = str(input(' Você quer PAR OU IMPAR[P/I]: ')).strip().upper()[0]
    s = (jog + pc) % 2
    if p_i == 'P':
        if s == 0:
            print('\33[32m')
            print('*' * 36)
            print(f'\tVocê jogou {jog} e eu joguei {pc}. \n\t A soma da {jog + pc} que é "PAR"!')
            print('')
            print(f'{' ':8}VOCÊ GANHOU ESSA!!')
            print(f'{' ':5}Vamos jogar novamente...')
            print('*' * 36)
            print('\33[m')
            c += 1
        elif s != 0:
            print('\33[31m')
            print('#' * 36)
            print(f'\tVocê jogou {jog} e eu joguei {pc}. \n\tSoma da {jog + pc} que é "ÍMPAR"! ')
            print('')
            print(f'{' ':9}Você Perdeu essa !!')
            print(f'{' ':13}GAME OVER!')
            print('#' * 36)
            print('\33[m')
            break
    elif p_i == 'I':
        if s != 0:
            print('\33[32m')
            print('*' * 36)
            print(f'\tVocê jogou {jog} e eu joguei {pc}. \n\t A soma da {jog + pc} que é "Ímpar"!')
            print('')
            print(f'{' ':8}VOCÊ GANHOU ESSA!!')
            print(f'{' ':5}Vamos jogar novamente...')
            print('*' * 36)
            print('\33[m')
            c += 1
        elif s == 0:
            print('\33[31m')
            print('#' * 36)
            print(f'\t Você jogou {jog} eu joguei {pc}. \n\t A soma da {jog + pc} que é "PAR"!')
            print('')
            print(f'{' ':9} Você Perdeu essa!!')
            print(f'{' ':13}GAME OVER!')
            print('#' * 36)
            print('\33[m')
            break

print('')
if c == 0:
    print('Que Pena! Você não vendeu nenhuma vez.')
elif c == 1:
    print('Você venceu só uma vez! Poderia ser melhor!')
elif c > 1:
    print(f'Você venceu {c} vezes!! Parabéns!!')
print('')
print('=' * 38)
print('\t Foi legal jogar com você! \n\tTente Novamente se gostou!!')
print('=' * 38)
print('')

