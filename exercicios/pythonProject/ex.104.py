#crie um programa que tenha a função leiaInt(), que vai funcionar de  forma semelhante á
# função input() do python, só que fazendo a vlidaçãp para aceitar apenas um valor númerico.


def leiaInt(txt):
    txt = input('\tDigite um número: ')
    if not txt.isdigit():
        return '\33[31mErro, Digite um número inteiro valido\33[m'.center(40)
    elif txt.isdigit():
        return f'\33[32mVocê acabou de digitar o número {txt}.\33[m'.center(40)


print('-' * 40)
n = leiaInt('Digite um número: ')
print(n)
print('-' * 40)
