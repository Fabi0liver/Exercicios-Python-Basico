# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação.Depois mostre:
# apenas os 5 primeiros colocados.
#Os últimos 4 colocados da tabela.
#Uma lsiata com os time em ordem alfabética.
#Em que posiçãona tabela está o time da Chapecoense.




times = ('Flamengo', 'Bahia', 'Botafogo', 'Palmeiras', 'Cruzeiro', 'Athletico-PR', 'São Paulo',
         'Bragantino', 'Internacional', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Criciúma',
    'Cuibá', 'Vitória', 'Vasco da Gama', 'Atlético Goianiense', 'Corinthias', 'Grêmio', 'Fluminense')

print('')
print('=' * 40)
print('\tTABELA DO BRASILEIRO DE 2024')
print('=' * 40)
print('')
for time in range(0, len(times)):
    print(f'\t* {time + 1:2}º {times[time]} ')
print('')
print('-' * 40)
print(f'Os 5 primeiros na classificação são: {times[:5]}.')
print('')
print(f'Os 4 últimos na classificação são: {times[-4:]}.')
print('')
print(f'''E os times organizados em ordem alfabética ficam:
{sorted(times)}''')
print('')
print(f'O Cuibá está {times.index('Cuibá')+1}º posição.')
print('')



