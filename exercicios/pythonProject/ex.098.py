#faça um programa que tenha uma função chamada cntador(), que receba três parâmetros:
#inicio, fim e passo e realize a contagem.
#seu programa tem que ralizar três contagem atraves da funções criadas:

#A)De 1 até 10, de 1 em 1
#B) De 10 até 0, de 2 em 2
#C)Uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}:'.center(35))
    sleep(2)
    if i < f:
        print(' ' * 5, end='')
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    elif i > f:
        print(' ' * 5, end='')
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')


# programa principal

print('=' * 35)
contador(1, 10, 1)
print('=' * 35)
contador(10, 0, 2)
print('=' * 35)
print('=' * 45)
print('Agora é sua vez de personalizar a contagem!'.center(45))
print('=' * 45)

print('')
i = int(input('\tNúmero onde começa: '))
f = int(input('\tNúmero onde termina: '))
p = int(input('''\tDe quanto em quanto 
   o número vai ser contado: '''))
print('')

print('=' * 35)
contador(i, f, p)
print('=' * 35)









