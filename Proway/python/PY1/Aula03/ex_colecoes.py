def listar():
    if ( len(itens) == 0):
        return 'Lista vazia'
    return itens

def cadastrar(pItem):
    if ( pItem in itens):
        return 'Produto já cadastrado'
    itens.append(pItem)
    return pItem.capitalize() + '- Cadastrado com Sucesso'

def excluir(pItem):
    if ( pItem in itens):
        itens.remove(pItem)
        return pItem + ' - Produto excluído com sucesso'
    return pItem + ' - Não está cadastrado'

def excluir2(pItem):
    if (len(itens) > 0):
        if (pItem in itens):
            for item in range (0, len(itens)):
                if(itens[item] == pItem):
                    itens.pop(item)
                    return pItem + ' excluído com sucesso.'
        return pItem + ' não cadastrado.'
def alterar(pItem):
    if (pItem in itens):
        for x in range(0, len(itens)):
            if (itens[x] == pItem):
                novo = input('Informe o novo nome do item: ')
                if (novo in itens):
                    return novo + ' já está cadastrado'
                itens[x] == novo
                return pItem + ' alterado para ' + novo + ' com sucesso.'
                break
    return pItem + ' não está cadastrado.'

itens = []
op = 0

while (op != 5):
    op = int(input('Selecione uma função: \n'
    '1 - Adicionar \n'
    '2 - Listar \n'
    '3 - Excluir \n'
    '4 - Alterar \n'
    '5 - Sair \n'))
    if (op == 1):
        produto = input('Informe nome do produto: ')
        print(cadastrar(produto))
    elif (op == 2):
        print(listar())
    elif (op == 3):
        produto = input('Informe nome do produto: ')        
        if (len(itens) == 0 ):
            print('Não tem itens listados')
        else:
            print(excluir(produto))
    elif (op == 4):
        produto = input('Informe nome do produto: ')
        if (len(itens) == 0 ):
            print('Não tem itens listados')
        else:
            print(alterar(produto))
    elif (op == 5):
        print('FIM!')
    else:
        print('Opção inválida')

