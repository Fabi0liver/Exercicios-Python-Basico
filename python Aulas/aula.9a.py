# Pratica

frase = 'Curso de Vídeo Python'

print(frase)
print('')
print('A 4º letra da minha frase é "{}".'.format(frase[3]))
print('')
print('Um corte minha frase que vai  da 4º letra  até a 12º letra é : "{}".'.format(frase[3:13]))
print('')
print('Agora faça um corte na minha frase do começo até a 12º letra é: "{}"'.format(frase[:13]))
print('')
print('E se for um corte da 12º letra até o final da frase fica: "{}"'.format(frase[13:]))
print('')
print('E se eu quiser um corte do começo da minha frase até a 17º letra pulando de 3 em 3 letras fica: "{}"' .format(frase[:18:3]))
print('')
print('se for do começa da frase até o final pulando de duas em duas letras fica: "{}"'.format(frase[::2]))
print('')
#print('''De tudo, ao meu amor serei atento
#Antes, e com tal zelo, e sempre, e tanto
#Que mesmo em face do maior encanto
#Dele se encante mais meu pensamento.''')
print('minha frase tem "{}" caracteres.'.format(len(frase)))
print('')
print('Na minha frase tem "{}" "o".'.format(frase.count('o')))
print('')
print('Transforme  toda minha frase em maiuscula: "{}"'.format(frase.upper()))
print('')
print('Transforme toda minha frase em minuscula: "{}"'.format(frase.lower()))
print('')
print('Agora só deixa a primeira letra da frase em maiscula: "{}"'.format(frase.capitalize()))
print('')
print('Agora todas a primeira letras das palavra em maiusculas: "{}"'.format(frase.title()))
print('')
print('Troque a palavra "Python na minha frase por "Android: "{}"'.format(frase.replace('Python', 'Android')))
print('')
print(' Na minha frase tem a palavra Vídeo? "{}"'.format('Vídeo' in frase))
print('')
print('E a palavra "aula", tem na minha frase? "{}"'.format('aula' in frase))
print('')
print('Faça um lista com as palvras da minha frase: {}'.format(frase.split()))
print('')
print('Agora junta a lista e coloque um * no meio  das palvras: {}'.format('*'.join(frase.split())))







