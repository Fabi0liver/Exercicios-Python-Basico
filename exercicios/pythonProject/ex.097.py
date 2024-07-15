#faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
#e mostre uma mensagem com tamanho adaptpavel.


def escreva(txt):
    tam = len(txt)+4
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)


# programa principal

escreva('Olá Mundo!')
escreva('Fábio de Araujo oliveira')
escreva('Poções')


