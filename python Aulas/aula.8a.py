#import math

    #aqui será importada toda a biblioteca do modúlo

#num = int(input(' Digite uma número:'))
#raiz = math.sqrt(num)
  #usando a "math.sqrt" se faz a raiz de um número

#print('')
#print('A raiz de {} é igual a {}!'.format(num, raiz))

#print('')
#print('A raiz de {} é igual a {:.2f}!'.format(num, raiz))

#print('')
#print('A raiz de {} é igual a {}!'.format(num, math.ceil(raiz)))
  # usando o "math.ceil" o número flutuante será arrendondado pra cima

#print('')
#print('A raiz de {} é igual a {}!'.format(num, math.floor(raiz)))
  # usando o "math.floor" o número flutuante será arrendondado para baixo



from math import sqrt , trunc

#aqui sera importadas apenas as funções "sqrt e trunc" da biblioteca math

num = int(input('Digite um número:'))
raiz =sqrt(num)

print('')
print('A raiz de {} é igual a {}!'.format(num, raiz))

print('')
print('A raiz de {} é igual a {}!'.format(num, trunc(raiz)))
  # usando o "math.trunc" os numeros depois da "." serão eliminados.



