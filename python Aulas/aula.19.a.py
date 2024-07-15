
dados = {'nome': 'Pedro', 'idade': '25'}
print(dados) # {'nome': 'Pedro', 'idade': '25'}
print('')

print(dados['nome']) # Pedro
print(dados['idade']) # 25
print('')

dados['sexo'] = 'Masculino' # acrecenta dados ao fim do dicionario
print(dados) # {'nome': 'Pedro', 'idade': '25', 'sexo': 'Masculino'}
print('')

del dados['idade'] # elimina a chave e  o valor do dicionario.
print(dados) # {'nome': 'Pedro', 'sexo': 'Masculino'}

print('\n')

filme = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}

print(filme) # {'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'}
print('')
print(filme.values()) # dict_values(['Star Wars', 1997, 'George Lucas'])

print(filme.keys()) # dict_keys(['titulo', 'ano', 'diretor'])

print(filme.items()) #dict_items([('titulo', 'Star Wars'), ('ano', 1997), ('diretor', 'George Lucas')])
print('')

for k, v in filme.items():
    print(f'O {k} é {v}.') #O titulo é Star Wars.
                           #O ano é 1997.
                           #O diretor é George Lucas.
print('\n')

locadora = [{'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(locadora) #[{'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'},
                # {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
                # {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(locadora[1]) # {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
print(locadora[1]['ano']) # 2012
print(locadora[2]['titulo']) # Matrix

print('\n')


pessoa = {'nome': 'Fábio', 'sexo': 'M', 'idade': 33}

print(pessoa) # {'nome': 'Fábio', 'sexo': 'M', 'idade': 33}

print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.') # O Fábio tem 33 anos.

for k in pessoa.keys():
    print(k) # nome
             # sexo
             # idade

for v in pessoa.values():
    print(v) # Fábio
             # M
             # 33

for k, v in pessoa.items():
    print(f'{k} = {v}') # nome = Fábio
                        # sexo = M
                        # idade = 33

pessoa['nome'] = 'Flávio'
pessoa['idade'] = 25
print(pessoa) #{'nome': 'Flávio', 'sexo': 'M', 'idade': 25}

pessoa['peso'] = 75.6
print(pessoa) # {'nome': 'Flávio', 'sexo': 'M', 'idade': 25, 'peso': 75.6}


del pessoa['sexo']
print(pessoa) # {'nome': 'Flávio', 'idade': 25, 'peso': 75.6}
print('\n')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[1]) # {'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[1]['uf']) # São Paulo
print('\n')

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Digite a Unidade Federativa: '))
    estado['sigla'] = str(input('Digite o sigla da Unidade Federativa: '))
    brasil.append(estado.copy())

print('')
print(brasil) #[{'uf': 'Bahia', 'sigla': 'Ba'}, {'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}]

print('')
for estado in brasil:
    print(estado) # {'uf': 'Bahia', 'sigla': 'Ba'}
                  # {'uf': 'São Paulo', 'sigla': 'Sp'}
                  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print('')

for estado in brasil:
    for k, v in estado.items():
        print(f'{k} = {v}') # uf = Bahia
                            # sigla = Ba
                            # uf = São Paulo
                            # sigla = SP
                            # uf = Rio de Janeiro
                            # sigla = RJ
print('')

for estado in brasil:
    for v in estado.values():
        print(f'{v:^5}', end='') # Bahia Ba
    print('')                    # São Paulo Sp
                                 # Rio de Janeiro RJ

print('')







