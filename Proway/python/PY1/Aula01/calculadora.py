
casas = int(input('Informe quantas casas decimais: '))
v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))

op = int(input('Informe a operação desejada (1- Soma | 2- Subtração | 3 - Multiplicação | 4- Divisão): '))


if (op == 1):
    #print(f'A soma dos valores é {v1:.2f} + {v2:.2f} = {(v1+v2):.2f}')
    print('A soma dos valores: ' + ('%.' + str(casas) + 'f') % (v1+v2))
elif (op == 2):
    #print(f'A subtracao dos valores é {v1:.2f} - {v2:.2f} = {(v1-v2):.2f}')
    print('A subtração dos valores: ' + ('%.' + str(casas) + 'f') % (v1-v2))
elif (op == 3):
    #print(f'A multiplicação dos valores é {(v1):.2f} x {(v2):.2f} = {(v1*v2):.2f}')
    print('A multiplcação dos valores: ' + ('%.' + str(casas) + 'f') % (v1*v2))
elif (op == 4):
    if (v2 == 0):
        print('Impossível fazer divisão')
    else:
        #print(f'A divisão dos valores é {(v1):.2f} / {(v2):.2f} = {(v1/v2):.2f}')
        print('A divisão dos valores: ' + ('%.' + str(casas) + 'f') % (v1/v2))
else:
    print('Operação inválida')
