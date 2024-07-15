#crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
#ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas gerada.

num = []
while True:
    print('-' * 30)
    num.append(int(input('Digite um número inteiro: ')))
    print('-' * 30)
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    while resp not in'S/N':
        if resp not in 'S' and 'N':
            print(f'Opção {resp} inválida... \n Tente novamente')
            print('-' * 30)
            resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
            print('-' * 30)
    if 'N' in resp:
        print('FINALIZANDO...')
        print('-' * 30)
        break
par = []
impar = []
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('=' * 60)
print(f'Você digitou {len(num)} números e eles são: {num}')
print(f'Os números PARES digitados foram: {par}')
print(f'Os números ÍMPARES digitados foram: {impar}')
print('=' * 60)
print('')
