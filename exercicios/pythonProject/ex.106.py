#Faça um mini_sistema que utilize o interactive Help da Pythom.O usuário vai digitar o comando
#e o manual vai aparecer.Quando o usuário digitar a palavra 'Fim' o programa se encerrará.
#Obs: use cores.

from time import sleep


def indicea(txt):
    n = len(txt)+8
    print(f'\033[1;30;43m{'~' * n}')
    print(f'{txt}'.center(n))
    print('~' * n)
    print('\33[m')


def indicep(txt):
    n = len(txt)+8
    print(f'\033[40m{'~' * n}')
    print(f'{txt}'.center(n))
    print('~' * n)


# Programa Principal
while True:
    indicea('SISTEMA DE AJUDA PYHELP')
    h = str(input('Função ou biblioteca: '))
    sleep(1)
    indicep(f'Acessando o manual do comando "{h}"')
    sleep(2)
    print('\33[7m')
    help(h)
    print('\033[m')
    sair = str(input('Quer sair do PYHELP:[S/N] ')).strip().capitalize()[0]
    while sair not in 'SN':
        if sair != 'SN':
            indicea(f'Opção {sair} inválida... tente novamente')
            sair = str(input('Quer sair do PYHELP:[S/N] ')).strip().capitalize()[0]
    if sair == 'S':
        sleep(1)
        indicep('ENCERRANDO PYHELP...')
        sleep(2)
        break
indicea('VOLTE SEMPRE!!')
