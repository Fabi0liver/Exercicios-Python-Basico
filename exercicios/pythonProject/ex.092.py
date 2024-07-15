#crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
#em um dicionário receberá tmabém o ano de contratação e o salário.CAlcuçe e acrescente, além da idade,
#com quantos anos a pessoa vai se aposentar.

from datetime import date
atual = date.today().year

cadastro = dict()

print('')
print('Informações para Cadastro:')
print('=' * 45)
cadastro['Nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = atual - nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho [0 para se não tem]: '))

if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    t_trabalho = (cadastro['Contratação'] - nascimento) + 35
    cadastro['Aposentadoria'] = t_trabalho

print('=' * 45)
for k, v in cadastro.items():
    print(f'{k} tem valor {v}')
