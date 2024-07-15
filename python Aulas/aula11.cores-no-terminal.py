                                     # cores no Terminal


# Vou tentar passar como utilizar os códigos de "escape sequence ANSI" para configurar cores para os seus
#programas em Python (Algumas das que são compatíveis).

#Existem outras formas de colocar cores, uma delas é :

#Quando você quiser apresentar uma cor em Python você vai começar com esse comando:
#                                  "\033[m"
#     contra barra + 033 + abrir colchetes e fechar o código com a letra "m"

#        E entre esse colchetes e "m" você vai colocar o código da cor.
#           Você poderá colocar 0 código, 1 código, 2 ou 3 códigos.

# exemplo com 3 código:

#                                \033[0;33;44m

#     Primeiro código "0" que eu inseri foi do "comportamento", "STYLE"
#               (Negrito, normal, itálico, Sublinhada )

#            Em seguida você colocará o " ; " (para separar ).

#      Segundo código "33" é o código do "Texto", "TEXT" (cor do texto )

# Terceiro código "44" é o código de "cor de fundo" , "BACKground" (cor do fundo)

#                       ALGUNS CODIGOS PARA STYLE SÃO:

# 0 = None (sem estilo)
#esse primeiro código é opcional caso você queria deixar sua fonte normal,
#         pode colocar ou não o "0", deixando v.

# 1 = Bolde (Negrito)

# 2 = Fraco

# 3 = Itálico

# 4 = Underline (Sublinhado)

#7 = Negative (Inverter as configurações Fundo vai pra letra e letra fundo)


#                 ALGUNS CODIGOS PARA TEXT SÃO (30 a 37):

# 30 = Branco

# 31 = Vermelho

# 32 = Verde

# 33 = Amarelo

# 34 = Azul

# 35 = Magenta

# 36 = Ciano

# 37 = Cinza

#              ALGUNS CODIGOS PARA BACK SÃO (40 a 47):

# 40 = Branco

# 41 = Vermelho

# 42 = Verde

# 44 = Azul

# 45 = Magenta

# 46 = Ciano

# 47 = Cinza