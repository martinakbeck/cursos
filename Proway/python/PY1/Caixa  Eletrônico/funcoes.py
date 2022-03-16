vl_valor = 0
vl_saldo = 0

def verifica_login(plogin):
    while plogin != 1234:
        print ('Acesso negado, tente novamente!')
        plogin = int(input('Número de conta: '))
    else:
        return verifica_senha()
    
def verifica_senha():
    senha = int(input('|  Insira senha: '))
    tentativas = 3
    while senha != 123456:
        print ('Senha incorreta, tente novamente (resta ' + str(tentativas) + ' tentativas: ')
        senha = int(input('|  Insira senha: '))
        tentativas = tentativas - 1
    if tentativas == 0:
        return('Acesso Bloqueado')
    else:
        return('Acesso Liberado')

def saque():
    global vl_saldo, vl_valor
    nome = 'Saque'
    vl_valor = float(input('Informe valor para saque: '))
    if vl_valor > vl_saldo:
        return('Saldo Indísponivel')
    else:
        vl_saldo = vl_saldo - vl_valor
        gera_historico(vl_valor,'Saque')
        return('Operação efetuada com sucesso')

   
def deposito():
    global vl_saldo, vl_valor
    nome = 'Depósito'
    vl_valor = float(input('Informe valor para depósito: '))
    vl_saldo = vl_saldo + vl_valor
    gera_historico(vl_valor,'Depósito')
    return('Depósito efetuado com sucesso')

def saldo():
    global vl_saldo
    return('Seu saldo é R$ ' + str(vl_saldo))

def transferencia():
    global vl_saldo, vl_valor
    nome = 'Transferência'
    taxa = 6
    vl_valor = float(input('Informe valor para transfêrencia: '))
    opcao = float(input('Será cobrado uma taxa de R$ 6,00, deseja continuar? 1- Sim | 2 -Não '))
    if opcao == 1:
        if (vl_valor+taxa) > vl_saldo:
            return('Saldo insuficiente')
        else:
            conta = input('Informe conta para transferência: ')
            if (len(conta) == 5):
                vl_saldo = vl_saldo - (vl_valor+taxa)
                gera_historico(vl_valor,'Transferência')
                return('Transferência realizada com sucesso!')
            else:
                return('Conta Inválida')
            
def ver_historico():
    arquivo = open('Histórico.txt', 'r')
    historico = arquivo.readlines()
    arquivo.close()
    for i in historico:
       print (i)
       
      
def gera_historico(p_valor,p_op):
    from datetime import datetime
    from pathlib import Path
    data = datetime.today()
    dia = data.day
    mes = data.month
    ano = data.year
    hora = data.hour
    minuto = data.minute
    if (dia < 0 ):
        dia = '0' + str(dia)
    if (mes < 10 ):
        mes = '0' + str(mes)
        
        
    arquivo = open('Histórico.txt', 'r')
    historico = arquivo.readlines()
    arquivo.close()
    arquivo = open('Histórico.txt', 'w')
    historico.append('Data: '+ str(dia)+'/'+ str(mes) + '/' +str(ano) + ' Hora: ' + str(hora) + ':' +str(minuto) +'\n')
    historico.append(p_op + '---------------- R$' + str('%.2f'%p_valor) + '\n')
    historico.append('Saldo ---------------- R$' + str('%.2f'%vl_saldo) + '\n')
    arquivo.writelines(historico)
    arquivo.close()
