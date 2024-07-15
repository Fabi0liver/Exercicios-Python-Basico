#Aprimore o desafio 093 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
gols = []

print('')
print('-' * 40)
print(f'{'Gerenciamento do jogador:':^40}')
print('-' * 40)
print('')

while True:
    print('-' * 40)
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partida = int(input(f'Quantas partidas {jogador['Nome']} jogou: '))
    print('')
    for c in range(1, partida + 1):
        gols.append(int(input(f'Quantos gols na {c}ª partida: ')))
    print('-' * 40)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    print('-' * 40)

    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    print('-' * 40)
    while r not in 'SN':
        if r != 'S' or 'N':
            print('Opção inválida... Tente Novamente.')
            print('-' * 40)
            r = str(input('Quer continuar?[S/N]')).strip().upper()[0]
            print('-' * 40)
    if r == 'N':
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('')
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')

while True:
    print('-' * 40)
    busca = int(input('Mostrar qual jogador: 999 para parar) '))
    print('-' * 40)
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Opção inválida... Não existe jogador com cod.{busca}')
    else:
        print('-' * 40)
        print(f'Informação do jogador {jogadores[busca]['Nome']}:')
        print('')
        for i, g in enumerate(jogadores[busca]['Gols']):
            print(f' no jogo {i + 1} fez {g} gols.')
        print('-' * 40)














