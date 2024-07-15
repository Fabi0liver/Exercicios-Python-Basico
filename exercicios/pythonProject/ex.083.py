#crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
#e fechados na oredem correta.



print('*' * 60)
print(f'{'Vamos saber se sua expressão matématica está correta?!':^60}')
print('*' * 60)
print('-' * 60)
expre = str(input(f'{'Digite a expressão matématica:':>35} '))
print('-' * 60)
par = []
for par in expre:
    if expre == '(':
        par.append('(')
    else:
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break

if len(par) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
