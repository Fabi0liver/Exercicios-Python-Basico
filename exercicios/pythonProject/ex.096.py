# faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno
#retangular (largura e comprimento) e mostre a aréa do terreno) e área do terreno.

def inicio(txt):
    cont = len(txt) + 4
    print('-' * cont)
    print(txt)
    print('-' * cont)


def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} é de {a}m².')


# progrma principal

inicio('   Calculo de área de terreno')
print('')
l = float(input('Largura do terreno(m): '))
c = float(input('Comprimento do terreno(m): '))
print('')
print('-' * 47)
area(l, c)
print('-' * 47)




