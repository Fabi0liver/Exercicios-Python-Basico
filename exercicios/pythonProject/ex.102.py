#crie um programa que  função fatorial() que receba doius parâmetros:
# o primeiro que indique  o número a calcular
# outro chmado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.


def fatorial(num=1, show=False):
    from math import factorial
    '''Função para saber a fatorial de um valor.
       num = Valor para saber o fatorial
       show = (opcional)
               (True) para ver a operação
              (False) para não ver a operação.
       return = retorna o valor '''

    f = factorial(num)
    if show == True:
        while num > 0:
            print(f'{num}', end='')
            print(' x ' if num > 1 else ' = ', end='')
            num -= 1
    return print(f)


# programa principal

print(f'{'~' * 30}'.center(50))
print('CALCULANDO FATORIAL'.center(50))
print(f'{'~' * 30}'.center(50))
print('-' * 50)
n = int(input('Digite um número para saber seu fatorial: '.center(45)))
print('-' * 50)
fatorial(n, True)


