#  Faça um programa que na tela um contagem regressiva para o estouro de fogos  de artifícios,
# indo de 10 até o 0, com a uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

sleep(1)
print('')
print('*' * 50)
print('  🎊VAMOS COMEÇAR NOSSA CONTAGEM REGRESSIVA!!🎊')
print('*' * 50)
sleep(2)
print('')
sleep(1)
print('')
for i in range(10, -1, -1):
    print('*' * 23, i, '*' * 23)
    sleep(1)
    print('')

print(' 🎉✨🎉✨🎉✨🎉✨🎉✨🎉✨🎉✨🎉✨🎉✨🎉✨🎉')



