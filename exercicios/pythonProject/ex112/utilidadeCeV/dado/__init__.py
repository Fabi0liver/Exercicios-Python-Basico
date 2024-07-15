
def leiaDinheiro(txt):
    valido = False
    while not valido:
        entrada = input(input(txt)).replace('.', '.').strip() == ' '
        if entrada.isalpha():
            print(f'ERRO!! <{entrada}> é inválido.')
        else:
            valido = True
            return float(entrada)
