#Crie um programa que gerencie o aproveitamento de um jogador e quantas partidas ele jogou.
#Depois Vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado e, um
#dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

print('')
print('-' * 40)
print(f'{'Gerenciamento do jogador:':^40}')
print('-' * 40)
print('')

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador['nome']} fez esse ano: '))

print('')
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols ele fez na {c}ª partida? ')))

print('')
print('-' * 40)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-' * 48)
print(jogador)
print('-' * 48)

print('-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 40)

print('-' * 35)
print(f'O jogador {jogador['nome']}, fez {partidas} partidas.')
print('')
for c in range(0, partidas):
    print(f'{f'=> na partida {c+1}, fez {jogador['gols'][c]} gols.':^35}')
print('')
print(f'Esse ano ele um total de {jogador['total']} gols.')
print('-' * 35)
