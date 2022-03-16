import funcoes
opcao = 0
print('----------- Banco Proway -----------')
login = int(input('Número de conta: '))
print(funcoes.verifica_login(login))



while opcao != 6:
    print('+-----Informe opção desejada-----+')
    print('+---------------|----------------+')
    print('|   1- SACAR    |  2- DEPOSITAR  |')
    print('+---------------+----------------+')
    print('|   3- SALDO    | 4 - TRANSFERIR |')
    print('+---------------+----------------+')
    print('| 5 - HISTÓRICO |   6 -SAIR      |')
    print('+---------------+----------------+')
    opcao = int(input())
    if opcao == 1:
        print(funcoes.saque())        
    elif opcao == 2:
        print(funcoes.deposito())
    elif opcao == 3:
        print(funcoes.saldo())
    elif opcao == 4:
        print(funcoes.transferencia())
    elif opcao == 5:
        print (funcoes.ver_historico())
    elif opcao == 6:
        print('Obrigado pela preferência')
    else:
        print('Opção inválida')
    

        

          
