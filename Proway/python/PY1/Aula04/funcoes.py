# Elabore um algoritmo que controle uma Itens de itens de informática. 
# Deverá ser exibido um menu com as seguintes opções:
# Adicionar, Itensr, Excluir, Alterar e Sair
# Adicionar somente poderá ser executado se o item já não exista
# Ao Itensr, caso a lista esteja vazia, não deve mostrar ela vazia, mas sim uma mensagem informando isso.
# Excluir somente poderá ser executado se o item existir. (Perguntar o nome e não a posição)
# Alterar somente poderá ser executado se o item existir, e deverá perguntar o novo nome do item. (aplicar regra1)
# Deverá sempre exibir o menu novamente até que o usuário opte por SAIR
# --------------------------------------------------------------------------------


def listar(pItens):
    if ( len(pItens) == 0):
        return 'Não há itens cadastrados.'
    return 'Relatório gerado'
    

def cadastrar(pItem, pItens):
    if ( pItem in pItens ):
        return pItem + ' já está cadastrado.'
    pItens.append(pItem)
    gravarHistorico(pItem, 'Cadastrado')
    return pItem + ' cadastrado com sucesso.'

def excluir2(pItem,pItens):
    if ( len(pItens) > 0 ):
        if ( pItem in pItens ):
            for item in range(0,len(pItens)):
                if ( pItens[item] == pItem):
                    pItens.pop(item)
                    gravarHistorico(pItem, 'Excluído')
                    return pItem + ' excluído com sucesso.'
        return pItem + ' não está cadastrado.'
    return 'Itens vazia'

def alterar(pItem, pItens):
    if ( pItem in pItens ):
        for x in range(0,len(pItens)):
            if ( pItens[x] == pItem ):
                novo = input('Informe o novo nome do item: ')
                if ( novo in pItens ):
                    return novo + ' já está cadastrado. '
                pItens[x] = novo
                gravarHistorico(pItem, 'Alterado')
                return pItem + ' alterado para ' + novo + ' com sucesso.'
    return pItem + ' não está cadastrado. '

def gravarInformacoes (pItens):
    arquivo = open('Aula04\dados.txt', 'w')
    for x in pItens:
        arquivo.writelines(x)
    arquivo.close()
    return 'Relatório Gerado'

def verHistorico():
    arquivo = open('Aula04\log.txtlog.txt', 'r')
    historico = arquivo.readlines()
    arquivo.close()
    for i in historico:
       print (i)

def gravarHistorico(pItem, pOp):
    arquivo = open('log.txt', 'r')
    historico = arquivo.readlines()
    arquivo.close()

    arquivo = open('Aula04\log.txt', 'w')
    historico.append(pOp + ' : ' + pItem + '\n' )
    arquivo.writelines(historico)
    arquivo.close()

