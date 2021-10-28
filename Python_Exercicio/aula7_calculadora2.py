class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(10,2))
print(calculadora.subtracao(22,6))
print(calculadora.multiplicacao(12,5))
print(calculadora.divisao(43,55))