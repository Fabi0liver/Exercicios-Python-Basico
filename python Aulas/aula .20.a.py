def linha():
    print('-' * 30)


# Programa principal
linha()                       # ------------------------------
print(f'{'Olá Mundo!':^30}')  #          Olá Mundo!
linha()                       # ------------------------------
linha()                       # ------------------------------
linha()                       # ------------------------------

print('\n')


def mensg(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


# Programa principal
mensg('OLÁ MUNDO!') # ------------------------------
                    #          OLÁ MUNDO!
                    # ------------------------------

print('\n')



def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'Soma de A + b = {s}')


# Programa principal
soma(17, 5) # A = 17 e B = 5
                 # Soma de A + b = 22

print('\n')


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='=> ')
    print('FIM!')


# programa principal
contador(2, 1, 7) # 2 => 1 => 7 => FIM!

contador(8, 0) # 8 => 0 => FIM!

contador(4, 4, 7, 6, 2) # 4 => 4 => 7 => 6 => 2 => FIM!


def cont(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


# Program principal
cont(1, 2, 3, 4) # Recebi os valores (1, 2, 3, 4) e são os todo 4 números!

print('\n')


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os Valores {valores} temos {s}')


# programa principal

soma(5, 2) # Somando os Valores (5, 2) temos 7
soma(2, 9, 4) # Somando os Valores (2, 9, 4) temos 15


print('\n')
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [3, 6 , 9, 12, 15]
dobra(valores)
print(valores) # [6, 12, 18, 24, 30]









