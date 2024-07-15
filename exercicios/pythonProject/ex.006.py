#crie um algarismo que leia um número e mostre o seu dobro, o seu tripo e a raiz quadrada.

n = int (input('Digite um número:'))
print('Você digitou {}? \nO dobro dele é {}. \nO tripo é {}. \nE a raiz quadrada dele é {:.2f}. \nEstou certo?'. format(n, (n*2), (n*3), (n**(1/2))))
                                                                                            # para saber a  raiz quadrada tbm pode se usar  pow(n,(1/2)

