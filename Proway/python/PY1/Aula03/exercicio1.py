def soma(p1,p2):
    print(str(p1) +' + ' + str(p2) + ' = ' + str(p1+p2))
def subtracao(p1,p2):
    print(str(p1) +' - ' + str(p2) + ' = ' + str(p1-p2))
def multiplcacao(p1,p2):
    print(str(p1) +' * ' + str(p2) + ' = ' + str(p1*p2))
def divisao(p1,p2):
    if (p2 == 0):
        print('Impossível fazer divisão')
    else:
        print(str(p1) +' / ' + str(p2) + ' = ' + str(p1/p2))


v1 = int(input('Informe um valor inteiro: '))
v2 = int(input('Informe outro valor inteiro: '))

op = int(input('Informe operação desejada: \n'
                '1 - Soma | 2 - Subtração \n'
                '3 - Multiplicação | 4 - Divisão '))

if (op == 1):
    soma(v1,v2)
elif (op == 2):
    subtracao(v1,v2)
elif (op == 3):
    multiplcacao(v1,v2)
elif (op == 4):
    divisao(v1,v2)
else:
    print('Operação Inválida')

