def listar(pItens):
    if ( len(pItens) == 0):
        return 'Não há itens cadastrados.'
    gravaLogDados('Listou os Itens')
    

def cadastrar(pItem, pItens):
    if ( pItem in pItens ):
        return pItem + ' já está cadastrado.'
    pItens.append(pItem)
    gravaLogDados('Cadastrou ' + pItem)
    return pItem + ' cadastrado com sucesso.'

def excluir2(pItem,pItens):
    if ( len(pItens) > 0 ):
        if ( pItem in pItens ):
            for item in range(0,len(pItens)):
                if ( pItens[item] == pItem):
                    pItens.pop(item)
                    gravaLogDados('Excluíu' + pItem)
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
                gravaLogDados('Alterou ' + pItem + ' para ' + novo)
                return pItem + ' alterado para ' + novo + ' com sucesso.'
    return pItem + ' não está cadastrado. '


def gravaLogDados(pMsg, pTipo = 1):
    if(pTipo == 1):
        arq = open('Aula04\Relatorios\log.txt', 'a')
        arq.write(pMsg + str('\n'))
        arq.close()
    else:
        arq = open('Aula04\Relatorios\dados.txt', 'w')
        arq.write(pMsg)
        arq.close()

def lerArquivo(pTipo = 1):
    if( pTipo == 1 ) :
        arq = open('Aula04\Relatorios\log.txt', 'r')
        for linha in arq:
            print(linha.rstrip())
        arq.close()
    else:
        arq = open('Aula04\Relatorios\dados.txt', 'r')
        for linha in arq:
            print(linha.rstrip())
        arq.close()

