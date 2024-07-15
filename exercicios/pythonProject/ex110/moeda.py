
def metade(n, f=False):
    n = n / 2
    if f is True:
        return f'R${n:.2f}'
    return n


def dobro(n, f=False):
    n = n * 2
    if f is True:
        return f'R${n:.2f}'
    return n


def aumentar(n, p=0, f=False):
    n = ((p / 100) * n) + n
    if f is True:
        return f'R${n:.2f}'
    return n


def diminuir(n, p=0, f=False):
    n = n - ((p / 100) * n)
    if f is True:
        return f'R${n:.2f}'
    return n


def moeda(txt):
    return f'R${txt:.2f}'


def resumo(n, a, d):
    print('-' * 32)
    print('RESUMO DO VALOR'.center(32))
    print('-' * 32)
    print('\033[33m-' * 32)
    print(f' Preço analisado:    R${n:.2f}')
    print(f' Dobro do Preço:     R${n * 2:.2f}')
    print(f' Metade do Preço:    R${n / 2:.2f}')
    print(f' {a}% de Aumento:     R${n + ((a / 100) * n):.2f}')
    print(f' {d}% de Redução:     R${n - ((d / 100) * n):.2f}')
    print('-' * 32)
    print('\033[m')


