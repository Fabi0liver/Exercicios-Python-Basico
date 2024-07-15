
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

