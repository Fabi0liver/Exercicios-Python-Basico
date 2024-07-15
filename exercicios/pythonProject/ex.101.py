#crie um programa que tenha uma função chamada voto() que vai receber com parâmetro
#o ano de nascimento de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto negado, opcional ou obrigatório na eleições.

def votar():
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if 16 <= idade < 18 or idade >= 70:
        return f'''\t  Sua idade é {idade}.
\tseu voto é OPCIONAL!'''

    elif idade < 16:
        return f'''\t\t Sua idade é {idade}.
Você ainda não tem idade para votar.
\t  Seu voto seria NEGADO!'''

    elif 18 <= idade < 69:
        return f'''\t\tSua idade é {idade}.
\tSeu Voto é OBRIGATÓRIO!'''


# programa principal
print('=' * 40)
print('Quer saber se você pode votar?'.center(40))
print('=' * 40)
print('-' * 40)
ano = int(input('Digite seu ano de nascimento: '.center(33)))
print('-' * 40)
print(votar())

