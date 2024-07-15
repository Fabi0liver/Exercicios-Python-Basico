#nome= input('Qual seu nome?')

#print('Prazer em ti conhecer {}! Vamos aprender Python?'.format(nome))
#print('Prazer em ti conhecer {:20}! Vamos aprender Python?'. format(nome))
          #acrecente :20 dentro da {} e a nome vai aparecer em 20 espaços
#print('Prazer em ti conhecer {:>20}! Vamos aprender Python?'. format(nome))
          #acrecente o :> ou :< e o nome vai se aliar o numero de vezes ao lado indicado
#print('Prazer em ti conhecer {:^20}! Vamos aprender Python?'. format(nome))
          #acrecente o :^ e o nome vai aliar ao centro do numero de espaços digitado
#print('Prazer em ti conhecer {:=^20}! Vamos aprender Python?'. format(nome))
          #acrecente o :=^ e o nome vai se aliar ao centro do numero de caracter indicado


n1 = int(input('Digite uma Valor:'))
n2 = int(input('Digite outro valor:'))

#print('A soma de {} e {}, o resultado é {}.'. format(n1, n2, n1+n2))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('a adição é {}, a sublitação é {}, e multiplicação é {}.'.format(a, s, m))
print('a divisão é {:.3f}, a divisão inteira é {}, e a potência é {}.'.format(d, di, p))
     #ao acrecentar o :.3f  dentro de {}, só sera mostrando o numero de casa flutiantes  digitada

print('a adição é {}, a sublitação é {}, e a multiplicação é {}.'. format(a, s, m), end=' ')
print(' a divisão é {}, a divisão inteira é {}, e a potência é {}.'.format (d, di, p))
    # para  deixar dois print na mesma linha, como continuação e só acrencentar no final do print o end='', que pode ser vazio ou com algo. exemplo  end='>>>'.

print('a adição é {},\n a sublitação é {},\n e a multiplicação é {}'.format(a, s, m))
print('a divisão é {},\n a divisão inteira é {},\n e a potência é {}.'.format(d, di, p))
   # para separar o print em linha diferentes, e só acrencentar 0 \n no meio onde quer separar.









