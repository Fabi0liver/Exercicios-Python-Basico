
def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, p=0):
    return ((p / 100) * n) + n


def diminuir(n, p=0):
    return n - ((p / 100) * n)


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
