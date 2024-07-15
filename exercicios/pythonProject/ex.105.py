#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - a média da turma
# - a situação(opcional)
#Adicione tanbém as docstrings da função.


def notas(*num, sit=False):
    '''Função receberá notas de alunos e retornará:
    * Quantidade de notas passadas
    * A maior notas passada
    * A menor nota passada
    * A média da notas passadas
    * A situação da média (Opcional)
      (True) aparecera a situação
      (False) Não aparecera s situação'''
    classe = dict()
    classe['Quantidade'] = len(num)
    classe['maior_nota'] = max(num)
    classe['menor_nota'] = min(num)
    classe['média'] = sum(num) / len(num)
    if sit is True:
        if classe['média'] >= 7.0:
            classe['situação'] = 'BOA'
        elif 5.0 <= classe['média'] < 7.0:
            classe['situação'] = 'RAZOAVEL'
        elif classe['média'] < 5.0:
            classe['situação'] = 'RUIM'
    return classe


# programa principal

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
