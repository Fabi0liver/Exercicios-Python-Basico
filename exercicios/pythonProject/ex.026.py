#faça um programa que leia uma frase pelo teclado mostre:
#Quantas Vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez
# em que posição ela aparece pela Ultima vez.

texto = str(input('Digite ums frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(texto.count('A')))
print('O Primeiro "A" apareceu na posição: {} '.format(texto.find('A')+1))
print('O Ultimo "A" apareceu na posição: {} '.format(texto.rfind('A')+1))

