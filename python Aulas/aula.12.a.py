nome = str(input('Qual seu nome? '))
if nome == 'Fábio':
    print(f'EU gosto do seu nome é bem legal!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'{nome}, é um nome bem popular me!!')
elif nome in 'Aline, Clara, Anna, Ana, Isabel':
    print(f'{nome}! E um nome feminino muito bonito!')
else:
    print(f'{nome}, seu nome me parece legal!')
print(f'Tenha um Bom dia {nome}!')


