from aula7_televisao import Televisao
from aula8_contado_letras import contator_letras
if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    lista = ['Cachorro', 'Gato','elefante']
    total_letras = contator_letras(lista)
    print('total de letras por palavras da lista: {}'.format(total_letras))
