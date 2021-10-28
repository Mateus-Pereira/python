# print(type(lista))
# Listas podem ser alteradas quando quiser
lista = [1, 5, 4 , 10, 92 ,20, 100]

lista_animal = ['leao', 'lobo', 'vaca', 'gato']

lista.sort()

lista_animal.sort()

print(lista)

print(lista_animal)

lista_animal.reverse()

print(lista_animal)

print(lista_animal[2])

nova_lista = lista_animal * 3

print(nova_lista)

if 'gato' in lista_animal:
    print('tem um gato na lista')
else:
    print('não tem um gato na lista')
    lista_animal.append('gato')
    print(lista_animal)
lista_animal.pop(2)
print(lista_animal)
lista_animal.remove('lobo')
print(lista_animal)


print(min(lista_animal))
print(max(lista_animal))

print(min(lista))
print(max(lista))
print(sum(lista))

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)
print(len(lista_animal))




# tuple não pode alterar
# tupla = (1, 12, 11, 10)
# print(tupla)
# print(len(tupla))
# tupla_animal = tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)
# lista_numerica = list(tupla)
# print(type(lista_numerica))
# print(lista_numerica)
# lista_numerica[0] = 1002
# print(lista_numerica)
