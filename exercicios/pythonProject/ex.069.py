#Crie um program que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
#programa deverá perguntar se o usiário quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres te, menos de 20.

print('-' * 40)
print('\tCADASTRO PESSOAL:')

c = p18 = h = m20 = 0

while True:
    print('-' * 40)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('-' * 40)
        print(f'Informação {sexo} é inválida.')
        print('\tTente novamente')
        print('-' * 40)
        sexo = str(input('Digite o sexo [M/F]:')).strip().upper()[0]

    if idade >= 18:
        p18 += 1
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        m20 += 1
    c += 1
    print('-' * 40)
    cont = str(input('Quer continuar o cadastro [S/N]: ')).strip().upper()[0]
    while cont not in 'S/N':
        print('-' * 40)
        print(f'Opção {cont} é inválida.')
        print('\tTente novamente')
        print('-' * 40)
        cont = str(input('Quer continuar o cadastro [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        print('-' * 40)
        print('FIM DO CADASTRO')
        break

print('')
print(f'O dados das {c} pessoas cadastradas:')
print('')
print(f'''As que tem mais de 18 são: {p18}
Os Homens cadastrados são: {h}
E as mulheres com menos de 20 são: {m20} ''')
