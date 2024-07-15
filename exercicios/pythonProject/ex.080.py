#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista,
#já na posição correta de inserção(sem usar o sort().
#No final, mostre a lista ordenada na tela.

num = list()
maior = 0
menor = 99999
for _ in range(0, 5):
    n = int(input('Digite um número: '))
    if n >= maior:
        maior = n
        num.append(n)
        print(f'O número {n} foi adicionado ao final da lista.')
    elif n <= menor:
        menor = n
        num.insert(0, n)
        print(f'O número {n} foi adicionado a posição 0 da lista.')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.isert(pos, n)
                print(f'O número {n} foi adicionado a posição 1 da lista.')

                break


print('')
print(f'Os valores digitados foram: {num}')








