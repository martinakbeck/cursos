num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

op = int(input('''Operação desejada:
1 - Soma
2 - Subtrair
3 - Multiplicação
4 - Divisão: '''))

class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        soma = self.numero1 + self.numero2
        print(f'{self.numero1} + {self.numero2} = {soma}')

    def subtrair(self):
        sub= self.numero1 - self.numero2
        print(f'{self.numero1} - {self.numero2} = {sub}')

    def multiplicacao(self):
        multi = self.numero1 * self.numero2
        print(f'{self.numero1} x {self.numero2} = {multi}')

    def divisao(self):
        if self.numero2 == 0:
            print('Impossível dividir por ZERO!')
        else:
            div = self.numero1 / self.numero2
            print(f'{self.numero1} / {self.numero2} = {div}')


calculo = Calculadora(num1, num2)

if op == 1:
    calculo.soma()
elif op == 2:
    calculo.subtrair()
elif op == 3:
    calculo.multiplicacao()
elif op == 4:
    calculo.divisao()

