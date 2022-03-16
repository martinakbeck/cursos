g_comum = 5.29
g_aditivada = 5.49
etanol = 4.99

opcao = int(input('Deseja inserir valor (R$) ou quantidade de litros? \n'
                '1- Valor (R$) \n'
                '2- Litros \n'))
if (opcao >= 2) or (opcao < 1):
    print('Opção inválida')    

combustivel = int(input('Qual combustível desejado? \n'
                        '1- Gasolina Aditivada \n'
                        '2- Gasolina Comum \n'
                        '3- Etanol \n'))
if (combustivel >= 4) or (combustivel < 1):
    print('Opção inválida')
else:
    if (opcao == 1):
        valor = float(input('Informe valor (R$): '))
        if (combustivel == 1):
            print('Valor total de litros %.2f' %(valor/g_aditivada) + ' litros.')
        elif (combustivel == 2):
            print('Valor total de litros %.2f' %(valor/g_comum) + ' litros.')
        elif (combustivel == 3):
            print('Valor total de litros %.2f' %(valor/etanol) + ' litros.')
    elif (opcao == 2):
        litros = float(input('Informe quantidade de litros: '))
        if (combustivel == 1):
            print('Valor total a pagar R$ %.2f' %(g_aditivada*litros))
        elif (combustivel == 2):
            print('Valor total a pagar R$ %.2f' %(g_comum*litros))
        elif (combustivel == 3):
            print('Valor total a pagar R$ %.2f' %(etanol*litros))

