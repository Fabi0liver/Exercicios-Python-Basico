
'''c = 1
while c <= 10:
    print(c, end=' ')
    c += 1
print('fim')
print('')
print('-' * 40)'''

'''C = 1
while True:
    print(c, end='')
    C += 1 #desse jeito vai ficar rodando eternamente '''


num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
s = (num + num1)
c = 2
while True:
    if c >= 2:
        print('')
        r = str(input('Quer acrescentar mais um número S/N: ')).strip().upper()[0]
        if r == 'S':
            print('')
            num_ac = int(input('Digite o número: '))
            s += num_ac
            c += 1
        elif r == 'N':
            print('')
            print('Finalizando ...')
            break
        else:
            print('')
            print('Opção inválida... tente novamente.')
print('')
print(f'A soma de todos os {c} números é: {s}')
print('')









