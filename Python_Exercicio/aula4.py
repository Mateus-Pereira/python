# a = int(input('Primeiro bimestre'))
# while a > 10:
#     a = int(input('Você digitou errado. Primeiro bimstre: '))
# b = int(input('Segundo bimestre'))
# while b > 10:
#     b = int(input('Você digitou errado. Segundo bimstre: '))
# c = int(input('Terceiro bimestre'))
# while c > 10:
#     c = int(input('Você digitou errado. Terceiro bimstre: '))
# d = int(input('Quarto bimestre'))
# while d > 10:
#     d = int(input('Você digitou errado. Quarto  bimstre: '))
# media = (a + b + c + d) / 4
# print('media: {}'.format(media))
#
#
#
# nota = int(input('Nota aqui '))
# while nota > 10:
#     nota = int(input('Nota aqui, nota esta errada'))


# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Escreva um numero '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resultado = num % x
#         # print (x, resultado)
#         # print(resultado)
#         if resultado == 0:
#             div += 1
#     if div == 2:
#         print(num)




a = int(input('Escreva um numero'))
div = 0
for x in range(1, a+1):
    resultado = a % x
    print (x, resultado)
    print(resultado)
    if resultado == 0:
        div += 1
if div == 2:
    print('número {} é primo'.format(a))
else:
    print('numero {} não é primo'.format(a))

