def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {factorial(n)}') # O fatorial de 5 é 120

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Os factoriais são: {f1}, {f2} e {f3}') # Os factoriais são: 120, 24 e 1


def par(num=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número:'))
if par(num):
    print(f'O número {num}, é par!') # O número 8, é par!
else:
    print(f'O número {num}, é ímpar!') # O número 5, é ímpar!

