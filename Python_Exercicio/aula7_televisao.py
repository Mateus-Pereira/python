class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 1
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

    def volume_mais(self):
        if self.ligada:
            self.volume += 1

    def volume_menos(self):
        if self.ligada:
            self.volume -= 1
# if __name__ == '__main__': / so executa o texto quando a chamada e pelo proprio arquivo
if __name__ == '__main__':

    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))

    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('canal: {}'.format(televisao.canal))

    televisao.diminui_canal()
    print('canal: {}'.format(televisao.canal))

    televisao.volume_mais()
    televisao.volume_mais()
    print('Volume do canal é: {}'.format(televisao.volume))
    televisao.volume_menos()
    print('Volume do canal é: {}'.format(televisao.volume))
