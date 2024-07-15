#crie Um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#no final, mostre um boletim contendo a média de cada um e permita que o usúário possa mostrar
#as notas de cada aluno individualmente.

print('')
print('-' * 40)
print(f'{'CADASTRO: ALUNOS NOTAS/MÉDIAS':^38}')
print('-' * 40)


alunos = []

while True:
    nomes = input('Aluno: ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nomes, [nota1, nota2], media])
    print('-' * 40)
    resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    print('-' * 40)
    while resp not in 'SN':
        if resp != 'S' or 'N':
            print(f'Opção {resp} inválida... Tente Novamente.')
            print('-' * 40)
            resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
            print('-' * 40)
    if resp in 'N':
        print('')
        print(f'{'CALCULANDO MÉDIA...':^40}')
        print('')
        break
print('-' * 40)
print(f'{'Nª':<4}{'NOME':<10}{'MÈDIA': >8}')
print('-' * 40)
for c in range(0, len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][2]:>8.1f}')

print('-' * 40)
while True:
    n = int(input('Notas de qual aluno [999 para terminar]]: '))
    if n <= len(alunos)-1:
        print(f'As notas de {alunos[n][0]} são {alunos[n][1]}')
        print('-' * 40)
    if n == 999:
        print('-' * 40)
        print('')
        print(f'{'FIM DO CADASTRO!':^40}')
        break

print('')



