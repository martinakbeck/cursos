import funcoes
vl_saque = 0
vl_deposito = 0
saldo = 0

def mostra_menu():
    print('+-----Informe opção desejada-----+')
    print('+---------------|----------------+')
    print('|   1- SACAR    |  2- DEPOSITAR  |')
    print('+---------------+----------------+')
    print('|   3- SALDO    | 4 - TRANSFERIR |')
    print('+---------------+----------------+')
    print('|   5- SAIR     |                |')
    print('+---------------+----------------+')
    opcao = int(input())
    while opcao < 6:
        if opcao == 1:
            print(funcoes.saque(saldo))
        elif opcao == 2:
            print(funcoes.deposito(saldo))
        elif opcao == 3:
            print(funcoes.saldo(saldo))
        elif opcao == 4:
            print(funcoes.transferencia(saldo))
        elif opcao == 5:
            print(funcoes.sair())
        else:
            print ('Operação escolhida inválida')


        def verifica_login(plogin):
        while plogin != 1234:
            print ('Acesso negado, tente novamente!')
            plogin = int(input('Número de conta: '))
        else:
            return verifica_senha()
        
   
def verifica_senha():
    senha = int(input('Insira senha: '))
    tentativas = 3
    while senha != 123456:
        print ('Senha incorreta, tente novamente (resta ' + str(tentativas) + ' tentativas: ')
        senha = int(input('|  Insira senha: '))
        tentativas = tentativas - 1
        if tentativas == 0:
            return ('Acesso Bloqueado')
            break
    else:
        return 'Acesso Liberado'

def saque(p_saldo):
    vl_saque = int(input('Informe valor para saque: '))
    if vl_saque <= p_saldo:
        return 'Saldo Indísponivel'
    else:
        p_saldo = p_saldo - vl_saque 
        return 'Operação efetuada com sucesso'
    
def deposito(p_saldo):
    vl_deposito = int(input('Informe valor para depósito: '))
    saldo = p_saldo + vl_deposito
    return 'Depósito efetuado com sucesso'

def saldo(p_saldo):
    return 'Seu saldo é R$ ' + str(p_saldo)

def transferencia(p_saldo):
    return 'transferencia'

def sair():
    return'Obrigado pela preferência'
    

