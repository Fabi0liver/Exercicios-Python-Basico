# Crie um programa que leia Vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('')
print('*' * 50)
print('\tVamos Brincar um pouco com matématica?!')
print('*' * 50)
print('')
print('''\tVocê vai dizer quantos valores quiser.
 E eu vou lhe passa algums dados sobre eles!!''')
print('')
print('\t  Conbinado?! Então vamos começar!!')
print('')
c = 1
l_n = []
while True:
    if c <= 1:
        n = int(input('\tDigite um número: '))
        l_n.append(n)
        c += 1
    elif c > 1:
        print('-' * 40)
        r = str(input('Você quer acrescentar outro número?(S/N):')).strip().upper()[0]
        if r == 'S':
            print('-' * 40)
            n1 = int(input('\tDigite o número: '))
            l_n.append(n1)
            c += 1
        elif r == 'N':
            print('-' * 40)
            break
        else:
            print('-' * 40)
            print('/' * 40)
            print('\tOpção inválida! Tente novamente!')
            print('/' * 40)



print('')
print('Os dados sobre estes números são: ')
print('=' * 30)
print(f'Você digitou {c - 1} números')
print(f'A soma de todos eles é : {sum(l_n)}')
print(f'E a média destes números é: {sum(l_n) / (c - 1):.1f}')
print(f'O maior número entre eles é {max(l_n)}')
print(f'E o menor número é o {min(l_n)}')
print('=' * 30)
print('')











