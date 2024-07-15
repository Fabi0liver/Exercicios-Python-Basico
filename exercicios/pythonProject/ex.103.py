#Faça Um programa que tenha uma função chamada ficha(), que receba dois parâmentros opcionais:
#O Nome de um jogador e quantos gols ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.


def ficha(jog='<desconhecido>', gol=0):
    '''Retorna um mensagem com o nome
     e quantos gols o jogador fez'''
    return print(f'O jogador {jog} fez {gol} gol(s).'.center(40))


# programa principal
print('=' * 40)
print('FICHA DE JOGADOR'.center(40))
print('=' * 40)
print('')
jogador = str(input('\tNome do Jogador: ')).strip().capitalize()
if jogador == '':
    jogador = '<desconhecido>'

gols = str(input('  Quanto(s) gol(s) ele fez: '))
if (gols.isdigit()) == False:
    gols = '0'
    gols = int(gols)

print('')
print('=' * 40)
ficha(jogador, gols)
print('=' * 40)
