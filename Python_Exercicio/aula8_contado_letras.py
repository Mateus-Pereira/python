def contator_letras(lista_palavras):
    contator = []
    for x in lista_palavras:
        quantidade = len(x)
        contator.append(quantidade)
    return contator

if __name__ == '__main__':
    lista = ['Cachorro', 'Gato']
    print(contator_letras(lista))